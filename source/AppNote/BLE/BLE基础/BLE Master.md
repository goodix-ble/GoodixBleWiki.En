## BLE Master

### 1. Introduction to the basic functions of BLE Master scanning

- BLE Master is the device responsible for scanning devices and initiating connection requests. As a master, GR5xx can connect to multiple slave devices.
- As a master, GR5xx can connect to multiple slave devices, i.e., after initiating a connection to one slave device successfully, it can initiate a connection to another slave device.
- After the scan is started, you can check whether the scan is started successfully by using the `BLE_GAPM_EVT_SCAN_START` event.
- The duration of the scan can be controlled by setting the scan timeout time. When timeout is set to 0, it means scanning is always on and you need to stop scanning manually; when timeout is set to other values, scanning will be stopped automatically. When the timeout is set to other values, the scanning will be stopped automatically. The `BLE_GAPM_EVT_SCAN_STOP` event will be reported after the scanning is stopped.
- The scan_dup_filt in the scan parameter can filter duplicate broadcasts. However, in a scenario with a particularly large number of Bluetooth devices, this function can only reduce the frequency of reported broadcasts, and cannot completely filter duplicate broadcasts.
- The use_whitelist in the scan parameter is also a filtering strategy to filter the devices added to the whitelist list.
- The scan_type in the scan parameter can be set to `BLE_GAP_SCAN_ACTIVE` (active scan) and `BLE_GAP_SCAN_PASSIVE` (passive scan). Active scanning initiates scan request packets randomly, while passive scanning does not initiate scan request packets.
- The interval and window in the scan parameters are used to control the scan interval and window opening time, and the window value must be less than or equal to the interval value.
- As a master, you can set the connection parameters, including interval, latency, and timeout, when initiating a connection.



### 2. BLE Master Scanning Application Notes

- Extended scanning is used in scenarios where extended broadcast scanning is required, and traditional scanning cannot obtain extended broadcast packets. For more information on how to use extended scanning, please refer to the extended scanning example project in the GR551x SDK version V1.7.0: `SDK_Folder\projects\ble\ble_basic_example\ble_app_gap_extended_scan`, where SDK_Folder is the root directory of the SDK. root directory.
- Setting the interval and window in the scan parameter to the same value turns on the RX duty cycle of the RF to the maximum, i.e., it will be in the RX state for the longest time.
- For each scan interval, only one channel will be scanned. Unlike broadcasting, each interval of broadcasting will broadcast on three channels.
- The scanned broadcast data is reported in the BLE_GAPM_EVT_ADV_REPORT event.
- When initiating a connection, you can configure the connection timeout by setting conn_timeout, which means that if the target device is not connected within the set time, the initiation of the connection will stop.
- GR5xx scanning channel supports configuration of private channel. Please consult FAE for details.



### 3. FAQ

#### 3.1 Do I need to stop scanning when I initiate a connection?

  **A**: You do not need to stop scanning to connect to the target device. The scanning will not stop after connecting to the target device.

#### 3.2 Does it support to connect to multiple devices at the same time?

  **A**: You can only connect to one device at a time. It is not possible to connect to multiple devices at the same time.

#### 3.3  Does it support to set scanning power?

  **A**: There is no such thing as scanning power. The performance of scanning is only related to the sensitivity and anti-interference index.

#### 3.4 How to use the scanning whitelist function?

  **A**: 1. Pairing binding has been completed with the target device.

  2. The target device has been added to the whitelist. 3.

  3. set use_whitelist to true when scanning again.

#### 3.5 Can Master act as Server and Slave act as Client?

  **A**: Master and Slave are two different roles. master usually refers to the device that initiates the connection and controls the communication, while Slave is the device that is connected and controlled.

  - In BLE, GATT (Generic Attribute Profile) defines attribute-based services and features, similar to the traditional client-server model. The Server role can be implemented on a BLE Master device through the GATT protocol to provide services and features. The Slave device, on the other hand, can connect to the Master as a client and communicate with it.
- Thus, the BLE Master can act as a Server and provide services and features to the connected devices. For example, iPhone acts as Master and supports ANCS services.   
  
