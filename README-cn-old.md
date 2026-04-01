# AidLux - ARM架构跨生态AIoT开发与部署平台

[



](LICENSE)
[



](https://www.aidlux.com)

**AidLux** 是一个创新的融合操作系统，旨在解决Android与Linux生态割裂问题，为开发者提供在ARM设备（如高通芯片）上同时运行Android应用和LinuxAI算法的原生环境。

## 🚀 核心优势

### 1. 独创融合架构

- **原生体验**：在一台设备上同时获得Android和Linux的原生开发体验，无需虚拟机或双系统切换
- **生态互补**：打通Android丰富的应用生态（摄像头、传感器、UI框架）与Linux强大的AI生态（Python, OpenCV, ROS）

### 2. 极致性能调度

- **异构计算**：通过极致性能AI工具链，一键释放SoC的AI算力
- **全栈调度**：综合调度CPU + GPU + NPU，支持高通等ARM架构芯片，实现高性能低功耗的端侧推理

### 3. 开箱即用

- **软硬一体**：提供从操作系统到底层驱动的完整解决方案，支持"开箱即用"的工业级部署
- **模型支持**：支持多种主流框架模型的优化和转换，解决芯片及算法异构问题

## 🛠️ 工具链介绍

### AidLux OS

融合操作系统，集成极致性能AI工具链，作为基础运行环境，释放SoC算力

### AI Model Optimizer

**模型优化平台**

- 支持多种主流框架模型优化与转换
- 菜单式一键操作，零代码实现模型迁移
- 精度损失小

### AI Creator

**可视化训练平台**

- 集标注、训练、部署于一体
- 基于行业领先正样本算法
- 快速完成模型训练与更新

### 端侧AI生态门户

全球首个高通物联网平台端侧AI生态门户，包含解决方案中心 + 模型广场

## 💡 适用领域

- 🤖 **智能机器人**：具身智能、服务机器人
- 🏭 **工业AI检测**：缺陷检测、自动化质检
- 🏙️ **智慧城市**：安防、停车管理
- 📱 **边缘计算与AI教育**

## 📦 安装与使用

### 系统要求

- Android 7.0及以上版本
- ARM架构处理器（推荐高通芯片）
- 至少2GB RAM

### 安装步骤

1. **下载AidLux APK**

```
# 从官网下载最新版本
wget https://www.aidlux.com/download/aidlux-latest.apk
```

2. **安装应用**

```
adb install aidlux-latest.apk
```

3. **启动服务**

```
# 通过Android Intent启动
am start -n com.aplux.aidlux/.MainActivity
```

4. **访问Linux环境**
    - 本地访问：直接在手机上使用
    - 远程访问：通过浏览器访问 `http://<device-ip>:8080`

### 基本使用

```
# 进入Linux终端
aidlux terminal

# 安装AI框架
sudo apt update
sudo apt install python3-pip
pip3 install tensorflow pytorch

# 运行Python程序
python3 your_ai_app.py
```

## 🧪 开发示例

### 运行AI模型

```
import cv2
import tensorflow as tf

# 直接调用手机硬件资源
cap = cv2.VideoCapture(0)  # 使用手机摄像头
model = tf.keras.models.load_model('your_model.h5')

while True:
    ret, frame = cap.read()
    prediction = model.predict(frame)
    # 处理预测结果
```

### 多语言开发支持

- **Python**：`python3`, `pip3`
- **C/C++**：`gcc`, `g++`, `make`
- **Java**：`openjdk-11-jdk`
- **Go**：`golang`
- **Shell**：`bash`, `zsh`

## 🧰 开发工具

- **VSCode**：集成开发环境
- **Jupyter Notebook**：交互式编程
- **Terminal**：完整的Linux命令行
- **File Manager**：图形化文件管理

## 📚 学习资源

- **官方文档**：https://www.aidlux.com/docs
- **开发者社区**：https://forum.aidlux.com
- **示例项目**：https://github.com/aidlux/examples

## 🤝 贡献指南

欢迎开发者贡献代码和文档！

1. Fork本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开Pull Request

## 📄 许可证

本项目采用Apache License 2.0，详情请查看LICENSE文件。

## 📬 联系方式

- **官网**：https://www.aidlux.com
- **邮箱**：support@aidlux.com
- **GitHub**：https://github.com/aidlux

---

**AidLux** - 让AI开发更简单，让边缘计算更强大！

