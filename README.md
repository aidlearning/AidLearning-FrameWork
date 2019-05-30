# AidLearning

[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](https://github.com/Yoline777/AidLearning/blob/master/license.md) 

Aid Learning FrameWork is a Linux system with GUI running on Android phone for AI programming without root. Aidlearning is also a Python programming framwork for mobile devices. In addition to some of the features available in the Linux environment, Aidlearning has supported GUI and neural network environments. For example, Caffe, Tensorflow, Mxnet, ncnn, Keras are perfectly supported.

Aidlearning是一个手机可用的Python编程框架。将带GUI的Linux系统移植到手机上，开发者可以高效、方便地进行Python编程。除了一些Linux环境下可用的功能，Aidlearning还加入了GUI(用户图形界面)和深度学习框架，现阶段已经完美支持Caffe, Tensorflow, Mxnet, ncnn, Keras
<p align="center">
<img src="Screenshot_10.jpg"  width="600">

</p>
	
Aid Learning FrameWork is a Linux system with GUI running on Android phone for AI programming without root. It means that when it is installed, your Android phone owned a Linux system with GUI which can run AI program in it. Now we support Caffe, Tensorflow, Mxnet, ncnn, Keras, cv2, Git/SSH powerfully. 

Furthermore we provide an AI coding develop tool named Aid_code. It can provide you a visual AI programming experience by using Python from zero on our framework!

Now you have a complete linux with a GUI running on Android (Real linux running on the busybox and not virtul environment. So it is faster and almost real-time.) and can write your AI code on it visually!

<p align="center">
	<img src="Screen_11.jpg"  width="400" >
</p>

---


### Support most common deep learning frameworks
### 支持大部分常用的深度学习框架
<p align="center">
	<img src="screen4.jpg"  width="400" >
</p>

* [Caffe](https://github.com/BVLC/caffe)
* [Tensorflow](https://github.com/tensorflow/tensorflow)
* [Mxnet](https://github.com/apache/incubator-mxnet)
* [Keras](https://github.com/keras-team/keras)
* [ncnn](https://github.com/Tencent/ncnn)

---

### Instructions
### 使用方法

You just need download the aidlux.apk, and install it, it only 7M size.
* http://www.aidlearning.net.img.800cdn.com/downloads/aidlux-05-10.apk

PC can connect to mobile by using **ssh-keygen**. Generate a new key pair with ***ssh-keygen*** in your PC. Then copy the public half of the key pair to your mobile. For instance, Copy ***/Users/yourname/.ssh/id_rsa.pub*** to your mobile's ***~/.ssh*** and rename it to ***authorized_keys***. Now, you can connenct to your mobile by command ***ssh USER@IP***

A easy method was released:
Just open the url:mobilephone'sip:8910/upload in the pc to upload ssh's file. for example:http://192.168.1.6:8910/upload

---

# Graphical User Interface
We fixed Graphical User Interface for the Linux on Andorid(It has been pruned by andorid!), so you can use the GUI just like on the pc. For instance, You can use opencv to open and view camera!
<p align="center">
	<img src="Screen5.jpg"  width="400" >
</p>

# Fast,Real-Time
Real linux running on the busybox and not virtul environment like VirtulBox. So it is faster and almost real-time

# Easy to use
We provide a plenty of examples and by using our framework, you can run it with a tap, and then get a visual log to show the informations or errors.
<p align="center">
	<img src="screen2.jpg"  width="400" >
</p>

# Coding anywhere
You can coding on your phone anywhere, anytime. Every inch of fragmentation have been fully utilized. Your creativity can be instantly realized with a flash of inspiration.
<p align="center">
	<img src="screen3.jpg"  width="400" >
</p>
# Energy Star

According to the test on the mainstream smartphone like Samsung, Aid Learning Framework only use 1% power consumption in a whole day (Standby)

# Need to occupy mobile phone Size
The entry app program（apk） is only 7M，when you install the apk ,the apk will download the depdence of the framework
is 350M and 350M examples of AI codes using python. all is about 700M size.

# How to work?
You just need download the aidlux.apk[ aidlux.apk](http://www.aidlearning.net/downloads/aidlux-05-10.apk),and install it,it only 7M size.

# Editing code by pc 
  you can open the url:mobilephone'sip:8900/ in the pc to Editing codes files(python files storing in the AidLearnig ) in the pc when the mobile phone and the pc in the same network group.
<p align="center">
	<img src="17693261-84fa9afe825f5b72.jpg"  width="400" >
</p>

# Youtobe show
<p align="center">
[![Watch the video](aidlearning.png)](https://youtu.be/bkvNXgCi3_c)
</p>

# Totally free
you can download the The entry app from the other way:
<p>
[!Download aidlux.apk directly](http://www.aidlearning.net.img.800cdn.com/downloads/aidlux-05-10.apk)
</p>
(have ad)
<p>
[!Download aidlux.apk from website](http://www.aidlearning.net)
<p>(no ad,free totally)

# Examples Inside:
<p>Facencnn(mobiefacenet ncnn) 15fps in mobile phone
<p>Face Landmark (106 keypoints ncnn) 15fps  in mobile phone
<p>handpose (tensorflow ) 5fps  in mobile phone
<p>body posenet for single person(converted from google ) 10fps  in mobile phone
<p>body posenet for multi-person(converted from google ) 7fps  in mobile phone
<p>Stylized picture(GAN ) 3fps in mobile phone
.....
<p align="center">
<img src="screen21.jpg" align = "center" width="200" >
</p>

# New version will be coming in the next week:
* Add python3 supported
* caffe、mxnet 1.5 gluoncv 0.3 tensorflow :1.13.1 keras 2.2.4 pytorch:0.5
   for python3
* more gui customize....
* more examples.....
welcome talk about....see [issues](https://github.com/aidlearning/AidLearning-FrameWork/issues/10)
