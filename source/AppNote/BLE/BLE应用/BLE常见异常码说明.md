## BLE exception code



### 1. BLE disconnected reason introduction and analysis

The event of BLE disconnected event has the reason of disconnection *gapc_evt.params.disconnected.reason*, which can be used to locate the problem initially.



### 2. Common causes of disconnection

#### 2.1 0x98 Timeout Disconnection

Corresponds to BLE Spec 0x08 error code. The problem may be caused by the master device suddenly stops sending packets and the slave device times out, or the slave device suddenly fails to receive data properly and times out.

When this problem occurs, you should:

1. first confirm that the RF performance is normal, i.e., whether the away or antenna appears to be normal.

2. if the RF performance is normal, confirm whether the master or slave device code scheduling is normal, i.e. whether there is a long time off interrupt, long time occupation of high priority interrupt operation.

	Chips such as GR5525\GR5526\GR5331 can be used to confirm if the scheduling is normal by the following method, i.e. isr and start are generated regularly and evenly.
	
	```
	typedef void (*diag_trace_func_t)(void);
	extern diag_trace_func_t diag_evt_start_cbk_start_func; 
	extern diag_trace_func_t diag_evt_start_cbk_done_func; extern diag_trace_func_t diag_evt_start_cbk_start_func 
	extern diag_trace_func_t diag_ble_isr_start_func; extern diag_trace_func_t diag_ble_isr_start_func 
	extern diag_trace_func_t diag_ble_isr_done_func;
	
	void evt_start_debug_gpio_set().
	void evt_start_debug_gpio_reset(); void evt_start_debug_gpio_reset().
	void ble_isr_debug_gpio_set();
	void ble_isr_debug_gpio_reset(); void
	
	diag_evt_start_cbk_start_func = evt_start_debug_gpio_set; void ble_isr_debug_gpio_reset(); void ble_isr_debug_gpio_reset()
	diag_evt_start_cbk_done_func = evt_start_debug_gpio_reset;
	diag_ble_isr_start_func = ble_isr_debug_gpio_set; diag_ble_isr_start_func = evt_start_debug_gpio_reset
	diag_ble_isr_done_func = ble_isr_debug_gpio_reset;
	```
	
	The GR5515 chip can confirm that the scheduling is normal, i.e., isr and start are generated regularly and evenly, by the following.
	
	```
	typedef void (*diag_trace_func_t)(void);
	extern diag_trace_func_t diag_evt_start_cbk_start_func; 
	extern diag_trace_func_t diag_evt_start_cbk_done_func; extern diag_trace_func_t diag_evt_start_cbk_start_func 
	extern diag_trace_func_t diag_no25_isr_start_func; extern diag_trace_func_t diag_no25_isr_start_func 
	extern diag_trace_func_t diag_no25_isr_done_func; void evt_start_delete_func
	
	void evt_start_debug_gpio_set().
	void evt_start_debug_gpio_reset();
	void ble_isr_debug_gpio_set();
	void ble_isr_debug_gpio_reset(); void
	
	diag_evt_start_cbk_start_func = evt_start_debug_gpio_set; void ble_isr_debug_gpio_reset(); void ble_isr_debug_gpio_reset()
	diag_evt_start_cbk_done_func = evt_start_debug_gpio_reset;
	diag_no25_isr_start_func = ble_isr_debug_gpio_set;
	diag_no25_isr_done_func = ble_isr_debug_gpio_reset;
	```
	
	

#### 2.2 0xB8 Immediate Instruction Misses

Corresponds to BLE Spec 0x28 error code. Refers to operations that the master device agrees to perform at a certain moment (channel table update, connection parameter update, or PHY update, etc.), but the slave device receives these packets after the agreed moment. The cause of this problem is analyzed as 0x98.

When this problem occurs, you should:

1. first confirm that the RF performance is normal, i.e. whether the away or antenna appears to be normal.
2. if the RF performance is normal, confirm whether the master or slave device code scheduling is normal, i.e., whether there are operations that turn off interrupts for a long time, or occupy high-priority interrupts for a long time.



#### 2.3 0xB2 Response Timeout

Corresponds to BLE Spec 0x22 error code. It refers to the command (encryption request, connection parameter update request, data length update request or PHY update request, etc.) sent to the opposite end, and the opposite end does not reply in time (within 40s), the local end appears to be disconnected at 0xB2, and the opposite end appears to be disconnected at 0xA3.

When this problem occurs, the peer should check the reason for not replying in time: whether the command sent by the peer is not supported, or whether there is an abnormality that prevents it from replying normally.



#### 2.4 0xCE Failure to establish connection

This disconnection often occurs at the master device side. That is, the master device receives the broadcast and initiates a connection request, but the slave device does not receive the request. According to the Spec protocol, after the master device initiates a connection request, by default the other party is able to receive the request normally, and the master device will enter the connection state. If the slave device fails to give a normal reply within 6 connection intervals after receiving the connection request, the master device will report the disconnection error code 0xCE.

When this problem occurs, you need to check whether there are too many Bluetooth devices in the environment, or whether the distance between master and slave devices is too far.

#### 2.5 0xA3 Remote Active Disconnection

Corresponds to BLE Spec 0x13 error code. This is a common cause of disconnection, i.e., if the remote device turns off the Bluetooth or the application disconnects the Bluetooth connection, the disconnection will occur at the slave device. If there is no active shutdown of Bluetooth or disconnection, it is necessary to capture the air packet to confirm whether there is a case that the device at the other end initiated the SMP/GATT/LLCP process 40s before the disconnection but there is no response from the device at the local end. If the local end supports the process but does not enable it, it needs to enable it; if the local end device does not support the process, it needs to notify the peer device to cancel the process.



#### 2.6 0xA6 Local active disconnection

Corresponds to BLE Spec 0x16 error code. This end actively disconnects from BLE.



#### 2.7 0xCD Crypto related disconnection

Corresponds to BLE Spec 0x3D error code.

1. Confirm whether there are operations such as clearing binding information, modifying binding information or modifying security parameters on both devices. If there is, confirm whether the operation meets normal business requirements. If it meets the demand, then it is a normal occurrence of 0xCD disconnection, otherwise the process needs to be adjusted.

2. Ensure that there is no non-paired encryption LLCP process (a series of control processes such as connection parameter update, channel table update, data length update, and so on) inserted during the pair encryption process. If present, 0xCD disconnection will occur.



#### 2.8 Other Disconnects

For more, see `SDK_Folder\components\sdk\ble_error.h`.
