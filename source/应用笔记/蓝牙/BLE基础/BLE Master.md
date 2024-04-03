## BLE Master

### 1. BLE Master/扫描 基本功能介绍

-	Master，BLE主设备。即负责扫描设备并且发起连接请求的设备。
-	作为Master,GR5XX 可以连接多台从设备，即对一台从设备设备发起连接成功后，再对另一台从设备发起连接。
-	启动扫描后，可通过BLE_GAPM_EVT_SCAN_START事件查看扫描是否启动成功。
-	通过设置扫描超时时间timeout来控制扫描的时间，设置为0则是一直扫描，必须手动停止。其他值则会自动停止扫描。停止扫描后会上报BLE_GAPM_EVT_SCAN_STOP事件。
-	扫描参数中的scan_dup_filt可过滤重复广播。但在蓝牙设备特别多的场景下，该功能只有降低上报广播的频率，无法做到完全过滤重复广播。
-	扫描参数中use_whitelist也是一种过滤策略，即过滤加入到白名单列表中的设备。
-	扫描参数中scan_type 可设置为BLE_GAP_SCAN_ACTIVE 主动扫描，和BLE_GAP_SCAN_PASSIVE 被动扫描。主动扫描会随机的发起扫描请求包。被动扫描不会发起扫描请求包。
-	扫描参数中 interval 和window 是用来控制扫描间隔和开窗时间的。其中window必须小于等于interval。
-	作为master，发起连接是可设置连接参数,包括 interval ,latency,timeout。

### 2. Master/扫描 应用笔记

- 需要扫描扩展广播的场景下，需要使用扩展扫描。传统扫描无法获取到扩展广播包。扩展扫描的使用方法可参考551x 1.7.0版本的SDK  SDK_Folder\projects\ble\ble_basic_example\ble_app_gap_extended_scan
- 将扫描参数中的interval 和 window设置成一样的值，将射频的RX占空比开到最大。即最长时间的处于RX状态。
- 每一个扫描interval，只会扫描一个信道。与广播不同。广播的每个interval，会在三个信道上广播。
- 扫描到的广播数据会在 BLE_GAPM_EVT_ADV_REPORT事件中上报。
- 发起连接时可以通过设置conn_timeout来设置连接超时时间，即：多久时间内没有连接上目标设备则停止发起连接。
- GR5XX 扫描信道支持配置私有信道，可咨询FAE获取方法。

### 3. BLE Master/扫描 FAQ

- Q:发起连接是否需要停止扫描？

  A: 不需要停止扫描也可以直接对目标设备发起连接。连接上目标设备后，扫描不会停止。

- Q:是否支持同时对多台设备发起连接？

  A:一次只能对一台设备发起连接。无法同时对多台设备发起连接。

- Q：是否支持设置扫描功率？

  A: 扫描没有功率这个说法。扫描的性能只与灵敏度，抗干扰指标相关。

- Q:扫描白名单功能如何使用？

  A:1.已经与目标设备完成了配对绑定。

  ​    2.已经将目标设备加入到白名单中。

  ​    3.再次扫描时将use_whitelist 设置为true。

- Q:Master是否可以作为Server?Slave是否可以作为Client？

  A:Master和Slave是两种不同的角色。Master通常是指发起连接和控制通信的设备，而Slave则是被连接和被控制的设备。

  在BLE中，GATT（Generic Attribute Profile）定义了基于属性的服务和特征，类似于传统的客户端-服务器模型。可以通过GATT协议在BLE Master设备上实现Server角色，提供服务和特征，而Slave设备则可以作为客户端连接并与Master通信。

  因此，BLE Master可以充当Server，向连接的设备提供服务和特征。例如iPhone作为Master ,但是iPhone支持 ANCS 服务。

  
