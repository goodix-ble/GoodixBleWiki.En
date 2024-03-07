# BLE常见异常说明

[TOC]

## 1. BLE 断连原因介绍分析

-	BLE 断连事件的event中有断连的原因gapc_evt.params.disconnected.reason，可通过断连原因初步定位问题。



## 2. 常见断连原因

### 2.1 0x98 超时断连

对应BLE Spec 0x08 错误码。可能是主设备突然不发包导致从设备超时断连，也可能是从设备突然无法正常收到，导致出现超时断连。

出现该问题后，需先确认射频性能是否正常，即是否出现了远离或天线是否正常。如射频性能正常，需确认主设备或从设备代码调度是否正常。

即是否存长时间关中断，长时间占用高优先级中断的操作。

	5525\5526\5331 等芯片可通过如下方法确认调度是否正常，即isr和 start 有规律的均匀产生
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
	5515 芯片可通过如下方法确认调度是否正常，即isr和 start 有规律的均匀产生
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



### 2.2 0xB8 即时指令错过

对应BLE Spec 0x28 错误码。指的主设备约定某一时刻经行变化的操作（信道表更新，连接参数更新，Phy更新等）。但时间过了后从设备才收到该数据包。出现的分析方法同0x98。需先确认射频性能是否正常，即是否出现了远离或天线是否正常。如射频性能正常，需确认主设备或从设备代码调度是否正常。即是否存长时间关中断，长时间占用高优先级中断的操作。



### 2.3 0xB2 响应超时

对应BLE Spec 0x22 错误码。指的是发送给对端的指令（加密请求，连接参数更新请求，数据长度更新请求，Phy更新请求等），
对端没有及时回复（40s之内）即本端出现0xB2断连,对端则出现0xA3断连，出现后需对端检查没有及时回复的原因，是否不支持本段发送的指令，或出现异常无法正常回复。



### 2.4 0xCE 建连失败

该断连原因常出现在主设备端。即主设备收到广播后发起连接请求，但从设备没有收到，根据Spec协议规定，主设备发出连接请求后，默认对方是可以正常收到的。主设备因此就会进入连接态。后续的6个连接间隔之内主设备若还没有正常收到从设备回复则会上报0Xce断连.出现该问题后，需确认环境是否有过多蓝牙设备。主从设备之间的距离是否太远。

### 2.5 0xA3 远端主动断连

对应BLE Spec 0x13 错误码。该断连原因较为常见，即对端设备设备主动关闭蓝牙，或应用主动断开蓝牙均会在从设备端出现该断连原因。若没有出现主动关闭或断开的操作。需抓取空口包确认在断连前40s 是否存在对端设备发起了SMP/GATT/LLCP流程，但本段设备无响应的情况。若本段支持该流程但未使能则需使能。若不支持需告知对端取消该流程。



### 2.6 0xA6 本端主动断连

对应BLE Spec 0x16 错误码。本段主动断开BLE。



### 2.7 0xCD 加密相关断连

对应BLE Spec 0x3D 错误码。

1. 确认两端设备是否存在清除绑定信息，修改绑定信息，修改安全参数等操作。若存在，需确认操作是否满足正常业务需求。如满足则是正常出现0xCD断连,否则需要调整流程。

2. 确保在配对加密过程中不存在非配对加密的LLCP流程（连接参数更新，channel map更新，数据长度更新等一系列控制流程）插入。如果存在，则会出现0xCD断连。



### 2.8 其他断连原因

- 参考SDK_Folder\components\sdk\ble_error.h

