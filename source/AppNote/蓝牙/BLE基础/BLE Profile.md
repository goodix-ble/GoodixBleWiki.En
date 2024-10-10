## BLE Profile



### 1. BLE Profile基本概念介绍

- BLE Profile指包含对应Client、Server以及相互之间操作说明的配置文件。
- 单个Profile可能包含若干个Service。
- 单个Service包含若干个Character，这些Character由若干个UUID组成。
- UUID是蓝牙规范中通用唯一标识符，用于标识蓝牙规范中提到的几乎所有实例。例如，标识某个服务、属性等。
- UUID分为蓝牙规范预留部分和用户自定义部分。
- 在一个BLE Server中，必须包含两个基本Profile：GAP & GATT，在协议栈中默认添加，无需用户添加。其他Profile可由用户自行按需定义添加。
- 详细概念介绍，请参考蓝牙规范《[Core Specification 5.4](https://www.bluetooth.com/specifications/core54-html/)》。
- 蓝牙规范预定义UUID，参考链接https://www.bluetooth.com/specifications/assigned-numbers/。



### 2. BLE Profile应用笔记

- 添加自定义Service，参考文档《[GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl/)》。
- 创建、修改自定义Service中的Character，参考文档《[GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl/)》中`samples_attr_tab[SAMPLES_IDX_NB]`定义，进行创建和修改。
- 添加自定义`128-bit uuid`示例，参考文档《[GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl/)》中`samples_attr_tab[SAMPLES_IDX_NB]`。
- 添加`16-bit uuid`示例，请参考任意标准Service示例，如`SDK_Folder\components\profiles\cts\cts.c`中的`cts_attr_tab[CTS_IDX_NB]`。



### 3. FAQ

- **Q**：在示例工程中未添加任何Service，但连接手机后能看到两个Service。请问这两个Service是从哪里来的？分别有什么用处？

  **A**：这两个服务分别是`Generic Access Service`和`Generic Attribute Service`，为BLE协议栈必需的基础服务，在底层由BLE协议栈默认添加。

  - `Generic Access Service（UUID 1800）`为`Generic Access Profile`的服务组成部分。`Generic Access Profile`简称GAP，定义了与发现蓝牙设备（未连接状态）相关的通用程序，以及连接蓝牙设备（连接状态）的链路管理，也规定了与使用不同安全级别相关的程序。另外，该配置文件包含用户界面可访问参数的通用格式要求。

  - `Generic Attribute Service（UUID 1801）`为`Generic Attribute Profile`的服务组成部分。`Generic Attribute Profile`简称GATT，定义了通用属性配置文件。它使用属性协议描述了一个服务框架，用于发现服务以及在对等设备上读取和写入特征值。

    这两个服务完全由协议栈维护，不需要用户额外操作，用户只需了解即可。

- **Q**：芯片创建BLE服务的数量有限制吗？最大可支持创建多少个服务？

  **A**：请参考SDK中*custom_config.h*文件中`CFG_MAX_PRFS`的配置范围。 目前，配置范围为`1 ~ 64`。

- **Q**：执行`ble_gattc_prf_read`，回调的status为`0x0005`，是什么意思？

  **A**：`0x0005`表示：

  - 该指令用于读取对应handle的值，读写值需要注意权限问题。

  - 需检查Server端对应Character的权限是否设置正确，或者当前连接状态是否满足操作权限。
  - 当前连接状态安全等级不够，需要先进行认证，再进行读值操作。

- **Q**：SDK中文件传输有没有范例，实现该功能的方法有什么建议？

  **A**：请参考示例工程`SDK_Folder\projects\ble\ble_peripheral\ble_app_uart`。具体使用方法，请参考文档《[GR5xx Serial Port Profile示例手册](https://docs.goodix.com/zh/online/serial_port_bl)》。

- **Q**：关于`static void samples_cccd_set_cb(uint8_t conn_idx, uint16_t handle, uint16_t cccd_value)`函数，在连接时总会报一个`cccd_value = SAMPLES_EVT_TX_NOTIFICATION_DISABLED`事件，请问这个函数的作用是什么？这个值的含义是什么？

  **A**：每次建立连接时，该回调接口用于通知用户恢复cccd值。如果设备bonded，恢复的cccd值将是上次保存到NVDS的值；如果是非bond设备，恢复的值为默认值0。

  cccd value属于`Client Characteristic Configuration`特征的Value，用户控制Server端发送通知和指示。可以理解为Server端为对端保存的一个订阅信息，表示是否订阅Server端的通知和指示。

  Client需要通过发起write请求写操作来修改cccd value。如果写操作时设备已经bond，写的cccd value同时存放到NVDS里面。下次建立连接时，如果对端是已经bond的设备，将会从NVDS里面加载订阅信息，通过此接口恢复`cccd value`通知给用户；如果连接的是非bond设备，此接口也会调用通知用户设置`cccd value `为默认值。