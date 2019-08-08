# Most of this was from Adrian Rosebrocks post on pyimagesearch to figure out
# the focal distance of my MacBook Pro's camera https://bit.ly/2KJVoKC

# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2

def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)

    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    c = max(cnts, key = cv2.contourArea)

    # compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth

# initialize the known distance from the camera to the object, which
# in this case is 12 inches
KNOWN_DISTANCE = 12.0

# initialize the known object width, which in this case, the piece of
# paper is 11 inches wide
KNOWN_WIDTH = 11.0

# load the  image that contains an object that is KNOWN TO BE 1 foot
# from our camera, then find the paper marker in the image, and initialize
# the focal length
image = cv2.imread('paper.jpg')
marker = find_marker(image)


focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
print('Focal Length:', focalLength)

# load the image, find the marker in the image, then compute the
# distance to the marker from the camera
image = cv2.imread('paper.jpg')
marker = find_marker(image)
inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])

# draw a bounding box around the image and display it
box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
box = np.int0(box)
print(box)
cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
cv2.circle(image, tuple(box[0]), 5, (255,0,0), thickness=2, lineType=8, shift=0)
cv2.circle(image, tuple(box[3]), 5, (0,0,255), thickness=2, lineType=8, shift=0)
cv2.putText(image, "%.2fft" % (inches / 12),
            (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
            2.0, (0, 255, 0), 3)
cv2.imshow("image", image)
cv2.waitKey(0)
