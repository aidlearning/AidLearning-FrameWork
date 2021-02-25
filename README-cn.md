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
  

## 简介
[AidLearning](http://www.aidlearning.net)是一个强大的移动端的AI开发平台，它几乎支持所有深度学习神经网络开发的框架和工具。它在移动端（Android）上构架了一个支持图形化界面的完整Linux系统，内置了最为流行的深度学习框架caffe/mxnet/keras/pytorch/tensorflow/ncnn/opencv…内置了可视化AI开发编辑器，内置了最为流行的VSCode、Jupyter等编程工具，支持触摸拖拽式界面设计，支持代码动态调试和运行。支持在移动端和PC端用python开发你的AI应用，支持把你的python源码转化为APP（Apk）发布。支持一键式安装，只需要安装一个10M左右的App即可自动引导完成安装。目前，已在各大App应用中心（华为、小米、vivo、oppo、酷安…）上线，下载和访问量已超150万，内置了大量的AI例子和教程，互联网上（知乎、简书、CSDN、百度等）也有大量中文教程，方便你学习和开发。最新版v0.87中加入cpu加速和GPU加速功能，0.87版内置了tflite_gpu模块，用python就可以把手机的GPU性能充分释放，支持cpu+gpu模式，同时加速！

<img src="http://www.aidlearning.net/git_img/0.jpg" />
<img src="https://www.aidlearning.net/git_img/1.jpg" />
<img src="http://www.aidlearning.net/git_img/2.jpg" />


[立即下载v0.87F2中文版进行安装](https://download.s21i.faiusr.com/23668748/0/0/ABUIABBKGAAg5KKrgQYorcTl-AU?f=aidv0.87F2.apk&v=1613418852) 

## 整体特点
### 创新性
- 移动端（手机）上最好的，环境最全的Linux模拟器，唯一支持图形化桌面的Linux模拟器...
- 唯一支持AI开发环境的模拟器、内置全球最流行Top 7的深度学习框架，内置大量深度学习的模型、例子和开发组件
- 唯一支持python图形化开发和调试的模拟器，支持触摸拖拽式界面设计，提高你的开发效率
- 支持用python开发可运行在手机的App，支持python代码直接编译生成可部署的apk文件
- 一键式安装，无任何依赖，你只需在手机上要安装一个10M的引导App，就可以自动完成所有环境的安装。
- 跨平台开发，支持云桌面（手机桌面和电脑桌面相同），既可以在手机或平版上或其他嵌入式主板上运行，也可以在电脑端基于web直接访问和开发。
- 支持加速库openblas，支持多线程和多进程，运行流畅、不卡顿，充分发挥ARM CPU和GPU的算力
- 最新版本支持python直接调用手机的gpu加速，一般深度学习的tflite模型，30fps～80fps，轻松达到（在主流手机上）
### 通用性
- 支持Tensorflow、Caffe、mxnet、keras、pytorch、ncnn、opencv、scipy....
- 支持Python2.7/Python3.7.3。
- 自带AidCode可视化编程IDE，也支持谷歌的Jupyter的IDE,同时支持微软的VSCode编程开发工具
- 内置完整原生的跨平台桌面，不需要安装第三方vnc等的支持，支持电脑端和手机端同桌面
- 既支持手机、Pad、也支持工业Arm板卡
- 开发的程序，既可以部署在手机端、也可以部署在电脑端
- 支持市面上99.5%的手机，已测试华为、VIVO、OPPO、三星、小米等全系列64位手机
- 支持Linux 原生xfce4桌面，不需要安装VNC等软件
- 支持pyqt5、pygame、turtle、SDL等开发
### 安全性
- Aid在手机上虚拟了一个封闭空间，不需要root，不会破坏你的手机的内容。
- 不会收集你的个人隐私，所有权限都可以自己设定...
### 易用性
- 一键式安装，自动下载最新依赖包、自动配置AI开发需要的环境，降低AI开发门槛
- 内置大量AI组件、模型、例子、教程，降低AI开发的门槛，你可以不懂AI算法，但可以用这个平台开发出AI应用。
- 内置传感器控制包，可方便控制手机上的各种传感器：声音、陀螺仪、位置、摄像头等等
- 一部手机，两个系统，Android和Linux共生共存，无重启自由切换；娱乐、开发、学习三不误
- 支持手机端开发与电脑端开发代码自动同步，支持界面触摸拖拽式设计，自动生成界面的代码
- 一键式编译和发布你开发支持AI的App
- 可扩展支持Java、C++、Go...等语言的支持

### 支持外设
- 内置传感器控制包，可方便控制手机上的各种传感器：声音、陀螺仪、位置、摄像头等等
- 通过OTG USB可支持外设扩展，支持控制Aduino，可对其进行python编程
- 通过OTG USB也可支持外设存储设备读取和写入操作
- 可作为智能机器人的操作系统

## 架构设计
AidLearning FrameWork可以分为Linux模拟器和AI编程平台两部分。

Linux模拟器由Terminal和Desktop构成。前者基于Android底层Linux kernel和busybox命令包构建了完整Linux的模拟器，你可以用apt命令安装任何你需要的依赖包；后者基于web构建了图形化操作桌面，你可以用在手机上用触摸操控整个系统，同时该桌面支持云桌面，你可以在电脑端通过一个网址轻松访达。

AI编程平台由深度学习框架和Python可视化编程框架（Python IDE）构成。前者包含了几乎所有目前流行的深度学习框架，负责模型的加载、计算图的调度；包含各计算的内存分配、Op实现。后则构建了Python可视化快速开发平台，不仅可以在线实时运行、调试Python代码，同时支持触摸拖拽式界面设计、并且可以生成最终的可执行程序、产出apk文件。


## 开始使用
- [安装配置](https://www.aidlearning.net/showdoc/web/#/5?page_id=26)
- [开发文档](https://www.aidlearning.net/showdoc/web/#/5?page_id=23)
- [示例代码](https://www.aidlearning.net/showdoc/web/#/5?page_id=40)

## 内置工具
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

## 贡献与参与
- [贡献代码](https://www.aidlearning.net/showdoc/web/#/5?page_id=39)
- [系统扩展](https://www.aidlearning.net/showdoc/web/#/5?page_id=38)
- [更新日志](https://www.aidlearning.net/showdoc/web/#/5?page_id=24)

##  交流与反馈
- [更多参考](http://code.aidlearning.net)
<img src="https://i.loli.net/2020/04/11/TtfxFj2rnkB7ZVM.png" height="256"/>

- [推特-twitter](https://twitter.com/aidlearning)

- [更多示例](http://code.aidlearning.net)


<img src="https://www.aidlearning.net/git_img/aid-examples.jpg" height="1024"/>

<img src="https://cdn.nlark.com/yuque/0/2020/png/726405/1588573935881-54e2a362-57f2-4afb-9312-a5ccd2355ecf.png"/>

## License
- [GPL 3.0](license.md)


## 致谢
AidLearning参与人员：bill、flay、gondon、willam、gugu、yoline777、qidiso、yuge......

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

