from cv import *
import facerecognition
import numpy as np
# facerecog = facerecognition.FaceRecognition("./models", 0.63)

# img = cv2.imread('point.jpg')
# image_char = img.astype(np.uint8).tostring()
# #facerecog.recognize(img.shape[0], img.shape[1], image_char)
# print 'add person:sxg',img.shape
# ret=facerecog.add_person("sxg", img.shape[0], img.shape[1], image_char)
# print 'ret',ret
# print 'add sucess!'
# img = cv2.imread('sunyi.png')
# image_char = img.astype(np.uint8).tostring()
# facerecog.add_person("sunyi", img.shape[0], img.shape[1], image_char)

def main():
    cap=cvs.VideoCapture(1)
    facerecog = facerecognition.FaceRecognition("./models", 0.73)

    max_none=0
    #facerecog = facerecognition.FaceRecognition("./models",0.6)
    while True:
        sleep(30)
        img =cvs.read()

        if img is None :
            continue
        #imshow(img)
        #continue

        #img=cv2.resize(img,(112,112))
        image_char = img.astype(np.uint8).tostring()
        
        msgType,msgName=cvs.getMsg()
        if msgName!='' and msgType=='add_person':
            ret=facerecog.add_person(msgName, img.shape[0], img.shape[1], image_char)
            if ret==0:
                print 'you add_person is success!'
                cvs.setMsg_status(1)
            else :
                print 'you add_person is failed!'
                cvs.setMsg_status(-1)
                #cv2.putText(img, ret['name'], (int(rect[0]), int(rect[1])-30),cv2.FONT_ITALIC, 2, (77, 255, 9), 2)

            continue #
        
        
        rets = facerecog.recognize(img.shape[0], img.shape[1], image_char)
        
        print 'rets:',rets
        for ret  in  rets:
            #for ret in each:
            print 'draw bounding box for the face'
            rect = ret['rect']
            p1 = (int(rect[0]), int(rect[1]))
            p2 = (int(rect[0]+rect[2]), int(rect[1]+rect[2]))
            
            #draw_name(img, rect, ret['name'])
            cv2.rectangle(img, p1,p2, (0, 255, 0) , 3, 1)
            cv2.putText(img, ret['name'], (int(rect[0]), int(rect[1])-30),cv2.FONT_ITALIC, 2, (77, 255, 9), 2)
            cvs.infoshow('your name:'+ret['name'])
           
            #final = cv2.copyMakeBorder(img,0,0,64,64, cv2.BORDER_CONSTANT,value=[255,255,255])
            #final=cv2.flip(final,1)
        cvs.imshow(img)

if __name__ == '__main__':

    initcv(main)
    startcv()

