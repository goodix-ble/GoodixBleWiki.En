## OSPI PSRAM应用笔记



-   说明：OSPI PSRAM是GR5526 SoC系列芯片（存在于GR5526VGBIP和GR5526RGNIP封装）扩展的外设，其他芯片系列没有OSPI PSRAM。



### 1. PSRAM的总线地址空间布局及管理

-   GR5526中，512 KB SRAM其中一组总线地址空间映射范围为【0x30000000, 0x3007FFFF】，而64Mbit OSPI PSRAM的总线地址空间范围映射为【0x30080000, 0x3087FFFF】，他们在总线上可被连续寻址。

![](../../../_images/gpu/psram_1.png)  

 

-   在实际的应用设计中，SRAM区域会被RAM Code、RW+ZI、系统堆栈、应用层逻辑及算法优先占用。一般情况下512 KB SRAM不会占用完，剩余的SRAM和PSRAM一并构成一个大块的Heap区域。用户可将其用于显示存储或数据存储等。典型的内部分布结构如下：

![](../../../_images/gpu/psram_2.png) 

 

-   为了方便应用工程管理上述内部布局，请在使用PSRAM版本SoC的应用工程中，采用专门的Scatter布局文件（Keil版本：${SDK}\platform\soc\linker\keil\flash_scatter_graphics.sct）。
-   为方便管理剩余SRAM及PSRAM组成的大块数据空间，SDK提供了专用的Heap管理驱动文件app_graphics_mem.c和app_graphics_mem.h。

-   堆管理文件位于${SDK}\components\libraries\app_graphics_mem，注册并初始化数据区域的基地址和数据块大小后，即可使用app_graphics_mem_malloc和app_graphics_mem_free进行数据块的申请和释放使用。

-   此堆管理驱动的堆节点和数据块实现了分离，堆节点始终存放在SRAM区域，可实现休眠下的Retention。

 

### 2. PSRAM的初始化和使用

-   PSRAM的初始化很简单，调用如下代码即可。接口会同时将OSPI模块和PSRAM设备初始化到工作状态。

    ```
    app_graphics_ospi_params_t params = PSRAM_INIT_PARAMS_Default;
    app_graphics_ospi_init(&params);  
    ```

-   确保编译器引用的分散加载文件为：${SDK}\platform\soc\linker\keil\flash_scatter_graphics.sct。

-   调用如下代码，将剩余SRAM和PSRAM组成的区域注册到Heap管理器。

    ```c
    mem_pwr_mgmt_mode_set(MEM_POWER_FULL_MODE);
    app_graphics_mem_init((void*)GFX_MEM_BASE, GFX_MEM_SIZE);  
    ```

-   接下来即可通过app_graphics_mem_malloc和app_graphics_mem_free接口使用这片堆区域。



### 3. PSRAM的工作模式

 

OSPI PSRAM设计了2种工作模式：Active和Deep-Sleep。

-   Active模式：PSRAM在Active模式随时可被访问，数据会一直保持住。当PSRAM正被访问时，根据访问强度，功耗约为2 mA ~ 5 mA级别；当PSRAM在Active下保持待机模式（Standby），功耗约为66 μA @ 20℃。

-   Deep-Sleep模式：当系统休眠且不需要保持数据时，可将PSRAM设备设置为Deep_Sleep模式。在Deep_Sleep模式下，PSRAM设备会被断电，工作电流接近 0 μA。

PSRAM驱动提供了工作模式切换接口，允许用户根据应用需要，切换PSRAM的工作模式。目前支持的模式为Active和Deep-Sleep模式。

 

### 4. PSRAM的休眠策略

由于系统休眠框架的设计，PSRAM设备在裸机环境下和OS环境下的休眠策略存在一些差异。

-   裸机模式下，系统休眠由用户负责管理。

-   OS模式下，以FreeRTOS为例，会在OS的移植层设计系统的休眠策略。

上述差异导致两种环境下的PSRAM模式使用存在一些差异。



#### 4.1 裸机环境下的休眠策略



![](../../../_images/gpu/psram_3.png) 

-   系统初始化时，将OSPI PSRAM初始化到工作状态。

-   如果初始化完成后，短期不会使用PSRAM，可以调用接口将PSRAM设置为Deep-Sleep。

-   系统休眠前，会调用模块的配置保存接口，将模块的寄存器配置保存到Retention SRAM区域；但驱动上没有提供OSPI模块的寄存器保持接口。

-   系统休眠，由于没有提供OSPI模块的寄存器保持接口，在休眠期间，OSPI模块配置会丢失。

-   系统唤醒时，会调用模块的配置恢复接口，将模块在休眠前保存到Retention SRAM区域的配置恢复到寄存器。驱动上没有设计寄存器恢复接口， 因此这里调用OSPI配置接口将OSPI重新配置一次（实测时间几 μs，可以接受）。

    由此可以看出，在裸机环境下，系统休眠策略集成了对OSPI模块的管理，但没有集成对PSRAM状态的管理，因为PSRAM由于功耗很大，休眠/唤醒耗时也比较长，需要跟应用层的业务逻辑强相关设计。

 

对于应用层而言：

1.  在系统初始化时，调用初始化接口。
2.  在PSRAM可以掉电休眠时，调用app_graphics_ospi_set_power_state(OSPI_STATE_DEEP_SLEEP)使PSRAM休眠掉电。
3.  在PSRAM需要重新工作时，调用app_graphics_ospi_set_power_state(OSPI_STATE_ACTIVE)恢复PSRAM状态。
4.  如果某个阶段需要PSRAM保持数据，在设置Active后，不调用休眠接口即可，但此期间会产生额外的功耗。



#### 4.2 RTOS环境下休眠策略

可参考FreeRTOS工程，系统已集成OS环境下的PSRAM状态管理。

