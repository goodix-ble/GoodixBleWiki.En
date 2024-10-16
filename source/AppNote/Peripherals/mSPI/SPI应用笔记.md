# SPI Application Notes

## 1. Introduction to Basic Functions
- The number and main parameters of SPI modules for each chip.

| SoC    | SPI Instance | Key Parameters                             |
| ------ | ------------ | ------------------------------------------ |
| GR551x | SPIM, SPIS   | SPIM max frequency 32 MHz; FIFO depth 8x4 bytes  |
| GR5525 | SPIM, SPIS   | SPIM max frequency 48 MHz; FIFO depth 16x4 bytes |
| GR5526 | SPIM, SPIS   | SPIM max frequency 48 MHz; FIFO depth 16x4 bytes |
| GR533x | SPIM, SPIS   | SPIM max frequency 32 MHz; FIFO depth 8x4 bytes  |

## 2. Application Notes
- It is recommended to use software-controlled chip select mode for the SPI Master module.
- When the application scenario only requires the SPI to provide the MOSI signal, consider using the SPI mode of the QSPI module instead.
- Precautions for using SPI Master:
    - When receiving data, if the data volume is large or the SPI operating frequency is high, the CPU or DMA may not keep up with the SPI FIFO read speed, causing a receive overflow and data loss. Optimization methods:
        - It is preferable to use DMA for transmission, as the transmission bandwidth of DMA is much larger than that of the CPU, effectively reducing the occurrence of receive overflows.
        - When using DMA to receive data, if overflow still occurs, configure a 4-byte transfer width at runtime to further improve the utilization of the SPI FIFO and enhance transmission bandwidth.
        - In scenarios where width requirements are not high, reduce the amount of data received in a single transfer to lower the probability of receive overflow.
        - If receive overflow still occurs after the above optimizations, implement a re-read logic at the software layer. When an overflow occurs, discard the previously read data and re-read it.
    - If using hardware-controlled CS chip select signal, when sending data, if the data volume is large or the SPI operating frequency is high, the CPU or DMA may not keep up with the SPI FIFO send speed, causing the CS signal to rise automatically, leading to subsequent timing data issues.
        - The optimization method is to use software to control the lowering and raising of the chip select signal.
- SPI is a strict timing protocol. When there are anomalies in SPI communication, use a logic analyzer to capture SPI signals and analyze potential issues.
- The SPI driver provides access interfaces in three modes: polling mode, interrupt mode, and DMA mode. The empirical recommendations for each mode are as follows. Following these recommendations can effectively reduce the probability of receive overflow, but the probability still exists.
    - GR551x and GR533x:
        - Conditions for using polling mode and interrupt mode:
            - It is recommended that the data volume for a single transmission be less than 4 bytes.
            - It is recommended to use it when the SPI operating frequency does not exceed 1 MHz.
            - Suitable for low-frequency and small data volume scenarios.
        - DMA mode usage conditions:
            - Any data amount less than 4095 bytes per single transmission.
            - Use when the SPI operating frequency is not greater than 32 MHz.
            - If receive overflow occurs, reduce the amount of data per single transmission and add a re-read mechanism at the Application Layer.
    -   GR5525 and GR5526:
        - Polling mode and interrupt mode usage conditions:
            - It is recommended that the data amount per single transmission be less than 8 bytes.
            - It is recommended to use when the SPI operating frequency is not greater than 8 MHz.
            - Suitable for low-frequency and small data amount scenarios.
        - DMA mode usage conditions:
            - Any data amount less than 4095 bytes per single transmission, but the data transmission limit can be extended through LLP.
            - Use when the SPI operating frequency is not greater than 48 MHz.
            - If receive overflow occurs, reduce the amount of data per single transmission and add a re-read mechanism at the Application Layer.