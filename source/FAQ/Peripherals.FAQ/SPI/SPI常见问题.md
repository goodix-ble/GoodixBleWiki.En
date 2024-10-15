## FAQ for SPI



### 1. What is the maximum frequency supported by SPI?

- SPI modules are divided into SPI Master and SPI Slave, in which the maximum frequency supported by SPI Master is one-half of the maximum system frequency. SPI Master supports even number of crossover coefficients between 2 and 65535, and does not support odd number of crossover frequencies.
- The maximum frequency supported by each chip SPI Master module is as follows:
    - GR551x full series of chips maximum main frequency is 64 MHz, SPI Master's maximum operating frequency is 32 MHz, the clock source is the system clock.
    - The maximum frequency of GR5525 chips is 96 MHz, the maximum frequency of SPI Master is 48 MHz, and the clock source is the peripheral clock.
    - GR5526 full series chips have a maximum frequency of 96 MHz, the maximum frequency of SPI Master is 48 MHz, and the clock source is the peripheral clock.
    - GR533x full series chips have a maximum main frequency of 64 MHz, a maximum SPI Master frequency of 32 MHz, and a peripheral clock source.



### 2. What is software chip select, what is hardware chip select, and what is the difference in usage?

- Software chip select: Before SPI transfer, the software pulls down the IO where CS pin is located; after SPI transfer is completed, the software pulls up the IO where CS pin is located. the behavior of CS is controlled by the software code. The CS behavior is controlled by the software code. The CS pin IO at this time needs to be configured as Output mode.
- Hardware Chip Select: The pull-down and pull-up of the SPI chip select signal are all taken care of by the SPI module of the chip, and the IO where the CS pin is located at this time needs to be configured as the Mux mode of the CS function.
- Why does software chip select exist?
    - When SPI sends data, it is possible that because of the large amount of data, high transmission rate or CPU can not process in time, etc., the speed of feeding data to the SPI FIFO cannot keep up with the speed of sending, resulting in the FIFO becomes empty, and if the hardware chip select is used at this time, the CS will be automatically pulled up to release, and the wrong access timing will be generated.
- When do I need to use software chip select?
    - It is recommended to use software chip select when the transmission data volume is large and the SPI frequency configuration is high. Since data size and frequency are relative concepts that cannot be calculated precisely based on the scenario, it is recommended that software chip select be enabled for all scenarios that use SPI transmission. This recommendation applies to all series of GR551x, GR5525, GR5526, and GR533x chips.
    - SPI is preconfigured with software chip select support in the app driver layer, just pay attention to turn on the related control macros when you use it. For details, please refer to the driver code in _app_spi.c_.



### 3. A callback error event APP_SPI_EVT_ERROR occurs when SPI receives data, how should I handle it?

- When SPI receives data, it is possible that the receive FIFO of the SPI module is stuffed with the data sent from Slave and a FIFO receive overflow error (Receive Overflow Error) occurs due to a large amount of data, a high transfer rate, or the CPU not being able to process it in time. When this error occurs, the user is informed via the callback event APP_SPI_EVT_ERROR. The correct way to handle this is to call the interface to receive the data again. Also, in this case, please use DMA transfer mode to reduce the probability.
- If it is not the above reason and DMA transfer mode is used at the same time, the amount of data transferred by DMA may be too large, and it is necessary to limit the DMA single transfer to 4095 beats or less.
