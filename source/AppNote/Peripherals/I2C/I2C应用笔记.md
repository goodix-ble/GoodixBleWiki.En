# I2C Application Notes



## 1. Introduction to GR5xx I2C Basic Functions

- Main I2C parameters for each chip:

| SoC    | Number of I2C Instances | Maximum Speed                                                | FIFO Depth                                      |
| ------ | ----------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| GR551x | 2: I2C0, I2C1           | Standard Mode: 100k bit/s<br><br>Fast Mode: 400k bit/s<br><br>Fast Plus Mode: 1M bit/s<br><br>High Speed Mode: 2M bit/s | TX FIFO: 8 x 8 bits<br><br>RX FIFO: 8 x 8 bits   |
| GR5525 | 4: I2C0 to I2C3         | Standard Mode: 100k bit/s<br><br>Fast Mode: 400k bit/s<br><br>Fast Plus Mode: 1M bit/s<br><br>High Speed Mode: 3.4M bit/s | TX FIFO: 32 x 8 bits<br><br>RX FIFO: 32 x 8 bits |
| GR5526 | 6: I2C0 to I2C5         | Standard Mode: 100k bit/s<br><br>Fast Mode: 400k bit/s<br><br>Fast Plus Mode: 1M bit/s<br><br>High Speed Mode: 3.4M bit/s | TX FIFO: 32 x 8 bits<br><br>RX FIFO: 32 x 8 bits |
| GR533x | 2: I2C0, I2C1           | Standard Mode: 100k bit/s<br><br>Fast Mode: 400k bit/s<br><br>Fast Plus Mode: 1M bit/s | TX FIFO: 8 x 8 bits<br><br>RX FIFO: 8 x 8 bits   |
- Each I2C instance can be configured as either Master or Slave.
- Supports both 7-bit and 10-bit address modes.
- Supports Polling mode, interrupt mode, and DMA mode.



## 2. Typical I2C Applications

### 2.1 How to Set Slave Address
- When calling the app I2C API, for example:
  uint16_t app_i2c_transmit_async(app_i2c_id_t id, uint16_t target_address, uint8_t *p_data, uint16_t size), the target address must be specified. If acting as a Master, the target_address here is the slave address.
- For the 16-bit slave address parameter of the I2C interface, only the actual 7-bit or 10-bit slave address needs to be filled in, with the remaining bits set to 0. During transmission, the actual I2C address will be constructed internally according to the address mode set by the initialization parameters.

### 2.2 I2C Circuit Pull Up Resistor Configuration Considerations
- It is recommended to use external pull-up resistors of 4.7K or 2.2K. Higher data rates require stronger driving capabilities, smaller pull-up resistors, and consequently higher power consumption.
- The internal pull-up resistors of the GR551x and GR5526 are approximately 120K, making them unsuitable for use as I2C pull-up resistors. In contrast, the internal pull-up resistors of the GR5525 and GR533x are around 20K, which can be used for I2C rates below 400K.

### 2.3 I2C Working Mode Recommendations
When using I2C to transmit at rates above 1M, especially in systems with Bluetooth LE + sleep-wake-up, it is recommended to prioritize DMA mode, followed by polling mode. Interrupt mode is not recommended because:
- The reception process can be frequently interrupted by high-priority interrupts. For example, in systems with Bluetooth LE functionality, the higher interrupt priority of Bluetooth LE can cause frequent interruptions, delaying FIFO data retrieval and resulting in FIFO overflow errors.
- After the system wakes up from sleep, transitioning from the wake-up handling part to the I2C reception handling part spans a large program range, exceeding 8K. This reduces the XIP Cache hit rate, requiring the program to be loaded from Flash, which significantly slows down efficiency and delays FIFO data retrieval, leading to FIFO overflow errors. Therefore, the system may function normally before sleep but is prone to errors after waking up.