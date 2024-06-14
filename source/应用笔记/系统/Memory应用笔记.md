## Memory应用笔记



### 1. 基本功能介绍



#### 1.1 Memory资源概述

- GR5xx提供的Memory资源如下（更多详情参见对应芯片Datasheet）：

| SoC    | SRAM (Up to KB)  | Flash (Up to KB) |
| ------ | ---------------- | ---------------- |
| GR533x | 96               | 512              |
| GR5513 | 128              | 512              |
| GR5515 | 256              | 1024             |
| GR5525 | 256              | 1024             |
| GR5526 | 512              | 1024             |

#### 1.2 Memory布局
- 不同芯片的SRAM和Flash布局有所不同，详情见芯片对应的开发者指南，如GR551x的Flash和SRAM布局可参考《[GR551x开发者指南](https://docs.goodix.com/zh/online/gr551x_develop_guide/V2.7)》“Flash存储映射”和“RAM存储映射”章节。

#### 1.3 典型应用资源使用和用户可用资源情况
- GR5515典型应用资源使用和用户可用资源情况（基于SDK V2.0.1, ARMCC V5.06 update 1(build 61), -O2, System stack 8KB, System heap 0KB。不同SDK版本、SDK示例、编译器和优化选项，结果有所不同，以实际编译结果为准）：


| Role               | Example                  | ADV Number  | SCAN Number | Bluetooth LE Connection Number | Bluetooth LE Bond Number | System Used SRAM (KB) | System Used Flash (KB) | Customer Available SRAM (KB) | Customer Available Flash (KB) |
| ------------------ | ------------------------ | ----------- | ----------- | --------------------- | --------------- | -------------------- | --------------------- | --------------------------- | ---------------------------------- |
| Central            |  ble_app_cts_c           |    0        |    1        |            1          |        1        |           51         |          92           |             205             |                932                 |
| Central            |  ble_app_cts_c           |    0        |    1        |            4          |        4        |           65         |          92           |             191             |                932                 |
| Peripheral         |  ble_app_cts             |    1        |    0        |            1          |        1        |           48         |          83           |             208             |                941                 |
| Peripheral         |  ble_app_cts             |    1       |    0       |            4          |        4        |           60         |          83           |             196             |                941                 |
| Central+Peripheral | ble_app_hrs_rscs_relay   |    1        |    1        |            4          |        4        |           66         |          99           |             190             |                925                 |

- GR533x典型应用资源使用和用户可用资源情况（基于SDK V1.0.5, ARMCC V5.06 update 1(build 61), -O2, System stack 4KB, System heap 0KB。不同SDK版本、SDK示例、编译器和优化选项，结果有所不同，以实际编译结果为准）：

| Role               | Example                | GATTC Support | GATTS Support | Master Support | Slave Support | ADV Number | SCAN Number | Bluetooth LE Connection Number | Bluetooth LE Bond Number | System Used SRAM (KB) | System Used Flash (KB) | Customer Available SRAM (KB) | Customer Available Flash (KB) |
| ------------------ | ---------------------- | ------------- | ------------- | -------------- | ------------- | ---------- | ----------- | ------------------------------ | ------------------------ | --------------------- | ---------------------- | ---------------------------- | ----------------------------- |
| Central            | ble_app_cts_c          | 1             | 0             | 1              | 0             | 0          | 1           | 1                              | 1                        | 42                    | 113                    | 54                           | 399                           |
| Central            | ble_app_cts_c          | 1             | 0             | 1              | 0             | 0          | 1           | 4                              | 4                        | 48                    | 113                    | 48                           | 399                           |
| Peripheral         | ble_app_cts            | 0             | 1             | 0              | 1             | 1          | 0           | 1                              | 1                        | 41                    | 106                    | 55                           | 406                           |
| Peripheral         | ble_app_cts            | 0             | 1             | 0              | 1             | 1          | 0           | 4                              | 4                        | 47                    | 106                    | 49                           | 406                           |
| Central+Peripheral | ble_app_hrs_rscs_relay | 1             | 1             | 1              | 1             | 1          | 1           | 4                              | 4                        | 50                    | 122                    | 46                           | 390                           |



### 2. 应用笔记

#### 2.1 链接脚本应用指南（以ARMCC Scatter File为例，其他链接脚本类似）
不同芯片的Scatter文件略有差异，以下是GR551x的Scatter文件的各个执行域，其他芯片类似：
- LR_FLASH
    - 固件的加载域，指定固件的起始地址（APP_CODE_RUN_ADDR）和固件最大大小（FLASH_SIZE）。
- FLASH_CODE
    - 固件代码执行域，指定固件代码段的起始地址（APP_CODE_RUN_ADDR）和代码段的最大大小（APP_MAX_CODE_SIZE）。
- TINY_RAM_SPACE
    - SDK内部存放代码的RAM区域，用户无需关注此区域。
- FPB
    - SDK内部存放FPB数据的RAM区域，用户无需关注此区域。
- RAM_RW
    - 存放程序已经初始化且数据不为0的全局变量的区域。
- RAM_CODE
    - 存放SDK和用户代码的RAM区域。
    - 放在RAM_CODE的代码可以分为两类：
        - 一是某些函数由于涉及到Flash操作的代码必须常驻内存，如果放到Flash中就会造成死机。
        - ⼆是放到RAM中执⾏的函数每次被调⽤时不需要在Cache未命中时从Flash重新读取，可以节省时间，所以对于⼀些执⾏时间有要求的函数可以放到常驻内存，提⾼执⾏效率。SDK中将睡眠唤醒等⼀些需要经常执⾏的函数常驻内存，⼤⼤降低执⾏时间，最终达到节省功耗的目的。
- RAM_RESERVE
    - RAM不会被初始化的执行域。
- RAM_ZI
    - RAM中存放程序未初始化的全局变量和初始化为0的全局变量的区域。
- ARM_LIB_HEAP
    - C库内存动态分配的Heap（如malloc等函数），C库的malloc等函数由于不具备线程安全，不建议用户使用C库提供的内存动态分配函数（如malloc）和内部带有malloc函数的C库函数（如strdup）。若用户是裸机开发，可使用app_memory模块；若使用RTOS，则建议使用RTOS的内存分配函数。
- ARM_LIB_STACK
    - 系统栈执行域。用户可以根据实际情况调整栈大小，GR551x的栈空间不能小于8 KB，GR531x的栈空间不能小于4 KB。

#### 2.2 计算程序所用RAM和固件大小（ARMCC编译器，其他编译器可参考以下方法）

##### 2.2.1 GR551x（SDK V2.0.1，用户未修改链接脚本）
- GR551x RAM使用情况
    - 在```\Keil_5\Listings```目录找到map文件。
    - 用文本编辑器打开map文件，找到```ARM_LIB_HEAP```的起始地址并记为```ARM_LIB_HEAP_START_ADDR```，如下所示```ARM_LIB_HEAP```的起始地址为```0x0080ce28```：
        ```
        Execution Region ARM_LIB_HEAP (Base: 0x0080ce28, Size: 0x00000000, Max: 0x00000000, ABSOLUTE)
        Base Addr    Size         Type   Attr      Idx    E Section Name        Object
        0x0080ce28   0x00000000   Zero   RW            1    ARM_LIB_HEAP.bss    anon$$obj.o
        ```
    - 可用以下公式算出RAM使用为```59.45 KB```：
        ```
        RAM_USED = ARM_LIB_HEAP_START_ADDR - RAM_BASE_ADDR + SYSTEM_HEAP_SIZE + SYSTEM_STACK_SIZE
        // 假设ARM_LIB_HEAP_START_ADDR=0x0080ce28，SYSTEM_HEAP_SIZE = 0KB, SYSTEM_STACK_SIZE= 8KB
        RAM_USED = 0x0080ce28 - 0x00800000 + 0 * 1024 + 8 * 1024 = 60872 B = 59.45 KB
        ```
- GR551x固件大小
    - 有多种获得固件大小的方法，以下是两种比较常用的方法：
        - 第一种是最直接的方法，在```\Keil_5\Listings```目录找到.bin文件，直接查看文件的大小。
        - 第二种方法是分析map文件：
            - 在```\Keil_5\Listings```目录找到map文件。
            - 用文本编辑器打开map文件并找到```Total ROM Size (Code + RO Data + RW Data)```，如下所示，固件大小为```82.21 KB```：
                ```
                Total RO  Size (Code + RO Data)                82952 (  81.01kB)
                Total RW  Size (RW Data + ZI Data)             30192 (  29.48kB)
                Total ROM Size (Code + RO Data + RW Data)      84184 (  82.21kB)
                ```
##### 2.2.2 GR533x （SDK V1.0.5，用户未修改链接脚本）
- GR533x RAM使用情况
    - 在```\Keil_5\Listings```目录找到map文件。
    - 用文本编辑器打开map文件，找到```FPB_TABLE```的起始地址并记为```FPB_TABLE_START_ADDR```，如下所示```FPB_TABLE```的起始地址为```0x20008500```：
        ```
        Execution Region FPB_TABLE (Base: 0x20008500, Size: 0x00000040, Max: 0x00000050, ABSOLUTE)
        Base Addr    Size         Type   Attr      Idx    E Section Name        Object
        0x20008500   0x00000040   Data   RW         2700    FPB                 ble_sdk.lib(sdk_fpb_mgmt.o)
        ```
    - 找到```ARM_LIB_STACK```的起始地址并记为```ARM_LIB_STACK_START_ADDR```，如下所示```ARM_LIB_STACK```的起始地址为```0x20013b80```：
        ```
        Execution Region ARM_LIB_STACK (Base: 0x20013b80, Size: 0x00002000, Max: 0x00002000, ABSOLUTE)
        Base Addr    Size         Type   Attr      Idx    E Section Name        Object
        0x20013b80   0x00002000   Zero   RW            2    ARM_LIB_STACK.bss   anon$$obj.o
        ```
    - 可用以下公式算出RAM使用为```50.44 KB```：
        ```
        // RAM_END_ADDR - ARM_LIB_STACK_START_ADDR，是因为System stack后面会分配一段RAM区域给BLE Controller用
        RAM_USED = FPB_TABLE_START_ADDR - RAM_BASE_ADDR + FPB_TABLE_SIZE + SYSTEM_HEAP_SIZE + (RAM_END_ADDR - ARM_LIB_STACK_START_ADDR)
        // 假设FPB_TABLE_START_ADDR=0x20008500，SYSTEM_HEAP_SIZE = 0KB, ARM_LIB_STACK_START_ADDR=0x20013b80
        RAM_USED = 0x20008500 - 0x20000000 + 0x40 + 0 * 1024 + (0x20018000 - 0x20013b80) = 51648 B = 50.44 KB
        ```
- GR33xx固件大小
  
    -  GR533x的固件大小可参考```GR551x 固件大小```的计算方法。

