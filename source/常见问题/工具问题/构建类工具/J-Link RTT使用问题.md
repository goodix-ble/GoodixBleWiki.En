## J-Link RTT使用问题


### 1. 如何在示例工程中开启 RTT功能

- 确保 文件 ${SDK}\external\segger_rtt\SEGGER_RTT.c 加入工程编译

- 将工程配置文件 custom_config.h 的宏APP_LOG_PORT 值修改为 1

  ```c
  // <o> APP log port type
  // <0=> UART
  // <1=> RTT
  // <2=> ITM
  #ifndef APP_LOG_PORT
  #define APP_LOG_PORT            1
  #endif
  ```

- 确保 位于文件  ${SDK}\platform\boards\board_SK.c的函数 bsp_log_init 在main 外设初始化时候被调用 （或确保 示例工程的 board_init 函数被调用, 此函数会调用bsp_log_init ）；因为 SDK中 RTT 功能的初始化放在函数bsp_log_init 中进行 



### 2. 获取 _SEGGER_RTT 编译地址的技巧 

- 在使用 J-Link RTT 时, 会填写 _SEGGER_RTT 的地址, 一种是填写范围工具进行自动搜索; 一种是填写固定的地址. 这里介绍第二种方法:

  - 先参考 <如何在示例工程中开启 RTT功能> 开启RTT功能, 然后编译工程

  - 编译完成后, 打开.map 文件搜索 _SEGGER_RTT 的变量地址, 参考如下:

    ```c
    _SEGGER_RTT      0x2000c220   Data     120  segger_rtt.o(.bss)
    ```

  - 修改 SEGGER_RTT.c  中变量的定义, 将 map 文件的变量地址使用 attribute at 属性, 强制固定下来, 这样后续  _SEGGER_RTT 变量地址就不会随 工程功能和变量的增加而发生变化了.

    ```c
    SEGGER_RTT_CB _SEGGER_RTT __attribute__ ((at(0x2000c220))); 
    ```



### 3. J-Link RTT打印日志时候, 工作一会后日志不再打印

- 检查是否工作在 Sleep 模式下, RTT 属于非 AON 模块, 对Sleep 模式支持不友好, 请在芯片的Active 模式使用 RTT

- 如果是 Active 模式下存在 RTT 日志停止打印, 尝试将 RTT工作模式修改为 SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL 阻塞模式测试下, 如果工作正常. 则尝试调整 RTT 缓存区大小

  ```
  #define SEGGER_RTT_MODE_DEFAULT                   SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL 
  ```

  