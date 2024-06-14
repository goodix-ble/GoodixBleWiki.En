## BLE Mesh

### 1. BLE Mesh基本概念介绍

- BLE Mesh Profile规范定义了基本要求，以支持蓝牙低功耗无线技术的互操作性网状网络解决方案。
- Mesh Profile是以BLE Stack protocol为基础制定的协议。
- Mesh Stack在V1.0版本称为Mesh Profile，在V1.1版本称为Mesh Protocol。目前Goodix BLE Mesh支持Mesh Profile V1.0。
- Mesh Profile主要分为三种角色，配网者（Provisioner）、未配网设备（Unprovisioned device）及节点（Node）。
  - 配网者用于管理未配网设备和节点之间的转换。
  - 未配网设备为未接入Mesh网络的设备。
  - 节点为已接入Mesh网络的设备。
  - 配网者为未配网设备配网后，未配网设备即转变成节点。
- Mesh Stack通常指Mesh Profile的部分，而Mesh面向用户的应用部分，则通常称为Mesh Model。

### 2. BLE Mesh应用笔记

- Goodix BLE Mesh目前支持Mesh Profile V1.0，支持的芯片为GR533x系列。
- Goodix BLE Mesh支持的Mesh Model协议版本为Mesh Model V1.0。
- GR533x系列的SDK支持Mesh Model V1.0包含的所有基础Model。
- 在Goodix BLE SDK中，Mesh Profile的功能已经实现，包含在SDK Lib中；Mesh Model在SDK中以源码的形式呈现。用户可以参考Model源码，实现自定义的Model功能。
- 在GR533x系列的SDK包中，`SDK_Folder\projects\mesh`目录下存放了Mesh工程，其中SIG目录下为Mesh Model定义的标准Model工程，Vendor目录下为Mesh自定义Model工程。
- 自定义Model可以通过修改Vendor目录下的工程来实现。如果想要引入标准Model，请参考SIG目录下的有引入多个Model的实现代码。
- Goodix BLE Mesh提供Demo Android App，作为Mesh配网端（Provisioner），搭配SDK中提供的Mesh工程，可以演示Mesh组网、Mesh Node控制等功能，供用户开发参考。
- 对应的SDK版本以及相关资料，请联系FAE提供。

### 3. FAQ

**Q**：请问Mesh原理和协议介绍可以在哪里找到？

**A**：请参考[官网协议列表](https://www.bluetooth.com/specifications/specs/?types=all)，Mesh Model、Mesh Profile/Mesh Protocol。

**Q**：BLE协议栈库文件中已经包含了BLE传统功能和BLE Mesh吗？还是BLE Mesh是一个单独的协议栈库文件？是否有BLE Mesh开发相关的一些文档和资料？

**A**：BLE Mesh软件协议栈建立在低功耗蓝牙技术之上，基于低功耗蓝牙协议栈进行通信。Goodix BLE芯片支持BLE Mesh，目前可提供`GR533x_Mesh_SDK`开发包支持，具体开发包请联系FAE提供。

**Q**：GR533x Mesh低功耗支持几种工作模式？不同工作模式的功耗分别是？GR533x是否支持特定微操作系统？

**A**：根据供电能力和处理能力的不同，节点可担任以下角色：中继节点、低功耗节点、朋友节点以及代理节点。不同节点电流消耗建议使用SK开发板根据应用设定进行测量。

GR533x SDK提供FreeRTOS示例工程。另外，可以便捷地将其它支持Cortex M4平台的RTOS移植到GR533x。

**Q**：Mesh最大支持多少个BLE节点连接？有分种网路拓扑结构么，还是只是星型结构？

**A**：BLE Mesh网络理论上最多支持32767个节点。在BLE Mesh组网中，采用网络泛洪的方式，消息传播的本质是多路径的，因此网络中一个单点的故障不会对整个网络传输造成致命性的影响。相比星型网络，这使得网络更加可靠。参考官网文章：[mesh-in-large-scale-network](https://www.bluetooth.com/blog/mesh-in-large-scale-networks/)。

**Q**：有Goodix Mesh SDK应用开发简介么？

**A**：请参考：[GR533x SDK Mesh应用简介](https://developers.goodix.com/zh/bbs/blog_detail/11d69fb8aff346de99a8010377d5cb93)。