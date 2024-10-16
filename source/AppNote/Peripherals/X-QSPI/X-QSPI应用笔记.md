## X-QSPI Application Note

### 1. Introduction to Basic Functions
- The "X" in X-QSPI stands for eXecute-in-place, meaning that code can be executed directly from the NOR Flash connected to X-QSPI. In contrast, external QSPI can only be used for data storage and cannot store or execute code. To enable code execution, X-QSPI and external QSPI have functional differences and cannot be used interchangeably.
- To accelerate code hit and execution efficiency, X-QSPI is designed with an instruction cache mechanism, all with sleep retention functionality. The cache sizes for different chips are as follows:
    - GR551x: 8 KB
    - GR5525: 8 KB
    - GR5526: 8 KB
    - GR533x: 8 KB
- Several series of chips offer package models with 1 Mbyte of integrated NOR Flash, which can be used to store code and small amounts of data. When the 1 Mbyte model does not meet product design requirements, the external X-QSPI Flash version of each chip can be used. The external Flash capabilities are as follows:
    - GR551x: Supports up to 16 Mbytes of external X-QSPI Flash space, but only the lower 8 Mbytes support XIP mode. The upper 8 Mbytes require register addressing mode and are used only for data storage, not for code storage.
    - GR5525: Supports up to 16 Mbytes of external X-QSPI Flash space, all supporting XIP mode.
    - GR5526: No chip package supports external X-QSPI Flash.
    - GR533x: Supports up to 16 Mbytes of external X-QSPI Flash space, all supporting XIP mode.
- The main frequency and maximum operating frequency of X-QSPI for different chips are as follows:
    - GR551x: 64 MHz / 64 MHz
    - GR5525: 96 MHz / 64 MHz
    - GR5526: 96 MHz / 64 MHz
    - GR533x: 64 MHz / 64 MHz

### 2. Application Notes
- During program execution with X-QSPI, writing to Flash will disable the system's global interrupts, which affects the timing logic of Bluetooth LE. Refer to the **Application Note** section "Handling Conflicts Between Bluetooth LE and Flash Code Execution" for program optimization in such scenarios.
- The GR5515I0NDA uses external X-QSPI Flash. Since Flash from different manufacturers and models have varying functionalities and usage limitations, users can refer to the "[GR5515I0NDA External Flash Selection Guide](https://docs.goodix.com/zh/online/detail/gr5515_flash_selection_guide/V1.4/44637c95d0d76dcb98bf8080fdd6f8bf)" to make appropriate selections based on the actual product situation. The guide provides instructions and electrical compatibility requirements for external Flash expansion and recommends a list of suggested selections, which can be downloaded from the official website. Other chip series can also use this document as a reference.
- If users need to implement special Flash instructions, they should pay attention to the conversion between XIP and QSPI states. Refer to the example code in the SDK\\components\\libraries\\hal_flash\\hal_exflash_user_operation.c file to implement it themselves. Since code on Flash cannot be executed during Flash operations, ensure to add the SECTION_RAM_CODE macro before the operation functions to execute them in SRAM.