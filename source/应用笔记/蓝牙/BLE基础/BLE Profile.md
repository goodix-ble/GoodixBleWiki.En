## BLE Profile



### 1. Profile 基本概念介绍

- BLE Profile是包含对应Client，Server以及相互之间操作说明的配置文件。
- 单个Profile可能包含若干个Services。
- 单个Service包含若干个characters，这些characters由若干个uuid组成。
- uuid是蓝牙规范中通用唯一标识符，用于标识蓝牙规范中提到的几乎所有实例。比如标识某个服务，某个属性等。
- uuid分为蓝牙规范预留的部分，和可用于用户自定义的部分。
- 在一个BLE server中，必须包含两个基本profile：GAP & GATT，在协议栈中默认添加，无需用户添加。其他profile可由用户自行按需定义添加。
- 详细概念参考蓝牙规范 `Core Specification 5.4`。
- 蓝牙规范预定义UUID，参考链接`https://www.bluetooth.com/specifications/assigned-numbers/`



### 2. Profile 应用笔记 

- 添加自定义service，请参考官网文档`GR5xx应用及自定义Sample Service`。
- 创建、修改自定义service中的character，参考官网文档`GR5xx应用及自定义Sample Service`中`samples_attr_tab[SAMPLES_IDX_NB]`定义，进行创建和修改。
- 添加自定义`128-bit uuid`示例，请参考官网文档`GR5xx应用及自定义Sample Service`中`samples_attr_tab[SAMPLES_IDX_NB]`。
- 添加`16-bit uuid`示例，请参考任意标准service示例，如`SDK_Folder\components\profiles\cts\cts.c`中`cts_attr_tab[CTS_IDX_NB]`。



### 3. Profile FAQ

1. 我在示例工程中未添加任何service，但是连接手机后还是能看到两个services，请问这两个工程是哪里来的，分别有什么用处。 
	- 这两个服务分别是`Generic Access Service`和`Generic Attribute Service`，为BLE协议栈必需的基础服务，在底层由我们的协议栈默认添加。
	- `Generic Access Service（UUID 1800）`为`Generic Access Profile`的服务组成部分。 `Generic Access Profile`简称GAP，定义了与发现蓝牙设备（未连接状态）相关的通用程序，以及连接到蓝牙设备的链路管理方面（连接状态）。它也规定了与使用不同安全级别相关的程序。此外，该配置文件包含了用户界面层次可访问参数的通用格式要求。
	- `Generic Attribute Service（UUID 1801）`为`Generic Attribute Profile`的服务组成部分。 `Generic Attribute Profile`简称GATT，该部分定义了通用属性配置文件，它使用属性协议描述了一个服务框架，用于发现服务以及在对等设备上读取和写入特征值。
	- 这两部分完全由协议栈维护，不需要用户额外操作，用户了解即可。
2. 芯片创建BLE服务的数量有限制吗？ 最大支持创建多少个？ 
	- 参考SDK中`custom_config.h`文件，`CFG_MAX_PRFS`配置范围。 目前配置范围为`1-64`。
3. 执行`ble_gattc_prf_read`，回调的status为0x0005， 是什么意思?
	- 该指令用于读取对应handle的值，读写值需要关注权限问题。
	- 请检查server端对应character的权限是否设置正确，或是当前连接状态是否满足操作权限。
	- 该问题为当前连接状态安全等级不够，需要先进行认证，之后进行读值操作。
4. SDK中文件传输有没有范例，实现该功能的方法 有什么建议？
	- 请参考示例工程`SDK_Folder\projects\ble\ble_peripheral\ble_app_uart`
	- 使用方法请参考文档：`《 GR551x Serial Port Profile示例手册 》`
5. 关于`static void samples_cccd_set_cb(uint8_t conn_idx, uint16_t handle, uint16_t cccd_value)`函数，在连接的时候总是会报一个这个事件，`cccd_value = SAMPLES_EVT_TX_NOTIFICATION_DISABLED`，问一下这个函数的作用是什么，这个值的含义是如何的？
	- 每次建立连接时，此回调接口用于通知用户恢复 cccd 值。如果设备bonded，恢复的cccd 值将是上次保存到nvds 的值。如果是非bond 设备恢复的值为默认值0.
	- `cccd value` 属于 `Client Characteristic Configuration`特征的value ， 用户控制server 端发送通知和指示。可以理解为server 端为对端保存的一个订阅信息，表示是否订阅server 端的通知和指示。
	- client 需要通过发起write 请求写操作来修改cccd value。如果写操作时设备已经bond，写的cccd value同时存放到nvds 里面。下次建立连接时候，如果对端是已经bond 的设备，将会从nvds 里面加载订阅信息，通过此接口恢复`cccd value`通知给用户；如果连接是非bond 设备，此接口也会调用通知用户设置`cccd value `为默认值。