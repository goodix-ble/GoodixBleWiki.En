# UART Application Notes

## 1. Introduction to UART Basic Functions
* GR551x and GR533x chips support 2 UARTs, GR5525 chip supports 4 UARTs, and GR5526 chip supports 6 UARTs.
* The hardware FIFO length for TX and RX in GR551x and GR552x is 128 bytes.
* The hardware FIFO length for TX and RX in GR533x is 16 bytes.
* The maximum baud rate supported by GR5xx chip UART interfaces is 4 Mbps.

## 2. UART Application Notes
* Only UART0 supports DMA on the GR551x.
* For GR5525 DMA configuration, UART0 and UART3 can select either DMA0 or DMA1, while UART1 and UART2 can only select DMA0.
* For GR5526 DMA configuration, UART0, UART3, and UART4 can select either DMA0 or DMA1, UART1 and UART2 can only select DMA0, and UART5 can only select DMA1.
* For certain GR5526 chips, when the DigCore is at a lower level, extreme conditions may require increasing the DigCore voltage for UART0 and UART4 usage. To modify, call the app_graphics_adjust_dcore_policy() interface during the initialization of the main function.
* When using the GR5xx UART module, refer to the chip's Datasheet to understand the detailed specifications and functions of the UART module, as well as the GPIO Pin Mux corresponding to the serial port. This aids in preliminary evaluation and schematic design.
* For actual UART code development, refer to the "GR5xx APP Driver User Manual" (https://docs.goodix.com/zh/online/detail/app_driver_bl/V1.4/cca9c0c5cf27f9dde90a1aa5d875e1af) for API interface usage instructions. Additionally, consult the example projects under SDK projects\periphal\uart for efficient use of the UART module.
* On the GR5xx chip SK board, the default USB serial port is limited by the serial port conversion chip to a maximum baud rate of 2 Mbps. It is usually recommended to configure it to 115200. For baud rates above 2M for verification testing, an external serial port board is recommended.
* For high-speed reception and transmission using the serial port, configure it in DMA mode. Minimize processing in the interrupt and use a Ring Buffer to handle data transfer operations in the interrupt, while data processing is done in the main loop or task.