from posenet.decode import *
from posenet.constants import *
import time
import scipy.ndimage as ndi


def within_nms_radius(poses, squared_nms_radius, point, keypoint_id):
    for _, _, pose_coord in poses:
        if np.sum((pose_coord[keypoint_id] - point) ** 2) <= squared_nms_radius:
            return True
    return False


def within_nms_radius_fast(pose_coords, squared_nms_radius, point):
    if not pose_coords.shape[0]:
        return False
    return np.any(np.sum((pose_coords - point) ** 2, axis=1) <= squared_nms_radius)


def get_instance_score(
        existing_poses, squared_nms_radius,
        keypoint_scores, keypoint_coords):
    not_overlapped_scores = 0.
    for keypoint_id in range(len(keypoint_scores)):
        if not within_nms_radius(
                existing_poses, squared_nms_radius,
                keypoint_coords[keypoint_id], keypoint_id):
            not_overlapped_scores += keypoint_scores[keypoint_id]
    return not_overlapped_scores / len(keypoint_scores)


def get_instance_score_fast(
        exist_pose_coords,
        squared_nms_radius,
        keypoint_scores, keypoint_coords):

    if exist_pose_coords.shape[0]:
        s = np.sum((exist_pose_coords - keypoint_coords) ** 2, axis=2) > squared_nms_radius
        not_overlapped_scores = np.sum(keypoint_scores[np.all(s, axis=0)])
    else:
        not_overlapped_scores = np.sum(keypoint_scores)
    return not_overlapped_scores / len(keypoint_scores)


def score_is_max_in_local_window(keypoint_id, score, hmy, hmx, local_max_radius, scores):
    height = scores.shape[0]
    width = scores.shape[1]

    y_start = max(hmy - local_max_radius, 0)
    y_end = min(hmy + local_max_radius + 1, height)
    x_start = max(hmx - local_max_radius, 0)
    x_end = min(hmx + local_max_radius + 1, width)

    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            if scores[y, x, keypoint_id] > score:
                return False
    return True


def build_part_with_score(score_threshold, local_max_radius, scores):
    parts = []
    height = scores.shape[0]
    width = scores.shape[1]
    num_keypoints = scores.shape[2]

    for hmy in range(height):
        for hmx in range(width):
            for keypoint_id in range(num_keypoints):
                score = scores[hmy, hmx, keypoint_id]
                if score < score_threshold:
                    continue
                if score_is_max_in_local_window(keypoint_id, score, hmy, hmx,
                                                local_max_radius, scores):
                    parts.append((
                        score, keypoint_id, np.array((hmy, hmx))
                    ))
    return parts


def build_part_with_score_fast(score_threshold, local_max_radius, scores):
    parts = []
    num_keypoints = scores.shape[2]
    lmd = 2 * local_max_radius + 1

    # NOTE it seems faster to iterate over the keypoints and perform maximum_filter
    # on each subarray vs doing the op on the full score array with size=(lmd, lmd, 1)
    for keypoint_id in range(num_keypoints):
        kp_scores = scores[:, :, keypoint_id].copy()
        kp_scores[kp_scores < score_threshold] = 0.
        max_vals = ndi.maximum_filter(kp_scores, size=lmd, mode='constant')
        max_loc = np.logical_and(kp_scores == max_vals, kp_scores > 0)
        max_loc_idx = max_loc.nonzero()
        for y, x in zip(*max_loc_idx):
            parts.append((
                scores[y, x, keypoint_id],
                keypoint_id,
                np.array((y, x))
            ))

    return parts


def decode_multiple_poses(
        scores, offsets, displacements_fwd, displacements_bwd, output_stride,
        max_pose_detections=10, score_threshold=0.5, nms_radius=20, min_pose_score=0.5):

    pose_count = 0
    pose_scores = np.zeros(max_pose_detections)
    pose_keypoint_scores = np.zeros((max_pose_detections, NUM_KEYPOINTS))
    pose_keypoint_coords = np.zeros((max_pose_detections, NUM_KEYPOINTS, 2))

    squared_nms_radius = nms_radius ** 2

    scored_parts = build_part_with_score_fast(score_threshold, LOCAL_MAXIMUM_RADIUS, scores)
    scored_parts = sorted(scored_parts, key=lambda x: x[0], reverse=True)

    # change dimensions from (h, w, x) to (h, w, x//2, 2) to allow return of complete coord array
    height = scores.shape[0]
    width = scores.shape[1]
    offsets = offsets.reshape(height, width, 2, -1).swapaxes(2, 3)
    displacements_fwd = displacements_fwd.reshape(height, width, 2, -1).swapaxes(2, 3)
    displacements_bwd = displacements_bwd.reshape(height, width, 2, -1).swapaxes(2, 3)

    for root_score, root_id, root_coord in scored_parts:
        root_image_coords = root_coord * output_stride + offsets[
            root_coord[0], root_coord[1], root_id]

        if within_nms_radius_fast(
                pose_keypoint_coords[:pose_count, root_id, :], squared_nms_radius, root_image_coords):
            continue

        keypoint_scores, keypoint_coords = decode_pose(
            root_score, root_id, root_image_coords,
            scores, offsets, output_stride,
            displacements_fwd, displacements_bwd)

        pose_score = get_instance_score_fast(
            pose_keypoint_coords[:pose_count, :, :], squared_nms_radius, keypoint_scores, keypoint_coords)

        # NOTE this isn't in the original implementation, but it appears that by initially ordering by
        # part scores, and having a max # of detections, we can end up populating the returned poses with
        # lower scored poses than if we discard 'bad' ones and continue (higher pose scores can still come later).
        # Set min_pose_score to 0. to revert to original behaviour
        if min_pose_score == 0. or pose_score >= min_pose_score:
            pose_scores[pose_count] = pose_score
            pose_keypoint_scores[pose_count, :] = keypoint_scores
            pose_keypoint_coords[pose_count, :, :] = keypoint_coords
            pose_count += 1

        if pose_count >= max_pose_detections:
            break

    return pose_scores, pose_keypoint_scores, pose_keypoint_coords
