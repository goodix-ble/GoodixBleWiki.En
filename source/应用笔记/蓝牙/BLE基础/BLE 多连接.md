## BLE多连接

### 1. GR5xx BLE多连接基本功能介绍

-	多连接可以是 “一主多从” 或 “一从多主”，也可以是 “多主多从”。GR5xx系列芯片可支持这三种类型。
-	GR5xx系列芯片总共可以同时支持12个业务，包括1个扫描1个广播，最大连接个数为10。可通过宏`CFG_MAX_CONNECTIONS`配置最大连接数。
-	GR5xx系列芯片支持同时开启广播和扫描，两业务时序冲突后底层动态调整优先级。

### 2. GR5xx多连接应用笔记

- 一旦设备连接上或者被连接上，将进入`BLE_GAPC_EVT_CONNECTE`事件。在该事件中可获取当前的conn_idx和对端设备的MAC地址。通过MAC地址和conn_idx可区分不同的设备。发送数据、接收数据、发现服务、配对加密均可使用conn_idx区分。

- “多主多从” 的通信模型可以实现简单的组网需求。可参照`SDK_Folder\projects\ble\ble_multi_role\ble_app_hrs_rscs_relay`工程。
- 在 “多主多从” 场景下，可通过ble_gap_evt_connected_t中的ll_role区分当前连接创建后本端角色是Master还是Slave，后续发送数据通过角色判断是使用ble_gatts_noti_ind或是ble_gattc_write/ble_gattc_write_no_resp。
- 在多连接场景下，支持不同的连接使用不同的PHY，可通过ble_gap_phy_update设置；同理，支持不同的链接和不同的发射功率，可通过ble_gap_tx_power_set设置。
- 在 “一从多主” 场景下，从机只需要初始化一次服务即可。后续任何主机连接上后，服务均相同。如果需要服务不同，请参考多从机`SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave`工程。
- 在 “一从多主” 场景下，每条链接的每个服务下的CCCD都是独立的，必须单独使能才可以执行发送ble_gatts_noti_ind。协议栈内部并没有对CCCD通知使能与否做判断。

### 3. FAQ

- **Q**：GR5xx芯片在多少个连接下可以稳定通信？

  **A**：实测在4～5个连接时，可以做到稳定通信。超过5个连接后可能存在断连现象，但是断连后可以立刻回连上。

- **Q**：如何优化多连接的稳定性？

  **A**：“一主多从” 场景下，一旦连接上从设备，每条连接执行一次连接参数更新，并重新排布时间划分，避免冲突，从而保证每条连接均稳定。详见https://developers.goodix.com/zh/bbs/detail/87e8f3be6c9b464496381ac8f8ff4893。

     “一从多主”场景下，可以修改连接参数，确保各个链路CI成倍数关系。但由于主机是多台无关联设备，依旧可能出现冲突。

- **Q**：“一从多主” 场景下广播在连接建立之后是否需要重新开启？

  **A**：需要重新开启广播。因为连接建立后，当前的广播会自动停止，可以在`BLE_GAPM_EVT_ADV_STO`或`BLE_GAPC_EVT_CONNECTED`中再次开启广播。若同时开启两个相同的广播，则其中一个广播被停止，另一个广播继续工作。

  

  
