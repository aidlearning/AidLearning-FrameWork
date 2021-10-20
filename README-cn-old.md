<p align="center">
  <img src="https://cdn.nlark.com/yuque/0/2020/png/726405/1578322228096-7dba507c-67f2-463b-a280-791bebed0418.png?x-oss-process=image%2Fresize%2Cw_1492"  width="900">
  <br>
  Linux, AI, Python, GUI: 4-in-1 Environments Running on Android. [中文版] <a href='README.md'>[English]</a>
</p>
<p align="center">
  <a href="https://travis-ci.org/lc-soft/LCUI"><img src="https://travis-ci.org/lc-soft/LCUI.png?branch=master" alt="Build Status"></a>
  <img src="https://img.shields.io/badge/coverage-100%25-brightgreen" alt="Coverage Status">
  <a href="http://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/lc-soft/LCUI.svg" alt="License"></a>
  <a href="https://github.com/aidlearning/AidLearning-FrameWork/releases">
  <img src="https://img.shields.io/github/v/tag/aidlearning/AidLearning-FrameWork" > </a>
<img src="https://img.shields.io/github/forks/aidlearning/AidLearning-FrameWork?style=flat" alt="Fork">
<img src="https://img.shields.io/github/stars/aidlearning/AidLearning-FrameWork?style=flat" alt="star">
<img src="https://img.shields.io/github/last-commit/aidlearning/AidLearning-FrameWork?style=plastic" alt="commit">
</p>

[AidLearning](http://www.aidlearning.net)是一个移动端的AI开发平台，支持所有主流深度学习神经网络的开发框架和工具。

它采用了独特的cpu+gpu加速技术，内置的tflite_gpu模块能够赋予深度学习算法性能上的大幅度提升。同时，AidLearning为开发者提供了VSCode、Jupiter Notebook等开发工具。

目前，AidLearning已在各大App应用中心上线，下载启动次数超过200万。

<img src="http://www.aidlearning.net/showdoc/server/index.php?s=/api/attachment/visitFile/sign/4a72d62cec051582170e99b3584da67c&showdoc=.jpg" width="960" />

<img src="http://www.aidlearning.net/showdoc/server/index.php?s=/api/attachment/visitFile/sign/846b7bfbf009ef144372943dc251c848&showdoc=.jpg"  width="960" />

## 开始使用
点击以下链接即可下载最新的安装包（约20M）：

[【AidLearning v0.87F3】](https://github.com/aidlearning/AidLearning-FrameWork/releases/download/v0.87F3/aidv0.87F3.apk) [【国内镜像】](https://download.s21i.faiusr.com/23668748/0/0/ABUIABBKGAAgsdH_gQYo-PrV4wU?f=aidv0.87F3.apk&v=1614784689) 

- [安装配置](https://www.aidlearning.net/showdoc/web/#/5?page_id=26)
- [开发文档](https://www.aidlearning.net/showdoc/web/#/5?page_id=23)
- [示例代码](https://www.aidlearning.net/showdoc/web/#/5?page_id=40)

## 架构设计

AidLearning FrameWork可以分为Linux环境和AI编程平台两部分。

Linux环境由Terminal和Desktop构成。前者基于Android底层Linux kernel和busybox命令包构建了完整Linux的环境。和原生Linux系统类似，用户可以通过apt命令安装任何依赖包；后者基于web构建了图形化操作桌面，用户可以直接通过触摸屏进行操作。

AidLearning同时提供了云桌面功能，桌面端可以通过局域网访问手机内容。

AI编程平台由深度学习框架和Python可视化编程框架构成。前者包含了所有目前的主流深度学习框架，负责模型的加载、计算图的调度，各计算的内存分配、Op实现。后者构建了Python可视化快速开发平台，不仅可以实时运行、调试Python代码。

用户可以通过AidLearning内置的[apk开发工具](https://www.aidlearning.net/showdoc/web/#/5?page_id=31)设计应用界面、一键编译打包，快速开发人工智能应用。

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

## 交流与反馈

- [AidLearning官网](http://www.aidlearning.net) 
- [AidLearning官方论坛](http://new.aidlearning.net/)

<details>
<summary>QQ交流群</summary>
<img src="https://i.loli.net/2020/04/11/TtfxFj2rnkB7ZVM.png" height="256"/>
</details>

## License
- [GPL 3.0](license.md)

## 致谢
AidLearning参与人员：bill、flay、gondon、willam、gugu、yoline777、qidiso、yuge等。

下列项目：

* VTE (libvte): Terminal emulator widget for GTK+, mainly used in gnome-terminal. [Source](https://github.com/GNOME/vte), [Open Issues](https://bugzilla.gnome.org/buglist.cgi?quicksearch=product%3A%22vte%22+), and [All (including closed) issues](https://bugzilla.gnome.org/buglist.cgi?bug_status=RESOLVED&bug_status=VERIFIED&chfield=resolution&chfieldfrom=-2000d&chfieldvalue=FIXED&product=vte&resolution=FIXED).
* iTerm 2: OS X terminal application. [Source](https://github.com/gnachman/iTerm2), [Issues](https://gitlab.com/gnachman/iterm2/issues) and [Documentation](http://www.iterm2.com/documentation.html) (which includes [iTerm2 proprietary escape codes](http://www.iterm2.com/documentation-escape-codes.html)).
* Konsole: KDE terminal application. [Source](https://projects.kde.org/projects/kde/applications/konsole/repository), in particular [tests](https://projects.kde.org/projects/kde/applications/konsole/repository/revisions/master/show/tests), [Bugs](https://bugs.kde.org/buglist.cgi?bug_severity=critical&bug_severity=grave&bug_severity=major&bug_severity=crash&bug_severity=normal&bug_severity=minor&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&product=konsole) and [Wishes](https://bugs.kde.org/buglist.cgi?bug_severity=wishlist&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&product=konsole).
* hterm: JavaScript terminal implementation from Chromium. [Source](https://github.com/chromium/hterm), including [tests](https://github.com/chromium/hterm/blob/master/js/hterm_vt_tests.js), and [Google group](https://groups.google.com/a/chromium.org/forum/#!forum/chromium-hterm).
* xterm: The grandfather of terminal emulators. [Source](http://invisible-island.net/datafiles/release/xterm.tar.gz).
* Connectbot: Android SSH client. [Source](https://github.com/connectbot/connectbot)
* Android Terminal Emulator: Android terminal app which Termux terminal handling is based on. Inactive. [Source](https://github.com/jackpal/Android-Terminal-Emulator).
* Termux: Android terminal and Linux environment - app repository. [Source](https://github.com/termux/termux-app).
* remi:Python REMote Interface library. Platform independent. In about 100 Kbytes, perfect for your diet.[Source](https://github.com/dddomodossola/remi).
* [Caffe](https://github.com/BVLC/caffe)
* [Tensorflow](https://github.com/tensorflow/tensorflow)
* [Mxnet](https://github.com/apache/incubator-mxnet)
* [Keras](https://github.com/keras-team/keras)
* [ncnn](https://github.com/Tencent/ncnn)
* [pytorch](https://github.com/pytorch/pytorch)
* [opencv](https://github.com/opencv/opencv)
