## BLE广播




### 1. BLE广播基本功能介绍
-	用于告知其他设备发现自己的存在。其中，传统广播在37、38、39信道上发送广播包；扩展广播可在剩余的37个信道上发送广播包。
-	传统广播包的最大应用数据长度为31 Bytes，SDK中默认添加了三个字节的ADV Flag，因此用户可使用的长度为28 Bytes。
-	扩展广播可以传输254 Bytes的广播数据。
-	广播可设置广播间隔，范围：20 ms ~ 10485 s。
-	广播信道可以单独设置在37、38或39信道进行广播，也可以选择剔除某一个信道，在剩余的两个信道上进行广播。
-	广播可以手动开启。开启广播后，触发回调事件`BLE_GAPM_EVT_ADV_START`，通过状态查看广播是否开启成功。
-	广播可以手动停止或设置超时时间自动停止。广播停止后，触发回调事件`BLE_GAPM_EVT_ADV_STOP`，通过状态查看广播是否停止成功。



### 2. 广播应用笔记

- 广播模式（adv_mode）通常使用非定向可扫描模式`BLE_GAP_ADV_TYPE_ADV_IND`。其他模式的使用场景，请参考《[Core Specification 5.4](https://www.bluetooth.com/specifications/core54-html/)》中的LE广播章节。
- 广播发现模式（disc_mode）通常使用一般可发现模式`BLE_GAP_DISC_MODE_GEN_DISCOVERABLE`。其他模式的使用场景，请参考《[Core Specification 5.4](https://www.bluetooth.com/specifications/core54-html/)》中的LE广播章节。
- 广播白名单的使用方法，请参考`SDK_Folder\projects\ble\ble_peripheral\ble_app_hids_keyboard`工程。
- 广播数据需要按照LTV格式放置，即1 Byte Length、1 Byte Type、N Byte data。 例如，{0x0b, BLE_GAP_AD_TYPE_COMPLETE_NAME,'G', 'o', 'o', 'd', 'i', 'x', '_', 'H', 'R', 'M',}。
- 在广播参数中，可以设置广播持续时间duration。当duration设置为0时，广播会一直保持开启，需要手动关闭；而当duration设置为其他数值时，广播会在持续时间结束后自动停止。
- GR551x最多一次可开启5个广播，GR5526最多一次可开启4个广播，GR5525、GR533x最多一次可开启2个广播。
- GR5xx广播信道支持配置私有信道。具体配置方法，请咨询FAE。



### 3. FAQ

- **Q**：广播数据可以一直修改吗？

  **A**： 可以通过`ble_gap_update_adv_data`持续修改广播数据、扫描回复数据，并且期间无需停止广播。**需要注意的是，必须在广播开启成功后调用`ble_gap_update_adv_data`，才能有效地修改。**

- **Q**：如何同时开启两个广播？

  **A**：当一个广播开启成功后再开启另一个，即收到`BLE_GAPM_EVT_ADV_START`事件后再开启不同adv_idx的另一个广播。具体方法，请参考`SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave`工程。

- **Q**：如何开启多广播？

  **A**：参考`SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave`工程，同时使用随机地址

  `ble_gap_adv_param_set(uint8_t adv_idx, gap_own_addr_t own_addr_type, gap_adv_param_t* p_adv_param)`配置广播参数时，own_addr_type使用`BLE_GAP_OWN_ADDR_GEN_RSLV`。

- **Q**：是否支持动态修改广播间隔？

  **A**：不支持动态修改。必须停止广播重新设置广播参数后启动广播。

- **Q**：如何设置广播功率？

  **A**：广播开启成功后，调用`ble_gap_tx_power_set()`进行设置。

- **Q**：HID设备如何设置广播以使系统蓝牙显示设备名称？

  **A**：如需在Android系统蓝牙中显示键盘图标，在广播包中添加描述符`BLE_APPEARANCE_HID_KEYBOARD `字段；如需在iOS系统蓝牙中显示设备名称，在广播包中添加描述符`BLE_ATT_SVC_HID`字段。

- **Q**：如何设置广播包可以使用31 Bytes，而不是28 Bytes？

  **A**：将`CFG_MAX_ADV_DATA_LEN_SUPPORT`配置为1，disc_mode设置为` GAP_DISC_MODE_NON_DISCOVERABLE`，可以移除默认的3 Bytes Flag。
