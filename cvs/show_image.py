from cv import *
# instead, you can do this 'from cv import cv2,cvs,initcv,startcv'


def main():
    img=cv2.imread("point.jpg")
    print 'show image in the aid learning!'
    cvs.imshow(img,20)
    
    
if __name__ == '__main__':
    
    initcv(main)
    startcv()
