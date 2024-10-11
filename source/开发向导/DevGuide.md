# Goodix BLE产品开发向导



## 1. 信息列表

当用户准备了解或基于Goodix Bluetooth LE SoC进行产品设计/开发时，需要先获取和找到如下信息（包括但不限于）：

- 芯片产品信息：了解芯片基本信息，进行芯片选型。
- 芯片SDK包：获取芯片的软件开发包，深入学习并熟悉源码和示例工程。
- 芯片及SK开发板：获取采购芯片和开发板的渠道，以便于产品硬件设计前进行功能验证和先期软件设计。
- 芯片开发工具：下载和获取所有需要用到的开发软件、工具。
- 芯片开发文档资料：查看并下载芯片Datasheet、硬件设计指南、SDK开发者指南，以及各种软件或工程的使用说明等。
- 芯片的产品方案资料：获取应用方案的参考资料，包括方案相关的软件和文档资料等。
- 技术支持服务：提前获取Goodix和代理可提供的技术支持服务和技术支持渠道。



## 2. 获取芯片产品信息

目前，Goodix推出了覆盖高端、中端和入门级市场的Bluetooth LE SoC系列。

- [Goodix Bluetooth LE SoC选型表](https://www.goodix.com/zh/down/resource/Goodix_Bluetooth_Chipset_Selection_Guide?objectId=5&objectType=design_resource&version=64)

![](../_images/goodi_ble_chipset_select_guide.png)

## 3. 获取芯片SDK开发包

| Bluetooth LE SoC | SDK下载地址                                        | 说明           |
| ---------------- | -------------------------------------------------- | -------------- |
| GR551x           | https://www.goodix.com/zh/software_tool/gr551x_sdk | 请下载最新版本 |
| GR5525           | https://www.goodix.com/zh/software_tool/gr5525_sdk | 请下载最新版本 |
| GR5526           | https://www.goodix.com/zh/software_tool/gr5526_sdk | 请下载最新版本 |
| GR533x           | https://www.goodix.com/zh/software_tool/gr533x_sdk | 请下载最新版本 |



## 4. 获取芯片及开发板

### 4.1 企业用户

请联系代理采购各系列芯片及相应的开发板，也可在以下淘宝链接中获取（或搜索利尔达商城，输入开发板名称选购）。
- SK板或小系统板：用于软件功能的验证和预开发。
  - [GR5331-SK-BASIC（淘宝链接）](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.29.44e37824v9pK8y&id=775605003005&skuId=5473168402830)
  - [GR5526-SK-BASIC](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.21.44e37824v9pK8y&id=757015248383)
  - [GR5525-SK-BASIC](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.33.44e37824v9pK8y&id=775644909891&skuId=5302971608278)
  - [GR5515-SK-BASIC-Rev.C](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.31.44e37824v9pK8y&id=775641073847&skuId=5476038335715)


- PPK板：用于功耗测试评估。
  - 采购后向代理索取

- PLT板：用于产线固件下载。
  - [PLT-LITE-GR55xx（淘宝链接）](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.23.44e37824v9pK8y&id=757604846504&skuId=5222694048026)




### 4.2 个人及社区用户

个人用户采购渠道正在积极建设中，可以加入社区群（QQ群号: 168552615）实时关注。



## 5. 获取芯片开发工具

Goodix为蓝牙产品提供开发下载、DFU、产测等多流程所需的软件。

### 5.1 标准开发软件

Goodix蓝牙全系列芯片均默认支持Keil/ARMCC编译工具链，也提供了GCC等其他构建方式，这类软件为标准开发软件，可以通过对应的软件供应商官网进行下载。

一些常用的标准软件如下所列：

| 软件   | 描述                    | 网站                                                         |
| ------ | ----------------------- | ------------------------------------------------------------ |
| Keil   | ARMCC IDE工具           | www.keil.com                                                 |
| J-Link | SWD 调试软件            | https://www.segger.com/downloads/jlink/                      |
| Ozone  | 一款SEGGER出品的调试器  | https://www.segger.com/products/development-tools/ozone-j-link-debugger/ |
| GCC    | ARM none eabi gcc编译器 | https://developer.arm.com/downloads                          |



### 5.2 Goodix开发工具合集

| 软件 |类型| 说明 | 下载地址 | 适用SoC |
| ---- | ---- | ---- | -------- | ------- |
| GProgrammer | 程序资源烧写及配置工具 | 一款支持Bluetooth LE全系列芯片的固件烧录工具，用于开发调试，支持固件下载、Flash读写、eFuse烧写、固件加密加签等功能。在量产阶段，Bluetooth LE系列芯片产品的批量烧录测试，可采用PLT Lite和GRPLT Lite配置工具进行批量烧录测试 | https://www.goodix.com/zh/software_tool/gprogrammer_ble | Bluetooth LE全系SoC |
| GRToolbox | 移动端开发验证App | 一款专为汇顶科技低功耗蓝牙产品设计的移动端工具，提供Android & iOS版本，可扫描、配置连接参数、演示标准Profile，以及调试汇顶科技低功耗蓝牙平台的Profile/Service | https://www.goodix.com/zh/software_tool/grtoolbox | Bluetooth LE全系SoC |
| GRDirect Test Mode Tool| DTM测试工具 | 用于Goodix Bluetooth LE DTM (Direct Test Mode) 测试 | https://www.goodix.com/zh/download?objectId=107&objectType=software | Bluetooth LE全系SoC |
| GRPLT Lite | 产测工具 | 为PLT Lite的配套工具，客户可使用该软件将开发完毕的应用固件、资源文件、量产配置等打包，通过串口下载至PLT Lite | https://www.goodix.com/zh/software_tool/grplt_lite | Bluetooth LE全系SoC |
| GRUart | 串口工具 | PC串口调试助手，适用于串口日志及协议栈日志打印 | https://www.goodix.com/zh/download?objectId=64&objectType=software | Bluetooth LE全系SoC |
| NemaPixpresso | 资源生成工具 | 用于图片和各种图像格式的转换，也可用于FrameBuffer的分析 | 随 LouisUI打包 | GR5526 |
| gdx_font_conv | 资源生成工具 | 用于生成支持GPU渲染的LVGL字体文件 | https://developers.goodix.com/zh/bbs/blog_detail/6b29cdf5923247029f4357a65de1b065 | GR5526 |
| LouisUI | 资源生成工具 | 用于将图片资源批量生成符合LVGL规范同时支持GPU渲染的.bin格式，并生成资源描述符文件 | https://developers.goodix.com/zh/bbs/blog_detail/2996e8f9f352491eb0ccca468f28f2ce | GR5526 |
| GRPPK | 功耗测试工具 | 配合PPK板进行产品的功耗评估 | 采购PPK后请向代理索取 | Bluetooth LE全系SoC |
| OTA SDK | 移动固件 | 提供Android & iOS DFU/OTA SDK，方便客户App开发 | https://developers.goodix.com/zh/bbs/detail/32869e79a7c84917b32ecb4ab10acac8 | Bluetooth LE全系SoC |


## 6. 获取芯片开发文档资料

- 芯片接口参考手册位于各芯片SDK的文档目录下。

- 芯片的软件设计、硬件设计、示例工程参考文档均开源，可从汇顶官网下载。

  

### 6.1 GR551x文档

  https://www.goodix.com/zh/product/connectivity/ble/gr551x

| 名称 | 权限     |
| ------------------------------------------------------------ | ---------- |
| [低功耗蓝牙产品开发快速入门](https://docs.goodix.com/zh/online/bluetooth_le_getting_started) | 公开 |
| [GR551x Datasheet](https://docs.goodix.com/zh/online/gr551x_datasheet) | 公开       |
| [GR551x勘误手册](https://docs.goodix.com/zh/online/gr551x_errata) | 公开       |
| [GR551x开发者指南](https://docs.goodix.com/zh/online/gr551x_develop_guide) | 公开       |
| [GR5xx IAR用户手册](https://docs.goodix.com/zh/online/gr55xx_iar_user_guide) | 公开       |
| [GR5xx GCC用户手册](https://docs.goodix.com/zh/online/gr55xx_gcc_user_guide) | 公开       |
| [GR551x API Reference](https://docs.goodix.com/zh/online/gr551x_api_reference) | 公开       |
| [GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl) | 公开       |
| [GProgrammer用户手册](https://docs.goodix.com/zh/online/gprogrammer_user_guide) | 公开       |
| [GR551x FCC RSE认证说明](https://docs.goodix.com/zh/online/fcc_rse_certificate_bl_a) | 公开       |
| [GR5515I0NDA外部Flash选型指导手册](https://docs.goodix.com/zh/online/gr5515_flash_selection_guide) | 公开       |
| [GR551x硬件设计指南](https://docs.goodix.com/zh/online/gr551x_hardware_design_guide) | 公开       |
| [GR551x Reference Design](https://www.goodix.com/zh/docview/GR551x Reference Design_V1.5?objectId=316&objectType=document&version=494) | 仅注册用户 |
| [GR5515 Starter Kit用户指南](https://docs.goodix.com/zh/online/gr5515_starter_kit_user_guide) | 公开       |
| [GR5515-SK-BASIC-RevE](https://www.goodix.com/zh/docview/GR5515-SK-BASIC-RevE_Rev.1.6?objectId=259&objectType=document&version=500) | 公开       |
| [GR5515-SK-BASIC-RevC](https://www.goodix.com/zh/docview/GR5515-SK-BASIC-RevC_Rev.1.5?objectId=100&objectType=document&version=133) | 公开       |
| [GR551x功耗模式及功耗测量说明](https://docs.goodix.com/zh/online/gr551x_sleep_mode_power_measure_note) | 公开       |
| [GR551x可靠性测试报告](https://docs.goodix.com/zh/online/reliablity_report_bl_a) | 公开       |
| [GR551x MCD](https://www.goodix.com/zh/docview/GR551x MCD_V1.0?objectId=314&objectType=document&version=490) | 公开       |
| [GR5xx鼠标示例手册](https://docs.goodix.com/zh/online/hid_mouse_bl) | 公开 |
| [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl) | 公开 |
| [GR5xx Serial Port Profile示例手册](https://docs.goodix.com/zh/online/serial_port_bl) | 公开 |
| [GR5xx HRS RSCS Relay示例手册](https://docs.goodix.com/zh/online/hrs_rscs_relay_bl) | 公开 |
| [GR5xx FreeRTOS示例手册](https://docs.goodix.com/zh/online/freertos_bl) | 公开 |
| [GR5xx Throughput示例手册](https://docs.goodix.com/zh/online/throughput_bl) | 公开 |
| [GR5xx AT Command示例手册](https://docs.goodix.com/zh/online/at_command_bl) | 公开 |
| [GR5xx ANCS Profile示例手册](https://docs.goodix.com/zh/online/ancs_profile_bl) | 公开 |
| [GR5xx AMS Profile示例手册](https://docs.goodix.com/zh/online/ams_profile_bl) | 公开 |
| [GR5xx Power Consumption Profile示例手册](https://docs.goodix.com/zh/online/power_consumption_bl) | 公开 |
| [GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl) | 公开 |
| [GR5xx固件升级开发指南](https://docs.goodix.com/zh/online/firmware_upgrade_bl) | 公开 |
| [GR5xx固件加密及应用介绍](https://docs.goodix.com/zh/online/firmware_encryption_bl) | 公开 |
| [GR5xx Fault Trace Module应用说明](https://docs.goodix.com/zh/online/fault_trace_bl) | 公开 |
| [GR5xx DTM测试指南](https://docs.goodix.com/zh/online/dtm_test_bl) | 公开 |
| [GRPLT Lite配置工具用户手册](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_user_guide) | 公开       |
| [GRPLT Lite配置工具自定义固件加密及应用介绍](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_firmware_introduction) | 公开       |
| [PLT Lite用户手册](https://docs.goodix.com/zh/online/plt_lite_guide_bl) | 公开    |
| [PLT Lite量产烧录指南](https://docs.goodix.com/zh/online/plt_lite_programming_guide_bl) | 公开    |



### 6.2 GR5525文档
https://www.goodix.com/zh/product/connectivity/ble/gr5525

| 名称                                                         | 权限       |
| ------------------------------------------------------------ | ---------- |
| [低功耗蓝牙产品开发快速入门](https://docs.goodix.com/zh/online/bluetooth_le_getting_started) | 公开       |
| [GR5525 Product Brief](https://www.goodix.com/zh/docview/GR5525 Product Brief_V1.0?objectId=348&objectType=document&version=538) | 公开       |
| [GR5525 Datasheet](https://docs.goodix.com/zh/online/datasheet_bl_c) | 公开       |
| [GR5525开发者指南](https://docs.goodix.com/zh/online/developer_guide_bl_c) | 公开       |
| [GR5525刷屏指南](https://docs.goodix.com/zh/online/display_guide_bl_c) | 公开       |
| [GR5xx IAR用户手册](https://docs.goodix.com/zh/online/gr55xx_iar_user_guide) | 公开       |
| [GR5xx GCC用户手册](https://docs.goodix.com/zh/online/gr55xx_gcc_user_guide) | 公开       |
| [GR5525 API Reference](https://docs.goodix.com/zh/online/api_reference_bl_c) | 公开       |
| [GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl) | 公开       |
| [GProgrammer用户手册](https://docs.goodix.com/zh/online/gprogrammer_user_guide) | 公开       |
| [GR5525 Starter Kit用户指南](https://docs.goodix.com/zh/online/starter_kit_manual_bl_c) | 公开       |
| [GR5525硬件设计指南](https://docs.goodix.com/zh/online/hardware_design_guide_c) | 公开       |
| [GR5525 Reference Design](https://www.goodix.com/zh/docview/GR5525%20Reference%20Design_V1.1?objectId=357&objectType=document&version=555) | 仅注册用户 |
| [GR5525-SK-BASIC-RevB](https://www.goodix.com/zh/docview/GR5525-SK-BASIC-RevB_V1.0?objectId=351&objectType=document&version=541) | 公开       |
| [GR5525功耗模式及功耗测量说明](https://docs.goodix.com/zh/online/power_measure_bl_c) | 公开       |
| [GR5525 Reliability Test Report](https://docs.goodix.com/zh/online/reliablity_report_bl_c) | 公开       |
| [GR5525 MCD](https://www.goodix.com/zh/docview/GR5525%20MCD_V1.0?objectId=349&objectType=document&version=539) | 公开       |
| [GR5xx鼠标示例手册](https://docs.goodix.com/zh/online/hid_mouse_bl) | 公开       |
| [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl) | 公开       |
| [GR5xx Serial Port Profile示例手册](https://docs.goodix.com/zh/online/serial_port_bl) | 公开       |
| [GR5xx HRS RSCS Relay示例手册](https://docs.goodix.com/zh/online/hrs_rscs_relay_bl) | 公开       |
| [GR5xx FreeRTOS示例手册](https://docs.goodix.com/zh/online/freertos_bl) | 公开       |
| [GR5xx Throughput示例手册](https://docs.goodix.com/zh/online/throughput_bl) | 公开       |
| [GR5xx AT Command示例手册](https://docs.goodix.com/zh/online/at_command_bl) | 公开       |
| [GR5xx ANCS Profile示例手册](https://docs.goodix.com/zh/online/ancs_profile_bl) | 公开       |
| [GR5xx AMS Profile示例手册](https://docs.goodix.com/zh/online/ams_profile_bl) | 公开       |
| [GR5xx Power Consumption Profile示例手册](https://docs.goodix.com/zh/online/power_consumption_bl) | 公开       |
| [GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl) | 公开       |
| [GR5xx固件升级开发指南](https://docs.goodix.com/zh/online/firmware_upgrade_bl) | 公开       |
| [GR5xx固件加密及应用介绍](https://docs.goodix.com/zh/online/firmware_encryption_bl) | 公开       |
| [GR5xx Fault Trace Module应用说明](https://docs.goodix.com/zh/online/fault_trace_bl) | 公开       |
| [GR5xx DTM测试指南](https://docs.goodix.com/zh/online/dtm_test_bl) | 公开       |
| [GRPLT Lite配置工具用户手册](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_user_guide) | 公开       |
| [GRPLT Lite配置工具自定义固件加密及应用介绍](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_firmware_introduction) | 公开       |
| [PLT Lite用户手册](https://docs.goodix.com/zh/online/plt_lite_guide_bl) | 公开       |
| [PLT Lite量产烧录指南](https://docs.goodix.com/zh/online/plt_lite_programming_guide_bl) | 公开       |




### 6.3 GR5526文档
https://www.goodix.com/zh/product/connectivity/ble/gr5526

| 名称 | 权限     |
| ------------------------------------------------------------ | ---------- |
| [低功耗蓝牙产品开发快速入门](https://docs.goodix.com/zh/online/bluetooth_le_getting_started) | 公开 |
| [GR5526 Product Brief](https://www.goodix.com/zh/docview/GR5526%20Product%20Brief_Rev.1.2?objectId=166&objectType=document&version=446) | 公开       |
| [GR5526 Datasheet](https://docs.goodix.com/zh/online/datasheet_bl_b) | 公开       |
| [GR5526 Datasheet Brief](https://docs.goodix.com/zh/online/datasheet_brief_bl_b/Rev.1.1) | 公开 |
| [GR5526开发者指南](https://docs.goodix.com/zh/online/developer_guide_bl_b) | 公开 |
| [GR5526刷屏指南](https://docs.goodix.com/zh/online/display_refresh_guide_bl_b) | 公开 |
| [GR5526 GPU开发者指南](https://docs.goodix.com/zh/online/gpu_guide_bl_b) | 公开 |
| [GR5xx IAR用户手册](https://docs.goodix.com/zh/online/gr55xx_iar_user_guide) | 公开       |
| [GR5xx GCC用户手册](https://docs.goodix.com/zh/online/gr55xx_gcc_user_guide) | 公开       |
| [GR5526 API Reference](https://docs.goodix.com/zh/online/api_reference_bl_b) | 公开 |
| [GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl) | 公开 |
| [GProgrammer用户手册](https://docs.goodix.com/zh/online/gprogrammer_user_guide) | 公开 |
| [GR5526 硬件设计指南](https://docs.goodix.com/zh/online/hardware_design_guidelines_bl_b) | 公开       |
| [GR5526 Reference Design](https://www.goodix.com/zh/docview/GR5526%20Reference%20Design_V1.0?objectId=280&objectType=document&version=443) | 仅注册用户       |
| [GR5526 Starter Kit用户指南](https://docs.goodix.com/zh/online/starter_kit_manual_bl_b) | 公开      |
| [GR5526-SK-BASIC-RevC](https://www.goodix.com/zh/docview/GR5526-SK-BASIC-RevC_V1.0?objectId=278&objectType=document&version=449) | 公开       |
| [GR5526功耗模式及功耗测量说明](https://docs.goodix.com/zh/online/power_application_bl_b) | 公开 |
| [GR5526 Reliability Test Report](https://docs.goodix.com/zh/online/reliablity_report_bl_b) | 公开      |
| [GR5526 MCD](https://www.goodix.com/zh/docview/GR5526%20MCD_V1.1?objectId=276&objectType=document&version=447) | 公开      |
| [GR5xx鼠标示例手册](https://docs.goodix.com/zh/online/hid_mouse_bl) | 公开 |
| [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl) | 公开 |
| [GR5xx Serial Port Profile示例手册](https://docs.goodix.com/zh/online/serial_port_bl) | 公开 |
| [GR5xx HRS RSCS Relay示例手册](https://docs.goodix.com/zh/online/hrs_rscs_relay_bl) | 公开 |
| [GR5xx FreeRTOS示例手册](https://docs.goodix.com/zh/online/freertos_bl) | 公开 |
| [GR5xx Throughput示例手册](https://docs.goodix.com/zh/online/throughput_bl) | 公开 |
| [GR5xx AT Command示例手册](https://docs.goodix.com/zh/online/at_command_bl) | 公开 |
| [GR5xx ANCS Profile示例手册](https://docs.goodix.com/zh/online/ancs_profile_bl) | 公开 |
| [GR5xx AMS Profile示例手册](https://docs.goodix.com/zh/online/ams_profile_bl) | 公开 |
| [GR5xx Power Consumption Profile示例手册](https://docs.goodix.com/zh/online/power_consumption_bl) | 公开 |
| [GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl) | 公开 |
| [GR5xx固件升级开发指南](https://docs.goodix.com/zh/online/firmware_upgrade_bl) | 公开 |
| [GR5xx固件加密及应用介绍](https://docs.goodix.com/zh/online/firmware_encryption_bl) | 公开 |
| [GR5xx Fault Trace Module应用说明](https://docs.goodix.com/zh/online/fault_trace_bl) | 公开 |
| [GR5xx DTM测试指南](https://docs.goodix.com/zh/online/dtm_test_bl) | 公开 |
| [GRPLT Lite配置工具用户手册](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_user_guide) | 公开       |
| [GRPLT Lite配置工具自定义固件加密及应用介绍](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_firmware_introduction) | 公开       |
| [PLT Lite用户手册](https://docs.goodix.com/zh/online/plt_lite_guide_bl) | 公开    |
| [PLT Lite量产烧录指南](https://docs.goodix.com/zh/online/plt_lite_programming_guide_bl) | 公开    |


### 6.4 GR533x文档
https://www.goodix.com/zh/product/connectivity/ble/gr533x


| 名称 | 权限       |
| ------------------------------------------------------------ | ---------- |
| [低功耗蓝牙产品开发快速入门](https://docs.goodix.com/zh/online/bluetooth_le_getting_started) | 公开 |
| [GR533x Product Brief](https://www.goodix.com/zh/docview/GR533x%20Product%20Brief_V1.1?objectId=359&objectType=document&version=557) | 公开       |
| [GR533x Datasheet](https://docs.goodix.com/zh/online/datasheet_bl_d) | 公开       |
| [GR533x 开发者指南](https://docs.goodix.com/zh/online/developer_guide_bl_d) | 公开       |
| [GR533x API Reference](https://docs.goodix.com/zh/online/api_reference_bl_d) | 公开       |
| [GR5xx IAR用户手册](https://docs.goodix.com/zh/online/gr55xx_iar_user_guide) | 公开       |
| [GR5xx GCC用户手册](https://docs.goodix.com/zh/online/gr55xx_gcc_user_guide) | 公开       |
| [GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl) | 公开 |
| [GProgrammer用户手册](https://docs.goodix.com/zh/online/gprogrammer_user_guide) | 公开 |
| [GR533x LCP开发者指南](https://docs.goodix.com/zh/online/lcp_bl_d) | 公开       |
| [GR533x 硬件设计指南](https://docs.goodix.com/zh/online/hardware_design_guide_d) | 公开       |
| [GR533x Reference Design](https://www.goodix.com/zh/docview/GR533x%20Reference%20Design_V1.2?objectId=362&objectType=document&version=609) | 仅注册用户       |
| [GR533x Module Reference Design](https://www.goodix.com/zh/docview/GR533x%20Module%20Reference%20Design_V1.1?objectId=363&objectType=document&version=611) | 仅注册用户        |
| [GR5331 Starter Kit用户指南](https://docs.goodix.com/zh/online/starter_kit_manual_bl_d) | 公开      |
| [GR5331-SK-BASIC-RevC](https://www.goodix.com/zh/docview/GR5331-SK-BASIC-RevC_RevC?objectId=366&objectType=document&version=564) | 公开       |
| [GR533x功耗测试用户手册](https://docs.goodix.com/zh/online/power_measure_bl_d) | 公开      |
| [GR533x RF PA应用指南](https://docs.goodix.com/zh/online/rf_pa_bl_d) | 公开      |
| [GR533x RF匹配调试指南](https://docs.goodix.com/zh/online/rf_matching_bl_d) | 公开      |
| [GR533x Reliability Test Report](https://docs.goodix.com/zh/online/reliablity_report_bl_d) | 公开      |
| [GR533x MCD](https://www.goodix.com/zh/docview/GR533x%20MCD_V1.0?objectId=360&objectType=document&version=558) | 公开      |
| [GR533x Mesh Simple On Off Models示例手册](https://docs.goodix.com/zh/online/mesh_sso_bl_d) | 公开      |
| [GR533x Mesh Light Lightness Models示例手册](https://docs.goodix.com/zh/online/mesh_lln_bl_d) | 公开      |
| [GR5xx鼠标示例手册](https://docs.goodix.com/zh/online/hid_mouse_bl) | 公开 |
| [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl) | 公开 |
| [GR5xx Serial Port Profile示例手册](https://docs.goodix.com/zh/online/serial_port_bl) | 公开 |
| [GR5xx HRS RSCS Relay示例手册](https://docs.goodix.com/zh/online/hrs_rscs_relay_bl) | 公开 |
| [GR5xx FreeRTOS示例手册](https://docs.goodix.com/zh/online/freertos_bl) | 公开 |
| [GR5xx Throughput示例手册](https://docs.goodix.com/zh/online/throughput_bl) | 公开 |
| [GR5xx AT Command示例手册](https://docs.goodix.com/zh/online/at_command_bl) | 公开 |
| [GR5xx ANCS Profile示例手册](https://docs.goodix.com/zh/online/ancs_profile_bl) | 公开 |
| [GR5xx AMS Profile示例手册](https://docs.goodix.com/zh/online/ams_profile_bl) | 公开 |
| [GR5xx Power Consumption Profile示例手册](https://docs.goodix.com/zh/online/power_consumption_bl) | 公开 |
| [GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl) | 公开 |
| [GR5xx固件升级开发指南](https://docs.goodix.com/zh/online/firmware_upgrade_bl) | 公开 |
| [GR5xx Fault Trace Module应用说明](https://docs.goodix.com/zh/online/fault_trace_bl) | 公开 |
| [GR5xx DTM测试指南](https://docs.goodix.com/zh/online/dtm_test_bl) | 公开 |
| [GRPLT Lite配置工具用户手册](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_user_guide) | 公开       |
| [PLT Lite用户手册](https://docs.goodix.com/zh/online/plt_lite_guide_bl) | 公开    |
| [PLT Lite量产烧录指南](https://docs.goodix.com/zh/online/plt_lite_programming_guide_bl) | 公开    |

## 7. 获取技术方案支持

### 7.1 产品技术方案

目前，Goodix提供了下列技术方案或参考设计。

| 技术方案               | 方案描述                                              | 获取方式       |
| ---------------------- | ----------------------------------------------------- | -------------- |
| GR5526穿戴手表参考设计 | 提供手表应用的示例参考，涵盖常用的软件模块和GUI框架   | GR5526 SDK     |
| FMNA (Apple Find My)   | 完整的FMNA方案，提供SDK及对应的各种工具和认证流程支持 | 请联系代理支持 |



### 7.2 生态技术集成

Goodix Bluetooth LE芯片集成或部分支持以下IoT技术生态服务，用户可以根据产品需要选择。

| IoT技术生态     | 服务说明                       | 芯片   | 获取方式                                       |
| --------------- | ------------------------------ | ------ | ---------------------------------------------- |
| Amazon FreeRTOS | Amazon FreeRTOS IoT认证        | GR551x | https://github.com/goodix/amazon-freertos      |
| RT-Thread       | 移植集成RT-Thread OS和驱动框架 | GR533x | https://github.com/goodix-ble/GR533x-RT-Thread |




## 8. 技术服务

Goodix Bluetooth LE产品提供代理技术服务和原厂社区技术服务支持，可以及时有效地帮助用户在前期需求研究、产品开发设计、技术问题支持解决、产测的各个阶段提供便捷和专业的技术服务，帮助用户节省开发时间、缩短开发周期、节省开发成本，快速落地产品抢占市场。

| 技术服务              | 备注                                           |
| --------------------- | ---------------------------------------------- |
| 官网渠道 - 技术博客   | https://developers.goodix.com/zh/bbs/blog_list |
| 官网渠道 - 技术论坛   | https://developers.goodix.com/zh/bbs/list      |
| 官网渠道 - QQ技术社群 | QQ社群号：168552615                            |
| 代理渠道              | 可选的现场/远程技术支持                        |







