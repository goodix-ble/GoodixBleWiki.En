## Conflict handling between BLE and XIP-Flash



In the GR5xx series chips, BLE tasks are scheduled in the highest priority interrupt, and interruptions are allowed but should not be too long. However, the interrupt must be turned off for on-chip Flash operation. Therefore, when Flash operation and BLE scheduling occur at the same time, a conflict occurs.



### 1. How to avoid conflicts between BLE and Flash operations

Flash is based on Page, 1 Page for every 256 Bytes and 1 Sector for every 4096 Bytes, where Read operation has no length limitation, Write operation is based on 1 Page, and Erase operation is based on 1 Sector. In addition, due to the characteristics of Flash, only 1 can be written to 0. Therefore, if you need to rewrite the same Page, you must erase the entire Sector first.

- Read 1 Sector: 143.63 μs; Write 1 Sector: 26.47 ms; Erase 1 Sector: 17.25 ms.

- Read 2 Sectors: 282.88 μs; Write 2 Sectors: 53.09 ms; Erase 2 Sectors: 34.30 ms.

- Depending on the read, write, and erase lengths, the elapsed time increases linearly.

Generally, the connection parameters when the Android device is first connected to the BLE are 45 ms Interval, 5s Timeout, under this parameter, if you need to erase 40 KB of Flash at a time, you only need to add 45 ms delay between each Sector operation to release the interrupt for the BLE to schedule. One connection interval at a time will be missed by operating the Flash off interrupt. Operating the 40 KB Flash in this way takes 900 ms with a stable Bluetooth connection.

In general, the connection parameter for an iOS device when it first connects to BLE is 30 ms Interval, under this parameter, if you want to erase and write 40 KB Flash at a time, you only need to add a 30 ms delay between each Sector operation to release the interrupt for BLE to schedule. One connection interval at a time will be missed by operating the Flash off interrupt. Operating the 40 KB Flash in this way takes 750 ms with a guaranteed stable Bluetooth link.



### 2. So when is each Sector Delay needed and when is it not? 

Assume that the time to operate one Flash is N ms, the connection interval is M ms, and the timeout is T ms:

a. When M > N, no Delay is required to operate Flash at all, i.e., it takes 95 ms to operate Flash and 100 ms to connect, then no Delay is required. b. When M > N, no Delay is required to operate Flash at all, i.e., it takes 95 ms to operate Flash and 100 ms to connect.

![](../../../_images/ble/BLE_FLASH_A.PNG) 

b. When T < N, it takes longer to operate Flash than Timeout, then it is recommended to Delay M ms once for each Sector.

![](../../../_images/ble/BLE_FLASH_B.PNG) 

c. When M*6 < N, the operation Flash moment is exactly the connection building moment, and there must be a reply within 6 intervals after the connection request is received from the device. Then it is recommended to delay M ms once per Sector operation.

![](../../../_images/ble/BLE_FLASH_C.PNG) 

d. When M < N < (5*M) and (5*M < T), the operation Flash time can guarantee the build time sequence without Delay.

![](../../../_images/ble/BLE_FLASH_D.PNG) 

The last recommended moment to operate Flash has the following notes:

1. Please avoid the time when Bluetooth is just connected, because the Timeout time is shorter when it is just connected, e.g. only 720 ms for iOS. this can avoid the situation c.
2. Please operate after the Bluetooth connection is stabilized, e.g. after the pre-discovery service and other operations have been completed to enter the state of maintaining the connection, i.e., operate Flash at the moment of situation a. 3.
3. If the service cannot be operated in scenario a, then for every 1 Sector operation, perform a Delay of 1 Interval to ensure the stability of the Bluetooth connection.


