AidLearnig 
执照

AidLearning FrameWork是一个Linux系统，在Android手机上运行GUI，无需root即可进行AI编程。Aidlearning也是移动设备的Python编程框架。除了Linux环境中可用的一些功能外，AidLearning还支持GUI和神经网络环境。例如，完美支持Caffe，Tensorflow，Mxnet，Gluoncv，ncnn，Keras，Pytorch ..


 

AidLearning是一个在Android上运行的Linux系统，支持GUI，AI和Python。具有Linux + Anroid + AI 3IN1环境的AidLearning项目由Cas大学和耶鲁大学的几名学生开发和维护。

Aid Learning 以简单的方式构建， 支持深度学习的顶级机器学习框架列表。现在我们支持Caffe，Tensorflow，Mxnet，ncnn，Keras，Pytorch，Gluoncv，cv2，scipy ....强大。

此外，我们提供了一个名为Aid_code的AI编码开发工具。它可以通过在我们的框架上使用Python来为您提供可视化的AI编程IDE！这意味着当它安装时，你的Android手机拥有一个带有GUI的Linux系统，可以在PC中编写和运行AI程序。

现在你有一个完整的Linux，在Android上运行GUI（真正的linux运行在busybox而不是虚拟环境。所以它更快，几乎是实时。）并且可以使用Python在视觉上编写你的AI代码！ 


新版本：AidLearning 0.70 
新功能： 

完全支持Python 3和python 2，以及PIP3和PIP2安装 

完全支持Caffe / MXNET / Gluoncv / Tensorflow / Keras / Pytorch / Opencv4 for Python3和Python2 

使用新的CVS包，您可以使用Python代码轻松自定义界面：

CVS。setTitle（“Face Recognize”）
cvs。setInput_dict（usr_dict）
cvs。setSubmitName（“注册你的FaceID”）
cvs。setCamX（350,480）
cvs。setInfoX（320,60）

现在您可以使用apt（apt-get）来安装新的软件包以改善您的Linux环境......

一些BUG已经解决，例如： 
按主页键返回主页然后进入应用程序：问题是返回到终端，而不是返回到GUI。
减少对网络流量的依赖。

为Aid_code IDE添加用于在线运行Python 3和python 2的新按钮 

添加AI示例中心，在网站上放一些示例，将来可以从网站上下载新的示例，以防止安装包的分发过大。

不激活邮箱修改账户可以登录直接，但也有提示激活登录后的界面... 



目录
▣依赖性
▣安装
▣支持AI框架
▣GUI自定义▣SSH 
（连接到PC）
▣主要功能
▣Youtobeshow▣AidLearning的
屏幕截图
▣示例内部
▣Aid_codeIDE▣ 
贡献者
▣参考



依赖
您只需要支持Arm64（aarch64）CPU的Android设备（手机，平板电脑或扶手板）即可。Android版本需要6.0以上。如果你认为参数不够清晰，我想说大多数主流手机都支持它，比如三星，华为，MI，OPPO，VIVO等。另外，对存储空间的要求还是有点大。建议应该有4G免费存储空间。
安装
要安装AidLearing，只需下载应用程序（apk文件）并将其安装在您的移动设备上即可。从http://www.aidlearning.net/downloads/aidlux-05-31.apk 下载
应用程序（apk）只有8M，当你安装apk时，apk会下载框架的depdence是700M和350M的例子使用python的AI代码。所有大约1G大小下载。因此建议您在WiFi环境中安装它。 

支持AI框架
[Caffe] https://github.com/BVLC/caffe
[Tensorflow] https://github.com/tensorflow/tensorflow
[Mxnet] https://github.com/apache/incubator-mxnet
[Keras] https://github.com/keras-team/keras
[ncnn] https://github.com/Tencent/ncnn
[pytorch] https://github.com/pytorch/pytorch
[opencv] https://github.com/opencv/opencv


GUI自定义
现在，您可以使用Python代码轻松自定义GUI！

CVS。setTitle（“Face Recognize”）
cvs。setInput_dict（usr_dict）
cvs。setSubmitName（“注册你的FaceID”）
cvs。setCamX（350,480）
cvs。setInfoX（320,60）




AidLearnig

如上图所示，我们将应用程序划分为四个区域：标题区域，摄像机区域，输入区域，信息显示区域。应用程序显示可以包含一个或多个区域。您可以使用Python（cvs类）语句来操作这些区域的标题，大小和布局。例如：在信息区域，你可以这样做：
cvs。setInfoX（320,60）＃设置信息区
cvs 的宽度，高度。infoshow（“这是信息显示”）＃显示信息区域中的信息
特别是输入区域，我们大大简化了操作过程，你只需要指定一个dict，AidLeaning会自动生成一个表单供你与用户交互，比如你需要注册一个face，你可以这样做： 

usr_dict = {'username'：''，'type'：'add_person'} #define输入列表

cvs.setInput_dict（usr_dict）#gui cvs.setSubmitName的设置

（“注册你的FaceID”）＃设置提交按钮的名称，

这样， aidlearning将产生这个gui：


>>>教程和指南


SSH（连接到PC）

PC可以使用** ssh-keygen **连接到移动设备。在PC中使用ssh-keygen命令生成新的密钥对。命令ssh-keygen在dir中生成id_rsa和id_rsa.pub的文件：〜/ .ssh /

只需要你这样做：打开url：mobilephone'sip：8910 / upload（例如：http：//192.168.1.6：8910 / upload ）在pc上传ssh的文件（id_rsa和id_rsa.pub）。



主要特点：
图形用户界面
我们为Andorid上的Linux修复了图形用户界面（它已经被andorid修剪了！），所以你可以像在电脑上一样使用GUI。例如，您可以使用opencv打开并查看相机！



快速，实时
真正的linux在busybox上运行而不是像VirtulBox这样的虚拟环境。所以它更快，几乎是实时的

使用方便
我们提供了大量示例，通过使用我们的框架，您可以通过点击运行它，然后获取可视日志以显示信息或错误。



随处编码
您可以随时随地在手机上进行编码。每一寸碎片都得到了充分利用。通过灵感的闪现，您的创造力可以立即实现。



＃ 能源之星
根据三星这样的主流智能手机的测试，Aid Learning Framework一天只消耗1％的功耗（待机）




Youtobe秀
[观看视频]（https://youtu.be/bkvNXgCi3_c）




帮助学习的ScreenShot




内部示例：
Facencnn（mobiefacenet ncnn）15fps在手机中

Face Landmark（106关键点ncnn）15fps在手机中

手机（tensorflow）5fps在手机中

单人的身体姿势网（从谷歌转换）10fps在手机上

身体posenet为多人（从谷歌转换）7fps的手机

手机中的程式化图片（GAN）3fps .....



python的Aid_code IDE
我们提供了一个名为Aid_code的AI编码开发工具。它可以通过在我们的框架上使用Python来为您提供可视化的AI编程IDE！使用该工具，您可以在线运行python2或python3代码。因此，您可以随时随地在手机上使用Aid_code IDE进行编码。


当然，您可以在网络上使用Aid_code在线编辑代码。例如，您可以在PC上使用带有Aid_code的Web编码。您只需要打开网址：手机的IP：8900 /，当您的PC和手机在同一个局域网中时。您可以在PC上打开它，例如：http：

//192.168.1.8：8900 /，如果您的手机的IP是192.168.1.8，您可以通过命令ifconfig检查手机的IP（在终端下运行ifconfig）




贡献者
我们邀请任何希望为AidLearning项目做出贡献的人与我们联系。我们主要需要将项目代码的文档翻译成主要语言，包括但不限于法语，西班牙语，葡萄牙语，阿拉伯语等。我们希望世界各地的每个开发人员和研究人员都能从这个项目中受益，而不管他们的母语是什么。
我们特别感谢qidiso在将AidLearning的文档翻译成中文时所做的出色而出色的工作。在下面找到那些对ImageAI项目做出巨大贡献的人的详细联系方式。

bill 
电子邮件： postmaster@aidlearning.com 
网站： http 
： //www.aidlearning.net 问题：@admin 

参考
VTE（libvte）：GTK +的终端模拟器小部件，主要用于gnome-terminal。来源，未决问题和所有（包括已结束）问题。iTerm 2：OS X终端应用程序。来源，问题和文档（包括iTerm2专有转义码）。Konsole：KDE终端应用程序。来源，特别是测试，错误和愿望。hterm：来自Chromium的JavaScript终端实现。来源，包括测试和Google小组。xterm：终端模拟器的祖父。资源。Connectbot：Android SSH客户端。源Android终端仿真器：Termux终端处理基于的Android终端应用程序。非活动。资源。
