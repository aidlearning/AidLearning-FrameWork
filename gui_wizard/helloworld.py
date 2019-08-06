
# -*- coding: utf-8 -*-


from remi.gui import *


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
        mainContainer = Widget()
        mainContainer.attributes.update({"editor_baseclass":"Widget","editor_tag_type":"widget","editor_newclass":"False","editor_constructor":"()","class":"Widget","editor_varname":"mainContainer"})
        mainContainer.style.update({"width":"266px","position":"absolute","top":"61px","left":"16px","margin":"0px","overflow":"auto","height":"257px"})
        button = Button('Say Hello')
        button.attributes.update({"editor_baseclass":"Button","editor_tag_type":"widget","editor_newclass":"False","editor_constructor":"('Say Hello')","class":"Button","editor_varname":"button"})
        button.style.update({"width":"149px","position":"absolute","top":"80px","left":"37px","margin":"0px","overflow":"auto","height":"29px"})
        mainContainer.append(button,'button')
        label = Label('My label')
        label.attributes.update({"editor_baseclass":"Label","editor_tag_type":"widget","editor_newclass":"False","editor_constructor":"('My label')","class":"Label","editor_varname":"label"})
        label.style.update({"width":"98px","position":"absolute","top":"20px","left":"20px","margin":"0px","overflow":"auto","height":"25px"})
        mainContainer.append(label,'label')
        mainContainer.children['button'].onclick.do(self.onclick_button)
        

        self.mainContainer = mainContainer
        return self.mainContainer
    
    def onclick_button(self, emitter):
        self.mainContainer.children['label'].set_text('hello world')
        pass





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
    
    initcv(cvs.openwin)
    startcv(untitled)

