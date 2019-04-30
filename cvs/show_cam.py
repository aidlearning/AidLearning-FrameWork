from cv import *

def main():
    cam=cvs.VideoCapture(0) #open the cam '0'
    fcount=0
    while True:
         sleep(30)
         img = cvs.read()

         fcount=fcount+1

         cvs.imshow(img)
         print 'frames:',fcount

if __name__ == "__main__":
    initcv(main)
    startcv()
