## BLE Profile



### 1. Introduction to the basic concept of BLE Profile

- A BLE Profile is a configuration file that contains descriptions of the operations of a Client, a Server, and each other.
- A single profile may contain several services.
- A single Service may contain several Characters, which are composed of several UUIDs.
- A UUID is a universally unique identifier used in the Bluetooth specification to identify almost all instances mentioned in the Bluetooth specification. For example, to identify a particular service, property, etc.
- UUIDs are divided into Bluetooth specification reserved parts and user-defined parts.
- In a BLE Server, there are two basic Profiles that must be included: GAP & GATT, which are added by default in the protocol stack and do not need to be added by the user. The other profiles can be added by user-defined profiles.
- Please refer to the Bluetooth specification “[Core Specification 5.4](https://www.bluetooth.com/specifications/core54-html/)” for more details.
- For the predefined UUID of Bluetooth specification, please refer to the link https://www.bluetooth.com/specifications/assigned-numbers/.



### 2. BLE Profile Application Notes

- Add custom Service, refer to the document “[GR5xx Application and Custom Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl/)”.
- Create and modify Character in the custom Service, refer to document << [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl/) >> in samples  `samples_attr_tab[SAMPLES_IDX_NB]` definition for creation and modification.
- To add a custom `128-bit uuid` example, refer to the   `samples_attr_tab[SAMPLES_IDX_NB]` defined in the document << [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl/) >>.
- To add `16-bit uuid` example, please refer to any standard Service example, such as `cts_attr_tab[CTS_IDX_NB]` in `SDK_Folder\components\profiles\cts\cts.c`.



### 3. FAQ

#### 3.1 I didn't add any Service in the sample project, but I can see two Services after connecting to the phone, where do these two Services come from? What are they used for?

  **A**: These two services are `Generic Access Service` and `Generic Attribute Service`, which are the basic services required by the BLE stack, and are added by default by the BLE stack at the bottom layer.

  - The `Generic Access Service (UUID 1800)` is a service component of the `Generic Access Profile`. The `Generic Access Profile`, abbreviated as GAP, defines the generic procedures related to the discovery of Bluetooth devices (unconnected state) and the link management for connecting Bluetooth devices (connected state), as well as the procedures related to the use of different security levels. In addition, this profile contains requirements for a common format for user interface accessible parameters.

  - The `Generic Attribute Service (UUID 1801)` is the service component of the `Generic Attribute Profile`. The `Generic Attribute Profile`, abbreviated as GATT, defines a generic attribute profile. It uses the Attribute Protocol to describe a framework of services for discovering services and for reading and writing feature values on peer devices.

    These two services are maintained entirely by the protocol stack and require no additional user action; the user only needs to know about them.

#### 3.2 Is there a limit to the number of BLE services that can be created by the chip? What is the maximum number of services that can be supported to be created?

  **A**: Please refer to the configuration range of `CFG_MAX_PRFS` in the *custom_config.h* file in the SDK. Currently, the configuration range is `1 ~ 64`.

#### 3.3 Execute `ble_gattc_prf_read` and the callback status is `0x0005`, what does it mean?

  **A**: `0x0005` means:

  - This instruction is used to read the value of the corresponding handle, reading and writing the value need to pay attention to the permission problem.

  - You need to check whether the permissions of the corresponding Character on the Server side are set correctly, or whether the current connection status meets the operation permissions.
  - If the current connection status is not secure enough, you need to authenticate first, and then read the value.

#### 3.4  Is there any example of file transfer in SDK and what is the suggested method to realize this function?

  **A**: Please refer to the example project `SDK_Folder\projects\ble\ble_peripheral\ble_app_uart`. Please refer to the document `[GR5xx Serial Port Profile Example Manual](https://docs.goodix.com/zh/online/serial_port_bl)' for details on how to use it.

#### 3.5 Regarding the `static void samples_cccd_set_cb(uint8_t conn_idx, uint16_t handle, uint16_t cccd_value)` function, when connecting it will always report a `cccd_value = SAMPLES_EVT_TX_ NOTIFICATION_DISABLED` event when connecting. What is the meaning of this value?

  **A** : This callback interface is used to notify the user to restore the cccd value every time a connection is established. If the device is bonded, the restored cccd value will be the value last saved to NVDS; if it is a non-bonded device, the restored value is the default value 0.

  - The cccd value belongs to the Value of the `Client Characteristic Configuration` feature, where the user controls the Server side to send notifications and instructions. It can be understood as a subscription information that Server side keeps for the peer side, indicating whether or not to subscribe to the notifications and instructions of Server side.

  - The Client needs to modify the cccd value by initiating a write request, and if the device is bonded during the write operation, the written cccd value is stored in the NVDS at the same time. If the device is bonded when the write operation is performed, the cccd value will be stored in the NVDS. The next time a connection is established, if the device is bonded, the subscription information will be loaded from the NVDS, and the cccd value will be restored to the user through this interface; if the device is not bonded, this interface will be called to notify the user that the cccd value is set to the default value.