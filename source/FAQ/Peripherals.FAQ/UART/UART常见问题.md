## FAQ for UART

### 1. GR5xx chip serial port no data output, print garbage, data reception abnormal, what may be the reason?

1. You can refer to “[GR5xx APP Driver User's Manual](https://docs.goodix.com/zh/online/app_driver_bl/V1.4)” chapter “APP UART Driver” to check whether the parameters are configured correctly, the serial port IO Pinmux, baud rate, DMA and other parameters are easier to be configured. Serial port, IO Pinmux, baud rate, DMA and other parameters are more likely to be wrong. 2.
2. If you use the default USB serial port of SK board to print, you need to check whether the default serial port IO configuration in _board_SK.h_ has been changed.



### 2. GR5xx chip serial port easily trigger APP_UART_EVT_ERROR interrupt, what is the reason?

When EVT_ERROR occurs, it is usually the RX FIFO overflow, you need to check whether the code closes the interrupt for too long, resulting in the UART interrupt did not respond in time; if this error occurs, you need to resume reception, you can call app_uart_receive_async to restart reception.



### 3. How to configure GR5xx chip serial module?

For detailed description, please refer to the chapter “APP UART Driver” in [GR5xx APP Driver User's Manual](https://docs.goodix.com/zh/online/app_driver_bl/V1.4).