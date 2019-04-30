We create a cvs class to show the gui instead of cv2 class of opencv
how to use：
1. from cv import *
use this ,actually you import cv2,cvs and other function initcv(),startcv
2. we use the cvs.VideoCapture() instead the cv2.VideoCapture() if you want to open the camera
   we use the cvs.imread() instead the cv2.imread() if you want to open one image
3. we use the cvs.imshow() instead the cv2.imshow() to show the img or frames
4. we use the initcv(),startcv function to use the multi-thread to balance the performence

