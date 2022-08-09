<a href="https://www.bilibili.com/video/BV1p3411x7iX" target="_blank"><img src="https://community.aidlux.com/_nuxt/img/logo1.9883420.svg" width="100%" ></a>
<p align="center"><a href="https://www.bilibili.com/video/BV1p3411x7iX" target="_blank">AidLux 1.0 正式发布！(观看视频⬆️📺)</a></p>
<p align="center">
  AI，Android，Linux，ARM：基于Android+Linux融合生态的AI应用开发平台。 <a href='README-en.md'>[English]</a>
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
[AidLux](https://docs.aidlux.com) 是一个基于ARM构建，同时支持多生态融合（Android+Linux）环境的AI应用开发和部署平台，为开发者带来强大、简单、无限创意可能的奇妙体验！ 
<img src="https://docs.aidlux.com/intro/images/linux应用01.png" alt="AidLux" width="100%">

## AidLux融合架构，实现多生态超级叠加 

<img src="https://aidlux.com/platform/double-system.png" alt="AidLux融合架构" width="70%"> 

通过共享Android Linux kernel构建了完整的Linux系统环境，并且与Android系统环境同时提供用户访问。在为用户提供和原生Linux系统类似的命令行使用体验（如通过 `apt` 命令进行包管理）的同时，基于Web构建了图形化桌面环境，用户可以直接通过触摸屏或浏览器访问。 

AidLux补全了AI运行所需的所有基础科学计算包/库，支持了业界主流深度学习框架，并内置自主研发的AI智能加速技术，为开发者提供了一个“AI 就绪”的应用开发平台。 

-----

### Android+Linux 共生, 1+1>2 

* 一部设备同时运行两个系统环境，既是一部Android设备，同时也是一部Linux设备。两个生态的资源优势可同时被加以利用。 

<img src="https://aidlux.com/github/appcenter_all.png" alt="应用中心" width="100%"> 

* 跨系统无缝交互，高效，安全，稳定。Android应用与Linux应用实现本地高效直接访问，无需外部接口（如网络），充分释放硬件效能。 Android负责用户交互，Linux负责服务支持的新型应用形态等待你的奇思妙想。

* 针对已有应用（Android或Linux），可轻松获得跨系统功能支持，使应用功能更加强大，充分保护已有开发投入。 

* 一键安装、自动部署、App式启动，过程快速、简单。 

<img src="https://aidlux.com/github/deploy_start_desk.png" alt="应用中心" width="100%"> 

---

### 低AI开发门槛, 快速、简单、极致性能

* 集成业界主流AI深度学习框架，无需配置，安装即用，极大的降低了AI开发和应用部署的环境配置复杂度，大幅减少了相关的时间投入。 框架支持如下：
  |TensorFlow|PyTorch|Caffe|MXNet|Keras|MindSpore|PandlePandle|TNN|MNN|OpenCV|
  |:---:|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
  |√|√|√|√|√|√|√|√|√|√| 
  
* 内置创新性的CPU+GPU+NPU智能加速技术，通过“硬件+框架+Op"多层优化，赋予深度学习运算性能的大幅度提升。并且提供统一API接口，在方便开发者调用的同时，还支持不同AI框架模型自动转换。以下测试为基于相同ARM设备，在Linux、AidLux上测试获得。单项测试进行20次取耗时（纵轴）平均值。

<img src="https://aidlux.com/github/pete_result.png" alt="性能对比图" width="100%"> 

* 在Wizard中进行拖拽式AI应用开发，AI组件快速赋能，1分钟生成你的第一个AI应用！ 

<img src="https://aidlux.com/github/wizard_ai.jpg" alt="Wizard" width="100%"> 

* 内置丰富AI应用案例及对应代码，方便开发者能快速入门。通过AidLux桌面应用中心或以下命令安装例子： 
  
```
aid install examples-gpu 
#进入案例目录 
cd /home/examples-gpu 
```

<table>
<div style="width: 100%; display: flex; flex-wrap: wrap; justify-content: space-around; align-items: center;">
    <div style="margin: 20px 0; flex: 1 1 33.33%; display: flex; justify-content: center; align-items: center;">
      <img style="width: 330px;height: 410px;" src="https://aidlux.com/github/demo_facemesh_c.gif" title="人脸关键点识别" alt="人脸关键点识别">
    </div>
    <div style="margin: 20px 0; flex: 1 1 33.33%; display: flex; justify-content: center; align-items: center;">
      <img style="width: 330px;height: 410px;" src="https://aidlux.com/github/demo_pose_c.gif" title="肢体识别" alt="肢体识别">
    </div>
    <div style="margin: 20px 0; flex: 1 1 33.33%; display: flex; justify-content: center; align-items: center;">
      <img style="width: 330px;height: 410px;" src="https://aidlux.com/github/demo_objectron_c.gif" title="3D检测" alt="3D检测">
    </div>
    <div style="margin: 20px 0; flex: 1 1 33.33%; display: flex; justify-content: center; align-items: center;">
<img style="width: 330px;height: 410px;" src="https://aidlux.com/github/demo_hair_recoloring_c.gif" title="头发识别" alt="头发识别">
    </div>
<div style="margin: 20px 0; flex: 1 1 33.33%; display: flex; justify-content: center; align-items: center;">
<img style="width: 330px;height: 410px;" src="https://aidlux.com/github/demo_hand_tracking_c.gif" title="手势识别" alt="手势识别">
    </div>
    <div style="margin: 20px 0; flex: 1 1 33.33%; display: flex; justify-content: center; align-items: center;">
      <img style="width: 330px;height: 410px;" src="https://aidlux.com/github/demo_face_detector_c.gif" title="人脸识别" alt="人脸识别">
    </div>
    <div style="margin: 20px 0; flex: 1 1 33.33%; display: flex; justify-content: center; align-items: center;">
      <img style="width: 330px;height: 410px;" src="https://docs.aidlux.com/static/faceswap.png" title="换脸" alt="换脸">
    </div>
    <div style="margin: 20px 0; flex: 1 1 33.33%; display: flex; justify-content: center; align-items: center;">
      <img style="width: 330px;height: 410px;" src="https://docs.aidlux.com/static/demo_object_detector.jpg" title="物体识别跟踪" alt="物体识别跟踪">
    </div>
    <div style="margin: 20px 0; flex: 1 1 33.33%; display: flex; justify-content: center; align-items: center;">
      <img style="width: 330px;height: 410px;" src="https://aidlux.com/github/demo_persionseg_c.gif" title="人体抠图" alt="人体抠图">
    </div>
  </div>
</table> 



更多案例，请访问 [AI应用案例中心](https://docs.aidlux.com/#/examples) 

----

### 便携、开放、一站式
* AidLux 云桌面系统，支持从PC, 平板, 手机等多种屏幕随时随地同时访问，实现你的超级移动开发平台。 快通过PC上的浏览器，输入云桌面地址，访问你手机上的AidLux桌面吧！

<table>
<div style="width: 100%; display: flex; justify-content: space-around; align-items: center;">
<img style="width: 74%;" src="https://aidlux.com/github/desktop_mob.png" alt="Desktop 手机">
<img style="width: 74%;" src="https://aidlux.com/github/desktop_pc.png" alt="Desktop PC">
</div>
</table> 

* 海量外设轻松支持(网络、USB、串口、...)，创意空间无限扩展。 

<table>
<div style="width: 100%; display: flex; align-items: center;">
<img style="width: 350px;margin: 0 10px;" src="https://aidlux.com/github/aid_arduino.png" alt="AidLux+Arduino">
      <img style="width: 350px; margin: 0 20px;" src="https://aidlux.com/github/toy.png" alt="小车">
      <img style="width: 350px;margin: 0 20px;" src="https://aidlux.com/github/demo_car_follow_c.gif" alt="跟随">
  </div>
</table> 

* 支持VSCode, Jupyter notebook 等多种开源开发工具及Python, C/C++, Java, JavaScript等开发语言。 

<img src="https://aidlux.com/github/aidcode.jpg" alt="AidCode" width="100%"> 

* 一站式开发、测试、部署全流程支持，AidLux关注效率，您关注创意！ `ApkBuild`应用，可以快速将基于Python开发的项目打包成APK进行发布，方便用户在其它Android系统进行部署。

----

#### 目前，AidLux已在各大App应用中心上线，下载启动次数超过200万。


## 开始使用
点击以下链接即可下载最新的安装包（约390M）：

[【AidLux v0.90PRE】](https://github.com/aidlearning/AidLearning-FrameWork/releases/download/0.90PRE/AidLux0.90PRE.apk) 

- [安装配置](https://docs.aidlux.com/#/quickstart)
- [开发文档](https://docs.aidlux.com/#/devdocs)
- [AI应用案例中心](https://docs.aidlux.com/#/examples)

## 内置工具
- [AidCode](https://docs.aidlux.com/#/tools?id=aidcode)
- [Wizard](https://docs.aidlux.com/#/tools?id=wizard)
- [文件管理器](https://docs.aidlux.com/#/tools?id=%e6%96%87%e4%bb%b6%e7%ae%a1%e7%90%86%e5%b7%a5%e5%85%b7-filebrowser)
- [云桌面Cloud_ip](https://docs.aidlux.com/#/tools?id=%e4%ba%91%e6%a1%8c%e9%9d%a2cloud_ip)
- [Blocky积木编程](https://docs.aidlux.com/#/tools?id=%e7%a7%af%e6%9c%a8%e7%bc%96%e7%a8%8b)
- [Apkbuild](https://docs.aidlux.com/#/tools?id=apkbuildapk%e7%94%9f%e6%88%90%e5%b7%a5%e5%85%b7)
- [Jupyter notebook](https://docs.aidlux.com/#/tools?id=jupyter)
- [VSCode](https://docs.aidlux.com/#/tools?id=vscode)
- [XFce4-Linux原生桌面](https://docs.aidlux.com/#/tools?id=xfce)

## 贡献与参与
- [贡献代码](https://www.aidlearning.net/showdoc/web/#/5?page_id=39)
- [系统扩展](https://www.aidlearning.net/showdoc/web/#/5?page_id=38)
- [更新日志](https://docs.aidlux.com/#/changelog)

## 交流与反馈

- [AidLux官网](https://www.aidlux.com/) 
- [AidLux官方论坛](https://community.aidlux.com/)

<details>
<summary>QQ交流群</summary>
<img src="https://i.loli.net/2020/04/11/TtfxFj2rnkB7ZVM.png" height="256"/>
</details>

## License
- [GPL 3.0](license.md)

## 致谢
AidLux参与人员：bill、flay、gondon、willam、gugu、yoline777、qidiso、yuge、muzi_ys等。

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
* [macUI](https://github.com/1099438829/macUI)
