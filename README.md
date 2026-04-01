# 🚀 AidLux（ori：AidLearning） - 端侧 AIoT 融合开发平台 <a href='README-en.md'>[English]</a>

AidLux：掌上的 AI 瑞士军刀。在手机上运行原生 Ubuntu，本地部署 LLM、VLM、VLA 与 OpenClaw，全能开发一机搞定。

[![Release](https://img.shields.io/badge/Version-2.1.0-green)](https://github.com/aidlux/AidLux)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20HarmonyOS%20%7C%20HyperOS-orange)]()

**AidLux** 是一个基于 ARM 架构的跨生态（Android/HarmonyOS + Linux）一站式 AIoT 应用开发和部署平台。它打破了 Android 与 Linux 的生态壁垒，让你可以在 Android 手机、平板或边缘计算设备上，同时获得原生的 Linux 桌面环境和 AI 开发能力。

> **核心理念**：持续降低 AI 应用开发门槛，实现端侧 AI 算力的一键释放。

---

## 📢 最新动态 (AidLux 2.1.0)

**发布日期**：2026年3月20日
**Build ID**：2.1.0.1968

*   **全新桌面环境**：默认桌面环境由 Xfce 升级为 **Ubuntu-desktop**，提供更现代、更完整的 Linux 桌面体验。
*   **硬件支持扩展**：**AidLite SDK** 现已正式支持 **Snapdragon 8 Gen 3** 及以上最新芯片组。
*   **AI 引擎升级**：集成更新的 **QNN (Qualcomm Neural Network)** 版本，并优化了底层推理逻辑 (AidQNN)。
*   **功能增强**：
    *   重构并扩展了 WiFi 管理功能。
    *   优化了 Linux 环境的安装与更新逻辑。
    *   应用中心安装 APK 的初始目录指定为 AidLux 内部空间，提升安全性。
    *   **Aid-Desktop** 界面交互与易用性全面优化。

---

## 🌟 核心优势

### 🔗 独创的融合架构 (Fusion Architecture)
*   **原生共存**：共享 Linux 内核，实现 Android (HarmonyOS) 与 Linux 的原生融合，无需虚拟机或双系统重启。
*   **生态互补**：无缝调用 Android 的硬件驱动（摄像头、传感器、GPS）与 Linux 的 AI 软件栈（Python, ROS, OpenCV）。

### ⚡ 极致的端侧算力调度
*   **异构计算**：通过 AidLite SDK 一键调度 CPU + GPU + NPU。
*   **高性能低功耗**：针对高通 (Qualcomm) 系列芯片进行了深度优化，支持 INT4/INT8/FP16 量化加速。

### 🤖 全场景 AI 开发支持
*   **大模型端侧部署**：支持近500款端侧大模型（LLM/VLM/VLA）的量化与推理，如 Qwen3、Phi3、Deepseek、Stable Diffusion 等。
*   **机器人开发**：原生集成 ROS/ROS2，支持 MoveIt2 和 Gazebo，支持VLA模型，是具身智能开发的理想平台。

---

## 🛠️ 核心工具链

AidLux 提供了一站式的开发工具，覆盖从代码编写到模型部署的全流程。

### 🧪 AidCode - 交互式 Python IDE
*   **功能**：专为端侧 AI 开发设计的代码编辑器。
*   **特性**：
    *   支持 Python 语法高亮、代码补全。
    *   内置交互式终端，支持一键运行 (`Run Now`) 和停止代码。
    *   支持直接调用 Android API（如语音播报 `droid.ttsSpeak`）。

### 🐍 完整的 Linux 终端 (AidTerminal)
*   **功能**：提供与原生 Ubuntu 系统一致的命令行体验。
*   **特性**：
    *   **Touch Bar**：底部定制化触控栏，包含 `Ctrl`, `Alt`, `Tab` 等组合键，完美适配手机/平板触屏。
    *   **多终端**：支持同时开启多个终端标签页，互不干扰。
    *   **键盘映射**：支持外接键盘和触屏软键盘切换。

### 📦 应用中心 (App Center)
*   **功能**：管理 AidLux 生态下的应用。
*   **特性**：
    *   **双生态应用**：既可安装 Linux 原生应用（如 VSCode, Firefox），也可将 Android 应用添加到桌面使用。
    *   **一键安装**：简化了复杂软件的依赖安装过程。

### 🤖 AI 与机器人工具
*   **AidGen / AidGenSE**：生成式 AI 推理工具与 HTTP 服务，支持 RAG 服务部署。
*   **AidStream**：高性能音视频流处理框架，支持 USB 摄像头推拉流。
*   **ROS2 Humble**：预装机器人操作系统，支持激光雷达、机械臂等外设开发。

---

## 📂 文件系统结构

AidLux 对 Android 存储进行了标准化映射，方便开发者进行文件管理：

| 目录路径 | 描述 | 说明 |
| :--- | :--- | :--- |
| `/home/aidlux` | **工作目录** | 默认的代码和项目存放位置，**唯一支持文件上传的目录**。 |
| `/sdcard` | **设备存储** | 对应 Android 的内部存储，存放图片 (`DCIM`)、下载文件等。 |
| `/media/sdi1` | **外接存储** | 识别并挂载的 U 盘或移动硬盘目录。 |
| `/opt` | **系统应用** | 存放预装的 SDK 和核心系统库。 |

---

## 🚀 快速开始

### 1. 环境要求
*   **支持系统**：Android 7.0+, HarmonyOS, Xiaomi HyperOS
*   **硬件架构**：ARM64 位设备
*   **推荐设备**：
    *   **手机/平板**：小米 12S/13/14/15 系列, 华为 Mate/P 系列 (部分), 三星 S 系列。
    *   **开发板**：犀牛派 X1 (Rhino Pi-X1), 犀牛派 A1。

### 2. 安装方式
*   **应用商店**：华为、联想、小米应用商店搜索 "AidLux" 下载。
*   **手动安装 (APK)**：
    *   下载地址：[aidlux_2.1.0_latest_release.apk](https://file.aidlux.com/repo/apk/aidlux_2.1.0_latest_release.apk)
    *   **注意**：若安装时提示 `Permission denied`，请先卸载旧版本，重启手机后再安装。

### 3. 开发流程
1.  **连接**：通过浏览器 Web 端或本地桌面进入 AidLux。
2.  **编码**：使用 `AidCode` 编写 Python 脚本。
3.  **运行**：直接调用 `AidStream` 捕获摄像头画面，或使用 `AidLite` 加载 ONNX/TensorFlow 模型进行推理。
4.  **部署**：将应用打包或直接在端侧运行。

---

## 💡 常见问题 (FAQ)

基于社区反馈整理，帮助你快速避坑：

*   **Q: 安装新版本后提示 "Permission denied" 或无法启动？**
    *   A: 这通常是因为残留了旧版本数据。请**卸载旧版本**，**重启手机**，再安装新版本 APK。

*   **Q: 手机上为什么找不到终端 (Terminal)？**
    *   A: 请检查是否安装了完整版。终端通常位于桌面的 "System" 菜单中，或在应用中心搜索 "Terminal" 确认是否已安装。

*   **Q: 能否在 AidLux 中运行需要 `systemd` 的软件 (如 HomeAssistant, OpenClaw)？**
    *   A: AidLux 基于 Android 内核，原生不支持 `systemd` (PID 1)。但社区已有通过 `proot` 或特定脚本兼容运行的方法（参考社区教程安装 HomeAssistant）。

*   **Q: 如何在手机和电脑之间传输代码/模型？**
    *   A: 推荐使用 AidLux 内置的 **AidDesktop** 通过浏览器访问，或使用 `scp` 命令。文件需放在 `/home/aidlux` 目录下才能被识别。

---

## 📚 学习资源

*   **官方论坛**：[AidLux 开发者社区 (最新教程与问答)](https://forum.aidlux.com)
*   **技术文档**：[AidLux 文档中心 (含犀牛派开发板指南)](https://rhinopi.docs.aidlux.com)
*   **模型广场**：[ModelFarm (400+ 优化模型)](https://aiot.aidlux.com/en/models)
*   **案例中心**：包含 YOLOv12 部署、MobileClip2-S3、SAM2、qwen3-vl 部署等实战教程。

---

## 🏷️ 标签
#端侧AI #AIoT #AndroidLinux #高通AI #大模型部署 #ROS #Python #开源 #AidLux
