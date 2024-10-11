## FAQ for LOG Module



### 1. What is the maximum baud rate of UART for LOG?

-   The maximum baud rate of UART of GR5xx series SoC is 4m, but considering the bit error rate and the ability of converting serial port to USB chip, it is not recommended to use 4m to play LOG. In addition, the maximum baud rate supported by the J-Link OB chip on the GR5xx Starter Kit is only up to the 460800, so if there is a higher requirement for the baud rate, the user needs to connect a serial port to USB board with better performance.



### 2. What should I do if I can't see the output on the computer when I use the serial port to type LOG?

You can check one by one according to the following steps:

1. Check the configuration of the serial port tool, including **Baud rate**, **Parity check**, **Data bit**, **Stop Bit**, **Flow control**etc., and keep consistent with the configuration when the UART is initialized in the code.
2. Check the configuration of the _ custom _ config. H _. `APP_LOG_ENABLE` Macros should be `1`. `APP_LOG_PORT` Macros should be `0`.
3. Check that the APP LOG module and UART are properly initialized. When calling `app_log_init()` a function, the second argument `trans_func` should be the function that outputs using the corresponding UART. Please refer to the implementation `platform\boards\board_SK.c` of SDK or the section of "Module Initialization and Scheduling" in the [GR5xx APP Log Application Notes](https://docs.goodix.com/zh/online/app_log_bl/V3.2).
4. Check whether Pin Mux is configured correctly when UART is initialized. Please refer to the Datasheet of the SoC used for the specific Pin Mux value.
5. If the DMA mode is used during LOG, check whether the UART DMA configuration is correct and whether the UART used supports DMA (for example, the UART1 of GR551x SoC does not support DMA).
6. If the problem still cannot be solved after the above five steps, it is recommended to use a logic analyzer or oscilloscope to capture the waveform on the UART TX/RX line to determine whether the GR5xx SoC outputs the correct UART signal. If so, you need to further troubleshoot the problem of serial port to USB or serial port tools. If not, it is recommended to conduct a comparison test with the Example project in the SDK to confirm whether it is a hardware problem or a software problem, and then analyze and troubleshoot the specific problem.



### 3. How to type LOG with SEGGER RTT?

All template projects provided by SDK support LOG via SEGGER RTT. Find `APP_LOG_PORT` the macro in the _ custom _ config. H _ corresponding to the project, and modify the value as `1` :


```c
// <o> APP log port type
// <0=> UART
// <1=> RTT
// <2=> ITM
#ifndef APP_LOG_PORT
#define APP_LOG_PORT            1
#endif
```

Then recompile and download. When connecting equipment in the J-Link RTT Viewer, **Connection to J-Link**one column is General Select **USB**and **Specify Target Device**the other is Fill **Cortex-M4**, **Target Interface &amp; Speed**Select **SWD**and **4000kHz**, **RTT Control Block**There are two ways to fill in. The first is to find `_SEGGER_RTT` the address of the symbol in the compiled `.map` file, and then use **Address**the option to fill in in RTT Viewer; The second way is to fill in the address range for RTT Viewer to search automatically. Here, it is usually enough to fill in the complete SRAM range. Please refer to the following table for the address range of each SoC:

SoC | Search Range
-- | ---
GR5515 | 0x30000000 0x3003FFFF
GR5513 | 0x30000000 0x3001FFFF
GR5525 | 0x20000000 0x2003FFFF
GR5526 | 0x20000000 0x2007FFFF
GR533x | 0x20000000 9x20017FFF

If it is your own project, please refer to the SDK implementation for migration, or refer to the "Module Initialization and Scheduling" section of the [GR5xx APP Log Application Notes](https://docs.goodix.com/zh/online/app_log_bl/V3.2).



### 4. Why does RTT print the log for a period of time and then stop printing, and the system is stuck?

1.  The reason why the log is no longer printed is that the log printing in RTT mode depends on the J-Link connection. When the GR5xx SoC enters the sleep mode, the J-Link connection will be disconnected. The J-Link Link RTT Viewer does not have the automatic reconnection function. When the system wakes up again, the J-link connection has been disconnected. Therefore, the subsequent LOG will not be printed.
2.  The reason why the system is stuck is likely to be that the RTT printing mode is blocking mode. When the transmission FIFO is full, the RTT will block and wait for the host computer to read the FIFO empty. Combined with the reason described in point 1, the J-Link connection has been disconnected after sleep wake-up, and the upper computer does not continue to read the FIFO. When the FIFO is full, the LOG is set, and the blocking waiting behavior will be stuck.

There are two solutions:

1.  Turn off the low power consumption mode and add it `pwr_mgmt_mode_set(PMR_MGMT_ACTIVE_MODE);` when the system is initialized. Keeping the SoC in the Active state can avoid the disconnection of J-Link connection and avoid the problems of "lost LOG" and "system stuck". The disadvantage is that it can not effectively debug the low power consumption part.
2.  Change the RTT output mode to non-blocking mode. Use `SEGGER_RTT_ConfigUpBuffer()` the function to modify the output mode when initializing the RTT. There are two non-blocking modes: `SEGGER_RTT_MODE_NO_BLOCK_SKIP` and `SEGGER_RTT_MODE_NO_BLOCK_TRIM`. When the remaining space of the FIFO is not enough to place the complete log to be printed, if it is set to SKIP, the printing will be skipped; if it is set to TRIM, only the FIFO will be filled up, and the excess part will be discarded. Although this method does not affect the low power consumption, it can only avoid that the J-Link connection will not be blocked after disconnection, and it can not avoid the loss of LOG.



### 5.  What should I do if I can't see the LOG after J-Link RTT Viewer is connected?

You can check one by one according to the following steps:

1. Check the configuration of the _ custom _ config. H _. `APP_LOG_ENABLE` Macros should be `1`. `APP_LOG_PORT` Macros should be `1`.

2. Check that the APP LOG module and RTT are properly initialized. When calling `app_log_init()` a function, the second parameter `trans_func` should be the function that is used `SEGGER_RTT_Write()` for output (but not `SEGGER_RTT_Write()` itself, because the input parameters are different). Please refer to the implementation `platform\boards\board_SK.c` of SDK or the section of "Module Initialization and Scheduling" in the [GR5xx APP Log Application Notes](https://docs.goodix.com/zh/online/app_log_bl/V3.2).

3. Check each configuration in the RTT. First check that `_SEGGER_RTT` the variables are placed correctly. It is generally not recommended to place a `_SEGGER_RTT` variable at a fixed address, but if the user chooses to place the variable at a fixed address, you need to ensure that the fixed address exists within the SRAM address range.

4. Check whether the address is set correctly when `RTT Control Block` the J-Link RTT Viewer is connected. The GR5xx SoC does not support **Auto Detection**the mode at present. You need to use the **Address**mode to fill in manually, or use the **Search Range**mode and fill in the address range to let the RTT Viewer search automatically. Please refer to "How to use SEGGER RTT to make LOG?" "For the specific setting method Chapter answers.

5. If the problem still cannot be located and solved after the above four steps, it is necessary to determine whether each link of each LOG is executed correctly and whether the input and return values are in line with expectations through single-step debugging and tracing.



### 6. How to export the stored LOG?

-   Use the GRToolbox App on the Android side to export. For specific operations, please refer to [GR5xx APP Log Application Notes](https://docs.goodix.com/zh/online/app_log_bl/V3.2)the section "Obtaining Logs".



### 7. When using GRToolbox to export the storage LOG, what should I do if the LOG is incomplete?

-   This is most likely caused by an overflow of the RingBuffer used to temporarily store the LOG. In order to reduce the impact of erasing Flash on the application timing as much as possible, the LOG will not carry out the real storage operation, but put the LOG data into the buffer Ring Buffer, and write Flash in the `app_log_store_schedule()` function. If `app_log_store_schedule()` a LOG exceeding the size of RingBuffer is output before execution, the LOG will be incomplete or even lost. There are two solutions to this problem:
    1. Increase the cache Ring Buffer. Modifying `components\libraries\app_log\app_log_store.h` the value of and `APP_LOG_STORE_CACHE_NUM` in `APP_LOG_STORE_LINE_SIZE` as appropriate increases the cache RingBuffer, but also increases the RAM footprint.
    2. Increase the frequency of calls `app_log_store_schedule()`. For example, in an environment using an RTOS, increasing the priority of a task for running `app_log_store_schedule()` as appropriate allows the task to be scheduled more times, but operating Flash more frequently may have an impact on some time-sensitive applications.



### 8. When using GRToolbox to export logs, I find that only the most recent logs are available, and I can't get earlier logs. What should I do?

-   LOG storage uses a ring overlay mechanism. When the storage space is insufficient, a new LOG will be used to overwrite the oldest LOG. Therefore, this problem can not be really solved, but can only be alleviated by increasing the storage area and reducing unnecessary LOG.

