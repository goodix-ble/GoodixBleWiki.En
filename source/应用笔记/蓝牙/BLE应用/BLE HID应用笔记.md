## BLE HID应用



### 1. BLE HID简介

* HID 全称 Human Interface Device，翻译为人类接口设备，该术语由微软 Mike Van Flandern 提出，USB 委员会创建了一个工作组(Human Input Device) 后该工作组更名为 Human Interface Device。所以可以在 [USB 委员会](https://www.usb.org/)查找协议相关的资料, 例如 [HID Usage Tables](https://www.usb.org/document-library/hid-usage-tables-14) 和 [Device Class Definition for HID 1.11](https://www.usb.org/document-library/device-class-definition-hid-111)
* BLE HID协议规范是以USB HID协议规范为蓝本，可以认为是USB HID的无线方式，具体Spec可以参考链接：[HID Over GATT Profile (HOGP)](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=245141)
* 在HOGP协议中有定义个两个角色:
  * HID Host。例如：手机，电脑，电视，平板，一个HID Host可以连接到多个HID Device
  *  HID Device。例如：鼠标，键盘，主动笔，遥控器，自拍杆等，一个HID Device一次只能主动连接到一个HIDHost
* BLE HID 设备支持三种报告（Report）：输入（Input）,输出（Output）, 特征（Feature）
  * 输入报告:BLE HID 从机设备发数据给 BLE HID主机设备
  * 输出报告:BLE HID 主机设备发数据给 BLE HID从机设备.
  * 特征报告:双向数据通道
* HID有两个Channel：
  * Control Channel，report 在此Channel上传输称为synchronous report
  * Interrupt Channel，report 在此Channel上传输称为asynchronous  report
* USB 工作小组有一个Report 创建工具 [Report Descriptor builder tool](https://www.usb.org/document-library/hid-descriptor-tool)，可以让你轻松的创建MAP表
* UUID为0x1812（标准规范），数据存放在报告中，通过下面的各个特征 characteristic 来收发 HID 的报告数据，具体的数据定义可参考[HOGP specification](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=245141)
* 我们常见产品有：蓝牙鼠标，蓝牙键盘，蓝牙游戏手柄，蓝牙自拍杆等。

### 2. BLE HID应用笔记

* 在实现BLE HID应用时，基本步骤如下：
  1. 针对应用功能，添加对应设备的hid map
  2. 服务中添加对应设备的数据长度，报告类型
  3. 按照需求发送对应的数据给主设备
  
* BLE HID 应用通常会进行配对绑定使用，在实际产品开发中了，为了获得更好的体验，在断连后，需要采用快慢广播策略，比如先进行定向广播，超时后，使用快广播，广播间隔100ms，持续5S，超时后，使用慢广播，广播间隔1S。具体的代码实现，可以参考SDK projects\ble\ble_peripheral目录下的ble_app_hids_keyboard示例工程。

* 不同应用模拟的动作不同，例如：
  * 鼠标: 左中右按键，滚轮，X，Y坐标
  * 键盘：全键盘，小键盘
  * 自拍杆：手机音量键
  * 触控板：触摸事件，X,Y坐标
  
* 在实现HID 应用时，可以参考SDK projects\ble\ble_peripheral目录下的ble_app_hids_keyboard和ble_app_hids_mouse示例工程，以及GR5xx鼠标示例手册：https://docs.goodix.com/zh/online/detail/hid_mouse_bl/V3.2/a9c4a8d0637cc6d73f125bdadebb4eec

* 在Android 系统蓝牙中需要显示键盘/鼠标的图标，需添加描述符BLE_APPEARANCE_HID_KEYBOARD 字段，例如SDK keyboard示例工程adv_dta：

  ```
  static const uint8_t s_adv_data_set[] =                 /**< Advertising data. */
  {
      0x0A,   // Length of this data
      BLE_GAP_AD_TYPE_COMPLETE_NAME,
      'G', 'o', 'o', 'd', 'i', 'x', '_', 'K', 'B',
      0x03,
      BLE_GAP_AD_TYPE_APPEARANCE,
      LO_U16(BLE_APPEARANCE_HID_KEYBOARD),
      HI_U16(BLE_APPEARANCE_HID_KEYBOARD),              //Android system ble can show keyborad
      0x07,   // Length
      BLE_GAP_AD_TYPE_COMPLETE_LIST_16_BIT_UUID,       //IOS system ble can show name 
      LO_U16(BLE_ATT_SVC_HID),
      HI_U16(BLE_ATT_SVC_HID),
      LO_U16(BLE_ATT_SVC_BATTERY_SERVICE),
      HI_U16(BLE_ATT_SVC_BATTERY_SERVICE),
      LO_U16(BLE_ATT_SVC_DEVICE_INFO),
      HI_U16(BLE_ATT_SVC_DEVICE_INFO),
  };
  ```

* 在IOS系统蓝牙中需要显示出设备名称，需添加描述符BLE_ATT_SVC_HID 字段，如上面示例代码展示

* IOS在14.2版本以后不再支持hid touchscreen，在IOS上实现应用上下翻页，点赞功能，需要通过hid input指针设备绑定自定义手势实现屏幕滑动，实测使用鼠标滚轮效果最佳，但不同版本IOS可能存在坐标或滚轮不兼容，此时需调整IOS 触控板灵敏度

* 与Android连接实现应用上下翻页，点赞功能，实测使用Finger Touch效果最佳，在60HZ interval下，保证每个interval发送一个数据包

* 市场上的设备的应用场景都是需要同时兼容Android,IOS设备，故为了兼容性考虑，一般在HID MAP中会同时添加 鼠标，触摸，媒体，键盘等多种设备的map信息，之后根据不同的应用场景选择使用不同HID 数据来发送。

* HID应用分很多设备类型，比如：鼠标、键盘、主动笔、触摸板等等，此类应用对CI的要求一般是比较明确的

  * 鼠标、主动笔：连续上报数据刷新率一般要求60Hz，因此一般CI都会设置为15ms
  * 键盘：一般要求CI越小越好
  * 触摸板：一般最小也是要求60Hz，但是一般产品为了差异化，会提升数据刷新率，此时调小到对应CI
  * 整体看来，HID应用中CI一般都由产品需求进行了明确，可调范围不大

* HID应用当CI明确下，降低功耗可考虑调整Slave Latency

  * 鼠标、主动笔、触摸板：可以配置Slave Latency，因仅存在设备上行数据；
  * 键盘：不一定可配置Slave Latency，比如存在Host配置设备大写指示灯状态；
  * 也可长时间不工作的情况下，主动断开连接，在使用时通过Sensor触发广播发出，等待Host回连

* HID应用一般不存在长距离通信，一旦发生通信交互异常，需快速断链开启广播等待回连，因此Sup Timeout可以配置较小值



### 3. BLE HID 应用FAQ

1. HID设备与IOS设备连接成功后，设备无响应，是什么原因？

   > IOS系统的连接策略是，当设备绑定后，只要不在手机系统端取消绑定，IOS端会自动连接设备；当将设备端将配对信息去掉，IOS端也是会自动连接设备，只是没有加密，所以需要检查应用代码中，是否将设备端的绑定信息进行了清除。如果需要在IOS端重新绑定，需要在设置界面，将之前配对的设备进行忽略删除，重新进行配对绑定。

2. HID 设备与主机端配对成功后，设备端发送数据无响应，是什么原因？

   > 在实际产品应用开发中，有遇到过HID设备跟一些电脑配对后，断连后回连时，电脑端没有enable cccd，导致设备端在发送数据时，发送失败。遇到此问题时，可以通过抓包进行分析，看数据是否发送成功，或者尝试修改HID profile中代码，将CCCD判断条件注释掉。

3. 产品应用中需要集成多Keyboard和Mouse功能，怎么实现？

   > 比如在自拍杆应用场景中，都是需要同时兼容Android,IOS设备，故为了兼容性考虑，一般在HID MAP中会同时添加 鼠标，触摸，媒体，键盘等多种设备的map信息，之后根据不同的应用场景选择使用不同HID 数据来发送

