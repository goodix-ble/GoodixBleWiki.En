## BLE Data Rates



### 1. Theoretical Transmission Rate

* BLE supports 2M PHY, 1M PHY and Coded PHY at the physical layer.
* BLE data transmits known information:
  * Using GFSK modulation, 2M PHY occupies 0.5 μs per bit and 1M PHY occupies 1 μs.
  * The packet time interval (T_IFS) is a fixed 150 μs.
  * Transmission time slot format is: TX packet + packet spacing + RX null packet + packet spacing 
  * ATT layer data transmission format is: Preamble (1 byte for 1M, 2 bytes for 2M) + Access address (4 bytes) + Header (2 bytes) + Payload (251 bytes) + CRC (3 bytes)
  * For applications running on top of GATT, both I2CAP and ATT have their own overhead. Typically, the maximum payload for GATT is (251 - 7) = 244 bytes.
* Using 2M PHY, the theoretical transmission rate is calculated as follows:
  * TX packet total length = 2096 bits with an occupancy time of 1048 μs.
  * Total RX null packet length = 88 bits, occupying 44 μs.
  * The total time for one transmission is: 1048 + 44 + (150*2) = 1392 μs
  * ** Maximum data rate for application layer in LE 2M PHY mode can be calculated = (244* 8) / 1392 µs ≈ 1402 kbps**.
* Using 1M PHY, the theoretical transmission rate is calculated as follows:
  * TX packet total length = 2120 bits, occupying 2088 µs.
  * Total RX null packet length = 80 bits, occupying 80 μs.
  * Total time for one transmission is: 2120 + 80 + (150*2) = 2500 μs
  * ** Maximum data transfer rate for application layer in LE 1M PHY mode can be calculated = (244* 8) / 2500 µs ≈ 780 kbps**.



### 2. Factors affecting BLE data transfer rate

* There are more factors affecting the BLE transmission rate, including PDU, CI, MTU, CE and PHY parameters, RF performance, environment, distance between Master and Slave, and communication modes.
* The communication modes commonly used by Slave and Master are Indicate, Notify, Write Without Response, and Write With Response. for Indicate and Write With Response, all of them require the mode of response from the opposite end, and an Interval will only send One Interval will only send one packet of data.
* BLE Connection related configuration parameters mainly affect the real-time communication, throughput rate, power consumption, anti-interference, real-time response to broken link, etc. Among them, throughput rate is mainly related to two factors. Among them, the throughput rate is mainly related to two factors: the communication period CI and the amount of data (MTU and PDU) that can be transmitted by each communication point.
* It is not the case that the smaller the CI, the higher the data throughput rate; or the larger the CI, the higher the throughput rate. the smaller the CI, the larger the proportion of the entire time period reserved for hardware preparation time, the shorter the actual communication data time, so it seems that the CI needs to be configured larger. However, when the CI is larger, once a data error occurs, the more time remaining in the CI is wasted, so it seems that the CI needs to be configured smaller, and the next communication can be quickly continued.
* ** In high data throughput scenarios, typical empirical values are generally used, with a CI of 30 ms to 45 ms, a PHY of 2M, a PDU of 251, and an MTU of 247**.
* If you need to test the BLE data transfer rate, you can use the `SDK_Folder\projects\ble\ble_peripheral\ble_app_throughput` example project in the SDK with the GRToolbox tool.



### 3. FAQ

#### 3.1 I want to modify the PDU parameters in cell phone, but I didn't find the API interface, how can I do it?

**A**: When the cell phone initiates the parameter update, the MTU is the value that can be obtained, if you want to modify the connection parameter accurately after the connection is made, you usually need to use the cell phone to send commands to the Slave chip, and then the chip will initiate the parameter update, the specific implementation can be referred to the Throughput sample project in the SDK.

When the cell phone is used for MTU setting, a PDU Update will be performed to update the PDU Max value of the cell phone. If you need to send a separate command to the device side for PDU setting, you need to update the MTU first, otherwise the phone side will always default to a maximum PDU Length of 27, and when the device side initiates an update of the MTU value larger than 27, the operation will fail.

#### 3.2 Why is the throughput rate of Apple phone low during throughput rate test?

**A**: iOS default connection interval CI is 30 ms. different cell phone OS, CI update, acceptable value is not the same. iOS supports minimum CI of 20 ms, but can not be like Android, CI can be updated to the minimum value of 7.5 ms. if the iOS version is different, then the MTU is not the same, it is about 185 Bytes. So the iOS BLE transfer rate can't reach the optimal value like Android.
