## APP LOG Module Application Notes



### 1. APP LOG module basic function introduction

APP Log module is a tool module provided by GR5xx SDK to assist developers in development and debugging, it has the following practical features:
 - Support customized hardware output mode, SDK provides UART output and J-Link RTT output by default, and users can also realize customized output mode by registering their own hardware transmission interface.
 - Support the implementation of log storage and export, you can store the logs into Flash, and use GRToolbox Android App to export and analyze the stored logs through Bluetooth LE when needed.
 - Support log filtering based on TAG and Level, and set different output formats for different Level logs.
 - Supports different output formats for different levels of logs. Supports colorful log output based on CSI.



### 2. Notes on APP LOG Module Usage

> For detailed usage notes of APP LOG module, please refer to “[GR5xx APP Log Application Notes](https://docs.goodix.com/zh/online/app_log_bl/V3.2)”.

 - The normal operation of `printf()` also relies on _app_log.c_, and the `trans_func` transfer function passed in when initializing the APP LOG module with `app_log_init()` is also used for `printf()` printing.

 - In _custom_config.h_, `APP_LOG_ENABLE` on or off does not affect `printf()` output. However, note that in the project that comes with the SDK, the entire APP LOG module is not initialized when `APP_LOG_ENABLE` is `0`, resulting in no `printf()` output.

 - When `APP_LOG_STORE_ENABLE` is set to 1, the LOG output by `printf()` and `APP_LOG_xxx()` will be stored in Flash, and at this time, due to the characteristic of `printf()`, all the LOGs output with `printf()`, every byte will be treated as a record, i.e., every byte is timestamped, which takes up a lot of space. Therefore, if LOG storage is enabled, you need to avoid typing LOGs with `printf()` as much as possible.

 - The actual writing of the LOG store to Flash does not occur when the LOG is hit. When hitting LOG, it just puts the LOG to be written into the ring buffer, and the actual operations involving Flash happen in the `app_log_store_schedule()` function, which is to avoid the time-consuming Flash operations affecting the timing-sensitive tasks. For more details, please refer to the “Log Scheduling Interface” section in [GR5xx APP Log Application Note](https://docs.goodix.com/zh/online/app_log_bl/V3.2). 

    