# 🚀 AidLux - ARM Architecture Edge AIoT Fusion Development Platform

**AidLux** is a cross-ecosystem (Android/HarmonyOS + Linux) one-stop AIoT application development and deployment platform based on ARM architecture. It breaks the ecological barriers between Android and Linux, allowing you to simultaneously obtain native Linux desktop environment and AI development capabilities on Android phones, tablets, or edge computing devices.

**Core Concept**: Continuously lower the threshold of AI application development and achieve one-click release of edge AI computing power.

## 📢 Latest Updates (AidLux 2.1.0)

**Release Date**: March 20, 2026
**Build ID**: 2.1.0.1968

- **New Desktop Environment**: Default desktop environment upgraded from Xfce to **Ubuntu-desktop**, providing a more modern and complete Linux desktop experience.
- **Hardware Support Expansion**: **AidLite SDK** now officially supports **Snapdragon 8 Gen 3** and above latest chipsets.
- **AI Engine Upgrade**: Integrated updated **QNN (Qualcomm Neural Network)** version with optimized底层推理 logic (AidQNN).
- **Feature Enhancements**:
    - Reconstructed and expanded WiFi management functions.
    - Optimized Linux environment installation and update logic, fixing some update issues.
    - Specified internal storage of AidLux as the initial directory for APK installation in the application center, enhancing security.
    - **Aid-Desktop** interface interaction and usability comprehensively optimized.

---

## 🌟 Core Advantages

### 1. Innovative Fusion Architecture

- **Native Coexistence**: Shares Linux kernel to achieve native fusion of Android (HarmonyOS) and Linux, without virtual machines or dual system restart.
- **Ecosystem Complementarity**: Seamlessly calls Android hardware drivers (camera, sensors, GPS) and Linux AI software stack (Python, ROS, OpenCV).

### 2. Ultimate Edge Computing Power Scheduling

- **Heterogeneous Computing**: One-click scheduling of CPU + GPU + NPU through AidLite SDK.
- **High Performance & Low Power**: Deeply optimized for Qualcomm series chips, supporting INT8/FP16 quantization acceleration.

### 3. Full-Scenario AI Development Support

- **Edge Large Model Deployment**: Supports quantization and inference of edge large models (LLM/VLM) such as Qwen3, Stable Diffusion.
- **Robotics Development**: Natively integrated ROS/ROS2, supporting MoveIt2 and Gazebo, ideal platform for embodied intelligence development.

---

## 🛠️ Core Toolchain & Development Environment

AidLux provides an all-in-one development tool covering the entire process from code writing to model deployment.

### 🧪 AidCode - Interactive Python IDE

- **Function**: Code editor designed specifically for edge AI development.
- **Features**:
    - Supports Python syntax highlighting and code completion.
    - Built-in interactive terminal with one-click run (`Run Now`) and stop functions.
    - Supports direct calling of Android APIs (such as voice broadcast `droid.ttsSpeak`).

### 🐍 Complete Linux Terminal (AidTerminal)

- **Function**: Provides command-line experience consistent with native Ubuntu systems.
- **Features**:
    - **Touch Bar**: Bottom customized touch bar with `Ctrl`, `Alt`, `Tab` and other combination keys, perfectly adapted to mobile/tablet touch screens.
    - **Multi-terminal**: Supports opening multiple terminal tabs simultaneously without interference.
    - **Keyboard Mapping**: Supports switching between external keyboards and on-screen soft keyboards.

### 📦 Application Center

- **Function**: Manages applications in the AidLux ecosystem.
- **Features**:
    - **Dual-ecosystem Applications**: Can install both native Linux applications (like VSCode, Firefox) and add Android applications to the desktop.
    - **One-click Installation**: Simplifies dependency installation process for complex software.

### 🤖 AI & Robotics Tools

- **AidGen / AidGenSE**: Generative AI inference tools and HTTP services, supporting RAG service deployment.
- **AidStream**: High-performance audio/video streaming framework supporting USB camera push/pull streaming.
- **ROS2 Humble**: Pre-installed robotics operating system supporting peripherals like LiDAR and robotic arms.

---

## 🏷️ Model Zoo & Ecosystem Resources

AidLux is not just a development environment, but also the world's first **Qualcomm IoT Platform Edge AI Ecosystem Portal**. We provide abundant ready-made resources to help you seamlessly transition from "idea" to "deployment".

### 🏷️ Model Zoo

We offer over **400+** mainstream AI models covering computer vision, speech audio, natural language processing, and multimodal fields.

- **Plug-and-Play**: All models are deeply optimized, supporting one-click download and deployment.
- **Real-device Benchmark Data**: Provides detailed performance metrics, allowing you to clearly understand model performance on different Qualcomm platforms (like QCS8550, QCS6490).
- **Popular Models**:
    - **Object Detection**: YOLOv8 (s/m/n), YOLOv5
    - **Segmentation & Tracking**: SAM2, MobileSAM
    - **Classification & Recognition**: MobileNet, ResNet, MobileClip
    - **Generative AI**: Stable Diffusion, Qwen-VL (multimodal large models)

### ⚡ Rapid Deployment Tools

Through the built-in **MMS (Model Management System)** tool, developers can directly pull models from the command line:

```
# Login to Model Zoo
mms login -u <username> -p <password>

# Search models
mms list yolov8

# One-click download models optimized for specific chips (e.g., QCS8550, INT8 precision)
mms get -m yolov8m -p int8 -c qcs8550 -b qnn2.36
```

---

## 📂 File System Structure

AidLux standardizes Android storage mapping for convenient file management:

| Directory Path | Description | Notes |
| ------ |------ |------ |
| `/home/aidlux` | **Working Directory** | Default location for code and projects, **the only directory supporting file upload**. |
| `/sdcard` | **Device Storage** | Corresponds to Android internal storage, storing images (`DCIM`), downloads, etc. |
| `/media/sdi1` | **External Storage** | Recognized and mounted USB drives or external hard disk directories. |
| `/opt` | **System Applications** | Stores pre-installed SDKs and core system libraries. |

---

## 🚀 Quick Start

### Environment Requirements

- **Supported Systems**: Android, HarmonyOS, Xiaomi HyperOS
- **Hardware Architecture**: ARM64 devices (supports Snapdragon 8 Gen 3, 865, 6490, etc.)

### Installation Methods

1. **App Store**: Huawei, Lenovo devices can directly search "AidLux" in the app store.
2. **Manual Installation**:
    - Download APK: AidLux 2.1.0 Latest Release
    - First launch after installation requires network configuration of Linux environment (about 1-3 minutes).

### Development Workflow

1. **Connect**: Access AidLux through browser web interface or local desktop.
2. **Code**: Use `AidCode` to write Python scripts.
3. **Run**: Directly call `AidStream` to capture camera footage, or use `AidLite` to load ONNX/TensorFlow models for inference.
4. **Deploy**: Package applications or run directly on edge devices.

---

## 📚 Learning Resources

- **Official Forum**: AidLux Developer Community
- **Technical Documentation**: AidLux Documentation Center
- **Case Center**: Practical tutorials including YOLOv5 deployment, MobileClip2-S3, SAM2 deployment, etc.

---

## 🏷️ Tags

#EdgeAI #AIoT #AndroidLinux #QualcommAI #LargeModelDeployment #ROS #Python #OpenSource

