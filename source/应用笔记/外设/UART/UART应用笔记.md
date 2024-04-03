# UART 应用笔记



## 1. UART基本功能介绍

* GR551x和GR533x芯片支持2路串口，GR5525芯片支持4路串口，GR5526芯片支持6路串口
* GR551x和GR552x TX和RX的硬件FIFO长度为128字节
* GR533x TX和RX的硬件FIFO长度为16字节
* GR5xx芯片串口波特率最大支持4Mbps



## 2. UART 应用笔记

* GR551x 只有UART0支持DMA
* GR5525 DMA配置时，UART0和UART3可选DMA0或DMA1，UART1和UART2 只能选择DMA0
* GR5526 DMA配置时，UART0、UART3和UART4可选DMA0或DMA1，UART1和UART2只能选择DMA0，UART5只能选择DMA1
* GR5526 个别芯片在Digcore较低时, 工艺较为极限导致UART0和UART4在使用时，需要提升DigCore电压， 具体修改方法为在main 函数初始化时调用 app_graphics_adjust_dcore_policy()接口 
* 在使用GR5xx UART模块时，可以先在芯片Datasheet中了解芯片UART模块的详细指标功能，以及串口对应的GPIO Pinmux，这样有助于进行前期的评估和原理图设计。
* 在进行UART实际代码开发时，可以先在GR5xx APP驱动用户手册中，对API接口使用说明进行了解，也可以参考SDK projects\periphal\uart目录下的示例工程，这样有助你高效使用UART模块。
* GR5xx 芯片SK板上，默认USB串口打印，因为串口转换芯片限制，最高支持波特率为2Mbps，通常建议配置为115200，如果要使用2M以上波特率进行验证测试，建议外接串口小板。
*  使用串口进行高速率的接收发送时，需要配置成DMA模式，在中断中尽量少的处理事情，可以使用ringbuffer，在中断中只做数据搬移操作，在main循环或task中进行数据处理。



