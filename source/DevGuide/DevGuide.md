# Goodix BLE Product Development Wizard



## 1. Information List

When users are ready to understand or design/develop products based on Goodix Bluetooth LE SoC, they need to obtain and find the following information (including but not limited to) first:

- Chip Product Information: Understand the basic chip information for chip selection.
- Chip SDK package: Get the software development kit of the chip, learn and familiarize with the source code and sample projects.
- Chip and SK development board: Get the channels for purchasing chips and development boards, so as to carry out functional verification and advance software design before product hardware design.
- Chip development tools: download and get all the development software and tools that need to be used.
- Chip development document information: view and download chip Datasheet, hardware design guide, SDK developer guide, and various software or engineering instructions.
- Chip's product program information: Get the reference materials of application programs, including program-related software and documentation, etc.
- Technical support services: Get the technical support services and technical support channels available from Goodix and agents in advance.



## 2. Access to Chip Product Information

Goodix currently offers a family of Bluetooth LE SoCs covering the high-end, mid-range and entry-level markets.

- [Goodix Bluetooth LE SoC Selection Chart](https://www.goodix.com/zh/down/resource/Goodix_Bluetooth_Chipset_Selection_Guide?objectId=5&objectType= design_resource&version=64)

![](../_images/goodi_ble_chipset_select_guide.png)

## 3. Get the chip SDK development kit

| Bluetooth LE SoC | SDK Download Link | Note |
| ---------------- | -------------------------------------------------- | -------------- |
| GR551x | https://www.goodix.com/zh/software_tool/gr551x_sdk | Please download the latest version |
| GR5525 | https://www.goodix.com/zh/software_tool/gr5525_sdk | Please download the latest version |
| GR5526 | https://www.goodix.com/zh/software_tool/gr5526_sdk | Please download the latest version |
| GR533x | https://www.goodix.com/zh/software_tool/gr5526_sdk | Please download the latest version |



## 4. Getting the Chip and Board

### 4.1 Enterprise users

Please contact the agent to purchase each series of chips and corresponding development boards, or you can get them from the following Taobao link (or search for LILEDA Mall and enter the name of the development board to purchase).
- SK board or small system board: for verification and pre-development of software functions.
  - [GR5331-SK-BASIC（TAOBAO）](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.29.44e37824v9pK8y&id=775605003005&skuId=5473168402830)
  - [GR5526-SK-BASIC](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.21.44e37824v9pK8y&id=757015248383)
  - [GR5525-SK-BASIC](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.33.44e37824v9pK8y&id=775644909891&skuId=5302971608278)
  - [GR5515-SK-BASIC-Rev.C](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.31.44e37824v9pK8y&id=775641073847&skuId=5476038335715)


- PPK board: for power consumption test evaluation.
  - Request from agent after purchase

- PLT Board: Used for production line firmware download.
  - [PLT-LITE-GR55xx（TAOBAO）](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-21080581561.23.44e37824v9pK8y&id=757604846504&skuId=5222694048026)




### 4.2 Individual and Community Users

Individual user procurement channel is under active construction, you can join the community group (QQ group number: 168552615) real-time attention.




## 5. Access to Chip Development Tools

Goodix provides the software required for Bluetooth products to develop multiple processes such as download, DFU, and production test.

### 5.1 Standard Development Software

All Goodix Bluetooth chips support Keil/ARMCC compilation toolchain by default, and also provide other build methods such as GCC, which are standard development software and can be downloaded from the official website of the corresponding software vendors.

Some of the commonly used standard software is listed below:

| software | description | website |
| ------ | ----------------------- | ------------------------------ |
| Keil | ARMCC IDE tool | www.keil.com |
| J-Link | SWD debugging software | https://www.segger.com/downloads/jlink/ |
| Ozone | a debugger from SEGGER | https://www.segger.com/products/development-tools/ozone-j-link-debugger/ |
| GCC | ARM none eabi gcc compiler | https://developer.arm.com/downloads |



### 5.2 Goodix Development Tools Collection

| Software | Type | Description | Download | For SoC |
| ---- | ---- | ---- | -------- | ------- |
| GProgrammer | Program Resource Burning and Configuration Tool | 一款支持Bluetooth LE全系列芯片的固件烧录工具，用于开发调试，支持固件下载、Flash读写、eFuse烧写、固件加密加签等功能。在量产阶段，Bluetooth LE系列芯片产品的批量烧录测试，可采用PLT Lite和GRPLT Lite配置工具进行批量烧录测试 | https://www.goodix.com/zh/software_tool/gprogrammer_ble | Bluetooth LE全系SoC |
| GRToolbox | Mobile Development and Verification App | 一款专为汇顶科技低功耗蓝牙产品设计的移动端工具，提供Android & iOS版本，可扫描、配置连接参数、演示标准Profile，以及调试汇顶科技低功耗蓝牙平台的Profile/Service | https://www.goodix.com/zh/software_tool/grtoolbox | Bluetooth LE全系SoC |
| GRDirect Test Mode Tool| DTM Test Tool | 用于Goodix Bluetooth LE DTM (Direct Test Mode) 测试 | https://www.goodix.com/zh/download?objectId=107&objectType=software | Bluetooth LE全系SoC |
| GRPLT Lite | Product Line Tool | 为PLT Lite的配套工具，客户可使用该软件将开发完毕的应用固件、资源文件、量产配置等打包，通过串口下载至PLT Lite | https://www.goodix.com/zh/software_tool/grplt_lite | Bluetooth LE全系SoC |
| GRUart | 串口工具 | PC串口调试助手，适用于串口日志及协议栈日志打印 | https://www.goodix.com/zh/download?objectId=64&objectType=software | Bluetooth LE全系SoC |
| NemaPixpresso | Image Resource Generator Tool | 用于图片和各种图像格式的转换，也可用于FrameBuffer的分析 | 随 LouisUI打包 | GR5526 |
| gdx_font_conv | Font Resource Generator Tool | 用于生成支持GPU渲染的LVGL字体文件 | https://developers.goodix.com/zh/bbs/blog_detail/6b29cdf5923247029f4357a65de1b065 | GR5526 |
| LouisUI | Image Resource Generator Tool | 用于将图片资源批量生成符合LVGL规范同时支持GPU渲染的.bin格式，并生成资源描述符文件 | https://developers.goodix.com/zh/bbs/blog_detail/2996e8f9f352491eb0ccca468f28f2ce | GR5526 |
| GRPPK | Power Consumption Test Tool | 配合PPK板进行产品的功耗评估 | 采购PPK后请向代理索取 | Bluetooth LE全系SoC |
| OTA SDK | Mobile Firmware | 提供Android & iOS DFU/OTA SDK，方便客户App开发 | https://developers.goodix.com/zh/bbs/detail/32869e79a7c84917b32ecb4ab10acac8 | Bluetooth LE全系SoC |


## 6. Obtaining Chip Development Documentation

- Chip interface reference manuals are located in the documentation directory of each chip SDK.

- The software design, hardware design, and sample project reference documents of the chips are open source and can be downloaded from the official website of Huitian.

  

### 6.1 GR551x Documents

https://www.goodix.com/zh/product/connectivity/ble/gr551x

| Document | Privileges |
| ------------------------------------------------------------ | ---------- |
| [低功耗蓝牙产品开发快速入门](https://docs.goodix.com/zh/online/bluetooth_le_getting_started) | PUBLIC |
| [GR551x Datasheet](https://docs.goodix.com/zh/online/gr551x_datasheet) | PUBLIC       |
| [GR551x勘误手册](https://docs.goodix.com/zh/online/gr551x_errata) | PUBLIC       |
| [GR551x开发者指南](https://docs.goodix.com/zh/online/gr551x_develop_guide) | PUBLIC       |
| [GR5xx IAR用户手册](https://docs.goodix.com/zh/online/gr55xx_iar_user_guide) | PUBLIC       |
| [GR5xx GCC用户手册](https://docs.goodix.com/zh/online/gr55xx_gcc_user_guide) | PUBLIC       |
| [GR551x API Reference](https://docs.goodix.com/zh/online/gr551x_api_reference) | PUBLIC       |
| [GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl) | PUBLIC       |
| [GProgrammer用户手册](https://docs.goodix.com/zh/online/gprogrammer_user_guide) | PUBLIC       |
| [GR551x FCC RSE认证说明](https://docs.goodix.com/zh/online/fcc_rse_certificate_bl_a) | PUBLIC       |
| [GR5515I0NDA外部Flash选型指导手册](https://docs.goodix.com/zh/online/gr5515_flash_selection_guide) | PUBLIC       |
| [GR551x硬件设计指南](https://docs.goodix.com/zh/online/gr551x_hardware_design_guide) | PUBLIC       |
| [GR551x Reference Design](https://www.goodix.com/zh/docview/GR551x Reference Design_V1.5?objectId=316&objectType=document&version=494) | Only For Registered Users |
| [GR5515 Starter Kit用户指南](https://docs.goodix.com/zh/online/gr5515_starter_kit_user_guide) | PUBLIC       |
| [GR5515-SK-BASIC-RevE](https://www.goodix.com/zh/docview/GR5515-SK-BASIC-RevE_Rev.1.6?objectId=259&objectType=document&version=500) | PUBLIC       |
| [GR5515-SK-BASIC-RevC](https://www.goodix.com/zh/docview/GR5515-SK-BASIC-RevC_Rev.1.5?objectId=100&objectType=document&version=133) | PUBLIC       |
| [GR551x功耗模式及功耗测量说明](https://docs.goodix.com/zh/online/gr551x_sleep_mode_power_measure_note) | PUBLIC       |
| [GR551x可靠性测试报告](https://docs.goodix.com/zh/online/reliablity_report_bl_a) | PUBLIC       |
| [GR551x MCD](https://www.goodix.com/zh/docview/GR551x MCD_V1.0?objectId=314&objectType=document&version=490) | PUBLIC       |
| [GR5xx鼠标示例手册](https://docs.goodix.com/zh/online/hid_mouse_bl) | PUBLIC |
| [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl) | PUBLIC |
| [GR5xx Serial Port Profile示例手册](https://docs.goodix.com/zh/online/serial_port_bl) | PUBLIC |
| [GR5xx HRS RSCS Relay示例手册](https://docs.goodix.com/zh/online/hrs_rscs_relay_bl) | PUBLIC |
| [GR5xx FreeRTOS示例手册](https://docs.goodix.com/zh/online/freertos_bl) | PUBLIC |
| [GR5xx Throughput示例手册](https://docs.goodix.com/zh/online/throughput_bl) | PUBLIC |
| [GR5xx AT Command示例手册](https://docs.goodix.com/zh/online/at_command_bl) | PUBLIC |
| [GR5xx ANCS Profile示例手册](https://docs.goodix.com/zh/online/ancs_profile_bl) | PUBLIC |
| [GR5xx AMS Profile示例手册](https://docs.goodix.com/zh/online/ams_profile_bl) | PUBLIC |
| [GR5xx Power Consumption Profile示例手册](https://docs.goodix.com/zh/online/power_consumption_bl) | PUBLIC |
| [GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl) | PUBLIC |
| [GR5xx固件升级开发指南](https://docs.goodix.com/zh/online/firmware_upgrade_bl) | PUBLIC |
| [GR5xx固件加密及应用介绍](https://docs.goodix.com/zh/online/firmware_encryption_bl) | PUBLIC |
| [GR5xx Fault Trace Module应用说明](https://docs.goodix.com/zh/online/fault_trace_bl) | PUBLIC |
| [GR5xx DTM测试指南](https://docs.goodix.com/zh/online/dtm_test_bl) | PUBLIC |
| [GRPLT Lite配置工具用户手册](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_user_guide) | PUBLIC       |
| [GRPLT Lite配置工具自定义固件加密及应用介绍](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_firmware_introduction) | PUBLIC       |
| [PLT Lite用户手册](https://docs.goodix.com/zh/online/plt_lite_guide_bl) | PUBLIC    |
| [PLT Lite量产烧录指南](https://docs.goodix.com/zh/online/plt_lite_programming_guide_bl) | PUBLIC    |



### 6.2 GR5525 Documents
https://www.goodix.com/zh/product/connectivity/ble/gr5525

| Document | Privileges |
| ------------------------------------------------------------ | ---------- |
| [低功耗蓝牙产品开发快速入门](https://docs.goodix.com/zh/online/bluetooth_le_getting_started) | PUBLIC       |
| [GR5525 Product Brief](https://www.goodix.com/zh/docview/GR5525 Product Brief_V1.0?objectId=348&objectType=document&version=538) | PUBLIC       |
| [GR5525 Datasheet](https://docs.goodix.com/zh/online/datasheet_bl_c) | PUBLIC       |
| [GR5525开发者指南](https://docs.goodix.com/zh/online/developer_guide_bl_c) | PUBLIC       |
| [GR5525刷屏指南](https://docs.goodix.com/zh/online/display_guide_bl_c) | PUBLIC       |
| [GR5xx IAR用户手册](https://docs.goodix.com/zh/online/gr55xx_iar_user_guide) | PUBLIC       |
| [GR5xx GCC用户手册](https://docs.goodix.com/zh/online/gr55xx_gcc_user_guide) | PUBLIC       |
| [GR5525 API Reference](https://docs.goodix.com/zh/online/api_reference_bl_c) | PUBLIC       |
| [GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl) | PUBLIC       |
| [GProgrammer用户手册](https://docs.goodix.com/zh/online/gprogrammer_user_guide) | PUBLIC       |
| [GR5525 Starter Kit用户指南](https://docs.goodix.com/zh/online/starter_kit_manual_bl_c) | PUBLIC       |
| [GR5525硬件设计指南](https://docs.goodix.com/zh/online/hardware_design_guide_c) | PUBLIC       |
| [GR5525 Reference Design](https://www.goodix.com/zh/docview/GR5525%20Reference%20Design_V1.1?objectId=357&objectType=document&version=555) | Only For Registered Users |
| [GR5525-SK-BASIC-RevB](https://www.goodix.com/zh/docview/GR5525-SK-BASIC-RevB_V1.0?objectId=351&objectType=document&version=541) | PUBLIC       |
| [GR5525功耗模式及功耗测量说明](https://docs.goodix.com/zh/online/power_measure_bl_c) | PUBLIC       |
| [GR5525 Reliability Test Report](https://docs.goodix.com/zh/online/reliablity_report_bl_c) | PUBLIC       |
| [GR5525 MCD](https://www.goodix.com/zh/docview/GR5525%20MCD_V1.0?objectId=349&objectType=document&version=539) | PUBLIC       |
| [GR5xx鼠标示例手册](https://docs.goodix.com/zh/online/hid_mouse_bl) | PUBLIC       |
| [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl) | PUBLIC       |
| [GR5xx Serial Port Profile示例手册](https://docs.goodix.com/zh/online/serial_port_bl) | PUBLIC       |
| [GR5xx HRS RSCS Relay示例手册](https://docs.goodix.com/zh/online/hrs_rscs_relay_bl) | PUBLIC       |
| [GR5xx FreeRTOS示例手册](https://docs.goodix.com/zh/online/freertos_bl) | PUBLIC       |
| [GR5xx Throughput示例手册](https://docs.goodix.com/zh/online/throughput_bl) | PUBLIC       |
| [GR5xx AT Command示例手册](https://docs.goodix.com/zh/online/at_command_bl) | PUBLIC       |
| [GR5xx ANCS Profile示例手册](https://docs.goodix.com/zh/online/ancs_profile_bl) | PUBLIC       |
| [GR5xx AMS Profile示例手册](https://docs.goodix.com/zh/online/ams_profile_bl) | PUBLIC       |
| [GR5xx Power Consumption Profile示例手册](https://docs.goodix.com/zh/online/power_consumption_bl) | PUBLIC       |
| [GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl) | PUBLIC       |
| [GR5xx固件升级开发指南](https://docs.goodix.com/zh/online/firmware_upgrade_bl) | PUBLIC       |
| [GR5xx固件加密及应用介绍](https://docs.goodix.com/zh/online/firmware_encryption_bl) | PUBLIC       |
| [GR5xx Fault Trace Module应用说明](https://docs.goodix.com/zh/online/fault_trace_bl) | PUBLIC       |
| [GR5xx DTM测试指南](https://docs.goodix.com/zh/online/dtm_test_bl) | PUBLIC       |
| [GRPLT Lite配置工具用户手册](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_user_guide) | PUBLIC       |
| [GRPLT Lite配置工具自定义固件加密及应用介绍](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_firmware_introduction) | PUBLIC       |
| [PLT Lite用户手册](https://docs.goodix.com/zh/online/plt_lite_guide_bl) | PUBLIC       |
| [PLT Lite量产烧录指南](https://docs.goodix.com/zh/online/plt_lite_programming_guide_bl) | PUBLIC       |




### 6.3 GR5526 Documents
https://www.goodix.com/zh/product/connectivity/ble/gr5526

| Document | Privileges |
| ------------------------------------------------------------ | ---------- |
| [低功耗蓝牙产品开发快速入门](https://docs.goodix.com/zh/online/bluetooth_le_getting_started) | PUBLIC |
| [GR5526 Product Brief](https://www.goodix.com/zh/docview/GR5526%20Product%20Brief_Rev.1.2?objectId=166&objectType=document&version=446) | PUBLIC       |
| [GR5526 Datasheet](https://docs.goodix.com/zh/online/datasheet_bl_b) | PUBLIC       |
| [GR5526 Datasheet Brief](https://docs.goodix.com/zh/online/datasheet_brief_bl_b/Rev.1.1) | PUBLIC |
| [GR5526开发者指南](https://docs.goodix.com/zh/online/developer_guide_bl_b) | PUBLIC |
| [GR5526刷屏指南](https://docs.goodix.com/zh/online/display_refresh_guide_bl_b) | PUBLIC |
| [GR5526 GPU开发者指南](https://docs.goodix.com/zh/online/gpu_guide_bl_b) | PUBLIC |
| [GR5xx IAR用户手册](https://docs.goodix.com/zh/online/gr55xx_iar_user_guide) | PUBLIC       |
| [GR5xx GCC用户手册](https://docs.goodix.com/zh/online/gr55xx_gcc_user_guide) | PUBLIC       |
| [GR5526 API Reference](https://docs.goodix.com/zh/online/api_reference_bl_b) | PUBLIC |
| [GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl) | PUBLIC |
| [GProgrammer用户手册](https://docs.goodix.com/zh/online/gprogrammer_user_guide) | PUBLIC |
| [GR5526 硬件设计指南](https://docs.goodix.com/zh/online/hardware_design_guidelines_bl_b) | PUBLIC       |
| [GR5526 Reference Design](https://www.goodix.com/zh/docview/GR5526%20Reference%20Design_V1.0?objectId=280&objectType=document&version=443) | Only For Registered Users       |
| [GR5526 Starter Kit用户指南](https://docs.goodix.com/zh/online/starter_kit_manual_bl_b) | PUBLIC      |
| [GR5526-SK-BASIC-RevC](https://www.goodix.com/zh/docview/GR5526-SK-BASIC-RevC_V1.0?objectId=278&objectType=document&version=449) | PUBLIC       |
| [GR5526功耗模式及功耗测量说明](https://docs.goodix.com/zh/online/power_application_bl_b) | PUBLIC |
| [GR5526 Reliability Test Report](https://docs.goodix.com/zh/online/reliablity_report_bl_b) | PUBLIC      |
| [GR5526 MCD](https://www.goodix.com/zh/docview/GR5526%20MCD_V1.1?objectId=276&objectType=document&version=447) | PUBLIC      |
| [GR5xx鼠标示例手册](https://docs.goodix.com/zh/online/hid_mouse_bl) | PUBLIC |
| [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl) | PUBLIC |
| [GR5xx Serial Port Profile示例手册](https://docs.goodix.com/zh/online/serial_port_bl) | PUBLIC |
| [GR5xx HRS RSCS Relay示例手册](https://docs.goodix.com/zh/online/hrs_rscs_relay_bl) | PUBLIC |
| [GR5xx FreeRTOS示例手册](https://docs.goodix.com/zh/online/freertos_bl) | PUBLIC |
| [GR5xx Throughput示例手册](https://docs.goodix.com/zh/online/throughput_bl) | PUBLIC |
| [GR5xx AT Command示例手册](https://docs.goodix.com/zh/online/at_command_bl) | PUBLIC |
| [GR5xx ANCS Profile示例手册](https://docs.goodix.com/zh/online/ancs_profile_bl) | PUBLIC |
| [GR5xx AMS Profile示例手册](https://docs.goodix.com/zh/online/ams_profile_bl) | PUBLIC |
| [GR5xx Power Consumption Profile示例手册](https://docs.goodix.com/zh/online/power_consumption_bl) | PUBLIC |
| [GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl) | PUBLIC |
| [GR5xx固件升级开发指南](https://docs.goodix.com/zh/online/firmware_upgrade_bl) | PUBLIC |
| [GR5xx固件加密及应用介绍](https://docs.goodix.com/zh/online/firmware_encryption_bl) | PUBLIC |
| [GR5xx Fault Trace Module应用说明](https://docs.goodix.com/zh/online/fault_trace_bl) | PUBLIC |
| [GR5xx DTM测试指南](https://docs.goodix.com/zh/online/dtm_test_bl) | PUBLIC |
| [GRPLT Lite配置工具用户手册](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_user_guide) | PUBLIC       |
| [GRPLT Lite配置工具自定义固件加密及应用介绍](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_firmware_introduction) | PUBLIC       |
| [PLT Lite用户手册](https://docs.goodix.com/zh/online/plt_lite_guide_bl) | PUBLIC    |
| [PLT Lite量产烧录指南](https://docs.goodix.com/zh/online/plt_lite_programming_guide_bl) | PUBLIC    |


### 6.4 GR533x Documents
https://www.goodix.com/zh/product/connectivity/ble/gr533x


| Document | Privileges |
| ------------------------------------------------------------ | ---------- |
| [低功耗蓝牙产品开发快速入门](https://docs.goodix.com/zh/online/bluetooth_le_getting_started) | PUBLIC |
| [GR533x Product Brief](https://www.goodix.com/zh/docview/GR533x%20Product%20Brief_V1.1?objectId=359&objectType=document&version=557) | PUBLIC       |
| [GR533x Datasheet](https://docs.goodix.com/zh/online/datasheet_bl_d) | PUBLIC       |
| [GR533x 开发者指南](https://docs.goodix.com/zh/online/developer_guide_bl_d) | PUBLIC       |
| [GR533x API Reference](https://docs.goodix.com/zh/online/api_reference_bl_d) | PUBLIC       |
| [GR5xx IAR用户手册](https://docs.goodix.com/zh/online/gr55xx_iar_user_guide) | PUBLIC       |
| [GR5xx GCC用户手册](https://docs.goodix.com/zh/online/gr55xx_gcc_user_guide) | PUBLIC       |
| [GR5xx APP驱动用户手册](https://docs.goodix.com/zh/online/app_driver_bl) | PUBLIC |
| [GProgrammer用户手册](https://docs.goodix.com/zh/online/gprogrammer_user_guide) | PUBLIC |
| [GR533x LCP开发者指南](https://docs.goodix.com/zh/online/lcp_bl_d) | PUBLIC       |
| [GR533x 硬件设计指南](https://docs.goodix.com/zh/online/hardware_design_guide_d) | PUBLIC       |
| [GR533x Reference Design](https://www.goodix.com/zh/docview/GR533x%20Reference%20Design_V1.2?objectId=362&objectType=document&version=609) | Only For Registered Users       |
| [GR533x Module Reference Design](https://www.goodix.com/zh/docview/GR533x%20Module%20Reference%20Design_V1.1?objectId=363&objectType=document&version=611) | Only For Registered Users        |
| [GR5331 Starter Kit用户指南](https://docs.goodix.com/zh/online/starter_kit_manual_bl_d) | PUBLIC      |
| [GR5331-SK-BASIC-RevC](https://www.goodix.com/zh/docview/GR5331-SK-BASIC-RevC_RevC?objectId=366&objectType=document&version=564) | PUBLIC       |
| [GR533x功耗测试用户手册](https://docs.goodix.com/zh/online/power_measure_bl_d) | PUBLIC      |
| [GR533x RF PA应用指南](https://docs.goodix.com/zh/online/rf_pa_bl_d) | PUBLIC      |
| [GR533x RF匹配调试指南](https://docs.goodix.com/zh/online/rf_matching_bl_d) | PUBLIC      |
| [GR533x Reliability Test Report](https://docs.goodix.com/zh/online/reliablity_report_bl_d) | PUBLIC      |
| [GR533x MCD](https://www.goodix.com/zh/docview/GR533x%20MCD_V1.0?objectId=360&objectType=document&version=558) | PUBLIC      |
| [GR533x Mesh Simple On Off Models示例手册](https://docs.goodix.com/zh/online/mesh_sso_bl_d) | PUBLIC      |
| [GR533x Mesh Light Lightness Models示例手册](https://docs.goodix.com/zh/online/mesh_lln_bl_d) | PUBLIC      |
| [GR5xx鼠标示例手册](https://docs.goodix.com/zh/online/hid_mouse_bl) | PUBLIC |
| [GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl) | PUBLIC |
| [GR5xx Serial Port Profile示例手册](https://docs.goodix.com/zh/online/serial_port_bl) | PUBLIC |
| [GR5xx HRS RSCS Relay示例手册](https://docs.goodix.com/zh/online/hrs_rscs_relay_bl) | PUBLIC |
| [GR5xx FreeRTOS示例手册](https://docs.goodix.com/zh/online/freertos_bl) | PUBLIC |
| [GR5xx Throughput示例手册](https://docs.goodix.com/zh/online/throughput_bl) | PUBLIC |
| [GR5xx AT Command示例手册](https://docs.goodix.com/zh/online/at_command_bl) | PUBLIC |
| [GR5xx ANCS Profile示例手册](https://docs.goodix.com/zh/online/ancs_profile_bl) | PUBLIC |
| [GR5xx AMS Profile示例手册](https://docs.goodix.com/zh/online/ams_profile_bl) | PUBLIC |
| [GR5xx Power Consumption Profile示例手册](https://docs.goodix.com/zh/online/power_consumption_bl) | PUBLIC |
| [GR5xx APP Log应用说明](https://docs.goodix.com/zh/online/app_log_bl) | PUBLIC |
| [GR5xx固件升级开发指南](https://docs.goodix.com/zh/online/firmware_upgrade_bl) | PUBLIC |
| [GR5xx Fault Trace Module应用说明](https://docs.goodix.com/zh/online/fault_trace_bl) | PUBLIC |
| [GR5xx DTM测试指南](https://docs.goodix.com/zh/online/dtm_test_bl) | PUBLIC |
| [GRPLT Lite配置工具用户手册](https://docs.goodix.com/zh/online/grplt_lite_configuration_tool_user_guide) | PUBLIC       |
| [PLT Lite用户手册](https://docs.goodix.com/zh/online/plt_lite_guide_bl) | PUBLIC    |
| [PLT Lite量产烧录指南](https://docs.goodix.com/zh/online/plt_lite_programming_guide_bl) | PUBLIC    |


## 7. Obtaining technical support

## 7.1 Product Technical Solutions

Goodix currently offers the following technical solutions or reference designs.

| Technical Programs | Program Description | Access |
| ---------------------- | ----------------------------------------------------- | -------------- |
| GR5526 Wearable Watch Reference Design | Provides a sample reference for a watch application, covering common software modules and GUI frameworks | GR5526 SDK |
| FMNA (Apple Find My) | Complete FMNA solution with SDK and corresponding tools and certification process support | Please contact agent support |



### 7.2 Eco-Technology Integration

Goodix Bluetooth LE chipset integrates or partially supports the following IoT technology eco-services, which can be selected by users according to their product needs.

| IoT Technology Ecosystem | Service Description | Chip | Access Methods |
| --------------- | ------------------------------ | ------ | ---------------------------------------------- |
| Amazon FreeRTOS | Amazon FreeRTOS IoT Certification | GR551x | https://github.com/goodix/amazon-freertos |
| RT-Thread | Porting Integrated RT-Thread OS and Driver Framework | GR533x | https://github.com/goodix-ble/GR533x-RT-Thread |




## 8. Technical Services

Goodix Bluetooth LE products provide agent technical service and original community technical service support, which can timely and effectively help users to provide convenient and professional technical services in the pre-demand study, product development and design, technical problem solving, production and testing of various stages, to help users save development time, shorten the development cycle, save the development cost, and quickly land the product to seize the market.

| Technical Services | Remarks |
| --------------------- | ---------------------------------------------- |
| Official Web Channels - Technical Blogs | https://developers.goodix.com/zh/bbs/blog_list |
| Official Web Channels - Technical BBS   | https://developers.goodix.com/zh/bbs/list |
| Official Website Channel - QQ Community | QQ Community No.: 168552615 |
| Agent Channel | Optional Onsite/Remote Technical Support |




