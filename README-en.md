# 🚀 AidLux - The AI/LLM Swiss Army Knife for your phone <a href='README.md'>[中文版]</a>

AidLux: The AI Swiss Army Knife for your phone. Run native Ubuntu and deploy LLMs, VLMs, VLAs, and OpenClaw locally—all in one device.

[![Release](https://img.shields.io/badge/Version-2.1.0-green)](https://github.com/aidlux/AidLux)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20HarmonyOS%20%7C%20HyperOS-orange)]()

**AidLux** is a one-stop AIoT application development and deployment platform based on the ARM architecture, bridging the Android/HarmonyOS and Linux ecosystems. It breaks the ecological barrier between Android and Linux, allowing you to simultaneously access a native Linux desktop environment and powerful AI development capabilities on Android phones, tablets, or edge computing devices.

> **Core Philosophy**: Continuously lower the barrier for AI application development and achieve one-click release of edge AI computing power.

---

## 📢 Latest Updates (AidLux 2.1.0)

**Release Date**: March 20, 2026
**Build ID**: 2.1.0.1968

*   **New Desktop Environment**: The default desktop has been upgraded from Xfce to **Ubuntu-desktop**, providing a more modern and complete Linux desktop experience.
*   **Hardware Support Expansion**: The **AidLite SDK** now officially supports the latest chipsets including the **Snapdragon 8 Gen 3** and above.
*   **AI Engine Upgrade**: Integrated with the latest **QNN (Qualcomm Neural Network)** version, optimizing the底层 inference logic (AidQNN).
*   **Feature Enhancements**:
    *   Re-architected and expanded WiFi management functionality.
    *   Optimized the installation and update logic of the Linux environment.
    *   The initial directory for APK installation in the App Center is now specified as internal AidLux storage, enhancing security.
    *   Comprehensive optimization of the **Aid-Desktop** interface interaction and usability.

---

## 🌟 Core Advantages

### 🔗 Proprietary Fusion Architecture
*   **Native Coexistence**: Shares the Linux kernel to achieve native fusion between Android (HarmonyOS) and Linux, eliminating the need for virtual machines or dual-system reboots.
*   **Ecosystem Synergy**: Seamlessly call Android hardware drivers (Camera, Sensors, GPS) and Linux AI software stacks (Python, ROS, OpenCV).

### ⚡ Ultimate Edge Computing Power Scheduling
*   **Heterogeneous Computing**: One-click scheduling of CPU + GPU + NPU via the AidLite SDK.
*   **High Performance & Low Power**: Deeply optimized for Qualcomm series chips, supporting INT8/FP16 quantization acceleration.

### 🤖 Full-Scenario AI Development Support
*   **On-Device LLM Deployment**: Supports quantization and inference of端侧大 models (LLM/VLM) such as Qwen3 and Stable Diffusion.
*   **Robotics Development**: Natively integrated ROS/ROS2, supporting MoveIt2 and Gazebo, making it an ideal platform for Embodied AI development.

---

## 🛠️ Core Toolchain

AidLux provides a one-stop development suite covering the entire process from coding to model deployment.

### 🧪 AidCode - Interactive Python IDE
*   **Function**: A code editor designed specifically for edge AI development.
*   **Features**:
    *   Supports Python syntax highlighting and code completion.
    *   Built-in interactive terminal supporting one-click run (`Run Now`) and stop.
    *   Supports direct calls to Android APIs (e.g., text-to-speech `droid.ttsSpeak`).

### 🐍 Complete Linux Terminal (AidTerminal)
*   **Function**: Provides a command-line experience consistent with native Ubuntu systems.
*   **Features**:
    *   **Touch Bar**: A customized bottom touch bar containing `Ctrl`, `Alt`, `Tab`, etc., perfectly adapting to phone/tablet touchscreens.
    *   **Multi-Terminal**: Supports multiple terminal tabs simultaneously.
    *   **Keyboard Mapping**: Supports switching between external keyboards and on-screen soft keyboards.

### 📦 App Center
*   **Function**: Manages applications within the AidLux ecosystem.
*   **Features**:
    *   **Dual-Ecosystem Apps**: Install Linux native apps (e.g., VSCode, Firefox) or add Android apps to the desktop.
    *   **One-Click Installation**: Simplifies the dependency installation process for complex software.

### 🤖 AI & Robotics Tools
*   **AidGen / AidGenSE**: Generative AI inference tools and HTTP services, supporting RAG service deployment.
*   **AidStream**: High-performance audio/video streaming framework supporting USB camera push/pull streams.
*   **ROS2 Humble**: Pre-installed Robot Operating System supporting peripherals like LiDAR and robotic arms.

---

## 📂 File System Structure

AidLux standardizes the mapping of Android storage for easy file management:

| Directory Path | Description | Notes |
| :--- | :--- | :--- |
| `/home/aidlux` | **Workspace** | Default location for code and projects, the **only directory supporting file uploads**. |
| `/sdcard` | **Device Storage** | Corresponds to Android's internal storage, holding images (`DCIM`), downloads, etc. |
| `/media/sdi1` | **External Storage** | Directory for recognized and mounted USB drives or external hard disks. |
| `/opt` | **System Apps** | Stores pre-installed SDKs and core system libraries. |

---

## 🚀 Quick Start

### 1. Environment Requirements
*   **Supported Systems**: Android 7.0+, HarmonyOS, Xiaomi HyperOS
*   **Hardware Architecture**: ARM64 devices
*   **Recommended Devices**:
    *   **Phones/Tablets**: Xiaomi 12S/13/14/15 series, Huawei Mate/P series (selected), Samsung S series.
    *   **Development Boards**: Rhino Pi-X1, Rhino Pi-A1.

### 2. Installation Methods
*   **App Store**: Search "AidLux" on Huawei, Lenovo, or Xiaomi app stores.
*   **Manual Installation (APK)**:
    *   Download: [aidlux_2.1.0_latest_release.apk](https://file.aidlux.com/repo/apk/aidlux_2.1.0_latest_release.apk)
    *   **Note**: If you encounter `Permission denied`, please uninstall the old version and restart your phone before installing.

### 3. Development Workflow
1.  **Connect**: Access AidLux via the browser Web interface or the local desktop.
2.  **Code**: Write Python scripts using `AidCode`.
3.  **Run**: Capture camera feeds directly using `AidStream`, or load ONNX/TensorFlow models for inference using `AidLite`.
4.  **Deploy**: Package the application or run it directly on the edge device.

---

## 💡 Frequently Asked Questions (FAQ)

Compiled from community feedback to help you avoid pitfalls:

*   **Q: Why does it show "Permission denied" or fail to start after installing the new version?**
    *   A: This is usually due to residual old version data. Please **uninstall the old version**, **restart your phone**, and then install the new APK.

*   **Q: Why can't I find the Terminal on my phone?**
    *   A: Please check if the full version is installed. The terminal is usually located in the "System" menu on the desktop, or search for "Terminal" in the App Center to confirm installation.

*   **Q: Can I run software requiring `systemd` (like HomeAssistant, OpenClaw) in AidLux?**
    *   A: AidLux is based on the Android kernel and does not natively support `systemd` (PID 1). However, the community has developed methods to run them via `proot` or specific scripts (refer to community tutorials for HomeAssistant installation).

*   **Q: How to transfer code/models between my phone and computer?**
    *   A: We recommend using the built-in **AidDesktop** via browser access, or using the `scp` command. Files must be placed in the `/home/aidlux` directory to be recognized.

---

## 📚 Learning Resources

*   **Official Forum**: [AidLux Developer Community (Latest Tutorials & Q&A)](https://forum.aidlux.com)
*   **Technical Docs**: [AidLux Documentation Center (Includes Rhino Pi guides)](https://rhinopi.docs.aidlux.com)
*   **Model Farm**: [ModelFarm (400+ Optimized Models)](https://aiot.aidlux.com/en/models)
*   **Case Center**: Includes tutorials for YOLOv12 deployment, MobileClip2-S3, and SAM2 、qwen3-vl deployment.

---

## 🏷️ Tags
#EdgeAI #AIoT #AndroidLinux #QualcommAI #LLM #ROS #Python #OpenSource #AidLux
