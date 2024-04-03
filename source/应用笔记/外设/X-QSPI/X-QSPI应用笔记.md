## X-QSPI 应用笔记



### 1. 基本功能介绍

-   X-QSPI 的X代表的是 eXecute-in-place , 表示可以执行代码的意思, 即代码可以在X-QSPI相连接的Nor Flash得到执行;  与之相对的是外部 QSPI, 只能用于数据存储访问, 不能存放和执行代码; 为了实现 执行代码的功能, X-QSPI 与外部QSPI功能实现上存在差异, 不能混用
-    为了加速代码的命中和执行效率, X-QSPI 设计了指令缓存机制, 均带休眠保持功能, 不同芯片的cache 缓存空间大小如下
    -   GR551x: 8 KB
    -   GR5525: 8 KB
    -   GR5526: 8 KB
    -   GR533x: 8 KB

-   多款系列芯片均提供了内部集成 1M Bytes Nor Flash的封装型号, 可用于存放代码和小量数据; 当1M Bytes 型号不满足产品设计需求时, 可以使用各芯片的外扩 X-QSPI Flash版本封装. 可外扩Flash 的能力如下: 
    -   GR551x: 可外扩 16 MBytes X-QSPI Flash空间, 但只有低8 MBytes 支持 XIP寻找, 高 8M Bytes 需要采用寄存器寻址模式,不用于存放代码, 只用于存放数据
    -   GR5525: 可外扩 16 MBytes X-QSPI Flash空间, 均支持XIP 寻址 
    -   GR5526: 暂无外扩 X-QSPI Flash的芯片封装
    -   GR533x: 可外扩 16 MBytes X-QSPI Flash空间, 均支持XIP 寻址 

-   不同芯片主频跟X-QSPI 最高运行频率分别为:
    -   GR551x: 64 MHz / 64 MHz
    -   GR5525: 96 MHz / 64 MHz
    -   GR5526: 96 MHz / 64MHz
    -   GR533x: 64 MHz / 64 MHz




### 2. 应用笔记

-   X-QSPI 在运行程序过程中, 如果对Flash执行写入操作, 会关闭系统的全局中断, 而全局中断的关闭会影响 BLE的时序逻辑, 请在 **BLE应用笔记** 章节查询文章 **BLE 与执行代码Flash 冲突处理**, 了解这种情况下的程序优化.

-   GR5515I0ND 使用外部X-QSPI Flash， 由于不同厂商和型号的 Flash 具有不同的功能和使用限制，用户可参考 **GR5515I0ND 外部 Flash 选型指导手册**， 根据产品实际情况进行合理选型。手册提供了外部扩展flash的指令和电气兼容性要求, 并推荐了建议选型列表,可以从官网搜索下载. 其他系列芯片也可以经验性参考此文档
-   如用户需要实现特殊的Flash指令，需要注意XIP和QSPI状态的转换，可参考SDK\components\libraries\hal_flash\hal_exflash_user_operation.c文件中示例代码自行实现。由于Flash操作期间无法执行Flash上的代码，操作函数前注意添加SECTION_RAM_CODE宏，使其在SRAM上执行  

