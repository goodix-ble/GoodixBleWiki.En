## BLE Multi Role


### 1. Introduction to GR5xx Multi-Master-Multi-Slave Concepts

1. BLE Master-Slave Device Profile
    - The BLE Generic Attribute Profile `GATT (Generic Attribute Profile)` defines the data communication between two devices. When two devices are connected, one device acts as a `GATT Server (Slave or Slave)` and the other device acts as a `GATT Client (Master or Host)`.
    - GATT client: the device initiates commands, requests and receives responses, notifications and instructions.
    - GATT server: the device receives commands, requests and sends responses, notifications and instructions.
    - A BLE device can act as both a master and a slave at the same time, a feature known as `Multiple Roles`.
    - A single BLE device can be enabled in this mode, i.e., **Master-Slave**. It has a dual identity as a master and a slave, and can search for, connect to, and manage other BLE slaves as a master, while also being discovered, connected to, and managed by other BLE host devices as a slave.
    - For details on the `GAP and GATT` content involved in multi-master multi-slave, please refer to the [GR551x BLE Stack User Guide](https://docs.goodix.com/zh/online/detail/gr55xx_ble_stack_user_guide).
2. Introduction to GR5xx Multi-Master Multi-Slave
    - GR5xx Multi-Master-Multi-Slave is based on BLE Master-Slave device, which is able to realize multi-role (Slave Peripheral & Host Central) and multi-connection application scenarios on a single SoC.
    - Functions supported by GR5xx host:
        - Scanning: The host can continuously scan and listen to the broadcasts of peripheral devices to search, discover and filter peripheral devices.
        - Initiate Connection: The host can initiate a connection request to selected slaves and establish one or more connections with them.
        - GATT Client: The host acts as a GATT client, controlling or exchanging data with the slaves by reading and writing the characteristics of the server.
        - Connection Management: The host is responsible for connection management with multiple slaves, and users can develop customized functions for different slaves.
        - Connection parameter update: The host can modify the parameters of the current connection to improve communication efficiency or reduce power consumption.
    - Functions supported by GR5xx slaves:
        - Broadcast: Slaves set up broadcast packets containing specific advertisement data (e.g., device name, services and features) and initiate periodic broadcasts.
        - Accept Scan and Respond to Connections: Slaves can be scanned, discovered, and requested to connect by a host.
        - GATT Server: The slave acts as a GATT server, defining the services and features provided by the BLE device and allowing the host to read or write.
        - Data Upload: The slave sends data proactively by sending Notification or Indication messages to the host.
        - Connection Parameter Update Request: The slave can request the host to change the existing connection parameters to optimize the transmission efficiency and power consumption.
3. GR5xx Multi-Master Multi-Slave Application Scenarios
    - Typical application scenarios: A smartwatch with health tracking function can be used as a BLE host to collect data from multiple other wearable devices, such as heart rate and blood oxygen sensors of a chest strap; at the same time, it can also be used as a slave to synchronize the data to the user's mobile app.
    - Other application scenarios include but are not limited to:
        - Sports and health tracking devices
        - Smart Wearable Devices
        - Smart home
        - Internet of Things (IoT) Gateway



### 2. GR5xx Multi-Master Multi-Slave Application Notes

- Multi-master multi-slave:
    - You can refer to the SDK sample project `SDK_Folder\projects\ble\ble_multi_role\ble_app_hrs_rscs_relay`.
    - This project demonstrates the application of the GR5xx chip to a multi-role, multi-connection scenario, realizing the heart rate sensor and running speed and step frequency sensor relay device functions.
- Master-Slave:
    - Refer to the SDK project `SDK_Folder\projects\ble\ble_multi_role\ble_app_uart_multi_link`.
    - This project demonstrates using a single GR5xx chip as both a master and a slave to support one master and multiple slaves.
- Multi-master, multi-slave multi-role scenarios **Host** Functionality Implementation Methodology:
    - Set the scanning parameters and turn on traditional or extended scanning. For the implementation of the scanning process, please refer to [Example description of turning on active scanning after Bluetooth connection](https://developers.goodix.com/zh/bbs/blog_detail/dc587d956a1a431c9021d6a9be8c52cb).
    - When the target device is scanned, set reasonable connection parameters and initiate extended connection (BT Core Spec 5.0 and above) process or traditional connection process.
    - Connecting to the device is successful, and the main services and features of the peer slave can be discovered in the protocol stack `BLE_GAPC_EVT_CONNECTED` callback.
    - Service discovery is complete, and the notification function is enabled by writing the CCCD feature configuration value of the opposite end to perform the GATT client (host) Write down message process.
    - The host also needs to process the `ATT_WRITE_RSP` packets sent by the slaves and the outgoing notification messages.
- Approach to **Slave** Functionality Implementation in Multi-Role Scenarios with Multiple Masters and Multiple Slaves:
    - The GATT Service (Slave) contains one or more BLE Profiles to implement specific Bluetooth features. To add a custom Service, please refer to “[GR5xx Application and Custom Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl)”.
    - Set the Broadcast Data, Scan Response Data, Parameters and Mode to turn on the broadcast.
    - The slave handles read and write requests from the host. For details, refer to “[GR551x BLE Stack User Guide](https://docs.goodix.com/zh/online/gr55xx_ble_stack_user_guide)”.
    - Slaves can use `uint16_t ble_gatts_noti_ind(uint8_t conn_idx, const ble_gatts_noti_ind_t *p_param)` function to send notifications and instructions to the host proactively.



### 3. FAQ

#### 3.1 What is the maximum number of connections that GR5xx can support when designing a master-slave application scenario?

**A**: GR5xx series chips can support a maximum of 12 activities (resource operations) simultaneously. A scannable broadcast occupies 2 activities, a non-scannable broadcast occupies 1 activity, and a connection occupies 1 activity.The maximum number of connections can be configured from 1 to 10 through the macro `CFG_MAX_CONNECTIONS`.

Example:
- In the absence of broadcast services. up to 10 connections are supported.
- With 2 scannable broadcast services, a maximum of 12 - 2 * 2 = 8 connections can be supported.
- At 1 scannable and 1 normal broadcast service, up to 10 connections are supported.

#### 3.2 In ble_app_uart_multilink master-slave example, how to differentiate the slaves? How do I change the slave device settings for the default connection?

**A**: In the sample project, first filter the scanned broadcast packets through the protocol stack `BLE_GAPM_EVT_ADV_REPORT` callback to confirm whether the data they carry is in accordance with the specification; then use the existing MAC address (see `first_slave_target_addr` array) to compare with the Slave address, and if it is the desired address, the connection is made.

- If you want to differentiate the slaves, you can get the paired slave address in the connection parameter of the connection callback function and use `conn_idx` to differentiate the slaves.
- For detailed operations, please refer to the `void app_connected_handler(uint8_t conn_idx, const ble_gap_evt_connected_t *p_param)` function.

#### 3.3 Common problem analysis of open broadcast or scanning failure in BLE multi-service scenarios.

Users may often encounter some multi-service scenarios where the protocol stack reports errors during development. For example, the following scenario:

- After the broadcast is turned on successfully, scanning is turned on again, and scanning fails.

- After the connection is established, the broadcast is turned on again, and the result is that the broadcast fails to be turned on.

- After the connection is established, scanning is turned on again, and scanning fails.

**A**: For detailed solution, please refer to [Analysis of Common Problems of Failure to Enable in BLE Multi-service Scenarios](https://developers.goodix.com/zh/bbs/blog_detail/213844795e8a45d59a4501fa80d519c4).



#### 3.4 In a master-multi-slave scenario, there is no problem with master-slave communication of one pair of one device, but when master-slave communication of one pair of ten devices, commands are sent to the slaves one by one via conn_idx, and the slaves can't receive the data in case of a large amount of data, which is because of Bluetooth transmission scheduling problem?

**A**: This may be caused by unreasonable configuration of connection parameters, please refer to the following suggestions for adjustment, for configuration details, please refer to [Multi-Connection Parameter Optimization Notes](https://developers.goodix.com/zh/bbs/detail/87e8f3be6c9b464496381ac8f8ff4893) :: Please refer to the following suggestions to adjust the configuration:

- Please make sure the sum of CE_LEN is less than CI_Min.
- Considering the precision conversion and the window expansion mechanism, the CE_LEN of the Slave device should be configured with a certain margin, and it is recommended to be at least 2.5 ms smaller than the theoretical value, e.g. if the theoretical value of the CE_LEN can be configured as 100 ms, the actual value should be configured as 97.5 ms.
- Make sure that the CI of each link is multiplicative.
- Configure the appropriate CE_LEN according to the amount of transmitted data of each link to adjust the bandwidth occupied by each link within CI_Min.
