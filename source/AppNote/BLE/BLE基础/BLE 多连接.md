## BLE Multi-Connect

### 1. GR5xx BLE Multi-connections Basic Function Introduction

- Multi-connections can be “one master multi-slave” or “one slave multi-master”, or “multi-master multi-slave”.GR5xx series chips can support these three types.
- GR5xx series chips can support a total of 12 services at the same time, including 1 scanning and 1 broadcasting, and the maximum number of connections is 10. The maximum number of connections can be configured by the macro `CFG_MAX_CONNECTIONS`.
- GR5xx series chipsets support to enable broadcast and scanning at the same time, and the bottom layer dynamically adjusts the priority after the timing conflict of two services.

### 2. GR5xx Multi-connections Application Notes

- Once the device connects or is connected, it will enter the `BLE_GAPC_EVT_CONNECTE` event. The current conn_idx and the MAC address of the peer device can be obtained in this event. The MAC address and conn_idx can be used to distinguish between different devices. Sending data, receiving data, discovering services, and pairing encryption can all be distinguished using the conn_idx.

- The `master-multislave' communication model allows for simple networking requirements. Refer to `SDK_Folder\projects\ble\ble_multi_role\ble_app_hrs_rscs_relay` project.
- In the “multi-master multi-slave” scenario, the ll_role in ble_gap_evt_connected_t can be used to distinguish whether the role of this end is Master or Slave after the current connection is created, and the subsequent sending of data through the role to determine whether to use ble_gatts_noti_ind or ble_gattts_noti_ind. ind or ble_gattc_write/ble_gattc_write_no_resp.
- In a multi-connection scenario, support for different connections using different PHYs can be set via ble_gap_phy_update; similarly, support for different links and different transmit power can be set via ble_gap_tx_power_set.
- In the “one-slave-many-masters” scenario, the slave only needs to initialize the service once. The service is the same when any subsequent hosts are connected. If the service needs to be different, please refer to the multi-slave `SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave` project.
- In the `multi_slave` scenario, the CCCD under each service of each link is independent and must be enabled separately to execute sending ble_gatts_noti_ind. there is no internal judgment on whether CCCD notification is enabled or not in the protocol stack.

### 3. FAQ

#### 3.1 How many connections can the GR5xx chip communicate stably?

  **A**: It is measured that the communication can be stabilized with 4 to 5 connections. There may be disconnection after more than 5 connections, but it can be reconnected immediately after disconnection.

#### 3.2 How to optimize the stability of multiple connections?

  **A**: In the “one master, many slaves” scenario, once the slave devices are connected, each connection performs a connection parameter update and rearranges the time division to avoid conflicts, so as to ensure the stability of each connection. See https://developers.goodix.com/zh/bbs/detail/87e8f3be6c9b464496381ac8f8ff4893 for details.

     In the “one-slave-multiple-master” scenario, the connection parameters can be modified to ensure that the CI of each link is multiplicative. However, since the hosts are multiple unrelated devices, conflicts may still occur.

#### 3.3 Does broadcasting need to be re-enabled after the connection is established in the “one-slave-many-hosts” scenario?

  **A**: The broadcast needs to be turned on again. Because the current broadcast is automatically stopped after the connection is established, the broadcast can be turned on again in `BLE_GAPM_EVT_ADV_STO` or `BLE_GAPC_EVT_CONNECTED`. If two identical broadcasts are turned on at the same time, one is stopped and the other continues to work.  

  

  