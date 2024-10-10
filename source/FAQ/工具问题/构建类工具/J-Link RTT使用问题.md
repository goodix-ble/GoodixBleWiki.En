## J-Link RTT使用问题


### 1. 如何在示例工程中开启RTT功能

- 确保文件${SDK}\external\segger_rtt\SEGGER_RTT.c加入工程编译。

- 将工程配置文件_custom_config.h_的宏APP_LOG_PORT值修改为1。

  ```c
  // <o> APP log port type
  // <0=> UART
  // <1=> RTT
  // <2=> ITM
  #ifndef APP_LOG_PORT
  #define APP_LOG_PORT            1
  #endif
  ```

- 确保位于文件${SDK}\platform\boards\board_SK.c的函数bsp_log_init在main外设初始化时候被调用（或确保示例工程的board_init函数被调用，此函数会调用bsp_log_init），因为SDK中RTT功能的初始化放在函数bsp_log_init中进行。



### 2. 获取_SEGGER_RTT编译地址的技巧 

- 在使用J-Link RTT时，会填写_SEGGER_RTT的地址，一种是填写范围工具进行自动搜索，一种是填写固定的地址。本文介绍第二种方法：

  - 先参考上文开启RTT功能，然后编译工程。

  - 编译完成后，打开.map文件搜索_SEGGER_RTT的变量地址，参考如下：

    ```c
    _SEGGER_RTT      0x2000c220   Data     120  segger_rtt.o(.bss)
    ```

  - 修改_SEGGER_RTT.c_中变量的定义，将map文件的变量地址使用attribute at属性，强制固定下来，这样后续_SEGGER_RTT变量地址就不会随工程功能和变量的增加而发生变化了。

    ```c
    SEGGER_RTT_CB _SEGGER_RTT __attribute__ ((at(0x2000c220))); 
    ```



### 3. J-Link RTT打印日志时，工作一会后日志不再打印

- 检查是否工作在Sleep模式下，RTT属于非AON模块，对Sleep模式支持不友好，请在芯片的Active模式使用RTT。

- 如果是Active模式下存在RTT日志停止打印，尝试将RTT工作模式修改为SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL阻塞模式测试下，如果工作正常，则尝试调整RTT缓存区大小。

  ```
  #define SEGGER_RTT_MODE_DEFAULT                   SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL 
  ```

  