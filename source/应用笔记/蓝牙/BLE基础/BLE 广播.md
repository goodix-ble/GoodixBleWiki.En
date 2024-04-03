## BLE 广播




### 1. BLE广播基本功能介绍
-	用于让其他设备发现自己存在的一个状态，其中传统广播在37 ，38，39信道上发送广播包。扩展广播可在剩余的37个信道上发送广播包。
-	传统广播包的应用数据长度最大位31Byte，SDK中默认添加了三个字节的ADV Flag，因此用户可使用的长度位28Byte。
-	扩展广播可以到254Byte广播数据。
-	广播可设置广播的间隔，最小20ms。最大10485s。
-	广播信道可以设置单独在37或者38或者39信道广播，也可剔除某个信道，在剩余两个信道广播。
-	广播可以手动开启。开启后有回调事件 BLE_GAPM_EVT_ADV_START，通过状态查看广播是否开启成功。
-	广播可以手动停止。也可设置超时时间自动停止。停止后有回调事件 BLE_GAPM_EVT_ADV_STOP，通过状态查看广播是否停止成功。



### 2. 广播应用笔记

- 广播模式（adv_mode）常用为BLE_GAP_ADV_TYPE_ADV_IND 非定向，可扫描。其他模式的使用场景请参考<<Core Specification 5.4>> LE 广播章节
- 广播发现模式（disc_mode）常用为BLE_GAP_DISC_MODE_GEN_DISCOVERABLE 一般可发现模式。其他模式的使用场景请参考<<Core Specification 5.4>> LE 广播章节。
- 广播白名单的使用方法请参考SDK_Folder\projects\ble\ble_peripheral\ble_app_hids_keyboard 工程。
- 广播数据需要按照LTV格式放置即1 Byte Length,1Byte Type,N Byte data 例如{0x0b, BLE_GAP_AD_TYPE_COMPLETE_NAME,'G', 'o', 'o', 'd', 'i', 'x', '_', 'H', 'R', 'M',}
- 广播参数中有广播持续时间duration，设置为0则是一直开广播，需要手动关闭，其他值则会到持续事件后自动停止广播。
- GR551X 最大一次开5个广播，GR5526 最大一次开4个广播，GR5525，GR533X 最大一次开2个广播。
- GR5XX 广播信道支持配置私有信道，可咨询FAE获取方法。



### 3. BLE 广播FAQ

- Q:广播数据是否可以一直改动？

  A: ble_gap_update_adv_data可以一直修改广播数据，扫描回复数据，并且期间不用停止广播。需要注意必须广播开启成功后调用ble_gap_update_adv_data才可生效修改。

- Q:如何同时启动两个广播？

  A:在一个广播开启成功后再开启另一个。即收到BLE_GAPM_EVT_ADV_START 事件后再开启adv_idx不同的另一个广播。 详细请参考SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave 工程

- Q：如何启动多广播？

  A: 参考SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave 工程，同时使用随机地址

  ble_gap_adv_param_set(uint8_t adv_idx, gap_own_addr_t own_addr_type, gap_adv_param_t* p_adv_param)

  配置广播参数时， own_addr_type 使用 BLE_GAP_OWN_ADDR_GEN_RSLV

- Q:是否支持动态修改广播间隔？

  A:不支持动态修改，必须停止广播重新设置广播参数后启动广播。

- Q:如何设置广播功率？

  A:在广播开启成功后，调用ble_gap_tx_power_set()。

- Q:HID设备如何设置广播可以让系统蓝牙显示出设备名称？

  A:Android系统蓝牙中需要显示键盘的图标，需在广播包中添加描述符BLE_APPEARANCE_HID_KEYBOARD 字段.在IOS系统蓝牙中需要显示出设备名称，需在广播包中添加描述符BLE_ATT_SVC_HID 字段

- Q：如何让广播包可以用31Byte,而不是28Byte?

  A: CFG_MAX_ADV_DATA_LEN_SUPPORT 配置为1 ，disc_mode 设置为 GAP_DISC_MODE_NON_DISCOVERABLE。就可以去掉默认的3Byte 默认Flag.
