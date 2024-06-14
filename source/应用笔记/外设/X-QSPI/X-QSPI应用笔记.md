## X-QSPI应用笔记



### 1. 基本功能介绍

-   X-QSPI的X代表的是eXecute-in-place，表示可以执行代码的意思，即代码可以在X-QSPI相连接的NOR Flash得到执行；与之相对的是外部QSPI，只能用于数据存储访问，不能存放和执行代码；为了实现执行代码的功能，X-QSPI与外部QSPI功能实现上存在差异，不能混用。
-    为了加速代码的命中和执行效率，X-QSPI设计了指令缓存机制，均带休眠保持功能。不同芯片的Cache缓存空间大小如下：
    -   GR551x：8 KB
    -   GR5525：8 KB
    -   GR5526：8 KB
    -   GR533x：8 KB

-   多款系列芯片均提供了内部集成1 Mbytes NOR Flash的封装型号，可用于存放代码和小量数据。当1 Mbytes型号不满足产品设计需求时，可以使用各芯片的外扩X-QSPI Flash版本封装。可外扩Flash的能力如下：
    -   GR551x：可外扩16 Mbytes X-QSPI Flash空间，但只有低8 Mbytes支持 XIP寻找，高8 Mbytes需要采用寄存器寻址模式，不用于存放代码，只用于存放数据
    -   GR5525：可外扩16 Mbytes X-QSPI Flash空间，均支持XIP寻址 
    -   GR5526：暂无外扩X-QSPI Flash的芯片封装
    -   GR533x：可外扩16 Mbytes X-QSPI Flash空间，均支持XIP寻址 

-   不同芯片主频与X-QSPI最高运行频率分别为：
    -   GR551x：64 MHz / 64 MHz
    -   GR5525：96 MHz / 64 MHz
    -   GR5526：96 MHz / 64MHz
    -   GR533x：64 MHz / 64 MHz




### 2. 应用笔记

-   X-QSPI在运行程序过程中，如果对Flash执行写入操作，会关闭系统的全局中断，而全局中断的关闭会影响Bluetooth LE的时序逻辑。请参考**应用笔记**部分《Bluetooth LE与执行代码Flash冲突处理》，了解针对此种情况的程序优化。

-   GR5515I0NDA使用外部X-QSPI Flash，由于不同厂商和型号的Flash具有不同的功能和使用限制，用户可参考《[GR5515I0NDA外部Flash选型指导手册](https://docs.goodix.com/zh/online/detail/gr5515_flash_selection_guide/V1.4/44637c95d0d76dcb98bf8080fdd6f8bf)》，根据产品实际情况进行合理选型。手册提供了外部扩展Flash的指令和电气兼容性要求，并推荐了建议选型列表，可以从官网搜索下载。其他系列芯片也可以经验性参考此文档。
-   如用户需要实现特殊的Flash指令，需要注意XIP和QSPI状态的转换，可参考SDK\components\libraries\hal_flash\hal_exflash_user_operation.c文件中示例代码自行实现。由于Flash操作期间无法执行Flash上的代码，操作函数前注意添加SECTION_RAM_CODE宏，使其在SRAM上执行。

