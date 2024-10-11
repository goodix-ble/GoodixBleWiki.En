## USB应用介绍

### 1. USB简介
GR5526提供了一个符合USB 2.0全速规范的通用串行总线（USB）设备控制器。该USB设备控制器支持六个端点和四种数据传输模式：控制传输、批量传输、中断传输和等时传输，支持6个端点：

| 端点 | 类型                               | 主要参数               |
| ---- | ---------------------------------- | ---------------------- |
| EP0  | 控制端点，同时集成了输入和输出功能 | 2 x 64 bytes FIFO      |
| EP1  | 支持中断和批量传输的输出端点       | 64 bytes FIFO          |
| EP2  | 支持中断和批量传输的输入端点       | 64 bytes FIFO          |
| EP3  | 支持中断和批量传输的输入端点       | 64 bytes FIFO    DMA √ |
| EP4  | 支持等时传输的输入端点             | 1023 bytes FIFO  DMA √ |
| EP5  | 支持等时传输的输出端点             | 1023 bytes FIFO  DMA √ |



### 2. USB应用笔记

* 考虑多芯片和操作平台移植，以及易用性，提供Demo都是基于TinyUSB开源库搭建的；
 * 不使用动态内存分配；
 * 阻塞所有中断事件，在非ISR任务功能中处理中断事件；
* 公开TinyUSB中未包含GR5526适配，GR5526 SDK中适配文件路径：`\external\TinyUSB\src\portable\goodix\gr552x\dcd_gr552x.c`；
* GR5526 SDK提供的Demo，其路径`\Src\usbd_user`下都有`tusb_config.h`文件，可配置MCU类型、操作系统类型和Class类型等；
* TinyUSB对于callback函数的定义都使用了weak修饰，为避免用户定义和weak使用的callback在编译、链接时非预期的结果，可在用户自己定义的callback函数加TU_ATTR_USED修饰，如在keil下勾选了One ELF Section per Function，用户定义callback可能被优化；
* TinyUSB使用了部分GNU特性，在非GCC环境下编译，注意开启GNU的支持，如keil下，需添加--gnu配置；
* 考虑到现有电脑等设备部兼容USB1.0 Host，至少支持USB2.0协议，因此对于Speed Low暂未做适配；



