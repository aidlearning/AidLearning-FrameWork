 ![](logo.png)
 
 **AidLearning** is a Linux system running on the Android with GUI, AI and  Python support . The [AidLearning](http://www.aidlearning.net) project which have the <b>Linux+Anroid+AI+Python 4in1</b> environments Developed and Maintained by several students from [Cas University](http://english.cas.cn) and [Yale University](https://www.yale.edu).
 
# AidLearning

[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](license.md)  / thank for <b>qidiso</b> provide the [中文说明](https://www.jianshu.com/p/f6ec13ece792)

**AidLearning** builds a Linux system  on Android mobile phone, and supports **GUI**, **Python** and **AI** programming.This means that when it is installed, your Android phone has a Linux system in which you can run Gui programs of python and AI.  Now supports a list of Top Machine Learning Frameworks for Deep Learning: **Caffe, Tensorflow, Mxnet(and Gluoncv), ncnn, Keras, Pytorch, Opencv,Scipy** powerfully build-in!

More Than this，we provide an AI coding develop tool named **Aid_code**. It can provide you a visual AI programming IDE by using Python from **zero** on our framework! It means that when it is installed, your Android phone owned a Linux system with GUI which can write and run AI program in it as same as in pc. In addition,Aid Learning can provide a new visual programming experience of **_touch-and-drag_** by using Python on our framework.

At the same time, **AidLearning** provides wifi-based mapping projection technology, which can project the code of mobile phone to PC and interact with **SSH** remote commands and web online. It can also be projected to TV and projector for large screen display.

In short, **AidLearning** has created a 4in1 and  touch-and-drag platform for rapid development and learning of **Android+Linux+AI+Python**. It can not only use mobile phones for fragmented programming, but also make full use of the development advantages of the two main operating systems (**Android+Linux**) and the perfect AI terminal advantages of mobile phones. With this advantage, **AidLearning** can build a perfect learning ecosphere of programming education.


## ++Dependencies++

All you need is an Android devices (phone ,tablet or arm board)  that supports the CPU of **Arm64(aarch64)**. The Android version requires more than 6.0. If you think the parameters are not clear enough, I would like to say that most of the mainstream mobile phones support it, such as _Samsung, Huawei, MI, OPPO, VIVO, nubia_ etc. In addition, the requirement of storage space is a little big. It is suggested that there should be **4G** free storage space.

##  ++One-click Installation++

To install **AidLearing**, Simply download an App (apk file) and install it on your mobile device. download newest version at :
[ Download v0.74 now!](http://www.aidlearning.net/downloads/aidlux-07-04.apk)  
Other version at:[https://github.com/aidlearning/AidLearning-FrameWork/releases](https://github.com/aidlearning/AidLearning-FrameWork/releases)
 
The  APP （apk） is only 6M，when you install the apk  and launch,the apk will auto download the depdence of the linux and examples of codes . all is about 1G size to download .So it's recommended that you install it _in a wifi environment_.

**Important reminder:**  Click the setting icon after entering the desktop, the dialog box for the camera permission will pop up, please click agree, if you want to use the built-in examples.

## ++Support Powerfully++
---
Support AI Framework:
  * [Caffe]https://github.com/BVLC/caffe
  * [Tensorflow]https://github.com/tensorflow/tensorflow
  * [Mxnet]https://github.com/apache/incubator-mxnet
  * [Keras]https://github.com/keras-team/keras
  * [ncnn]https://github.com/Tencent/ncnn
  * [pytorch]https://github.com/pytorch/pytorch
  * [opencv]https://github.com/opencv/opencv
---

Support Python2.7 and Python3.6.4:

| AidLearning      | Python2.7    |  Python3.6|
| --------- | -------- | -----: | 
| caffe    | ✓1.0.0 | ✓ 1.0.0| 
| mxnet     | ✓1.0.0     |   ✓1.5.0 | 
| tensorflow     | ✓1.10.0     |   ✓1.5.0 | 
| Gluoncv     | ✗  | ✓ 0.40|
| Keras | ✓2.2.4 | ✓2.2.4 |
| Pytorch |  ✗ | ✓1.1.0 |
| Opencv(cv2) | ✓2.4.9 | ✓3.4.6 |
| Scipy | ✓0.18.1 | ✓1.3.0 |
| Numpy | ✓1.14.5 | ✓1.16.3 |

![screen](image/Aiframe.png)

## Touch and Drag Programming Wizard

Now you can easily customize your GUI with touch and drag！Wizard will produce the code automatic like this:

```
class MyApp(App):
 	def __init__(self, *args):
  		super(MyApp, self).__init__(*args)

	def main(self):
		container = gui.VBox(width=120, height=100)
		self.lbl = gui.Label('Hello world!')
		self.bt = gui.Button('Press me!')

	    # setting the listener for the onclick event of the button
		self.bt.onclick.do(self.on_button_pressed)

	    # appending a widget to another, the first argument is a string key
		container.append(self.lbl)
		container.append(self.bt)

	    # returning the root widget
		return container

        #listener function
	def on_button_pressed(self, widget):
		self.lbl.set_text('Button pressed!')
		self.bt.set_text('Hi!')
```

![drag_touch](image/drag_touch.png)
## ++SSH (pc connected)++
PC can connect to mobile by using **ssh-keygen**. Generate a new key pair with <b>ssh-keygen</b> command in your PC.  the command ssh-keygen produce the file of id_rsa and id_rsa.pub in the dir: ~/.ssh/

Just need you do: open the url:mobilephone'sip:8910/upload(for example:http://192.168.1.6:8910/upload)  on the pc to upload ssh's file(id_rsa and id_rsa.pub). 

<img src="image/ssh.png" align = "left" width="300" >

When upload finished , just restart the app on the android ,open the terminal the type this command like this to connect:

```
ssh u0_a311@192.168.1.6 -p8022
```

watch the video:

## Aid_code IDE of python
We provide an AI coding develop tool named **Aid_code**. It can provide you a visual AI programming IDE by using Python from zero on our framework! Using the tool, you can run your python2 or python3 codes online. So ,you can coding with Aid_code IDE on your phone anywhere, anytime. 
<img src="image/Screenshot_2019-07-06-12-21-02-38.png" align = "left" width="175" >  ++_Left on android_++ / ++_Right on pc_++  <img src="image/A15101DB465CDCCA18796F76D8121483.png" align = "right" width="374" >
Of course, you can use Aid_code on the web to edit your code online. For example, you can use web coding with Aid_code on PC. You just need to open the web address: IP of your mobile phone:8900/, when your PC and mobile phone are in the same LAN.
You can open it on a PC, for example:
http://192.168.1.8:8900/
 if your phone's IP is 192.168.1.8, you can check your phone's IP by commanding ifconfig (run ifconfig command under terminal)

## ++Files transfer++

* The sdcard directory on your Android phone has been mapped to the / sdcard directory under AidLearning

* If you install QQ Instant Messaging Tool, the file directory transferred through QQ is mapped to / sdcard / Tencent / QQfile_recv / directory.
![sdcard](image/sdcardshow.png)
## ++Examples inside++
---
* Facencnn(mobiefacenet ncnn) 15fps in mobile phone
* Face Landmark (106 keypoints ncnn) 15fps  in mobile phone
* handpose (tensorflow ) 5fps  in mobile phone
* body posenet for single person(converted from google ) 10fps  in mobile phone
* body posenet for multi-person(converted from google ) 7fps  in mobile phone
* Stylized picture(GAN ) 3fps in mobile phone
![examle](image/examle.png)

## ++References++

* VTE (libvte): Terminal emulator widget for GTK+, mainly used in gnome-terminal. [Source](https://github.com/GNOME/vte), [Open Issues](https://bugzilla.gnome.org/buglist.cgi?quicksearch=product%3A%22vte%22+), and [All (including closed) issues](https://bugzilla.gnome.org/buglist.cgi?bug_status=RESOLVED&bug_status=VERIFIED&chfield=resolution&chfieldfrom=-2000d&chfieldvalue=FIXED&product=vte&resolution=FIXED).
* iTerm 2: OS X terminal application. [Source](https://github.com/gnachman/iTerm2), [Issues](https://gitlab.com/gnachman/iterm2/issues) and [Documentation](http://www.iterm2.com/documentation.html) (which includes [iTerm2 proprietary escape codes](http://www.iterm2.com/documentation-escape-codes.html)).
* Konsole: KDE terminal application. [Source](https://projects.kde.org/projects/kde/applications/konsole/repository), in particular [tests](https://projects.kde.org/projects/kde/applications/konsole/repository/revisions/master/show/tests), [Bugs](https://bugs.kde.org/buglist.cgi?bug_severity=critical&bug_severity=grave&bug_severity=major&bug_severity=crash&bug_severity=normal&bug_severity=minor&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&product=konsole) and [Wishes](https://bugs.kde.org/buglist.cgi?bug_severity=wishlist&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&product=konsole).
* hterm: JavaScript terminal implementation from Chromium. [Source](https://github.com/chromium/hterm), including [tests](https://github.com/chromium/hterm/blob/master/js/hterm_vt_tests.js), and [Google group](https://groups.google.com/a/chromium.org/forum/#!forum/chromium-hterm).
* xterm: The grandfather of terminal emulators. [Source](http://invisible-island.net/datafiles/release/xterm.tar.gz).
* Connectbot: Android SSH client. [Source](https://github.com/connectbot/connectbot)
* Android Terminal Emulator: Android terminal app which Termux terminal handling is based on. Inactive. [Source](https://github.com/jackpal/Android-Terminal-Emulator).
* Termux: Android terminal and Linux environment - app repository. [Source](https://github.com/termux/termux-app).
* remi:Python REMote Interface library. Platform independent. In about 100 Kbytes, perfect for your diet.[Source]
(https://github.com/dddomodossola/remi).
* [Caffe]https://github.com/BVLC/caffe
* [Tensorflow]https://github.com/tensorflow/tensorflow
* [Mxnet]https://github.com/apache/incubator-mxnet
* [Keras]https://github.com/keras-team/keras
* [ncnn]https://github.com/Tencent/ncnn
* [pytorch]https://github.com/pytorch/pytorch
* [opencv]https://github.com/opencv/opencv
