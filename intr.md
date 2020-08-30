![AidLearning](https://cdn.nlark.com/yuque/0/2020/png/726405/1578322228096-7dba507c-67f2-463b-a280-791bebed0418.png?x-oss-process=image%2Fresize%2Cw_1492)
  <p align="center">
    Linux+AI+Python+GUI 4in1 Environments Running on the Android . <a href='README-cn.md'>[中文版]</a> <a href='README.md'>[English]
  </p>
  <p align="center">
    <a href="https://travis-ci.org/lc-soft/LCUI"><img src="https://travis-ci.org/lc-soft/LCUI.png?branch=master" alt="Build Status"></a>
    <img src="https://img.shields.io/badge/coverage-100%25-brightgreen" alt="Coverage Status">
    <a href="http://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/lc-soft/LCUI.svg" alt="License"></a>
    <a href="https://github.com/aidlearning/AidLearning-FrameWork/releases">
    <img src="https://img.shields.io/github/v/tag/aidlearning/AidLearning-FrameWork" > </a>
    <img src="https://img.shields.io/badge/repo%20size-37%20MB-blue" alt="Repo size">
    <img src="https://img.shields.io/badge/code%20size-11.83%20MB-blue" alt="Code size">
<img src="https://img.shields.io/github/forks/aidlearning/AidLearning-FrameWork?style=flat" alt="Fork">
<img src="https://img.shields.io/github/stars/aidlearning/AidLearning-FrameWork?style=flat" alt="star">
<img src="https://img.shields.io/github/last-commit/aidlearning/AidLearning-FrameWork?style=plastic" alt="commit">

</p>


## Intro
[AidLearning](http://www.aidlearning.net) is a powerful mobile AI development platform, which supports almost all frameworks and tools for deep learning neural network development. It has built a complete Linux OS supporting GUI desktop on Android, built-in the most popular deep learning framework Caffe / mxnet / keras / Python / tensorflow / ncnn / opencv... Built in Visual AI development IDE, built-in most popular programming tools such as VSCode and Jupyter, supporting touch-and-drop ui design, supporting dynamic debugging and running of code. Support the development of AI applications in Python on mobile and pad, and support the package your Python source code into app (APK) to release. One click installation is supported. You only need to install a 10m app to automatically boot to complete the installation. At present, it has been online in major app application centers, with more than 1.5 million downloads and visits, and a large number of AI examples and tutorials are built-in. There are also a large number of tutorials on the Internet to facilitate your learning and development.
<img src="http://www.aidlearning.net/git_img/0.jpg" />
<img src="https://www.aidlearning.net/git_img/1.jpg" />
<img src="http://www.aidlearning.net/git_img/2.jpg" />


[Download the v0.86b2f3 now!](http://23668748.s21d-23.faiusrd.com/0/ABUIABBKGAAggZnz_QUosomgnAQ?f=aid-0.86b2f3.apk&v=1597820033) 

## Features
### Innovation
- The best Linux environment on android terminal (mobile phone), the only Linux os that supports GUI desktop without vnc running on the android.
- It is the only simulator that supports AI development environment, built-in deep learning framework with the world's most popular top 7, and a large number of deep learning models, examples and development components
- The only simulator that supports Python Visual development and debugging supports touch and drag interface design to improve your development efficiency
- It supports the development of apps that can run on mobile phones with Python, and supports the direct compilation of Python code to generate deployable APK files
- One click installation, without any dependence, you only need to install a 10m boot app on your mobile phone, and you can automatically complete the installation of all environments.
- Cross platform development, support cloud desktop (mobile desktop and computer desktop are the same), can not only run on mobile phone or tablet or other embedded motherboard, but also can be directly accessed and developed on the computer side based on Web.
- It supports openblas, multi thread and multi process, runs smoothly without jamming, and gives full play to the computing power of ARM CPU and GPU

### Versatility
- Support Tensorflow, Caffe, mxnet, keras, python, ncnn, opencv, SciPy
- Supports Python 2.7 / Python 3.7.3.
- Buildin AidCode visual programming IDE, it also supports Jupyter notebook and Microsoft's vscode programming development tool.
- Built in complete and native cross platform desktop, no need to install third-party VNC support, support the same desktop of computer and mobile phone
- It supports not only mobile phone/pad, but also industrial arm board
- The developed program can be deployed on both mobile phone and computer
- It supports 99.5% of the mobile phones on the market, and has tested a full series of 64 bit mobile phones such as Huawei, vivo, oppo, Samsung and Xiaomi
- Support Linux native xfce4 desktop, do not need to install VNC and other software
- Support the development of pyqt5, pyGame, vortex, SDL, etc

### Safety
- Aid virtualizes a closed space on the mobile phone. It doesn't need root and won't destroy the content of your mobile phone.
- Will not collect your personal privacy, all permissions can be set by yourselves
### Easy to use
- One click installation, automatically download the latest dependency package, automatically configure the environment required for AI development, and reduce the threshold of AI development
- Built in a large number of AI components, models, examples, tutorials, reduce the threshold of AI development, you can not understand AI algorithm, but you can use this platform to develop AI applications.
- The built-in sensor control package can easily control various sensors on the mobile phone: sound, gyroscope, position, camera, etc
- One mobile phone, two systems, Android and Linux co-exist, no restart, free switching; entertainment, development, learning three not wrong
- It supports the automatic synchronization of mobile phone development and computer development code, supports interface touch and drag design, and automatically generates interface code
- One click compilation and release of AI enabled apps
- Extensible support Java, C + +, go... And other languages

### support peripherals
- 内置传感器控制包，可方便控制手机上的各种传感器：声音、陀螺仪、位置、摄像头等等
- 通过OTG USB可支持外设扩展，支持控制Aduino，可对其进行python编程
- 通过OTG USB也可支持外设存储设备读取和写入操作
- 可作为智能机器人的操作系统

## Architecture
AidLearning FrameWork可以分为Linux模拟器和AI编程平台两部分。

Linux模拟器由Terminal和Desktop构成。前者基于Android底层Linux kernel和busybox命令包构建了完整Linux的模拟器，你可以用apt命令安装任何你需要的依赖包；后者基于web构建了图形化操作桌面，你可以用在手机上用触摸操控整个系统，同时该桌面支持云桌面，你可以在电脑端通过一个网址轻松访达。

AI编程平台由深度学习框架和Python可视化编程框架（Python IDE）构成。前者包含了几乎所有目前流行的深度学习框架，负责模型的加载、计算图的调度；包含各计算的内存分配、Op实现。后则构建了Python可视化快速开发平台，不仅可以在线实时运行、调试Python代码，同时支持触摸拖拽式界面设计、并且可以生成最终的可执行程序、产出apk文件。


## Quick start
- [安装配置](https://www.aidlearning.net/showdoc/web/#/5?page_id=26)
- [开发文档](https://www.aidlearning.net/showdoc/web/#/5?page_id=23)
- [示例代码](https://www.aidlearning.net/showdoc/web/#/5?page_id=40)

## Buildin Tools
- [AidCode](https://www.aidlearning.net/showdoc/web/#/5?page_id=28)
- [文件管理器](https://www.aidlearning.net/showdoc/web/#/5?page_id=27)
- [云桌面icloud](https://www.aidlearning.net/showdoc/web/#/5?page_id=29)
- [Blocky积木编程](https://www.aidlearning.net/showdoc/web/#/5?page_id=34)
- [Service-依赖包、系统服务](https://www.aidlearning.net/showdoc/web/#/5?page_id=33)
- [Apkbuild](https://www.aidlearning.net/showdoc/web/#/5?page_id=31)
- [Jupyter notebook](https://www.aidlearning.net/showdoc/web/#/5?page_id=30)
- [X模式--兼容开发模式](https://www.aidlearning.net/showdoc/web/#/5?page_id=36)
- [VSCode](https://www.aidlearning.net/showdoc/web/#/5?page_id=32)
- [XFce4-Linux原生桌面](https://www.aidlearning.net/showdoc/web/#/5?page_id=35)

## Expansion
- [贡献代码](https://www.aidlearning.net/showdoc/web/#/5?page_id=39)
- [系统扩展](https://www.aidlearning.net/showdoc/web/#/5?page_id=38)
- [更新日志](https://www.aidlearning.net/showdoc/web/#/5?page_id=24)

##  FeedBack
- [更多参考](http://code.aidlearning.net)
<img src="https://i.loli.net/2020/04/11/TtfxFj2rnkB7ZVM.png" height="256"/>

- [推特-twitter](https://twitter.com/aidlearning)

- [更多示例](http://code.aidlearning.net)


<img src="https://cdn.nlark.com/yuque/0/2020/png/726405/1588573935881-54e2a362-57f2-4afb-9312-a5ccd2355ecf.png"/>


## License
- [GPL 3.0](license.md)


## Thanks
AidLearning参与人员：bill，耶鲁大学gondon、中科院大学yoline777、qidiso。

AidLearning参考、借鉴了下列项目（目前是测试阶段，未来我们会逐步开源）：

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

