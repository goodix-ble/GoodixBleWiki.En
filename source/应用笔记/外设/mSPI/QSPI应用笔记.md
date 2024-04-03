# QSPI应用笔记



## 1. 基本功能介绍

-   每个QSPI 模块均可提供 SPI、Dual SPI、Quad SPI 时序模式

-   各芯片的QSPI 模块数量及主要参数

| SoC    | QSPI实例            | 主要参数                                                     |
| ------ | ------------------- | ------------------------------------------------------------ |
| GR551x | QSPI0、QSPI1        | 最高主频32MHz; 挂载APB总线;不支持 Memory Map模式;FIFO深度8x4字节 |
| GR5525 | QSPI0、QSPI1、QSPI2 | 最高主频48MHz; 挂载AHB总线;支持 Memory Map模式; FIFO深度 (16~32)x4字节 |
| GR5526 | QSPI0、QSPI1、QSPI2 | 最高主频48MHz; 挂载AHB总线;支持 Memory Map模式; FIFO深度 (16~32)x4字节 |
| GR533x | 无                  | 略                                                           |

-   GR5525 及 GR5526 扩展了Memory Map能力, 可以将 Nor Flash 及QSPI PSRAM 设备空间映射到总线地址空间访问. 各 QSPI 实例的总线地址空间如下 (总线地址空间和别名空间段是等效的, 最低地址均对应 被映射设备的0地址)

| 芯片   | QSPI 实例 | 内存映射的总线地址空间段 (应用中建议使用) | 别名空间段               |
| ------ | --------- | ----------------------------------------- | ------------------------ |
| GR5526 | QSPI0     | [0xC0000000, 0xC4000000)                  | [0x10000000, 0x14000000) |
|        | QSPI1     | [0xC4000000, 0xC4000000)                  | [0x14000000, 0x18000000) |
|        | QSPI2     | [0xC8000000, 0xCC000000)                  | [0x18000000, 0x1C000000) |
| GR5525 | QSPI0     | [0x10000000, 0x14000000)                  |                          |
|        | QSPI1     | [0x14000000, 0x18000000)                  |                          |
|        | QSPI2     | [0x18000000, 0x1C000000)                  |                          |



## 2. 应用笔记

-   使用Memory Map方式访问 外部Flash时, 请注意使用地址对齐, 非地址对齐的数据, 可能发生错序.

-   芯片涉及QSPI & SPI时序的硬件模块较多, 下面说明帮助用户进行区分:

| 泛SPI时序模块 | 使用场景说明                                                 | 涉及芯片系列                   |
| ------------- | ------------------------------------------------------------ | ------------------------------ |
| XQSPI         | 每款芯片用于支持XIP代码执行的模块,主要用于烧写和执行代码使用, 一般合封在芯片内部,部分芯片有外部连接的封装 | GR551x、GR5525、GR5526、GR533x |
| SPIM          | SPI Master模块, 挂载在APB总线, 支持全双工工作模式. 用于SPI 协议的小尺寸屏幕、传感器等外设驱动 | GR551x、GR5525、GR5526、GR533x |
| SPIS          | SPI Slave模块, 挂载在APB总线, 需要对端作为 Master通讯, 使用场景较少 | GR551x、GR5525、GR5526、GR533x |
| QSPI          | QSPI 硬件模块, 全系芯片的QSPI模块都可以支持配置为SPI、Dual SPI、Quad SPI模式使用,当配置为SPI使用时, 行为和 SPIM 模块相似; GR551x的QSPI模块挂载在APB总线, GR5525、GR5526 的QSPI模块挂载在AHB总线, 其Dual/Quad SPI模式支持 Memory Map访问模式; GR533x 没有QSPI模块. QSPI主要用于驱动Nor/Nand Flash、PSRAM、显示屏等外设器件 | GR551x、GR5525、GR5526         |
| DC            | DC全称为Display Controller, 注意和Direct Current区分. 此硬件模块主要和GPU模块配合, 用于显示屏的驱动控制, 支持产生MIPI DBI Type-C 协议族下的所有时序类型, 包括 SPI、1-SPI、3/4-wire SPI、QSPI等. 此模式只存在于GR5526 | GR5526                         |
| OSPI          | Octual SPI, 只存在于GR5526. OSPI 控制器用于作为 芯片内部 OSPI DDR 接口的PSRAM设备的驱动控制器存在. 其产生的时序为 OSPI DDR时序. | GR5526                         |


-   可通过文章 [SPI/QSPI协议专题(1) - 基础协议特征介绍](https://developers.goodix.com/zh/bbs/blog_detail/49a0f09333f3412380b8a58ce22f879b) 进一步理解 SPI 及泛SPI协议. 
-   注意区分不同应用场景下的QSPI的概念
-   当用于指代硬件模块时, QSPI模块属于芯片的外设
-   当用于表示时序概念时, QSPI 指CS、CLK、D0~D3 构成的时序信号。


-   QSPI 跟DMA的搭配使用原则:
    -   GR551x 下, QSPI0/QSPI1 均可搭配DMA使用
    -   GR5525 & GR5526下
        -   当 QSPI0/QSPI1/QSPI2 工作在 Memory Map模式下时, DMA0/DMA1 均可以用于访问QSPI0/QSPI1/QSPI2的内存空间
        -   当 QSPI0/QSPI1/QSPI2 工作在API接口访问的寄存器模式下时, DMA0可配合QSPI0/QSPI1使用; DMA1可以配合QSPI1/QSPI2使用
        -   当QSPIx和DMA配合用于Flash、屏幕等高吞吐率访问场景下时, 务必使用 DMA的通道0, 通道0设计了最深的FIFO 

-   使用GR5526设计屏幕应用产品时, 请注意, 屏幕接口务必使用 QSPI2 的时序接口, 因为QSPI2硬件模块 和 DC控制器的QSPI时序IO是一致的,这样驱动屏幕时, 既可以使用QSPI2模块,有可以使用DC 模块.
-   GR5525 & GR5526 的Memory Map模式支持最大 512 MByte的寻址空间.
-   GR5525 & GR5526 的Memory Map模式下使用 memcpy 接口, 注意编译时不能使用micro-lib. micro-lib 会严重降低QSPI memory map模式下memcpy的传输效率
-   以下建议对 GR5525 & GR5526 的QSPI模块适用
    -    一般情况在SRAM和工作在内存映射模式下的QSPI设备移动数据时，如果数据量小于1 KB，可优先使
        用 memcpy 函数进行；如果数据量大于1 KB，建议使用DMA进行搬运。数据量越大，DMA会展现越
        大的优势
    -   在内存映射模式下访问数据时，如果需要使用memcpy/memset函数，Keil工程下请优先编译使用系统
        标准库，而不要选用microlib；前者能更好的激活总线Burst传输行为，获得更好的访问效率
    -   部分QSPI设备时序上需要较大的Tcsu(CS Setup Delay Time), 否则不能获得正确稳定的访问数据：
        • 如果设备支持时钟模式3，可尝试设置时钟模式3。时钟模式3会比模式0有更大的Tcsu
        • 可通过寄存器配置增加Tcsu时间
    -    一般QSPI PSRAM 设备需要定时释放片选以完成内部数据保持电路的自刷新，最长的片选时间
        为tCEM，尤其对于写访问，需要严格遵守。
        -   内存映射模式下写访问时，从设计上考虑了tCEM，不用再关注此参数
        -   寄存器模式下，从驱动层考虑了tCEM，但寄存器模式接口复杂度较高。建议QSPI PSRAM设备不在寄存器模式下使用
    -    QSPI 存在预取模式，当进行QSPI读访问时，可以进一步提高 QSPI的读效率，但此模式只能配合DMA工作，不能在CPU访问时开启。
    -   GR5525 & GR5526在设计时对各个QSPI的FIFO进行了差异化优化，一般情况下外设混接QSPI不存在问题；同时，GR5525 & GR5526在设计时也对DMA的FIFO进行了差异化优化，为了发挥GR5525 & GR5526的最佳效率，使用建议如下：
        -   QSPI0优先用于连接Flash设备，可搭配DMA0的通道0工作
        -   QSPI1优先用于连接PSRAM设备，可搭配DMA0/DMA1的通道0工作
        -   QSPI2优先用于连接Display设备，可搭配DMA1的通道0工作
        -   请将DMA0/DMA1的通道0优先留给QSPI0/QSPI1/QSPI2 等高速外设使用，且尽量不同时混用  



## 3. 典型应用场景

### 3.1 GR5526支持使用外部Flash作为OTA升级时的固件缓存空间

- 请参考如下连接:

> [[Patch\] - GR5526 支持使用外部Flash 作为OTA 升级时的固件缓存空间 | 低功耗蓝牙 | 汇顶科技开发者社区 (goodix.com)](https://developers.goodix.com/zh/bbs/detail/51d67bb927704dadab2a53c0602e1d36)