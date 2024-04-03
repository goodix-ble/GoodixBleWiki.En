# QSPI常见问题



## 1. QSPI支持的最大频率是多少?

-   QSPI 模块支持的最大频率是系统最高频率的二分之一, 支持的分频系数为 2 ~ 65535 之间的偶数, 不支持奇数分频.
-   各款芯片QSPI模块的最大频率支持如下:
-   GR551x 全系列芯片最高主频为64MHz, QSPI的最大工作频率为 32MHz, 时钟源为系统时钟
-   GR5525 全系列芯片最高主频为96MHz, QSPI的最大工作频率为 48MHz, 时钟源为外设时钟
-   GR5526 全系列芯片最高主频为96MHz, QSPI的最大工作频率为 48MHz, 时钟源为外设时钟 
-   GR533x 全系列芯片最高主频为64MHz, QSPI的最大工作频率为 32MHz, 时钟源为外设时钟



## 2. QSPI的工作模式介绍.

-   按照QSPI工作时候需要的数据线划分, QSPI 可配置工作在 SPI 、Dual SPI、Quad SPI模式下；其中 SPI模式和SPI Master模块的工作模式类似
-    QSPI模块下, Dual SPI 和Quad SPI模式又被称为 Enhanced SPI模式. GR5525和GR5526扩展了Enhanced SPI模式的能力. 支持了Memory Map 能力, 支持将挂载到 QSPI接口的 Nor Flash 和 QSPI PSRAM 存储设备映射到系统的总线地址空间, 使用 Memory Map模式进行访问. 而传统的基于API 访问外设的方式, 称作寄存器工作模式.
-   关于 工作模式更详细的介绍, 请参考文档: [GR552x刷屏指南](https://docs.goodix.com/zh/online/detail/display_refresh_guide_bl_b/V1.0/aee091969c2eaa366cb279984812bb42) 



## 3. 使用Memory Map模式访问访问外部Flash时, 数据端序异常是什么原因? 

-   对于GR5525 & GR5526 芯片,  对Memory Map方式增加了灵活端序模式, 允许用户根据自己的需要, 配置数据的读出端序. 这种情况就是期望的数据端序和配置的端序不匹配导致的, 请参考文档 [GR552x刷屏指南](https://docs.goodix.com/zh/online/detail/display_refresh_guide_bl_b/V1.0/aee091969c2eaa366cb279984812bb42)  关于QSPI Memory Map模式下数据端序配置的描述. 在访问数据前, 使用驱动接口 app_qspi_mmap_set_endian_mode 配置期望的数据端序.



## 4. 使用传统API接口(非Memory Map方式) 读取外部Flash, 数据和期望的数据端序不一致, 请问怎么处理?

-   请参考文档 [GR552x刷屏指南](https://docs.goodix.com/zh/online/detail/display_refresh_guide_bl_b/V1.0/66d6424af28a73c815b87abfa38a20f6)关于读写端序的描述, 应该是数据的写入和读出使用了不匹配的传输宽度导致的逆序. 请尝试调整 DMA 数据传输宽度来修改数据端序行为. 比如
    
    -   使用 8 bit 传输宽度模式导致2字节的逆序行为, 可以尝试将传输宽度调整为 16 bit (或反之)
    
        


## 5. 如何支持QSPI 模块使用Memory Map模式,访问大于16MB 4字节地址的Flash？

-   app_qspi 驱动预置了flash常用3字节地址(最大寻址范围16MB)的读取指令, 如果用户需要扩展4字节的读取指令. 可参考下述定义进行, 以 GD25Q256E 芯片的 EBH 指令为例:

    ![image-20240110140833395](../../../_images/qspi_4B_EBH.png)

-   时序格式为:

    -   指令 EBH长度1字节, 通过单线模式发送
    -   地址长度4字节, 通过Quad 模式发送
    -   模式位占用 2个 时钟, 但不需要启用. 归为 Dummy 域
    -   Dummy 域4个时钟加模式位占用的2个时钟， 共6个时钟
    -   其他为数据域

-   用户扩展定义指令的方法:

    -   在 app_qspi.h 枚举类型app_qspi_flash_mmap_rd_cmd_e下添加自定义枚举值 **FLASH_MMAP_CMD_4READ_EBH_32** :

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

    -   在 app_qspi.c 文件结构体变量增加指令定义, 注意添加位置和 枚举值的索引值保持一直

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

    -   在Flash 的 Memory Map模式初始化时, 读指令引用上述定义的指令进行初始化即可.
    
        


## 6. 使用SDK的QSPI 示例工程访问Flash失败, 为什么?

-   注意检查 示例工程的QSPI 实例配置和实际硬件Flash 连接是否匹配

-   SDK提供的示例工程适配了常见的Flash 驱动, 如果测试的Flash 不是适配的flash型号,请检查flash的datasheet, 是否和参考驱动兼容, 如果不兼容,请自行进行适配
-   如果硬件环境恶劣, 比如飞线等场景, 尝试降低 Flash 通讯频率
-   检查下驱动配置的时钟模式是否和Flash 支持的时钟模式匹配
-   此外, 还可以使用逻辑分析仪抓取访问 Flash 时序信号分析. 



## 7. QSPI 外设有哪些参考程序?

-   工程  ${SDK}/projects/peripheral/qspi/app_qspi 提供了 app_qspi 驱动访问Nor Flash 的一个应用参考, 可以在SDK 配套的 SK板运行, 用户可以通过这个示例工程, 了解 QSPI APP接口的初步使用.
-   此外, 针对 GR5525和GR5526, 在 路径 ${SDK}/components/drivers_ext/qspi_device 下提供了如下QSPI外设的驱动参考, 用户可以根据产品的具体情况进行参考和二次开发.
    -   amo139_display_454.c/.h : 基于型号 FLS-AMO139WV334 , 分辨率454x54, 驱动IC  SH8601A 的显示屏开发. 
    -   qspi_flash.c/.h : 兼容 PUYA、XTX等多款市面常用Nor Flash的驱动参考
    -   qspi_nand_flash.c/.h : 基于 Nand Flash DOSILICON.DS35 的驱动参考
    -   qspi_psram.c/.h : 基于 APMemory QSPI 接口的PSRAM 驱动参考
    -   qspi_screen_390.c/.h : 基于鑫世界 RM69330 的显示屏驱动参考, 适配了 390p和454p分辨率


​    
​    
​    