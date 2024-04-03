## BLE 多链接

### 1. GR5XX BLE 多链接 基本功能介绍

-	多链接可以是1主多从，1从多主，也可以是多主多从。在GR5XX系列芯片中，三种模型都可以支持。
-	GR5XX 系列芯片总共可以同时支持12个业务，包括1个扫描1个广播在内.即最大连接个数为10个。通过宏CFG_MAX_CONNECTIONS 来配置最大连接个数。
-	GR5XX系列芯片支持同时开启广播和扫描，两业务时序冲突后底层动态调整优先级。

### 2. GR5XX多链接 应用笔记

- 每当有设备连接上或者被连接上时都会走进BLE_GAPC_EVT_CONNECTED事件，在该事件中可获取当前的conn_idx和对端设备的mac地址。通过mac地址和conn_idx可区分不同的设备。发送数据，接收数据，服务发现，配对加密同样是使用conn_idx区分。

- 多主多从的通信模型可以实现简单的组网需求。可参照SDK_Folder\projects\ble\ble_multi_role\ble_app_hrs_rscs_relay 工程。

- 多主多从场景下，可通过ble_gap_evt_connected_t 中ll_role 来区分当前连接创建后本段的角色是master还是slave，后续发送数据通过角色来判断是使用ble_gatts_noti_ind 或是 ble_gattc_write/ble_gattc_write_no_resp。

- 在多链接场景下，不同的链接使用不同的Phy是支持的通过ble_gap_phy_update设置，同理，不同的链接，不同的发射功率也支持，通过ble_gap_tx_power_set设置。

- 1从多主场景下，从机只需要初始化一次服务即可。后续任何主机连接上后，服务均相同。如果需要服务不同，请参考多从机SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave工程。

- 1从多主场景每条链接的每个服务下的CCCD都是独立的，必须单独使能才可以执行到发送ble_gatts_noti_ind。协议栈内部并没有对CCCD通知使能与否做判断。

### 3.GR5XX 多链接 FAQ

- Q:GR5XX芯片多少个链接下可以稳定通信？

  A: 实测在4-5个连接时，可以做到稳定通信。超过5个连接后可能存在断连现象，但是断连后可以立刻回连上。

- Q:如何优化多链接的稳定性？

  A:1主多从场景下，每当连接上从设备后，每条链接做一次链接参数更新，重新排布时间划分，避免冲突。可以做到每条链接均稳定。祥见(https://developers.goodix.com/zh/bbs/detail/87e8f3be6c9b464496381ac8f8ff4893)

  ​    1从多主场景下，可以修改链接参数，确保各个链路CI成倍数关系，但是由于主机是多台无关联设备，依旧存在出现冲突的可能。

- Q:1从多主场景下广播在连接上之后是否需要重新开启？

  A:需要重新开启广播。因为被连接上后，当前的广播会自动停止，可以在BLE_GAPM_EVT_ADV_STO或BLE_GAPC_EVT_CONNECTED中再次开启广播，如果同时开启两个相同的广播，则是其中一个广播被停止，另一个广播继续工作。

  

  
