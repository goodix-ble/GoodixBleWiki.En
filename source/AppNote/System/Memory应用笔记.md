## Memory application notes



### 1. Introduction to Basic Functions



#### 1.1 Memory Resources Overview

- The Memory resources provided by GR5xx are as follows (see the corresponding chip Datasheet for more details):

| SoC    | SRAM (Up to KB)  | Flash (Up to KB) |
| ------ | ---------------- | ---------------- |
| GR533x | 96               | 512              |
| GR5513 | 128              | 512              |
| GR5515 | 256              | 1024             |
| GR5525 | 256              | 1024             |
| GR5526 | 512              | 1024             |

#### 1.2 Memory Layout
- The SRAM and Flash layout varies from chip to chip, please refer to the corresponding developer's guide for details, e.g. for the Flash and SRAM layout of GR551x, please refer to [GR551x开发者指南](https://docs.goodix.com/zh/online/gr551x_develop_guide/V2.7).

#### 1.3 Typical Application Resource Usage and User Available Resources
- GR5515 typical application resource usage and user available resources (based on SDK V2.0.1, ARMCC V5.06 update 1(build 61), -O2, System stack 8KB, System heap 0KB. The results may vary with different SDK versions, SDK examples, compilers and optimization options, and the actual compilation results shall prevail). (Results may vary with different SDK versions, SDK examples, compilers and optimization options:)


| Role               | Example                  | ADV Number  | SCAN Number | Bluetooth LE Connection Number | Bluetooth LE Bond Number | System Used SRAM (KB) | System Used Flash (KB) | Customer Available SRAM (KB) | Customer Available Flash (KB) |
| ------------------ | ------------------------ | ----------- | ----------- | --------------------- | --------------- | -------------------- | --------------------- | --------------------------- | ---------------------------------- |
| Central            |  ble_app_cts_c           |    0        |    1        |            1          |        1        |           51         |          92           |             205             |                932                 |
| Central            |  ble_app_cts_c           |    0        |    1        |            4          |        4        |           65         |          92           |             191             |                932                 |
| Peripheral         |  ble_app_cts             |    1        |    0        |            1          |        1        |           48         |          83           |             208             |                941                 |
| Peripheral         |  ble_app_cts             |    1       |    0       |            4          |        4        |           60         |          83           |             196             |                941                 |
| Central+Peripheral | ble_app_hrs_rscs_relay   |    1        |    1        |            4          |        4        |           66         |          99           |             190             |                925                 |

- GR533x typical application resource usage and user available resources (based on SDK V1.0.5, ARMCC V5.06 update 1(build 61), -O2, System stack 4KB, System heap 0KB. Results may vary with different SDK versions, SDK examples, compilers, and optimization options. (Results may vary with different SDK versions, SDK examples, compilers and optimization options:)

| Role               | Example                | GATTC Support | GATTS Support | Master Support | Slave Support | ADV Number | SCAN Number | Bluetooth LE Connection Number | Bluetooth LE Bond Number | System Used SRAM (KB) | System Used Flash (KB) | Customer Available SRAM (KB) | Customer Available Flash (KB) |
| ------------------ | ---------------------- | ------------- | ------------- | -------------- | ------------- | ---------- | ----------- | ------------------------------ | ------------------------ | --------------------- | ---------------------- | ---------------------------- | ----------------------------- |
| Central            | ble_app_cts_c          | 1             | 0             | 1              | 0             | 0          | 1           | 1                              | 1                        | 42                    | 113                    | 54                           | 399                           |
| Central            | ble_app_cts_c          | 1             | 0             | 1              | 0             | 0          | 1           | 4                              | 4                        | 48                    | 113                    | 48                           | 399                           |
| Peripheral         | ble_app_cts            | 0             | 1             | 0              | 1             | 1          | 0           | 1                              | 1                        | 41                    | 106                    | 55                           | 406                           |
| Peripheral         | ble_app_cts            | 0             | 1             | 0              | 1             | 1          | 0           | 4                              | 4                        | 47                    | 106                    | 49                           | 406                           |
| Central+Peripheral | ble_app_hrs_rscs_relay | 1             | 1             | 1              | 1             | 1          | 1           | 4                              | 4                        | 50                    | 122                    | 46                           | 390                           |




### 2. Application Notes

#### 2.1 Link Script Application Guide (ARMCC Scatter File as an example, other link scripts are similar)
The Scatter file varies slightly from chip to chip, the following are the individual execution fields of the Scatter file for the GR551x, other chips are similar:
- LR_FLASH
    - Firmware load field, specify the start address of the firmware (APP_CODE_RUN_ADDR) and the maximum size of the firmware (FLASH_SIZE).
- FLASH_CODE
    - Firmware code execution domain specifying the start address of the firmware code segment (APP_CODE_RUN_ADDR) and the maximum size of the code segment (APP_MAX_CODE_SIZE).
- TINY_RAM_SPACE
    - The RAM area where the SDK stores the code internally, the user does not need to pay attention to this area.
- FPB
    - The RAM area inside the SDK where the FPB data is stored, so the user does not need to pay attention to this area.
- RAM_RW
    - RAM_RW Area for global variables that have been initialized by the program and have non-zero data.
- RAM_CODE
    - The RAM area where the SDK and user code are stored.
    - The code in RAM_CODE can be divided into two categories:
        - One is that some functions must be resident in the memory due to the code related to Flash operation, which will cause crash if it is put into Flash.
        - Second, functions executed in RAM can save time because they do not need to be re-read from Flash when the Cache is not hit each time the function is called, so functions that require execution time can be executed in RAM to increase execution efficiency, and functions that need to be executed frequently, such as sleep and wakeup, can be executed in RAM in the SDK to greatly reduce execution time, which in turn saves power consumption.
- RAM_RESERVE
    - RAM_RESERVE is an execution field in which RAM is not initialized.
- RAM_ZI
    - The area of RAM that holds the uninitialized global variables of the program and the global variables that are initialized to zero.
- ARM_LIB_HEAP
    - C library memory dynamic allocation of Heap (such as malloc and other functions), C library malloc and other functions due to the lack of thread-safe, it is not recommended that users use the C library to provide memory dynamic allocation function (such as malloc) and internal with malloc function of the C library function (such as strdup). If the user is bare-metal development, app_memory module can be used; if using RTOS, it is recommended to use the memory allocation function of RTOS.
- ARM_LIB_STACK
    - System stack execution field. Users can adjust the stack size according to the actual situation, the stack space of GR551x can not be less than 8 KB, and the stack space of GR531x can not be less than 4 KB.

#### 2.2 Calculate the RAM and firmware size used by the program (ARMCC compiler, other compilers can refer to the following method)

##### 2.2.1 GR551x (SDK V2.0.1, user unmodified link script)
- GR551x RAM usage
    - Find the map file in the ```\Keil_5\Listings``` directory.
    - Open the map file with a text editor and find the start address of ```ARM_LIB_HEAP``` and note it as ARM_LIB_HEAP_START_ADDR  as shown below  ARM_LIB_HEAP  starts at ``0x0080ce28``:
        ```
        Execution Region ARM_LIB_HEAP (Base: 0x0080ce28, Size: 0x00000000, Max: 0x00000000, ABSOLUTE)
        Base Addr Size Type Attr Idx E Section Name Object
        0x0080ce28 0x00000000 Zero RW 1 ARM_LIB_HEAP.bss anon$$obj.o
        ```
    - The following formula can be used to calculate the RAM usage as ```59.45 KB```:
        ```c
        RAM_USED = ARM_LIB_HEAP_START_ADDR - RAM_BASE_ADDR + SYSTEM_HEAP_SIZE + SYSTEM_STACK_SIZE
        // Assume ARM_LIB_HEAP_START_ADDR = 0x0080ce28, SYSTEM_HEAP_SIZE = 0KB, SYSTEM_STACK_SIZE= 8KB.
        RAM_USED = 0x0080ce28 - 0x00800000 + 0 * 1024 + 8 * 1024 = 60872 B = 59.45 KB
        
        ```
- GR551x Firmware Size
    - There are multiple ways to get the firmware size, here are two of the more common methods:
        - The first is the most direct method, find the .bin file in the ```\Keil_5\Listings``` directory and check the file size directly.
        - The second method is to analyze the map file:
            - Find the map file in the ```\Keil_5\Listings``` directory.
            - Open the map file with a text editor and find ```Total ROM Size (Code + RO Data + RW Data)``` as shown below, the firmware size is ``82.21 KB``:
                ```
                Total RO Size (Code + RO Data) 82952 ( 81.01kB)
                Total RW Size (RW Data + ZI Data) 30192 ( 29.48kB)
                Total ROM Size (Code + RO Data + RW Data) 84184 ( 82.21kB)
                ```
##### 2.2.2 GR533x (SDK V1.0.5, user unmodified link script)
- GR533x RAM usage
    - Find the map file in the ```\Keil_5\Listings``` directory.
    - Open the map file with a text editor and locate the start address of ```FPB_TABLE``` and note it as ``FPB_TABLE_START_ADDR``` as shown below ```FPB_TABLE``` starts at ``0x20008500``:
        ```
        Execution Region FPB_TABLE (Base: 0x20008500, Size: 0x00000040, Max: 0x00000050, ABSOLUTE)
        Base Addr Size Type Attr Idx E Section Name Object
        0x20008500 0x00000040 Data RW 2700 FPB ble_sdk.lib(sdk_fpb_mgmt.o)
        ```
    - Find the start address of ```ARM_LIB_STACK`` and write it down as ```ARM_LIB_STACK_START_ADDR`` as shown below ```ARM_LIB_STACK`` starts at ``0x20013b80``:
        ```
        Execution Region ARM_LIB_STACK (Base: 0x20013b80, Size: 0x00002000, Max: 0x00002000, ABSOLUTE)
        Base Addr Size Type Attr Idx E Section Name Object
        0x20013b80 0x00002000 Zero RW 2 ARM_LIB_STACK.bss anon$$obj.o
        ```
    - The following formula can be used to calculate the RAM usage as ```50.44 KB``:
        ```
        // RAM_END_ADDR - ARM_LIB_STACK_START_ADDR because the System stack allocates a section of RAM behind it for the BLE Controller.
        RAM_USED = FPB_TABLE_START_ADDR - RAM_BASE_ADDR + FPB_TABLE_SIZE + SYSTEM_HEAP_SIZE + (RAM_END_ADDR - ARM_LIB_STACK_START_ADDR)
        // Assume FPB_TABLE_START_ADDR = 0x20008500, SYSTEM_HEAP_SIZE = 0KB, ARM_LIB_STACK_START_ADDR = 0x20013b80
        RAM_USED = 0x20008500 - 0x20000000 + 0x40 + 0 * 1024 + (0x20018000 - 0x20013b80) = 51648 B = 50.44 KB
        ``
        ```
- GR33xx firmware size
  
    - The GR533x firmware size can be calculated by referring to the ``GR551x firmware size``.



