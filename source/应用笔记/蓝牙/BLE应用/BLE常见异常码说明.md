## BLE常见异常码说明



### 1. BLE断连原因介绍分析

BLE断连事件的event中有断连的原因*gapc_evt.params.disconnected.reason*，可通过断连原因初步定位问题。



### 2. 常见断连

#### 2.1 0x98超时断连

对应BLE Spec 0x08错误码。可能是由于主设备突然停止发送数据包导致从设备超时而断连，或是由于从设备突然无法正常接收数据而出现超时断连。

出现该问题后，应当：

1. 先确认射频性能是否正常，即是否出现了远离或天线是否正常。

2. 如果射频性能正常，则需确认主设备或从设备代码调度是否正常，即是否存在长时间关中断、长时间占用高优先级中断的操作。

	GR5525\GR5526\GR5331等芯片可通过如下方法确认调度是否正常，即isr和start有规律地均匀产生。
	
	```
	typedef void (*diag_trace_func_t)(void);
	extern diag_trace_func_t diag_evt_start_cbk_start_func; 
	extern diag_trace_func_t diag_evt_start_cbk_done_func; 
	extern diag_trace_func_t diag_ble_isr_start_func; 
	extern diag_trace_func_t diag_ble_isr_done_func;
	
	void evt_start_debug_gpio_set();
	void evt_start_debug_gpio_reset();
	void ble_isr_debug_gpio_set();
	void ble_isr_debug_gpio_reset();
	
	diag_evt_start_cbk_start_func = evt_start_debug_gpio_set;
	diag_evt_start_cbk_done_func = evt_start_debug_gpio_reset;
	diag_ble_isr_start_func = ble_isr_debug_gpio_set;
	diag_ble_isr_done_func = ble_isr_debug_gpio_reset;
	```
	
	GR5515芯片可通过如下方法确认调度是否正常，即isr和start有规律地均匀产生。
	
	```
	typedef void (*diag_trace_func_t)(void);
	extern diag_trace_func_t diag_evt_start_cbk_start_func; 
	extern diag_trace_func_t diag_evt_start_cbk_done_func; 
	extern diag_trace_func_t diag_no25_isr_start_func; 
	extern diag_trace_func_t diag_no25_isr_done_func;
	
	void evt_start_debug_gpio_set();
	void evt_start_debug_gpio_reset();
	void ble_isr_debug_gpio_set();
	void ble_isr_debug_gpio_reset();
	
	diag_evt_start_cbk_start_func = evt_start_debug_gpio_set;
	diag_evt_start_cbk_done_func = evt_start_debug_gpio_reset;
	diag_no25_isr_start_func = ble_isr_debug_gpio_set;
	diag_no25_isr_done_func = ble_isr_debug_gpio_reset;
	```
	
	

#### 2.2 0xB8即时指令错过

对应BLE Spec 0x28错误码。指主设备约定某一时刻执行的操作（信道表更新、连接参数更新或PHY更新等），但从设备在约定时刻之后才接收到这些数据包。导致该问题的原因分析同0x98。

出现该问题后，应当：

1. 先确认射频性能是否正常，即是否出现了远离或天线是否正常。
2. 如果射频性能正常，则需确认主设备或从设备代码调度是否正常，即是否存在长时间关中断、长时间占用高优先级中断的操作。



#### 2.3 0xB2响应超时

对应BLE Spec 0x22错误码。指发送给对端的指令（加密请求、连接参数更新请求、数据长度更新请求或PHY更新请求等），对端没有及时回复（40s之内），本端出现0xB2断连，对端则出现0xA3断连。

出现该问题后，需对端检查没有及时回复的原因：是否不支持本端发送的指令，或出现异常无法正常回复。



#### 2.4 0xCE建连失败

该断连常出现在主设备端。即主设备接收到广播后发起连接请求，但从设备未收到请求。根据Spec协议规定，主设备发起连接请求后，默认对方是可以正常接收到请求，主设备会进入连接态。如果从设备未能在接收到连接请求后的6个连接间隔内给出正常回复，主设备将会上报断连错误码0xCE。

出现该问题后，需确认：环境是否有过多蓝牙设备，或者主从设备之间的距离是否太远。

#### 2.5 0xA3远端主动断连

对应BLE Spec 0x13错误码。该断连原因较为常见，即对端设备主动关闭蓝牙或应用主动断开蓝牙连接，均会在从设备端出现该断连。若没有出现主动关闭蓝牙或断开连接的操作，则需抓取空口包确认在断连前40s是否存在对端设备发起了SMP/GATT/LLCP流程，但本端设备无响应的情况。若本端支持该流程但未使能，则需将其使能；若本端设备不支持该流程，则需要通知对端设备取消该流程。



#### 2.6 0xA6本端主动断连

对应BLE Spec 0x16错误码。本端主动断开BLE。



#### 2.7 0xCD加密相关断连

对应BLE Spec 0x3D错误码。

1. 确认两端设备是否存在清除绑定信息、修改绑定信息或修改安全参数等操作。若存在，则需确认操作是否满足正常业务需求。如满足需求，则是正常出现0xCD断连，否则需要调整流程。

2. 确保在配对加密过程中不存在非配对加密的LLCP流程（连接参数更新、信道表更新、数据长度更新等一系列控制流程）插入。如果存在，则会出现0xCD断连。



#### 2.8 其他断连

更多内容，请参考`SDK_Folder\components\sdk\ble_error.h`。

