from cvs import *
import numpy as np

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)
        
    def main(self):
        #creating a container VBox type, vertical (you can use also HBox or Widget)
        main_container = gui.VBox(width=360, height=680, style={'margin':'0px auto'})
        
        self.aidcam = OpencvVideoWidget(self, width=340, height=480)
        self.aidcam.style['margin'] = '10px'
        
        self.aidcam.set_identifier("myimage_receiver")
        main_container.append(self.aidcam)
         
        # returning the root widget
        return main_container
        

        
        
def process():

    cap=cvs.VideoCapture(1)

    while True:
        sleep(30)
        img =cap.read()
        
        if img is None :
            continue
        cvs.imshow(img)

if __name__ == '__main__':
    #init proceess thread
    initcv(process)
    #start gui show
    startcv(MyApp)
