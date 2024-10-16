# DMA

## 1. Introduction to Basic Functions
- Different SoCs have different DMA function configurations, with varying numbers of DMA instances and different available transfer channels for each instance.
- The table below describes the DMA channel configuration and capabilities for each chip.

| SoC    | DMA Instance | Number of Channels and FIFO Depth                    | Basic Functionality      | Usage Restrictions                                           |
| ------ | ------------ | ---------------------------------------------------- | ------------------------ | ------------------------------------------------------------ |
| GR551x | DMA0         | Supports 8 channels, each channel FIFO 8x4 bytes     | Basic data transmission  | Single transmission does not exceed 4095 beats               |
| GR5525 | DMA0         | Supports 6 channels, channel 0 FIFO 32x4 bytes, other channels FIFO 4x4 bytes | Basic data transmission, S&G, LLP | 1. Single transmission does not exceed 4095 beats;<br/>2. Use LLP function to extend the amount of data per single transmission |
|        | DMA1         | Supports 6 channels, channel 0 FIFO 32x4 bytes, other channels FIFO 4x4 bytes | Basic data transmission, S&G, LLP | 1. Single transmission does not exceed 4095 beats;<br/>2. Use LLP function to extend the amount of data per single transmission |
| GR5526 | DMA0         | Supports 6 channels, channel 0 FIFO 32x4 bytes, other channels FIFO 4x4 bytes | Basic data transmission, S&G, LLP | 1. Single transmission does not exceed 4095 beats;<br/>2. Use LLP function to extend the amount of data per single transmission |
|        | DMA1         | Supports 6 channels, channel 0 FIFO 32x4 bytes, other channels FIFO 4x4 bytes | Basic data transmission, S&G, LLP | 1. Single transmission does not exceed 4095 beats;<br/>2. Use LLP function to extend the amount of data per single transmission |
| GR533x | DMA0         | Supports 5 channels, channel 0 FIFO 8x4 bytes, other channels FIFO 4x4 bytes | Basic data transmission  | Single transmission does not exceed 4095 beats               |


- - DMA supports the following transfer modes:
    - Memory to Memory
    - Memory to Peripheral
    - Peripheral to Memory
    - Peripheral to Peripheral

> Note: 

```
When one end of the transfer is a peripheral, the DMA transfer signal relies on hardware handshake signals. For GR5525 and GR5526, which have multiple DMA instances, DMA and peripherals cannot be arbitrarily paired. Refer to the DMA hardware handshake signal allocation table in the Datasheet. For details, refer to the DMA and handshake signal sections in the Datasheet of each SoC.
```

- In a basic DMA data transfer, up to 4095 beats of data can be transmitted at a time. "Beat" refers to the bit width of the data transmitted through DMA.
    - If the data bit width is in bytes, up to 4095 bytes of data can be transmitted in a single DMA transmission.
    - If the data bit width is in half-words, up to 4095 x 2 bytes of data can be transmitted in a single DMA transmission.
    - If the data bit width is in words, up to 4095 x 4 bytes of data can be transmitted in a single DMA transmission.
    - If more than 4095 beats of data are transmitted in a single basic DMA transfer, an error message will pop up, indicating that the DMA transmission is interrupted.
    - To extend a single transfer beyond 4095 beats, use Linked List Pointer (LLP) chained transfer. Only GR5525 & GR5526 support this transfer mode; GR551x and GR553x do not support it.
- Increasing the data transfer width of DMA can improve DMA transfer performance. Using a 32-bit transfer width provides better performance than 16-bit and 8-bit.
- GR5525 and GR5526 extend the LLP and S&G capabilities of DMA, which, when used with peripherals like QSPI, can significantly improve the throughput of such peripherals. For more information on LLP and S&G, refer to the document "[GR5526 Display Refresh Guide](https://docs.goodix.com/zh/online/display_refresh_guide_bl_b)" or "[GR5525 Display Guide](https://docs.goodix.com/zh/online/display_guide_bl_c)".



## 2. Application Notes

- GR5525 & GR5526 provide two DMA instances for users: DMA0 and DMA1. There are six DMA channels in total. The FIFO depth is 32 (channel 0) or 4 (channels 1–5).
    
    - Channel 0 features large FIFO depth, so it can cache more data in DMA transmission, improving DMA transmission throughput. Therefore, in wearable applications, it is recommended to allocate channel 0 of DMA0/DMA1 to peripherals with high throughput in such scenarios as Flash access, PSRAM access, bulk memory block transfer, and display.
    
- Compared to the DMA of GR551x and GR553x, the DMA of GR5525 & GR5526 has the following extended features:
    - DMA chained data transmission: Manage all to-be-transmitted data blocks using a pointer linked list. After a data block is sent, the next block is automatically loaded according to the Next pointer until the Next pointer becomes empty. Its advantages are:
        - Transmit more than 4095 beats of data in a single transmission.
        - Transmit data from a discontinuous address space in a single transmission cycle.
        - Use different transmission configurations to transmit data in a single transmission cycle.
    - DMA scatter transmission: In a DMA scatter transmission, data in a continuous address space is scattered to a discontinuous address space based on certain rules.
    - DMA gather transmission: In a DMA gather transmission, data in a discontinuous address space is gathered in a continuous address space. DMA gather transmission can be regarded as a reverse process of DMA scatter transmission.
    
- GR551x and GR553x each have only one DMA instance, and all peripheral modules can use DMA for transmission. GR5525 and GR5526 have two DMA instances, and the support for peripherals varies for each instance.

- The support status of GR5525 DMA with different peripherals is as follows:



| Peripheral | DMA0 | DMA1 |
| ---------- | ---- | ---- |
| QSPI0      | YES  | NO   |
| QSPI1      | YES  | YES  |
| QSPI2      | NO   | YES  |
| SPI Master | YES  | YES  |
| SPI Slave  | YES  | NO   |
| UART0      | YES  | YES  |
| UART1      | YES  | NO   |
| UART2      | YES  | NO   |
| UART3      | YES  | YES  |
| I2C0       | NO   | YES  |
| I2C1       | NO   | YES  |
| I2C2       | YES  | NO   |
| I2C3       | YES  | NO   |
| I2S Master | NO   | YES  |
| I2S Slave  | NO   | YES  |
| DSPI       | NO   | YES  |
| PDM        | NO   | YES  |
| ADC        | YES  | NO   |


- The support status of GR5526 DMA with different peripherals is as follows:


| Peripheral | DMA0 | DMA1 |
| ---------- | ---- | ---- |
| QSPI0      | YES  | NO   |
| QSPI1      | YES  | YES  |
| QSPI2      | NO   | YES  |
| SPI Master | YES  | YES  |
| SPI Slave  | YES  | NO   |
| UART0      | YES  | YES  |
| UART1      | YES  | NO   |
| UART2      | YES  | NO   |
| UART3      | YES  | YES  |
| UART4      | YES  | YES  |
| UART5      | NO   | YES  |
| I2C0       | NO   | YES  |
| I2C1       | NO   | YES  |
| I2C2       | YES  | NO   |
| I2C3       | YES  | NO   |
| I2C4       | YES  | NO   |
| I2C5       | YES  | NO   |
| I2S Master | NO   | YES  |
| I2S Slave  | NO   | YES  |
| DSPI       | NO   | YES  |
| PDM        | NO   | YES  |
| ADC        | YES  | NO   |