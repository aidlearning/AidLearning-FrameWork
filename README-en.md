<p align="center">
  <img src="https://aidlux.com/logo.svg"  width="900">
  <br>
  Linux, AI, Python, GUI: 4-in-1 Environments Running on Android. <a href='README.md'>[中文版]</a> [English]
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

[AidLearning](http://www.aidlearning.net) is a mobile AI development platform that supports all mainstream development frameworks and tools for deep learning and neural networks.

It has a unique cpu+gpu+npu(dsp) acceleration technology, that brings a significant boost on performance of deep-learning algorithm by the built-in aidlite module. At the same time, AidLearning also provides developers with popular development tools, such as VSCode and Jupyter Notebook.

<a href="https://www.youtube.com/watch?v=VaG12AsujNE&t=5s" target="_blank"><img src="https://docs.aidlux.com/intro/ai/desktop_1.png" width="100%" ></a>
<p align="center"><a href="https://www.youtube.com/watch?v=VaG12AsujNE&t=5s" target="_blank">AidLux 1.0 is officially released! (Click to watch video ⬆️ 📺)</a></p>

## Usage
The lastest version of release is in the link below (About 388MB):

[【AidLearning v0.90PRE】](https://github.com/aidlearning/AidLearning-FrameWork/releases/download/0.90PRE/AidLux0.90PRE.apk)

- [Install and Config](https://www.aidlearning.net/showdoc/web/#/5?page_id=26)
- [Dev Docs](https://www.aidlearning.net/showdoc/web/#/5?page_id=23)
- [Sample Code](https://www.aidlearning.net/showdoc/web/#/5?page_id=40)

## Architecture

There're two parts of the AidLearning framework: the Linux environment and the AI programming platform.

The Linux environment is composed of Terminal and Desktop. A complete Linux environment on Android is built underlying Linux kernel and busybox command package. Similar to the original Linux system, users can install any dependency package through `apt` command. Also, a graphical operating desktop based on web is provided for users, which can help them operate directly through touching screen.

AidLearning also provides a cloud desktop function, which means the mobile device is accessable via LAN for computers with Aidlearning Framework.

The AI programming platform part consists of a deep learning framework and a Python visual programming framework. AidLearning contains all the current mainstream deep learning frameworks, which are responsible for model loading, scheduling of computational graphs, memory allocation for each computation, and Op implementation. Mean while, a python visualization development platform, which can run and debug Python code in real time, is created for developers. They can design the app's interface, compile and package it with one click, and quickly develop AI applications through AidLearning's built-in [apk dev-tools](https://www.aidlearning.net/showdoc/web/#/5?page_id=31).

## Built-in Tools
- [AidCode](https://docs.aidlux.com/)
- [File Manager](https://docs.aidlux.com/)
- [icloud](https://docs.aidlux.com/)
- [Blocky](https://docs.aidlux.com/)
- [Service](https://docs.aidlux.com/)
- [Apkbuild](https://docs.aidlux.com/)
- [Jupyter notebook](https://docs.aidlux.com/)
- [X Mode](https://docs.aidlux.com/)
- [VSCode](https://docs.aidlux.com/)
- [XFce4](https://docs.aidlux.com/)

## Contribution to AidLearning
- [Code Contributions](https://docs.aidlux.com/)
- [System Extends](https://docs.aidlux.com/)
- [Update Logs](https://docs.aidlux.com/)

## Community & Feedback

- [AidLearning Official Website](http://www.aidlearning.net) 
- [AidLearning Forum](http://new.aidlearning.net/)

<details>
<summary>Groupchat in QQ</summary>
<img src="https://i.loli.net/2020/04/11/TtfxFj2rnkB7ZVM.png" height="256"/>
</details>

## License
- [GPL 3.0](license.md)

## Acknowledgements
Contributors：bill、flay、gondon、willam、gugu、yoline777、qidiso、yuge、muzi_ys

Repos list below：

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
* [macUI](https://github.com/1099438829/macUI)
