## APP LOG模块常见问题



### 1. UART打LOG最高波特率能到多少？

-   GR5xx系列 SoC的UART最大波特率均为4M，但考虑到误码率以及串口转USB芯片的能力，非常不推荐使用4M来打LOG。另外，GR5xx Starter Kit板载的J-Link OB芯片最大支持的波特率只到460800，所以如果对波特率有更高的要求，需要用户外接性能更好的串口转USB板。



### 2. 使用串口打LOG在电脑上看不到输出怎么办？

可以根据下面的步骤逐一进行排查：

 - 1. 检查串口工具的配置，包括**波特率**，**奇偶校验**，**数据位**,**停止位**，**流控**等配置，与代码中初始化UART时的配置保持一致。
 - 2. 检查`custom_config.h`的配置。`APP_LOG_ENABLE`宏应当为`1`，`APP_LOG_PORT`宏应当为`0`。
 - 3. 检查APP LOG模块与UART是否正确初始化。在调用`app_log_init()`函数时，第二个参数`trans_func`应当是使用对应UART进行输出的函数。具体的写法可以参考SDK的实现`platform\boards\board_SK.c`或文档[GR5xx APP Log应用说明 - 模块初始化与调度](https://docs.goodix.com/zh/online/detail/app_log_bl/V3.2/0c248feb9aaedf20e43b751ac2f81b37)。
 - 4. 检查UART初始化时Pin Mux是否正确配置。具体的Pin Mux值请参考所使用SoC的Datasheet。
 - 5. 如果打LOG时使用了DMA方式，需要检查UART DMA的配置是否正确，以及使用的UART是否支持DMA（例如GR551x SoC的UART1是不支持DMA的）。
 - 6. 如果经过上述5步仍不能解决问题，则建议使用逻辑分析仪或示波器在UART TX/RX线上抓取波形，来判断GR5xx SoC是否有输出正确的UART信号。如果有，则需要进一步排查串口转USB或串口工具的问题。如果没有，则推荐先用SDK中的Example工程进行对比测试，来确认是硬件问题还是软件问题，然后针对具体问题进行分析排查。



### 3. 怎么用SEGGER RTT打LOG？

SDK提供的所有模板工程均支持通过RTT打LOG。在工程对应的`custom_config.h`中找到`APP_LOG_PORT`宏，将值修改为`1`：

```c
// <o> APP log port type
// <0=> UART
// <1=> RTT
// <2=> ITM
#ifndef APP_LOG_PORT
#define APP_LOG_PORT            1
#endif
```

然后重新编译下载即可。在J-Link RTT Viewer中连接设备时，**Connection to J-Link**一栏一般选择**USB**，**Specify Target Device**一栏填写**Cortex-M4**，**Target Interface & Speed**选择**SWD**和**4000kHz**，**RTT Control Block**中有两种填写方法，第一种是在编译产生的`.map`中寻找`_SEGGER_RTT`符号的地址，然后在RTT Viewer中使用**Address**选项填写；第二种方式是填写地址范围让RTT Viewer自动搜索，这里通常填写完整的SRAM范围即可，各SoC的地址范围请参考下表：

SoC | Search Range
-- | ---
GR5515 | 0x30000000 0x3003FFFF
GR5513 | 0x30000000 0x3001FFFF
GR5525 | 0x20000000 0x2003FFFF
GR5526 | 0x20000000 0x2007FFFF
GR533x | 0x20000000 9x20017FFF

如果是自己的工程，请参考SDK的实现进行移植，或者参考文档[GR5xx APP Log应用说明 - 模块初始化与调度](https://docs.goodix.com/zh/online/detail/app_log_bl/V3.2/0c248feb9aaedf20e43b751ac2f81b37)。



### 4. 为什么RTT打印日志一段时间后就不再打印了，系统也卡死了？

1.  不再打印日志的原因是RTT方式打印日志依赖J-Link连接，当GR5xx SoC进入睡眠模式之后，J-Link连接会断开，J-Link RTT Viewer不具备自动重连功能，当系统再次唤醒时，J-Link连接已经断开了，所以表现为后续LOG就没了。
2.  系统卡死的原因则很有可能是RTT打印模式为阻塞模式，当传输FIFO满了之后，RTT就会阻塞等待上位机将FIFO读空。结合第1点中描述的原因，睡眠唤醒之后J-Link连接已经断开，上位机没有再继续读取FIFO，当FIFO满了之后再打LOG，阻塞等待的行为就会表现为卡死。

解决办法有2种：

1.  关闭低功耗模式，在系统初始化时加入`pwr_mgmt_mode_set(PMR_MGMT_ACTIVE_MODE);`。让SoC保持在Active状态可以避免J-Link连接断掉，同时规避“丢LOG”与“系统卡死”的问题，缺点是无法针对低功耗部分进行有效调试。
2.  将RTT输出模式更改为非阻塞模式，在初始化RTT时使用`SEGGER_RTT_ConfigUpBuffer()`函数来修改输出模式。非阻塞模式分两种：`SEGGER_RTT_MODE_NO_BLOCK_SKIP`和`SEGGER_RTT_MODE_NO_BLOCK_TRIM`。当遇到FIFO剩余空间不足以放下完整的待打印日志，如果设置为SKIP，则跳过该次打印；如果设置为TRIM，则只把FIFO填满，超出的部分全部丢弃。这种方法虽然不影响低功耗，只能避免J-Link连接断开后不会阻塞卡死，并不能避免丢LOG的情况。



### 5.  J-Link RTT Viewer连上之后看不到LOG怎么办？

可以根据下面的步骤逐一进行排查：

 - 1. 检查`custom_config.h`的配置。`APP_LOG_ENABLE`宏应当为`1`，`APP_LOG_PORT`宏应当为`1`。
 - 2. 检查APP LOG模块与RTT是否正确初始化。在调用`app_log_init()`函数时，第二个参数`trans_func`应当是使用`SEGGER_RTT_Write()`进行输出的函数（但不能是`SEGGER_RTT_Write()`本身，因为入参不一样）。具体的写法可以参考SDK的实现`platform\boards\board_SK.c`或文档[GR5xx APP Log应用说明 - 模块初始化与调度](https://docs.goodix.com/zh/online/detail/app_log_bl/V3.2/0c248feb9aaedf20e43b751ac2f81b37)。
 - 3. 检查RTT中的各项配置。首先检查`_SEGGER_RTT`变量是否被正确放置。通常情况下不推荐将`_SEGGER_RTT`变量放置到固定的地址，但如果用户选择了将这个变量放到固定地址，则需要确保这个固定地址存在于SRAM地址范围以内。
 - 4. 检查J-Link RTT Viewer连接是`RTT Control Block`的地址设置是否正确。GR5xx SoC暂不支持**Auto Detection**模式，需要使用**Address**模式手动填入，或者使用**Search Range**模式并填入地址范围让RTT Viewer自动去搜索。具体的设置方法请参考前面问题“怎么用J-Link RTT打LOG？”的回答部分
 - 5. 如果经过上述4步依然无法定位并解决问题，则需要通过单步调试跟踪来确定每一个打LOG的每一个环节是否都正确执行，入参与返回值是否符合预期等等。



### 6. 存储的LOG怎么导出来？

-   使用Android端的GRToolBox App导出，具体操作请参考[GR5xx APP Log应用说明 - 获取日志](https://docs.goodix.com/zh/online/detail/app_log_bl/V3.2/448f70b039394c36cef3d090a6eb45ff)。



### 7. 使用GRToolbox导出存储LOG时，LOG不完整怎么办？

-   很有可能是由于用来临时存储LOG的RingBuffer溢出导致的。为了尽可能降低擦写Flash对应用时序的影响，打LOG时并不会进行真正的存储操作，而是将LOG数据放入缓存RingBuffer中，并在`app_log_store_schedule()`函数中真正写入Flash。如果在`app_log_store_schedule()`执行之前就输出了超过RingBuffer大小的LOG，就会出现LOG不完整甚至丢LOG的情况。处理这个问题有两种解决办法：
    -   增大缓存RingBuffer。根据情况修改`components\libraries\app_log\app_log_store.h`中`APP_LOG_STORE_LINE_SIZE`与`APP_LOG_STORE_CACHE_NUM`的值可以增大缓存RingBuffer，但同时也会增加RAM占用。
    -   增加调用`app_log_store_schedule()`的频次。例如在使用RTOS的环境下，视情况提高用于运行`app_log_store_schedule()`的任务的优先级可以让该任务得到更多次的调度，但更高频次的操作Flash可能会对某些时序敏感的应用造成影响。



### 8. 使用GRToolbox导出日志时，发现只有最近的日志，无法获取更早的日志怎么办？

-   LOG存储使用了环形覆盖机制，当存储空间不足时，会用新的LOG去覆盖最老的LOG。所以这个问题无法真正的解决，只能通过增大存储区和减少不必要的LOG来尽量缓解问题。