## Fault Trace模块应用笔记

### 1. Fault Trace模块基本功能介绍

Fault Trace模块是GR5xx SDK提供用于辅助开发调试阶段定位系统异常问题的模块。该模块支持以下实用功能：

 - 将异常信息存入NVDS中，方便异常记录与后续分析。
 - 支持多种方式读取保存的异常信息：使用GRToolbox App通过Bluetooth LE读取，或者GProgrammer工具通过J-Link/串口读取。
 - 可选的cortex-backtrace组件，该组件可在异常发生时记录增加调用栈与HFSR寄存器所指示的异常原因内容。

Fault Trace模块的具体使用方法请参考《[GR5xx Fault Trace Module应用说明](https://docs.goodix.com/zh/online/fault_trace_bl/V3.2)》。

### 2. Fault Trace模块使用注意事项

 - Fault Trace模块依赖APP LOG模块、Assert模块与Error模块，使用时需要确保下面的文件加入到了工程中，并将它们的所在目录加入到Include Path中：
     - `components\libraries\app_assert\app_assert.c`
     - `components\libraries\app_error\app_error.c`
     - `components\libraries\app_log\app_log.c`
 - Fault Trace模块不止支持记录HardFault异常信息，也支持记录使用宏`APP_ERROR_CHECK`、`APP_BOOL_CHECK`与`APP_ASSERT_CHECK`产生的错误信息。
 - Fault Trace模块默认支持**16**条错误信息存储，该上限可通过`components\libraries\fault_trace\fault_trace.h`中的宏`FAULT_INFO_RECORDS_MAX`进行调整。超出上限条数的错误信息会循环覆盖最老的错误信息。
 - 如果要使用Cortex Backtrace的扩展功能，需要在_custom_config.h_中将宏`ENABLE_BACKTRACE_FEA`的值置为`1`。
