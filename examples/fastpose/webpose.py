from cv import *
cap=cvs.VideoCapture(0)
print 'import tensorflow.....wait...'
import tensorflow as tf
import cv2
import numpy as np

imageSize = 257
width = imageSize
height = imageSize
#import imutils
#from imutils.video import VideoStream
#import urllib2

#from cv import VideoCapture,imshow,initcv,startcv,sleep
#from cv import *
def load_model(PATH_TO_CKPT):
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    return detection_graph

def resizeimg(img, width, height):
    #img = cv2.imread(path)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (width,height))
    
    img = img.astype(float)
    img = img * (2.0 / 255.0) - 1.0
    return img

def main():
    #cam=cvs.VideoCapture(0)
    detection_graph = load_model("frozen_model.pb")
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image = detection_graph.get_tensor_by_name('image:0')
            heatmaps=detection_graph.get_tensor_by_name('heatmap:0')
            offsets=detection_graph.get_tensor_by_name('offset_2:0')
            displacementFwd=detection_graph.get_tensor_by_name('displacement_fwd_2:0')
            displacementBwd=detection_graph.get_tensor_by_name('displacement_bwd_2:0')

            
            #img = cam.read()
            fcount=0

            while True:
                sleep(30)
                img = cvs.read()
                if img is None :
                    sleep(50)
                    continue
                    # img=cv2.imread('/loading.png')
                    # if img is None:
                    #     continue
                    # else:
                    #     imshow(img)
                    
                fcount=fcount+1
                #if fcount%5!=1 :
                #    continue

                input_image = resizeimg(img,width,height)
                tmpimg = img
                tmpimg = cv2.resize(tmpimg, (width,height))
            
            
                input_image = np.array(input_image,dtype=np.float32)
                input_image = input_image.reshape(1,width,height,3)
                heatmaps_result,offsets_result,displacementFwd_result,displacementBwd_result = sess.run(
                        [heatmaps,offsets,displacementFwd,displacementBwd], feed_dict={ image: input_image } )
                colors = [[255, 0, 0], [255, 170, 0], [255, 170, 0],[255, 255, 0], [255, 255, 0], [170, 255, 0], [170, 255, 0], [0, 255, 0],
                      [0, 255, 0], [0, 255, 170], [0, 255, 170], [0, 170, 255], [0, 170, 255], [0, 0, 255], [0, 0, 255],
                      [255, 0, 255], [255, 0, 255]]
                #myList  = [0 for i in range(64*64)]
                #for i in range(64*64):
                #    myList[i]=' '
                #pairs = [[8,9],[11,12],[11,10],[2,1],[1,0],[13,14],[14,15],[3,4],[4,5],[8,7],[7,6],[6,2],[6,3],[8,12],[8,13]]
            
                pairs = [[5,6],[5,7],[6,8],[7,9],[8,10],[5,11],[6,12],[11,12],[11,13],[12,14],[13,15],[14,16]]
                keypoint = []
                ckeypoint = []

                heatmaps_result = heatmaps_result[0]
                aaaa= np.transpose(heatmaps_result,(2, 0, 1))
                offsets_result=offsets_result[0]
                bbb= np.transpose(offsets_result,(2, 0, 1))

                for k in range(0,17):
                    heatmaps_result=aaaa[k]
                    maxheat=np.max(heatmaps_result)
                    re=np.where(heatmaps_result==maxheat)
                
                    ry=re[0][0]
                    rx=re[1][0]
                    offsets_resulty=bbb[0+k]
                    offsets_resultx=bbb[17+k]
                    ofx=int(offsets_resultx[ry][rx]+0.5)
                    ofy=int(offsets_resulty[ry][rx]+0.5)
           
                    px=(rx)*16+ofx
                    py=(ry)*16+ofy
                    if maxheat>0.2 :
                        cv2.circle(tmpimg, (int(px), int(py)), 3, colors[k], -1)
                        keypoint.append(int(px))
                        keypoint.append(int(py))
                    else :
                        keypoint.append(-1);
                        keypoint.append(-1);
                                                                                                                                                            
                ckeypoint.append(keypoint[0])
                ckeypoint.append(keypoint[1])

                for i in range(1,16,2):
                    if keypoint[2*i]>keypoint[2*(i+1)] and keypoint[2*(i+1)]>0 :
                        ckeypoint.append(keypoint[2*i+2])
                        ckeypoint.append(keypoint[2*i+2+1])
                        ckeypoint.append(keypoint[2*i])
                        ckeypoint.append(keypoint[2*i+1])
                        print 'chang:',i,'to',i+1
                    else :
                        ckeypoint.append(keypoint[2*i])
                        ckeypoint.append(keypoint[2*i+1])
                        ckeypoint.append(keypoint[2*i+2])
                        ckeypoint.append(keypoint[2*i+2+1])
                                                                                                                                                                         
                for pair in pairs:                                                                                                                                                          
                    if ckeypoint[2*pair[0]]>0 and ckeypoint[2*pair[1]]>0 :
                        cv2.line(tmpimg,(ckeypoint[2*pair[0]],ckeypoint[2*pair[0]+1]),(ckeypoint[2*pair[1]],ckeypoint[2*pair[1]+1]),(0,0,255),1)
            
                cvs.imshow(tmpimg)
                print 'frames:',fcount

            
                #if cv2.waitKey(1) & 0xFF == ord('q'):
                #    break

if __name__ == "__main__":
    initcv(main)
    startcv()
