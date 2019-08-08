
# -*- coding: utf-8 -*-

from cvs import *


class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        aidcam = OpencvVideoWidget(self)
        aidcam.set_identifier("myimage_receiver")#aidcam.attributes.update({"src":"/528175722896/get_image_data","editor_newclass":"False","editor_baseclass":"OpencvVideoWidget","editor_constructor":"()","class":"OpencvVideoWidget","editor_tag_type":"widget","editor_varname":"aidcam"})
        aidcam.style.update({"width":"190px","position":"absolute","top":"20px","left":"20px","margin":"0px","overflow":"auto","height":"177px"})
        

        self.aidcam = aidcam
        return self.aidcam
    

#processing_code

def process():

    cap=cvs.VideoCapture(1)

    while True:
        sleep(30)
        img =cap.read()

        if img is None :
            continue
        cvs.imshow(img)

if __name__ == "__main__":
    
    initcv(process)
    startcv(untitled)
   