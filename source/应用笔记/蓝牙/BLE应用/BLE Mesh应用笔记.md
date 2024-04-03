## BLE Mesh

### 1. BLE Mesh 基本概念介绍 

- BLE Mesh Profile规范定义了基本要求，以支持蓝牙低功耗无线技术的互操作性网状网络解决方案。
- Mesh Profile以BLE Stack protocol为基础制定的协议。
- Mesh stack在V 1.0版本称为Mesh Profile，在V1.1版本称为Mesh Protocol。目前Goodix BLE Mesh支持Mehs profile V1.0。
- Mesh Profile主要分为三种角色，配网者（Provisioner），未配网设备（Unprovisioned device），节点（Node）。配网者用于管理未配网设备和节点之间的转换。
  - 未配网设备为未接入mesh网络的设备。
  - 节点为已接入mesh网络的设备。
  - 配网者给未配网设备配网后，未配网设备即转变成节点。
- Mesh stack通常指的是mesh Profile的部分，而mesh面向用户的应用部分，则通常称为Mesh Model。

### 2. BLE Mesh 应用笔记

- Goodix BLE目前支持Mesh Profile v 1.0，支持的芯片为GR551x系列和GR533x系列。
- Goodix BLE支持Mesh Model协议版本为 Mesh Model v 1.0。
- GR551x系列和GR533x系列SDK版本上支持Mesh Model v 1.0包含的所有基础Models。
- 在Goodix BLE SDK中，Mesh Profile的功能，已经实现，包含在SDK Lib中；Mesh Model在SDK中，以源码的形式呈现。用户可以参考model源码，实现自己的model功能。
- GR551x系列和GR533x系列SDK包中，`SDK_Folder\projects\\mesh`目录下存放了mesh工程，其中SIG目录下为Mesh Model定义的标准model工程，Vendor目录下为Mesh 自定义model工程。
- 自定义Model可以修改Vendor目录下工程来实现。如果想要引入标准model，参考SIG目录下的有引入多个model的实现代码。
- Goodix BLE Mesh提供Demo Android App，作为Mesh配网端（Provisioner），搭配SDK中提供的Mesh工程，可以演示Mesh组网，Mesh Node控制等功能，供客户开发参考。
- 对应的SDK版本以及相关资料，请联系FAE提供。

### 3. BLE Mesh FAQ

1. 请问mesh原理和协议介绍可以在哪里找到？
  - 请参考[官网协议列表](https://www.bluetooth.com/specifications/specs/?types=all)，Mesh Model、Mesh Profile/Mesh Protocol。
2. ble协议栈库文件中是已经包含了ble传统功能和ble mesh了吗？还是ble mesh是一个单独的协议栈库文件？有没有有关mesh开发的一些文档和资料？
  - BLE Mesh 软件协议栈建立在低功耗蓝牙技术之上，基于低功耗蓝牙协议栈进行通信, Goodix BLE 芯片支持 ble mesh,分别有两款芯片提供`GR551x_Mesh_SDK`和`GR533x_Mesh_SDK`开发包支持，具体开发包请联系FAE提供。
3. GR551x mesh 低功耗支持几种工作模式？不同工作模式的功耗分别是？GR551x 有支持特点微操作系统？
  - 根据供电能力和处理能力的不同，节点可担任以下的角色：中继节点,低功耗节点,朋友节点,代理节点,不同节点电流消耗建议使用Sk开发板根据应用设定进行测量。
  - GR551x SDK提供free rtos示例工程, 另外,可以便捷地移植其它支持cortex m4平台rtos到gr551x
4. mesh 最大支持多少个BLE节点连接？这边有分种网路拓扑结构么，还是只是星型结构？
  - BLE Mesh网络理论上最多支持32767个节点 , ble mesh组网中，采用网络泛洪的方式，消息传播的本质是多路径的，因此网络中一个单点的故障不会对整个网络传输造成致命性的影响，相比星型网络,这使得网络更加可靠。
  - 参考官网文章：[mesh-in-large-scale-network](https://www.bluetooth.com/blog/mesh-in-large-scale-networks/)。
5. 有Goodix Mesh SDK应用开发简介么？
  - 请参考官网链接[GR533x SDK Mesh应用简介](https://developers.goodix.com/zh/bbs/blog_detail/11d69fb8aff346de99a8010377d5cb93)