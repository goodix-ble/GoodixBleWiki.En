## BLE与执行代码Flash冲突处理



在GR5xx系列芯片中，BLE任务在最高优先级中断中执行调度，允许打断但是打断时间不宜过长。但片上Flash操作必须关闭中断。因此，当Flash操作和BLE调度同时发生时，就会产生冲突。

### 1. 如何避免BLE与Flash之间的操作冲突
Flash以Page为基础单位，每256 Bytes为1 Page，每4096 Bytes为1 Sector。其中，Read操作没有长度限制；Write操作以1 Page为基础单位；Erase操作以1 Sector为基础单位。另外，由于Flash特性，只能由1写为0。因此，如果需要重新写入同一个Page，必须先擦除整片Sector。

- Read 1 Sector：143.63 μs；Write 1 Sector：26.47 ms；Erase 1 Sector：17.25 ms。

- Read 2 Sectors：282.88 μs；Write 2 Sectors：53.09 ms；Erase 2 Sectors：34.30 ms。

- 根据读、写、擦除长度，耗时按照线性增长。

一般情况下，Android设备刚连接上BLE时的连接参数为45 ms Interval、5s Timeout。在此参数下，如需一次擦除40 KB Flash，只需在每个Sector操作之间增加45 ms delay，来释放中断让BLE调度。每次有一个连接间隔会因操作Flash关中断错过。按照该方法操作40 KB Flash，在保证蓝牙稳定连接的情况下，需要耗时900 ms。

一般情况下，iOS设备刚连接上BLE时的连接参数为30 ms Interval。在此参数下，如需一次擦写40 KB Flash，只需在每个Sector操作之间增加30ms delay，来释放中断让BLE调度。每次有一个连接间隔会因操作Flash关中断错过。按照该方法操作40 KB Flash，在保证蓝牙稳定链接的情况下，需要耗时750 ms。

**那什么时候需要每个Sector Delay，什么时候不需要呢？**

假设操作一次Flash的时间为N ms，连接间隔为M ms，timeout为T ms：

a. 当M > N时，操作Flash完全不需要Delay。即操作一次Flash需要95 ms，连接间隔为100 ms，那么可不Delay。

![](../../../_images/ble/BLE_FLASH_A.PNG) 

b. 当T < N时，操作Flash的时间比Timeout的时间还要长，则推荐每操作一个Sector Delay一次M ms。

![](../../../_images/ble/BLE_FLASH_B.PNG) 

c. 当M*6 < N时，操作Flash时刻正好是建连时刻，从设备接收到连接请求后6个interval内必须有回复。则推荐每操作一个Sector Delay一次M ms。

![](../../../_images/ble/BLE_FLASH_C.PNG) 

d. 当M < N < (5*M) 且 (5*M <T)时，操作Flash时间可以保证建连时序，无需Delay。

![](../../../_images/ble/BLE_FLASH_D.PNG) 

最后推荐操作Flash的时刻有如下注意点：

1. 请避开蓝牙刚连接的时间，因为刚连接上Timeout时间较短，例如iOS只有720 ms。这样可以避免情形c的发生。
2. 请在蓝牙连接稳定后操作，例如前期发现服务等操作完成后进入维持连接状态，即在情形a时刻操作Flash。
3. 如果业务无法在a情形下操作，那么每操作1 Sector，进行一次1个Interval的Delay，以保证蓝牙连接的稳定性。



