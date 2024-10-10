# QSPI常见问题



## 1. QSPI支持的最大频率是多少？

-   QSPI模块支持的最大频率是系统最高频率的二分之一，支持的分频系数为2～65535之间的偶数，不支持奇数分频。
- 各款芯片QSPI模块的最大频率支持如下：

  - GR551x全系列芯片最高主频为64 MHz，QSPI的最大工作频率为 32 MHz，时钟源为系统时钟。

  - GR5525全系列芯片最高主频为96 MHz，QSPI的最大工作频率为 48 MHz，时钟源为外设时钟。

  - GR5526全系列芯片最高主频为96 MHz，QSPI的最大工作频率为 48 MHz，时钟源为外设时钟。

  - GR533x全系列芯片最高主频为64 MHz，QSPI的最大工作频率为 32 MHz，时钟源为外设时钟。



## 2. QSPI工作模式介绍

-   按照QSPI工作时需要的数据线划分，QSPI可配置工作在SPI、Dual SPI、Quad SPI模式下；其中SPI模式和SPI Master模块的工作模式类似。
-    QSPI模块下，Dual SPI和Quad SPI模式又被称为Enhanced SPI模式。GR5525和GR5526扩展了Enhanced SPI模式的能力，支持Memory Map，可将挂载到QSPI接口的NOR Flash和QSPI PSRAM存储设备映射到系统的总线地址空间，使用Memory Map模式进行访问。而传统的基于API访问外设的方式，称作寄存器工作模式。
-   关于工作模式更详细的介绍，请参考《[GR5525刷屏指南](https://docs.goodix.com/zh/online/detail/display_guide_bl_c/V1.0/c801a35abdf0f5deb034f4c5cd1ece44)》/《[GR5526刷屏指南](https://docs.goodix.com/zh/online/detail/display_refresh_guide_bl_b/V1.0/aee091969c2eaa366cb279984812bb42)》。



## 3. 使用Memory Map模式访问外部Flash时，数据端序异常是什么原因？

-   对于GR5525和GR5526芯片，对Memory Map方式增加了灵活端序模式，允许用户根据自己的需要，配置数据的读出端序。这种情况就是期望的数据端序和配置的端序不匹配导致的。请参考《[GR5525刷屏指南](https://docs.goodix.com/zh/online/detail/display_guide_bl_c/V1.0/c801a35abdf0f5deb034f4c5cd1ece44)》/《[GR5526刷屏指南](https://docs.goodix.com/zh/online/detail/display_refresh_guide_bl_b/V1.0/aee091969c2eaa366cb279984812bb42)》关于QSPI Memory Map模式下数据端序配置的描述。在访问数据前，使用驱动接口app_qspi_mmap_set_endian_mode配置期望的数据端序。



## 4. 使用传统API接口（非Memory Map方式）读取外部Flash，数据和期望的数据端序不一致，该如何处理？

-   请参考《[GR5525刷屏指南](https://docs.goodix.com/zh/online/detail/display_guide_bl_c/V1.0/c801a35abdf0f5deb034f4c5cd1ece44)》/《[GR5526刷屏指南](https://docs.goodix.com/zh/online/detail/display_refresh_guide_bl_b/V1.0/aee091969c2eaa366cb279984812bb42)》关于读写端序的描述，应该是数据的写入和读出使用了不匹配的传输宽度导致的逆序。请尝试调整DMA数据传输宽度来修改数据端序行为。比如：
    
    -   使用8 bit传输宽度模式导致2字节的逆序行为，可以尝试将传输宽度调整为16 bit（或反之）。
    
        


## 5. 如何支持QSPI模块使用Memory Map模式，访问大于16 MB 4字节地址的Flash？

-   app_qspi驱动预置了Flash常用3字节地址（最大寻址范围16 MB）的读取指令，如果用户需要扩展4字节的读取指令，可参考下述定义进行。以GD25Q256E芯片的EBH指令为例：

    ![image-20240110140833395](../../../_images/qspi_4B_EBH.png)

-   时序格式为：

    -   指令EBH长度1字节，通过单线模式发送。
    -   地址长度4字节，通过Quad模式发送。
    -   模式位占用2个时钟，但不需要启用，归为Dummy域。
    -   Dummy域4个时钟加模式位占用的2个时钟，共6个时钟。
    -   其他为数据域。

-   用户扩展定义指令的方法：

    -   在_app_qspi.h_枚举类型app_qspi_flash_mmap_rd_cmd_e下添加自定义枚举值**FLASH_MMAP_CMD_4READ_EBH_32**：

        ```c
        typedef enum {
            FLASH_MMAP_CMD_DREAD_3BH         = 0x00,    /**< 3BH in Dual */
            FLASH_MMAP_CMD_2READ_BBH         = 0x01,    /**< BBH in 2Read */
            FLASH_MMAP_CMD_2READ_BBH_SIOO    = 0x02,    /**< BBH in 2Read with SIOO mode */
        
            FLASH_MMAP_CMD_QREAD_6BH         = 0x03,    /**< 6BH in QRead */
            FLASH_MMAP_CMD_4READ_EBH         = 0x04,    /**< EBH in 4Read */
            FLASH_MMAP_CMD_4READ_EBH_SIOO    = 0x05,    /**< EBH in 4Read with SIOO mode */
            FLASH_MMAP_CMD_4READ_EBH_32      = 0x06,    /**< ECH in 4Read with 32 bits address mode */
            FLASH_MMAP_CMD_READ_MAX,
        } app_qspi_flash_mmap_rd_cmd_e;
        
        ```

    -   在_app_qspi.c_文件结构体变量增加指令定义，注意添加位置和枚举值的索引值保持一致。

        ```
        const qspi_memorymapped_t g_flash_typical_mmap_read_cmd[FLASH_MMAP_CMD_READ_MAX] =
        {
            //…},
            [FLASH_MMAP_CMD_4READ_ECH_32] = {
                .x_endian_mode                  = QSPI_CONCURRENT_XIP_ENDIAN_MODE_0,
                .x_prefetch_en                  = QSPI_CONCURRENT_XIP_PREFETCH_DISABLE,
                .x_continous_xfer_en            = QSPI_CONCURRENT_XIP_CONT_XFER_DISABLE,
                .x_instruction_en               = QSPI_CONCURRENT_XIP_INST_ENABLE,
                .x_instruction_size             = QSPI_CONCURRENT_XIP_INSTSIZE_8BIT,
                .x_address_size                 = QSPI_CONCURRENT_XIP_ADDRSIZE_32BIT,
                .x_inst_addr_transfer_format    = QSPI_CONCURRENT_XIP_INST_IN_SPI_ADDR_IN_SPIFRF,
                .x_mode_bits_en                 = QSPI_CONCURRENT_XIP_MODE_BITS_DISABLE,
                .x_mode_bits_length             = QSPI_CONCURRENT_XIP_MBL_8,
                .x_mode_bits_data               = 0x00,
                .x_dummy_cycles                 = 6,
                .x_continous_xfer_toc           = 0,
                .x_sioo_mode                    = QSPI_CONCURRENT_XIP_INST_SENT_EVERY_ACCESS,
                .x_data_frame_format            = QSPI_CONCURRENT_XIP_FRF_QUAD_SPI,
                .x_instruction                  = 0xEB,
            }
        };
        
        ```

    -   在Flash的Memory Map模式初始化时，读指令引用上述定义的指令进行初始化即可。
    
        


## 6. 使用SDK的QSPI示例工程访问Flash失败，为什么？

-   注意检查示例工程的QSPI实例配置和实际硬件Flash连接是否匹配。

-   SDK提供的示例工程适配了常见的Flash驱动。如果测试的Flash不是适配的Flash型号，请检查Flash的Datasheet，是否和参考驱动兼容；如果不兼容，请自行进行适配。
-   如果硬件环境恶劣，比如飞线等场景，尝试降低Flash通讯频率。
-   检查驱动配置的时钟模式是否和Flash支持的时钟模式匹配。
-   此外，还可以使用逻辑分析仪抓取访问Flash时序信号进行分析。



## 7. QSPI外设有哪些参考程序？

-   工程${SDK}/projects/peripheral/qspi/app_qspi提供了一个app_qspi驱动访问NOR Flash的应用参考，可以在SDK配套的SK板运行。用户可通过这个示例工程，了解QSPI APP接口的初步使用。
-   此外，针对GR5525和GR5526，在路径${SDK}/components/drivers_ext/qspi_device下提供了如下QSPI外设的驱动参考。用户可根据产品的具体情况进行参考和二次开发。
    -   amo139_display_454.c/.h：基于型号 FLS-AMO139WV334 , 分辨率454x54, 驱动IC  SH8601A 的显示屏开发. 
    -   qspi_flash.c/.h：兼容PUYA、XTX等多款市面常用NOR Flash的驱动参考
    -   qspi_nand_flash.c/.h：基于NAND Flash DOSILICON.DS35的驱动参考
    -   qspi_psram.c/.h：基于APMemory QSPI接口的PSRAM驱动参考
    -   qspi_screen_390.c/.h：基于鑫世界RM69330的显示屏驱动参考，适配了390p和454p分辨率


