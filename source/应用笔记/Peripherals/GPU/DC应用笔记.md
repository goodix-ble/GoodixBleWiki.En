## DC应用笔记



> 说明：
> -   “DC” 在图形化场景下，是指Display Controller（显示控制器）模块，注意跟Direct Current（直流电）概念区分。
> -   “DC” 是GR5526 SoC系列芯片（存在于GR5526VGBIP和GR5526RGNIP封装）扩展的外设，其他芯片系列没有DC。



### 1. 基本功能介绍

显示控制器（Display Controller）主要用于配合GPU使用，将渲染完成的帧缓冲区（FrameBuffer），送至Display进行图形显示，帧缓冲区典型格式包括RGBA8888、RGB565、TSCx等。支持的屏幕接口规范主要为MIPI DBI（Display Bus Interface）Type-C，涵盖的时序协议主要有：

1.  3-Wire SPI

    包含SPI_CS（片选信号）、SPI_SCLK（时钟信号）、SPI_SD（数据输出）三根信号线，其中命令字（Command Word）由9-bit构成，包含1-bit的数据/命令指示位和8-bit的命令字（Command Word）；而数据字（Data Command）由1-bit数据/命令指示位和若干位像素数据位构成。

2.  4-Wire SPI（扩展DCX信号线）
    包含SPI_CS（片选信号）、SPI_SCLK（时钟信号）、SPI_SD（数据输出）和SPI_DC（数据/命令指示信号）4根信号线，其中命令字（Command Word）由8-bit构成，而数据字（Data Command）由若干位像素数据位构成。

3.  Dual SPI
    包含SPI_CS（片选信号）、SPI_SCLK（时钟信号）、SPI_SD（数据输出）和SPI_SD1（数据输出1）4根信号线，命令字（Command Word）一般由SPI_SD线发送而数据由SPI_SD和SPI_SD1共同发送；其中命令字（Command Word）由9-bit构成，包含1-bit的数据/命令指示位和8-bit的命令字（Command Word）；而数据字（Data Command）由1-bit数据/命令指示位和若干位像素数据位构成。

4.  Quad SPI
    包含SPI_CS（片选信号）、SPI_SCLK（时钟信号）、SPI_SD（数据输出）、SPI_SD19（数据输出1）、SPI_SD2（数据输出2）、SPI_SD3（数据输出3）6根信号线，命令类型可以被SPI_SD或所有SPI_SDx传输。时序一般由8-bit命令头、24-bit命令字和若干像素数据组成。



> -   显示控制器内置DMA，用于加速帧数据对送显，同时具备一次性送显一个完整帧数据对能力。
> -   显示控制器（Display Controller）时常缩写为DC，请注意和DC（Direct Current）区分。
>



### 2. 应用笔记

-   DC模块和QSPI2模块复用了主要的IO引脚（CSn、CLK、D0～D3），当屏幕的QSPI信号线挂载在这些I/O下时：
    -   如果Frame Buffer是RGB565非压缩格式，用户可以选择使用QSPI2或者DC模块驱动屏幕。
    -   如果Frame Buffer是TSCx压缩格式，用户只能使用DC模块驱动屏幕。
    -   在使用了GPU的产品工程中，建议用户优先选择DC模块驱动外设屏幕，以便具有更好的兼容性和更好的刷屏带宽。
-   DC的刷屏接口app_graphics_dc_send_single_frame支持同步和异步调用两种模式：
    -   同步调用模式下，CPU会一直等待Frame Buffer刷屏逻辑结束，才会继续执行后续的逻辑。
    -   异步调用模式下，CPU启动Frame Buffer刷屏传输后就会退出接口。因此，需要用户通过回调事件关心接口的调用生命期，防止重入调用和接口刷屏未执行完毕就进行了休眠等其他操作。
    -   同步调用模式一般由用户调试，最终建议使用异步调用模式，可以将任务并行执行，最大化芯片的计算能力并提高刷新帧率。
-   对于DC模块的休眠管理建议：
    -   系统允许休眠时，检查app_graphics_dc_send_single_frame调用完成后，主动调用app_graphics_dc_set_power_state(GDC_POWER_STATE_SLEEP)，允许系统将DC休眠。
    -   系统唤醒后准备刷屏前，可主动调用app_graphics_dc_set_power_state(GDC_POWER_STATE_ACTIVE)，将DC模块唤醒准备工作。
-   对DC模块提供的主要时序接口，在《[GR5526刷屏指南](https://docs.goodix.com/zh/online/display_refresh_guide_bl_b)》中使用图片描述其发送时序特征。使用接口存在疑惑时，可以参阅该文档。
-   DC模块提供了CS Setup Delay（Tcsu，片选建立时延）电气参数的调整，如果外设屏幕要求较大的Tcsu，可以通过初始化结构体app_graphics_dc_params_t的参数tcsu_cycle进行调整。 
-   DC模块刷屏时的Frame Buffer要和GPU使用的Frame Buffer相对应，DC模块具备空中帧格式转换功能，可以将GPU Frame Buffer的帧格式转换为另一个格式发送给屏幕，比如：
    -   GPU采用RGBA8888格式进行Frame渲染，DC可以将目标帧格式设置为RGB565发送给屏幕显示。
    -   GPU采用TSCx格式进行Frame渲染，DC可以将目标帧格式设置为RGB565发送给屏幕显示。
