# UART常见问题

## 1. GR5xx芯片串口无数据输出，打印乱码，数据接收异常，可能是什么原因？

1. 可以参考《[GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl/V1.4)》“APP UART驱动”章节，检查参数配置是否正确，串口IO Pinmux、波特率、DMA等参数是比较容易出错的点。
2. 如果使用SK板默认USB串口打印，需要检查_board_SK.h_中默认串口IO配置是否有改动。



## 2. GR5xx芯片串口容易触发APP_UART_EVT_ERROR中断，是什么原因？

当出现EVT_ERROR，一般情况下是RX FIFO溢出了，需要检查代码中是否关闭中断太长，导致UART中断没有及时响应；如果出现此错误，需要恢复接收，可调用app_uart_receive_async重新开始接收。



## 3. GR5xx芯片串口模块怎么配置？

详细描述可参考《[GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl/V1.4)》“APP UART驱动”章节。