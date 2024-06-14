## APP LOG模块应用笔记



### 1. APP LOG模块基本功能介绍

APP Log模块是GR5xx SDK提供用于辅助开发者进行开发和调试的工具模块，有以下几个实用特性：
 - 支持自定义硬件输出方式，SDK默认提供了UART输出与J-Link RTT输出两种方式，用户也可通过注册自己的硬件传输接口实现自定义的输出方式。
 - 支持日志存储与导出的实现，可以将日志存储到Flash中，并在需要的时候使用GRToolbox Android App通过Bluetooth LE将存储的日志导出分析。
 - 支持基于TAG和Level的日志过滤，支持针对不同Level的日志设置不同的输出格式。
 - 支持基于CSI的彩色日志输出。



### 2. APP LOG模块使用注意事项

> APP LOG模块的详细使用说明请参考《[GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl/V3.2)》。

 - `printf()`的正常工作同样依赖_app_log.c_，且在使用`app_log_init()`初始化APP LOG模块时传入的`trans_func`传输函数也会被用于`printf()`的打印。

 - 在_custom_config.h_中，`APP_LOG_ENABLE`的开或关并不会影响`printf()`的输出。但是要注意，在SDK自带的工程中，`APP_LOG_ENABLE`为`0`的情况下整个APP LOG模块都不会初始化，进而导致`printf()`没有输出。

 - 当`APP_LOG_STORE_ENABLE`置为1后，通过`printf()`与`APP_LOG_xxx()`输出的LOG都会被存储在Flash中，且此时由于`printf()`的特性，所有使用`printf()`输出的LOG，每一个字节都会被当做是一条记录，即每一个字节都会被打上时间戳，非常占用空间。所以在使能LOG存储的情况下，需要尽量避免用`printf()`打LOG。

 - LOG存储真正写入Flash并不发生在打LOG的时候。打LOG时只是将待写入的LOG放入环形缓冲区，实际涉及Flash的操作都发生在`app_log_store_schedule()`函数中，这是为了避免Flash操作耗时影响时序敏感的任务。详情请参考《[GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl/V3.2)》“日志调度接口”章节。

    
