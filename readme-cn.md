![AidLearning](image/AidLearning-1.png)
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
[English Version](README.md)

## 简介
AidLearning是一个运行在移动端（Android）上的支持图形化界面的Linux虚拟机，同时是一个支持深度神经网络开发的框架和平台，内置了最为流行的深度学习框架caffe/mxnet/keras/pytoch/tensorflow/ncnn/opencv...内置了可视化AI开发编辑器，支持触摸拖拽式界面设计，支持代码动态调试和运行。支持在移动端和PC端用python开发你的AI应用，支持把你的python源码转化为APP（Apk）发布。支持一键式安装，只需要安装一个8M的App即可自动引导完成安装。目前，已在各大App应用中心（华为、小米、vivo、oppo...）上线，下载和访问量已超100万，内置了大量的AI例子和教程，互联网上（知乎、简书、CSDN、百度等）也有大量中文教程，方便你学习和开发。


## 整体特点

### 创新性
- 移动端（手机）上最好的，环境最全的Linux模拟器，唯一支持图形化桌面的Linux模拟器...
- 唯一支持AI开发环境的模拟器、内置全球最流行Top 7的深度学习框架，内置大量深度学习的模型、例子和开发组件
- 唯一支持python图形化开发和调试的模拟器，支持触摸拖拽式界面设计，提高你的开发效率
- 支持用python开发可运行在手机的App，支持python代码直接编译生成可部署的apk文件
- 一键式安装，无任何依赖，你只需在手机上要安装一个8M的引导App，就可以自动完成所有环境的安装。
- 跨平台开发，支持云桌面（手机桌面和电脑桌面相同），既可以在手机或平版上或其他嵌入式主板上运行，也可以在电脑端基于web直接访问和开发。
- 支持加速库openblas，支持多线程和多进程，运行流畅、不卡顿，充分发挥ARM CPU的算力

### 通用性
- 支持`Tensorflow`、`Caffe`、`mxnet`、`keras`、`pytoch`、`ncnn`、`opencv`、`scipy`....
- 支持Python2.7/Python3.6.4。
- 自带AiCode可视化编程IDE，也支持谷歌的Jupyter的IDE。
- 内置完整原生的跨平台桌面，不需要安装第三方vnc等的支持，支持电脑端和手机端同桌面
- 既支持手机、Pad、也支持工业Arm板卡
- 开发的程序，既可以部署在手机端、也可以部署在电脑端
- 支持市面上99.5%的手机，已测试华为、VIVO、OPPO、三星、小米等全系列64位手机

### 安全性
- Aid在手机上虚拟了一个封闭空间，不需要root，不会破坏你的手机的内容。
- 不会收集你的个人隐私，所有权限都可以自己设定...

### 易用性
- 一键式安装，自动下载最新依赖包、自动配置AI开发需要的环境，降低AI开发门槛
- 内置大量AI组件、模型、例子、教程，降低AI开发的门槛，你可以不懂AI算法，但可以用这个平台开发出AI应用。
- 一部手机，两个系统，Android和Linux共生共存，无重启自由切换；娱乐、开发、学习三不误
- 支持手机端开发与电脑端开发代码自动同步，支持界面触摸拖拽式设计，自动生成界面的代码
- 一键式编译和发布你开发支持AI的App
- 可扩展支持Java、C++等语言的支持

## 架构设计
![architecture](doc/architecture.png)

AidLearning FrameWork可以分为Linux模拟器和AI编程平台两部分。

Linux模拟器由Terminal和Desktop构成。前者基于Android底层Linux kernel和busybox命令包构建了完整Linux的模拟器，你可以用apt命令安装任何你需要的依赖包；后者基于web构建了图形化操作桌面，你可以用在手机上用触摸操控整个系统，同时该桌面支持云桌面，你可以在电脑端通过一个网址轻松访达。

AI编程平台由深度学习框架和Python可视化编程框架（Python IDE）构成。前者包含了几乎所有目前流行的深度学习框架，负责模型的加载、计算图的调度；包含各计算的内存分配、Op实现。后则构建了Python可视化快速开发平台，不仅可以在线实时运行、调试Python代码，同时支持触摸拖拽式界面设计、并且可以生成最终的可执行程序、产出apk文件。

## 开始使用
- [安装配置](http://www.aidlearning.net/mnn/cn/usage)
- [开发文档](http://www.aidlearning.net/mnn/en/ops)
- [界面截图](doc/API/API_index.html)
- [示例代码](http://www.aidlearning.net/mnn/cn/demo_zoo)

## 内置工具
- [测试工具](http://www.aidlearning.net/mnn/cn/tool_test)
- [性能测试](http://www.aidlearning.net/mnn/cn/tool_benchmark)
- [模型压缩](http://www.aidlearning.net/mnn/cn/tool_quantize)
- [基于表达式构建模型并评测](benchmark/Readme_CN.md)

## 如何修改
- [自定义后端](http://www.aidlearning.net/mnn/cn/customize_backend)
- [自定义算子](http://www.aidlearning.net/mnn/cn/customize_op)
- [贡献代码](http://www.aidlearning.net/mnn/cn/contribute)

##  交流与反馈
- [常见问题](http://www.aidlearning.net/mnn/en/faq)
<img src="images/QQqun.png" height="256"/>


## License
Apache 2.0

## 致谢
AidLearning参与人员：耶鲁大学gondon、中科院大学yoline777、qidiso。

AidLearning参考、借鉴了下列项目：
- [Caffe](https://github.com/BVLC/caffe)
- [flatbuffer](https://github.com/google/flatbuffers)
- [gemmlowp](https://github.com/google/gemmlowp)
- [Google Vulkan demo](http://www.github.com/googlesamples/android-vulkan-tutorials) 
- [Halide](https://github.com/halide/Halide)
- [Mace](https://github.com/XiaoMi/mace)
- [ONNX](https://github.com/onnx/onnx)
- [protobuffer](https://github.com/protocolbuffers/protobuf)
- [skia](https://github.com/google/skia)
- [Tensorflow](https://github.com/tensorflow/tensorflow)
- [ncnn](https://github.com/Tencent/ncnn)
- [paddle-mobile](https://github.com/PaddlePaddle/paddle-mobile)
- [stb](https://github.com/nothings/stb)
- [rapidjson](https://github.com/Tencent/rapidjson)
