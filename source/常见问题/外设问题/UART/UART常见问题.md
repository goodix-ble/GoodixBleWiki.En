# UART 常见问题

## 1. GR5xx 芯片串口未数据输出，打印乱码，数据接收异常，可能是什么原因？

1. 可以参考GR5xx APP驱动用户手UART驱动章节，检查参数配置是否正确，串口IO Pinmux，波特率，DMA等参数是比较容易出错的点。
2. 如果使用SK板默认USB串口打印，需要检查board_SK.h中默认串口IO配置是否有改动



## 2. GR5xx 芯片串口容易触发APP_UART_EVT_ERROR中断，是什么原因？

当出现EVT_ERROR，一般情况下是RX FIFO溢出了，需要检查代码中是否关闭中断太长，导致UART中断没有及时响应；如果出现此错误，恢复接收，需要调用app_uart_receive_async重新开始接收。



## 3. GR5xx 芯片串口模块怎么配置？

在GR5xx APP驱动用户手册中，有对APP UART驱动进行详细的描述，可以进行参考https://docs.goodix.com/zh/online/detail/app_driver_bl/V1.3/ed7aa3f4beefb8e018c880fcf9335f73