## BLE Multi Slave

### 1. Introduction to GR5xx Multi Slave Basic Concepts

1. BLE Slave Device Profile
    - The Generic Access Profile (GAP) defines four device roles: Broadcaster, Observer, Central, and Peripheral.
    - Peripheral devices in low-power Bluetooth, also known as “Slave Devices” or “Slaves,” are widely used in application areas such as healthcare, industrial monitoring, smart home, and IoT, which require low-power consumption and wireless data transmission.
2. Introduction of BLE slave device function
    - The slave device (Peripheral) periodically sends broadcast data outward and passively receives physical connections initiated by other devices.
    - The slave device waits for the connection request from the master device (Central), and once the connection is established, it can provide specific services or data information to the host.
    - The slave acts as a GATT server, providing Characteristic and Service for the master to read or write data.
    - Slave devices send Notification or Indication messages to the master device and proactively report updated data to the master device.
    - For details on the contents of the Generic Attribute Profile (GATT) involved in slave devices, refer to the [GR551x BLE Stack User Guide](https://docs.goodix.com/zh/online/gr55xx_ble_stack_user_). guide).
3. GR5xx Multi-slave Profile
    - GR5xx Multi Slave is based on BLE slave device, which is able to turn on multiple independent BLE broadcasts (with different addresses and different broadcast data) on a single SoC.
    - Multi-slave supports multiple Bluetooth connections, and each connection can be paired and bound.
    - Each connection can be paired and bound. After establishing a connection with the host, each connection can discover different Bluetooth services.
    - Multi-slave supports multiple apps on the same cell phone. 4.
4. Application Scenarios of GR5xx Multi-Slaves
    - If the host is more than one physical device, “Multi-Connection” can meet the needs of this application. There is a difference between Multi-Slave and traditional Multi-Connection.
    - Multi-slave allows GR5xx single Bluetooth chip to connect and communicate with multiple applications on the same cell phone simultaneously and independently, without interfering with each other.
    - Each slave is discovered by multiple apps on the phone to provide different services, which is equivalent to a single SoC constructing multiple virtual slaves to realize the functions of BLE devices independently of each other.


### 2. GR5xx Multi-slave Application Notes

- For the multi-slave example, refer to the SDK project `SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave`.

- The dual-slave example project contains slave 1 (HRS heart rate service) and slave 2 (HID service) connected to the same cell phone to realize the different performance of heart rate sensor and keypad functions on the two Bluetooth links respectively.

- As an example, a dual slave is used to illustrate the implementation of multiple slaves:

  - Each slave contains one or more BLE Profiles to realize specific Bluetooth functions. To add custom Service, please refer to “[GR5xx Application and Custom Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl)”.

  - Each slave needs to enable one BLE broadcast (different address, parameters and Payload are set by yourself). To ensure that the broadcasts are independent of each other, make sure that the broadcast index `adv_idx` of the dual slaves is different.

  - After the two broadcasts are enabled, the host can establish a connection with each of the two slaves. At this point, you need to use the interface `void ble_gap_conn_local_addr_get(uint8_t conidx,uint8_t *p_addr)` to determine which broadcast the current connection is based on, and record the connection index `conn_idx` for the subsequent process.

  - Finally, configure the visibility of the service through the interface `uint16_t ble_gatts_service_hide_set(uint8_t conn_idx, uint16_t handle)`. Hides certain services `Service Handles` of the other slave at each connection build, thus ensuring that the current slave's services are visible. For detailed information, please refer to the `void app_connected_handler(uint8_t conn_idx, const ble_gap_evt_connected_t *p_param)` function in the dual-slave example project.

- In summary, a single slave in a multi-slave is a standard BLE device. GR5xx virtualizes multiple BLE entities on a single SoC, and constructs multiple links with the same host in a time-sharing multiplexing manner for independent communication without interfering with each other, so that it can meet more diversified and customized BLE application scenarios.

### 3. FAQ

#### 3.1 BLE slave devices originally support multiple connections, so what is the difference between multiple connections and multiple slaves? What are the specific application scenarios of dual or multiple slaves?

**A**: Currently, GR5xx multi-slaves are mainly used in Apple Find Network Accessories products. In this application scenario, users have the following needs:

- Apple Find App is limited to the query and location of accessories, Apple Find My SPEC prohibits the addition of other commands, the accessories side of the open source but the App side of the closed, the user does not have the right to use the App for other operations.
- Daily use of scooters with the Find Network function also has many customized needs such as checking mileage, checking power and close to unlocking.

   At the same time, based on the following technical limitations, multiple connections from the device may not be able to meet the actual product requirements:
   
   - The same BLE device cannot establish two paired encrypted connections with the same master device (e.g. cell phone) in the Bluetooth specification.
   - Apple Find a Network accessory is not allowed to add BLE Service outside the specification, and when a non-Owner cell phone connects, the accessory will actively disconnect the device after 10s.
   
   
   Therefore, one of the GR5xx dual slaves is used to support Apple Find My service, and the other slave is used for product-specific applications, such as OTA, device status query and control, and other rich functions, to help customers' products easily support the Finder Network, and achieve many customized needs, and will not undermine the security specifications of Apple's Finder Network.

#### 3.2 In the actual application of dual-slave project, the broadcast of each link is independent, if there are frequent modification of the broadcast address of the application scenarios, how should it be realized?

**A**: In order to ensure that the broadcasts of dual slaves are independent of each other, assuming that slave 1 has successfully turned on broadcast 1, and slave 2 wants to start a broadcast 2 with a different address, it can be realized in the following way:

1. Before starting broadcast 2, the `uint16_t ble_gap_addr_get(ble_gap_bdaddr_t *p_addr)` function should first be used to save the address of broadcast 1 into the global variable `ble_gap_bdaddr_t s_gap_default_addr`.

2. use the `uint16_t ble_gap_addr_set(ble_gap_bdaddr_t const *p_addr)` function to set a different address for broadcast 2.

3. When broadcast 2 is successfully turned on, the saved global variable is used in the protocol stack `BLE_GAPM_EVT_ADV_START` callback to restore the previous configuration of the broadcast 1 address.

   Do the same before starting the broadcast next time and realize this requirement in this way.

#### 3.3 The same phone can connect to both slaves normally, but why does each slave find services that are not as expected after the connection is established?

**A**: If each slave can discover all the services of the two slaves, check whether the logic for configuring the visibility of service Service has been added and implemented properly; if the current slave discovers the services of the other slave, but not the services it is supposed to have, check whether the connection index `conn_idx` is misjudged, or just set the other way around.

#### 3.4 The dual slaves are connected normally, and the service discovery is normal, but when I send a message from the device to the cell phone, why can't the cell phone receive it?

**A**: When a host establishes a connection, the variable `conn_idx` should be maintained globally, it represents the current connection index.

- This value not only distinguishes which link the host sends data under, but the slave device side should also reply or send data to the host on the corresponding connection.

- Data transfer from the slave to the host, whether Indication or Notification, requires the correct connection index.
- Please check that the first parameter of the `uint16_t ble_gatts_noti_ind(uint8_t conn_idx, const ble_gatts_noti_ind_t *p_param)` function in the individual slaves is the same as the `conn_idx` at the time of connection establishment.
