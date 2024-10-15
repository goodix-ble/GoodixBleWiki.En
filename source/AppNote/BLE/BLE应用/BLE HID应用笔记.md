## BLE HID Applications



### 1. Introduction to BLE HID

* The full name of HID is Human Interface Device, which translates to Human Machine Interface Device, a term coined by Microsoft's Mike Van Flandern. The USB committee created a working group (Human Input Device) which was renamed Human Interface Device. Committee](https://www.usb.org/) for protocol-related information, such as [HID Usage Tables](https://www.usb.org/document-library/hid-usage-tables-14)  and  [Device Class Definition for HID 1.11](https://www.usb.org/document-library/device-class-definition-hid-111).
* The BLE HID protocol specification is modeled after the USB HID protocol specification, which can be considered as the wireless method of USB HID, and the specific Spec can refer to [HID Over GATT Profile (HOGP)](https://www.bluetooth.org/docman/handlers/downloaddoc .ashx?doc_id=245141).
* The HOGP protocol defines two roles:
  * HID Host: e.g. cell phone, computer, TV, tablet etc. A HID Host can connect to multiple HID Devices.
  * HID Device: e.g. Mouse, Keyboard, Active Pen, Remote Control, Selfie Stick, etc. A HID Device can only be actively connected to one HID Device at a time. A HID Device can only be actively connected to one HID Host at a time.
* BLE HID Device supports three kinds of reports (Report): Input, Output and Feature.
  * Input report: BLE HID slave device sends data to BLE HID Host device.
  * Output report: BLE HID master device sends data to BLE HID slave device.
  * Feature Report: Bidirectional Data Channel
* HID has two Channels:
  * Control Channel: Report is transmitted on this Channel is called Synchronous Report.
  * Interrupt Channel: Report is transmitted on this Channel is called Asynchronous Report.
* The USB Working Group has released the Report Creation Tool [Report Descriptor Tool](https://www.usb.org/document-library/hid-descriptor-tool) to easily create MAP tables.
* The UUID is 0x1812 (standard specification), the data is stored in the report, and the report data of the HID is sent and received by each characteristic Characteristic below. The specific data definition can refer to [HOGP specification](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=245141).
* Common products include Bluetooth Mouse, Bluetooth Keyboard, Bluetooth Gamepad, Bluetooth Selfie Stick and so on.



### 2. BLE HID Application Notes

* When realizing BLE HID application, the basic steps are as follows:
  1. Add the HID Map of the corresponding device for the application function.
  2. Add the data length and report type of the corresponding device in the service. 3.
  3. Send the corresponding data to the master device as required.
  
* BLE HID applications are usually pair-bound. In actual product development, in order to get a better experience, after disconnection, a fast and slow broadcast strategy is needed. For example, directional broadcasting is performed first; after timeout, fast broadcasting is used, with 100 ms broadcasting interval, lasting for 5s; after timeout, slow broadcasting is used, with 1s broadcasting interval. For the specific code implementation, you can refer to the ble_app_hids_keyboard sample project in the `SDK projects\ble\ble_peripheral` directory.

* Different applications simulate different actions, for example:
  * Mouse: left-middle-right buttons, scroll wheel, X/Y coordinates
  * Keyboard: full keyboard, keypad
  * Selfie stick: phone volume keys
  * Trackpad: touch events, X/Y coordinates
  
* When implementing the HID application, you can refer to the ble_app_hids_keyboard and ble_app_hids_mouse sample projects in the `SDK projects\ble\ble_peripheral` directory, as well as the document “[GR5xx Mouse Sample Manual](https://docs. goodix.com/zh/online/hid_mouse_bl)”.

* Need to display keyboard/mouse icon in Android Bluetooth, need to add descriptor `BLE_APPEARANCE_HID_KEYBOARD` field, e.g. SDK keyboard sample project adv_dta:

```c
  static const uint8_t s_adv_data_set[] = /**< Advertising data. */
  {
      0x0A, // Length of this data
      'G', 'o', 'o', 'd', 'i', 'x', '_', 'K', 'B'.
      0x03,
      BLE_GAP_AD_TYPE_APPEARANCE,
      LO_U16(BLE_APPEARANCE_HID_KEYBOARD),
      HI_U16(BLE_APPEARANCE_HID_KEYBOARD), //Android system ble can show keyborad
      0x07, // Length
      BLE_GAP_AD_TYPE_COMPLETE_LIST_16_BIT_UUID, //IOS system ble can show name 
      LO_U16(BLE_ATT_SVC_HID), // HI_U16(BLE_GAP_AD_TYPE_COMPLETE_LIST_16_BIT_UUID)
      HI_U16(BLE_ATT_SVC_HID), LO_U16(BLE_ATT_SVC_HID), //IOS system ble can show name.
      HI_U16(BLE_ATT_SVC_DEVICE_INFO),
  };
```

* In iOS system Bluetooth if you need to display the device name, you need to add the descriptor `BLE_ATT_SVC_HID` field, as shown in the above sample code.

* HID Touchscreen is no longer supported in iOS after version 14.2. If you need to realize the up and down page flip and like function of the application on iOS, you can use the hid input pointer device to bind custom gestures to realize the screen sliding. It is best to use the mouse wheel. However, different versions of iOS may have incompatible coordinates or scroll wheel, this time you need to adjust the iOS trackpad sensitivity.

* Connect with Android to realize up and down page flip and like function. It is measured that using Finger Touch works best. Under the 60 Hz interval, ensure that each interval to send a packet.

* The application scenarios of commercially available devices need to be compatible with both Android and iOS devices. Therefore, for the sake of compatibility, the map information of various devices such as mouse, touch, media and keyboard will be added in HID MAP at the same time. Users can choose to use different HID data to send according to different application scenarios.

* HID applications are categorized into many device types, such as: mouse, keyboard, active pen, touch pad, etc. The requirements of such applications for CI are generally clearer.

  * Mouse, active pen: Continuous upload data refresh rate is generally required to be 60 Hz, so the CI is generally set to 15 ms.
  * Keyboard: the smaller the CI is generally required, the better.
  * Touchpad: the general minimum CI requirement of 60 Hz. However, the general product in order to differentiate, will enhance the data refresh rate, at this time, adjusted down to the corresponding CI.
  * Overall, HID applications in the CI is generally clear from the product requirements, adjustable range is not large.

* HID applications in the case of CI clear, reduce power consumption can consider adjusting Slave Latency.

  * Mouse, active pen, touchpad: can be configured Slave Latency, because only the presence of device uplink data.
  * Keyboard: not necessarily configurable Slave Latency, such as the existence of Host configuration device capitalization indicator state.
  * In the case of can not work for a long time, active disconnection, in use through the Sensor trigger broadcast issued, waiting for Host back to connect.

* HID applications generally do not exist long-distance communication. In case of abnormal communication interactions, it is necessary to disconnect quickly and turn on the broadcast to wait for the return connection, so the Sup Timeout can be configured with a smaller value.



### 3. FAQ

#### 3.1 After the HID device is successfully connected to the iOS device, the device does not respond, what is the reason?

**A**: The connection policy of iOS system is: when the device is bound, as long as the binding is not canceled on the mobile system side, the iOS side will automatically connect to the device. When the device side removes the pairing information, the iOS side will still connect to the device automatically, just not encrypted, so you need to check whether the app code has cleared the binding information on the device side. If you need to re-bind on iOS side, you need to delete the previously paired device by ignoring it in the setting interface, and re-pair and bind again.



#### 3.2 After the HID device is successfully paired with the host side, there is no response from the device side to send data, what is the reason?

**A**: In the actual product application development, you may encounter HID device paired with some computers, disconnected back to the connection, the computer side did not Enable CCCD, resulting in the device side in the data sent, the send failure. When encountering this problem, you can analyze it by capturing packets to see if the data is sent successfully, or try to modify the code in the HID profile to comment out the CCCD judgment conditions.



#### 3.3 The product application needs to integrate multiple Keyboard and Mouse functions, how to realize it?

**A**: For example, in the selfie stick application scenario, it needs to be compatible with both Android and iOS devices. In order to ensure compatibility, generally in the HID MAP will be added at the same time in the mouse, touch, media and keyboard and other devices map information, can be based on different application scenarios choose to use different HID data to send.
