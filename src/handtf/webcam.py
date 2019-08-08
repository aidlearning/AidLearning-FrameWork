import datetime
import argparse

from utils import detector_utils as detector_utils

from cvs import *

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--display', dest='display', type=int,
                        default=1, help='Display the detected images using OpenCV. This reduces FPS')
args = vars(ap.parse_args())


detection_graph, sess = detector_utils.load_inference_graph()


def main():
    # Detection confidence threshold to draw bounding box
    score_thresh = 0.60

    vs=cvs.VideoCapture(1)

    # max number of hands we want to detect/track
    num_hands_detect = 1

    # Used to calculate fps
    start_time = datetime.datetime.now()
    num_frames = 0

    im_height, im_width = (None, None)

    try:
        while True:
            sleep(30)
            # Read Frame and process
            frame =cvs.read()
            if frame is None:
                continue
            frame = cv2.resize(frame, (640, 480))

            if im_height == None:
                im_height, im_width = frame.shape[:2]

            # Convert image to rgb since opencv loads images in bgr, if not accuracy will decrease
            try:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            except:
                print("Error converting to RGB")

            # Run image through tensorflow graph
            boxes, scores, classes = detector_utils.detect_objects(
                frame, detection_graph, sess)
            
            
            # Draw bounding boxeses and text
            detector_utils.draw_box_on_image(
                num_hands_detect, score_thresh, scores, boxes, classes, im_width, im_height, frame)

            # Calculate Frames per second (FPS)
            num_frames += 1
            elapsed_time = (datetime.datetime.now() -
                            start_time).total_seconds()
            fps = num_frames / elapsed_time
            
            # Display FPS on frame
            lbs = "FPS : " + str("{0:.2f}".format(fps))
            cvs.setLbs(lbs)

            if args['display']:
                
                detector_utils.draw_text_on_image("FPS : " + str("{0:.2f}".format(fps)), frame)

                cvs.imshow(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        
        print("Average FPS: ", str("{0:.2f}".format(fps)))

        

    except KeyboardInterrupt:
        print("Average FPS: ", str("{0:.2f}".format(fps)))
        

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def idle(self):
        #idle function called every update cycle
        self.lbl.set_text(cvs.getLbs())
        pass
    
    def main(self):
        # initcv(process)
        #creating a container VBox type, vertical (you can use also HBox or Widget)
        main_container = gui.VBox(width=360, height=680, style={'margin':'0px auto'})
        
        self.aidcam = OpencvVideoWidget(self, width=340, height=480)
        self.aidcam.style['margin'] = '10px'

        self.aidcam.set_identifier("myimage_receiver")
        main_container.append(self.aidcam)
        
        # Display FPS on frame
        self.lbl = gui.Label('This is a LABEL!', width=360, height=30, margin='10px')
        main_container.append(self.lbl)

        return main_container

            
        
if __name__ == '__main__':
    initcv(main)
    startcv(MyApp)
