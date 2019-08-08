
from cvs import *

print ('import tensorflow.....wait...')
import tensorflow as tf
import numpy as np
import time

imageSize = 257
width = imageSize
height = imageSize


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

    img = cvs.resize(img, (width,height))
    
    img = img.astype(float)
    img = img * (2.0 / 255.0) - 1.0
    return img

def main():
    cam=cvs.VideoCapture(0)
    detection_graph = load_model("frozen_model.pb")
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image = detection_graph.get_tensor_by_name('image:0')
            heatmaps=detection_graph.get_tensor_by_name('heatmap:0')
            offsets=detection_graph.get_tensor_by_name('offset_2:0')
            displacementFwd=detection_graph.get_tensor_by_name('displacement_fwd_2:0')
            displacementBwd=detection_graph.get_tensor_by_name('displacement_bwd_2:0')

            
            fcount=-1
            start = time.time()
            while True:
                sleep(30)
                img = cam.read()
                if img is None :
                    sleep(50)
                    continue

                    
                fcount=fcount+1
                # global lbs
                lbs = 'Average FPS: '+ str(fcount / (time.time() - start))
                cvs.setLbs(lbs)


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
                    if maxheat>0.7 :
                        cvs.circle(tmpimg, (int(px), int(py)), 3, colors[k], -1)
                        keypoint.append(int(px))
                        keypoint.append(int(py))
                    else :
                        keypoint.append(-1);
                        keypoint.append(-1);
                                                                                                                                                            
                ckeypoint.append(keypoint[0])
                ckeypoint.append(keypoint[1])

                for i in range(1,16,2):
                    # if keypoint[2*i]>keypoint[2*(i+1)] and keypoint[2*(i+1)]>0 :
                    #     ckeypoint.append(keypoint[2*i+2])
                    #     ckeypoint.append(keypoint[2*i+2+1])
                    #     ckeypoint.append(keypoint[2*i])
                    #     ckeypoint.append(keypoint[2*i+1])
                    #     print ('chang:',i,'to',i+1)
                    # else :
                    ckeypoint.append(keypoint[2*i])
                    ckeypoint.append(keypoint[2*i+1])
                    ckeypoint.append(keypoint[2*i+2])
                    ckeypoint.append(keypoint[2*i+2+1])
                                                                                                                                                                         
                for pair in pairs:                                                                                                                                                          
                    if ckeypoint[2*pair[0]]>0 and ckeypoint[2*pair[1]]>0 :
                        cvs.line(tmpimg,(ckeypoint[2*pair[0]],ckeypoint[2*pair[0]+1]),(ckeypoint[2*pair[1]],ckeypoint[2*pair[1]+1]),(0,0,255),1)
            
                cvs.imshow(tmpimg)
                print ('frames:',fcount)



class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)
    
    def idle(self):
        #idle function called every update cycle
        self.lbl.set_text(cvs.getLbs())
        pass    
        
    def main(self):
        #creating a container VBox type, vertical (you can use also HBox or Widget)
        main_container = gui.VBox(width=360, height=680, style={'margin':'0px auto'})
        
        self.aidcam = OpencvVideoWidget(self, width=340, height=480)
        self.aidcam.style['margin'] = '10px'
        
        self.aidcam.set_identifier("myimage_receiver")
        main_container.append(self.aidcam)
        
        #label show fps
        self.lbl = gui.Label('This show FPS!', width=360, height=30,left='100px', margin='10px')
        main_container.append(self.lbl)

        return main_container
        


if __name__ == "__main__":
    initcv(main)
    startcv(MyApp)
