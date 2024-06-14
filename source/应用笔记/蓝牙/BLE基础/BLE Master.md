## BLE Master

### 1. BLE Master扫描基本功能介绍

-	BLE Master，主设备，即负责扫描设备并且发起连接请求的设备。
-	作为Master，GR5xx可以连接多台从设备，即对一台从设备发起连接成功后，再对另一台从设备发起连接。
-	启动扫描后，可通过`BLE_GAPM_EVT_SCAN_START`事件查看扫描是否启动成功。
-	可以通过设置扫描超时时间timeout，控制扫描的时间。当timeout设置为0时，表示一直扫描，需手动停止扫描；当timeout设置为其他值时，会自动停止扫描。停止扫描后会上报`BLE_GAPM_EVT_SCAN_STOP`事件。
-	扫描参数中的scan_dup_filt可过滤重复广播。但在蓝牙设备特别多的场景下，该功能只能降低上报广播的频率，无法完全过滤重复广播。
-	扫描参数中的use_whitelist也是一种过滤策略，可过滤加入到白名单列表中的设备。
-	扫描参数中的scan_type可设置为`BLE_GAP_SCAN_ACTIVE`（主动扫描）和`BLE_GAP_SCAN_PASSIVE`（被动扫描）。主动扫描会随机地发起扫描请求包，被动扫描则不会发起扫描请求包。
-	扫描参数中的interval和window用于控制扫描间隔和开窗时间，并且window值必须小于等于interval值。
-	作为Master，发起连接时可设置连接参数，包括interval 、latency、timeout。

### 2. BLE Master扫描应用笔记

- 在需要扫描扩展广播的场景下，使用扩展扫描，传统扫描无法获取扩展广播包。如需扩展扫描的使用方法，可参考GR551x SDK V1.7.0版本中的扩展扫描示例工程：`SDK_Folder\projects\ble\ble_basic_example\ble_app_gap_extended_scan`，其中SDK_Folder为SDK根目录。
- 将扫描参数中的interval和window设置成相同的值，可将射频的RX占空比开到最大，即最长时间地处于RX状态。
- 每一个扫描interval，只会扫描一个信道。与广播不同，广播的每个interval，会在三个信道上进行广播。
- 扫描到的广播数据会在BLE_GAPM_EVT_ADV_REPORT事件中上报。
- 发起连接时，可以通过设置conn_timeout来配置连接超时时间，即在设定的时间内若未连接上目标设备，则停止发起连接。
- GR5xx扫描信道支持配置私有信道。具体配置方法，请咨询FAE。

### 3. FAQ

- **Q**：发起连接是否需要停止扫描？

  **A**：不需要停止扫描也可以直接对目标设备发起连接。连接上目标设备后，扫描不会停止。

- **Q**：是否支持同时对多台设备发起连接？

  **A**：一次只能对一台设备发起连接。无法同时对多台设备发起连接。

- **Q**：是否支持设置扫描功率？

  **A**：没有扫描功率这个说法。扫描的性能仅与灵敏度、抗干扰指标相关。

- **Q**：如何使用扫描白名单功能？

  **A**：1. 已经与目标设备完成了配对绑定。

  ​      2. 已经将目标设备加入到白名单中。

  ​      3. 再次扫描时将use_whitelist设置为true。

- **Q**：Master是否可以作为Server？Slave是否可以作为Client？

  **A**：Master和Slave是两种不同的角色。Master通常指发起连接和控制通信的设备，而Slave则是被连接和被控制的设备。

  在BLE中，GATT（Generic Attribute Profile）定义了基于属性的服务和特征，类似于传统的客户端-服务器模型。可以通过GATT协议在BLE Master设备上实现Server角色，提供服务和特征。而Slave设备则可以作为客户端与Master连接，并进行通信。

  因此，BLE Master可以充当Server，向连接的设备提供服务和特征。例如，iPhone作为Master，并支持ANCS服务。

  
