from cv import *
import facerecognition
import numpy as np
#facerecog = facerecognition.FaceRecognition("./models", 0.63)

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
    facerecog = facerecognition.FaceRecognition("./models", 0.63)

    max_none=0
    #facerecog = facerecognition.FaceRecognition("./models",0.6)
    while True:
        sleep(30)
        img =cvs.read()

        if img is None :
            continue
        #imshow(img)
        #continue
        img=cv2.flip(img,1)
        #img=cv2.resize(img,(112,112))
        image_char = img.astype(np.uint8).tostring()
        rets = facerecog.getfacepose(img.shape[0], img.shape[1], image_char)

        #print 'rets:',rets
        for ret  in  rets:
            #for ret in each:
            print 'draw bounding box for the face'
            rect = ret['rect']
            print rect
            mtcnn = ret['mtcnn']
            print mtcnn
            for i in range(5):
                cv2.circle(img,(mtcnn[i],mtcnn[5+i]),2,(0,0,255),2)
            keypoint=ret['keypoints']
            #print keypoint
            p1 = (int(rect[0]), int(rect[1]))
            p2 = (int(rect[0]+rect[2]), int(rect[1]+rect[3]))
            
            #draw_name(img, rect, ret['name'])
            cv2.rectangle(img, p1,p2, (0, 255, 0) , 3, 1)
            for p in range(0,106):
                print p*2,' = ',keypoint[p*2]
                print p*2+1,' = ',keypoint[p*2+1]
                k1=int(rect[0]+keypoint[p*2])
                k2=int(rect[1]+keypoint[p*2+1])
                cv2.circle(img,(k1,k2),2,(253,0,0),2)
            #cv2.putText(img, ret['name'], (20, 50),cv2.FONT_ITALIC, 2, (77, 255, 9), 2)
            #final = cv2.copyMakeBorder(img,0,0,64,64, cv2.BORDER_CONSTANT,value=[255,255,255])
            #final=cv2.flip(final,1)
            cvs.imshow(img)

if __name__ == '__main__':

    initcv(main)
    startcv()

