# I2C应用笔记 #


## 1. GR5xx I2C基本功能介绍

- 各芯片I2C主要参数：

  | SoC    | I2C实例个数     | 最高速率                                                     | FIFO深度                                       |
  | ------ | --------------- | ------------------------------------------------------------ | ---------------------------------------------- |
  | GR551x | 2个：I2C0、I2C1 | Standard Mode: 100k bit/s<br />Fast Mode: 400k bit/s<br />Fast Plus Mode: 1M bit/s<br />High Speed Mode: 2M bit/s | TX FIFO: 8 x 8 bits<br />RX FIFO: 8 x 8 bits   |
  | GR5525 | 4个：I2C0～I2C3 | Standard Mode: 100k bit/s<br />Fast Mode: 400k bit/s<br />Fast Plus Mode: 1M bit/s<br />High Speed Mode: 3.4M bit/s | TX FIFO: 32 x 8 bits<br />RX FIFO: 32 x 8 bits |
  | GR5526 | 6个：I2C0～I2C5 | Standard Mode: 100k bit/s<br />Fast Mode: 400k bit/s<br />Fast Plus Mode: 1M bit/s<br />High Speed Mode: 3.4M bit/s | TX FIFO: 32 x 8 bits<br />RX FIFO: 32 x 8 bits |
  | GR533x | 2个：I2C0、I2C1 | Standard Mode: 100k bit/s<br />Fast Mode: 400k bit/s<br />Fast Plus Mode: 1M bit/s | TX FIFO: 8 x 8 bits<br />RX FIFO: 8 x 8 bits   |

- 每个I2C实例均可配置为Master或Slaver。

- 每个I2C实例均支持7-bit或10-bit地址模式。

- 每个I2C实例均支持Polling模式、中断模式和DMA模式。



## 2. I2C应用笔记

### 2.1 如何设置从机地址

- 调用app i2c API时，比如
  uint16_t app_i2c_transmit_async(app_i2c_id_t id, uint16_t target_address, uint8_t *p_data, uint16_t size)，需要指定对端地址。如果做为Master，这里的target_address就是从机地址。

- I2C接口入参的16bit从机地址，只填真正的7-bit或10-bit从机地址即可，其余位填0。传输时，内部会根据初始化参数设置的地址模式进行真正I2C地址的构造。

### 2.2 I2C电路上拉电阻配置注意事项

- 建议用外部上拉电阻，4.7K或2.2K，速率越高要求驱动能力越强、上拉电阻越小，功耗相对也高一些。
- GR551x和GR5526的内部上拉电阻有120K左右，不适合用作I2C的上拉电阻；GR5525、GR533x的内部上拉电阻在20K左右，对于低于400K速率的I2C，也可以用。

### 2.3 I2C工作模式使用建议

用I2C进行1M以上的速率传输时，特别是在带Bluetooth LE+休眠唤醒的系统中，建议优先用DMA模式，其次是Polling模式，不建议用中断模式，因为：

- 接收处理会被高优先级中断频繁打断，比如带Bluetooth LE功能的系统中，Bluetooth LE的中断优先级更高，频繁打断会导致取FIFO数据不及时，从而会出现FIFO溢出的错误。
- 系统休眠唤醒后，从唤醒处理部分再跳到I2C接收处理部分，程序跨度大，超过8K范围，导致XIP Cache命中率降低，需要从Flash加载程序出来运行，效率慢很多，导致取FIFO数据不及时，从而会出现FIFO溢出的错误。所以会出现休眠前正常，唤醒后容易出错的情况。
