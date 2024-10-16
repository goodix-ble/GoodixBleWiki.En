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

-  [Goodix Bluetooth LE SoC Selection Chart](https://www.goodix.com/zh/down/resource/Goodix_Bluetooth_Chipset_Selection_Guide?objectId=5&objectType= design_resource&version=64) 

![](../_images/goodi_ble_chipset_select_guide.png)

## 3. Get the chip SDK development kit

| Bluetooth LE SoC | SDK Download Link | Note |
| ---------------- | -------------------------------------------------- | -------------- |
| GR551x | https://www.goodix.com/en/software_tool/gr551x_sdk | Please download the latest version |
| GR5525 | https://www.goodix.com/en/software_tool/gr5525_sdk | Please download the latest version |
| GR5526 | https://www.goodix.com/en/software_tool/gr5526_sdk | Please download the latest version |
| GR533x | https://www.goodix.com/en/software_tool/gr533x_sdk | Please download the latest version |



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
| GProgrammer | Program Resource Burning and Configuration Tool | chip firmware burning tool for development , supporting firmware download, Flash read/write, eFuse burning, firmware encryption and signing and other functions. At the mass production stage, the PLT Lite and GRPLT Lite configuration tools can be used for batch burn-in testing of Bluetooth LE series chips. | https://www.goodix.com/zh/software_tool/gprogrammer_ble | All Bluetooth SoC |
| GRToolbox | Mobile Development and Verification App | A mobile tool designed specifically for Goodix BLE products, providing Android & iOS versions, which can scan, configure connection parameters, demonstrate standard profiles, and debug Profiles/Services of Goodix BLE platform. | https://www.goodix.com/zh/software_tool/grtoolbox | All Bluetooth SoC |
| GRDirect Test Mode Tool| DTM Test Tool | Used for Goodix BLE DTM (Direct Test Mode) | https://www.goodix.com/zh/download?objectId=107&objectType=software | All Bluetooth SoC |
| GRPLT Lite | Product Line Tool | As a supporting tool for PLT Lite, customers can use this software to package the developed application firmware, resource files, mass production configuration, etc., and download them to PLT Lite through the serial port. | https://www.goodix.com/zh/software_tool/grplt_lite | All Bluetooth SoC |
| GRUart | Serial port debugging assistant | PC serial port debugging assistant for serial port log and protocol stack log printing | https://www.goodix.com/zh/download?objectId=64&objectType=software | All Bluetooth SoC |
| NemaPixpresso | Image Resource Generator Tool | Used for conversion of pictures and various image formats, also for FrameBuffer analysis | Packaged in  LouisUI | GR5526 |
| gdx_font_conv | Font Resource Generator Tool | For generating LVGL font files that support GPU rendering | https://developers.goodix.com/zh/bbs/blog_detail/6b29cdf5923247029f4357a65de1b065 | GR5526 |
| LouisUI | Image Resource Generator Tool | Used to batch generate LVGL-compliant and GPU-renderable .bin format for image resources and generate resource descriptor files. | https://developers.goodix.com/zh/bbs/blog_detail/2996e8f9f352491eb0ccca468f28f2ce | GR5526 |
| GRPPK | Power Consumption Test Tool | Evaluation of power consumption of products with PPK boards | Consulting Agents | All Bluetooth SoC |
| OTA SDK | Mobile Firmware | Android & iOS DFU/OTA SDK | https://developers.goodix.com/zh/bbs/detail/32869e79a7c84917b32ecb4ab10acac8 | All Bluetooth SoC |


## 6. Obtaining Chip Development Documentation

- Chip interface reference manuals are located in the documentation directory of each chip SDK.

- The software design, hardware design, and sample project reference documents of the chips are open source and can be downloaded from the official website of Huitian.

  

### 6.1 GR551x Documents

https://www.goodix.com/en/product/connectivity/ble/gr551x

| Document | Privileges |
| ------------------------------------ | ---------- |
| [Getting Started with Bluetooth LE Device](https://docs.goodix.com/en/online/bluetooth_le_getting_started/Rev.2.6) | For Public          |
| [GR551x Datasheet](https://docs.goodix.com/en/online/gr551x_datasheet/Rev.2.9) | For Public          |
| [GR551x Errata Note](https://docs.goodix.com/en/online/gr551x_errata/Rev.1.2) | For Public          |
| [GR5515 Starter Kit User Guide](https://docs.goodix.com/en/online/gr5515_starter_kit_user_guide/Rev.2.0) | For Public          |
| [GProgrammer User Manual](https://docs.goodix.com/en/online/gprogrammer_user_guide/Rev.3.2) | For Public          |
| [GR5xx IAR User Manual](https://docs.goodix.com/en/online/gr5xx_iar_guide/Rev.1.1) | For Public          |
| [GRPLT Lite Config Tool User Manual](https://docs.goodix.com/en/online/grplt_lite_configuration_tool_user_guide/Rev.1.7) | For Public          |
| [GR5xx GCC User Manual](https://docs.goodix.com/en/online/gr5xx_gcc_guide/Rev.1.0) | For Public          |
| [GR551x FCC RSE Certification Note](https://docs.goodix.com/en/online/fcc_rse_certificate_bl_a/Rev.1.1) | For Public          |
| [GR551x Developer Guide](https://docs.goodix.com/en/online/gr551x_develop_guide/Rev.2.7) | For Public          |
| [GR5515I0NDA Flash Selection Guide](https://docs.goodix.com/en/online/gr5515_flash_selection_guide/Rev.1.4) | For Public          |
| [GR551x Hardware Design Guidelines](https://docs.goodix.com/en/online/gr551x_hardware_design_guide/Rev.2.6) | For Public          |
| [GR551x Reference Design](https://www.goodix.com/en/docview/GR551x Reference Design_Rev.1.5?objectId=190&objectType=document&version=352) | Register Users Only |
| [GR5515-SK-BASIC-RevE](https://www.goodix.com/en/docview/GR5515-SK-BASIC-RevE_Rev.1.6?objectId=135&objectType=document&version=354) | For Public          |
| [GR5515-SK-BASIC-RevC](https://www.goodix.com/en/docview/GR5515-SK-BASIC-RevC _Rev.1.5?objectId=56&objectType=document&version=79) | For Public          |
| [GR551x API Reference](https://docs.goodix.com/en/online/api/gr551x_api_reference/Rev.2.0.2) | For Public          |
| [GR5xx Sample Service Application and Customization](https://docs.goodix.com/en/online/custom_sample_service_bl/Rev.3.1) | For Public          |
| [GR5xx HID Mouse Example Application](https://docs.goodix.com/en/online/hid_mouse_bl/Rev.3.2) | For Public          |
| [GR5xx Serial Port Profile Example Application](https://docs.goodix.com/en/online/serial_port_bl/Rev.3.1) | For Public          |
| [GR5xx Power Consumption Profile Example Application](https://docs.goodix.com/en/online/power_consumption_bl/Rev.3.1) | For Public          |
| [GR5xx HRS RSCS Relay Example Application](https://docs.goodix.com/en/online/hrs_rscs_relay_bl/Rev.3.1) | For Public          |
| [GR5xx FreeRTOS Example Application](https://docs.goodix.com/en/online/freertos_bl/Rev.3.1) | For Public          |
| [GR5xx Throughput Example Application](https://docs.goodix.com/en/online/throughput_bl/Rev.3.1) | For Public          |
| [GR5xx AT Command Example Application](https://docs.goodix.com/en/online/at_command_bl/Rev.3.1) | For Public          |
| [GR5xx ANCS Profile Example Application](https://docs.goodix.com/en/online/ancs_profile_bl/Rev.3.1) | For Public          |
| [GR5xx AMS Profile Example Application](https://docs.goodix.com/en/online/ams_profile_bl/Rev.3.1) | For Public          |
| [GR5xx DTM Test Application Note](https://docs.goodix.com/en/online/dtm_test_bl/Rev.3.5) | For Public          |
| [GR5xx APP Log Application Note](https://docs.goodix.com/en/online/app_log_bl/Rev.3.2) | For Public          |
| [GR5xx Fault Trace Module Application Note](https://docs.goodix.com/en/online/fault_trace_bl/Rev.3.2) | For Public          |
| [GR5xx Firmware Encryption Application Note](https://docs.goodix.com/en/online/firmware_encryption_bl/Rev.3.0) | For Public          |
| [GRPLT Lite Config Tool Customized Firmware   Encryption Application Note](https://docs.goodix.com/en/online/grplt_lite_config_tool_customized_firmware_encryption/Rev.1.5) | For Public          |
| [GR551x Power Mode and Power Consumption Measurement   Application Note](https://docs.goodix.com/en/online/gr551x_sleep_mode_power_measure_note/Rev.2.1) | For Public          |
| [GR551x Reliability Test Report](https://docs.goodix.com/en/online/reliablity_report_bl_a/Rev.1.3) | For Public          |
| [GR551x MCD](https://www.goodix.com/en/docview/GR551x MCD_Rev.1.0?objectId=188&objectType=document&version=348) | For Public          |



### 6.2 GR5525 Documents

https://www.goodix.com/en/product/connectivity/ble/gr5525

| Document | Privileges |
| ---------------------------- | ---------- |
| [GR5525 Product Brief](https://www.goodix.com/en/docview/GR5525 Product Brief_Rev.1.1?objectId=213&objectType=document&version=511) | For Public          |
| [GR5525 Datasheet](https://docs.goodix.com/en/online/datasheet_bl_c/Rev.1.2) | For Public          |
| [GR5525 Starter Kit User Guide](https://docs.goodix.com/en/online/starter_kit_manual_bl_c/Rev.1.2) | For Public          |
| [GR5525 Display Refresh Module Guide](https://docs.goodix.com/en/online/display_guide_bl_c/Rev.1.2) | For Public          |
| [GR5525 Developer Guide](https://docs.goodix.com/en/online/developer_guide_bl_c/Rev.1.2) | For Public          |
| [GProgrammer User Manual](https://docs.goodix.com/en/online/gprogrammer_user_guide/Rev.3.2) | For Public          |
| [GR5xx IAR User Manual](https://docs.goodix.com/en/online/gr5xx_iar_guide/Rev.1.1) | For Public          |
| [GRPLT Lite Config Tool User Manual](https://docs.goodix.com/en/online/grplt_lite_configuration_tool_user_guide/Rev.1.7) | For Public          |
| [GR5xx GCC User Manual](https://docs.goodix.com/en/online/gr5xx_gcc_guide/Rev.1.0) | For Public          |
| [GR5525 Reference Design](https://www.goodix.com/en/docview/GR5525 Reference Design_Rev.1.3?objectId=216&objectType=document&version=514) | Register Users Only |
| [GR5525 Hardware Design Guidelines](https://docs.goodix.com/en/online/hardware_design_guide_bl_c/Rev.1.3) | For Public          |
| [GR5525-SK-BASIC-RevB](https://www.goodix.com/en/docview/GR5525-SK-BASIC-RevB_Rev.1.1?objectId=218&objectType=document&version=513) | For Public          |
| [GR5525 API Reference](https://docs.goodix.com/en/online/api/api_reference_bl_c/Rev.1.0.2) | For Public          |
| [GR5xx Sample Service Application and Customization](https://docs.goodix.com/en/online/custom_sample_service_bl/Rev.3.1) | For Public          |
| [GR5xx HID Mouse Example Application](https://docs.goodix.com/en/online/hid_mouse_bl/Rev.3.2) | For Public          |
| [GR5xx Serial Port Profile Example Application](https://docs.goodix.com/en/online/serial_port_bl/Rev.3.1) | For Public          |
| [GR5xx Power Consumption Profile Example Application](https://docs.goodix.com/en/online/power_consumption_bl/Rev.3.1) | For Public          |
| [GR5xx HRS RSCS Relay Example Application](https://docs.goodix.com/en/online/hrs_rscs_relay_bl/Rev.3.1) | For Public          |
| [GR5xx FreeRTOS Example Application](https://docs.goodix.com/en/online/freertos_bl/Rev.3.1) | For Public          |
| [GR5xx Throughput Example Application](https://docs.goodix.com/en/online/throughput_bl/Rev.3.1) | For Public          |
| [GR5xx AT Command Example Application](https://docs.goodix.com/en/online/at_command_bl/Rev.3.1) | For Public          |
| [GR5xx ANCS Profile Example Application](https://docs.goodix.com/en/online/ancs_profile_bl/Rev.3.1) | For Public          |
| [GR5xx AMS Profile Example Application](https://docs.goodix.com/en/online/ams_profile_bl/Rev.3.1) | For Public          |
| [GR5xx DFU Development Application Note](https://docs.goodix.com/en/online/firmware_upgrade_bl/Rev.1.6) | For Public          |
| [GR5xx DTM Test Application Note](https://docs.goodix.com/en/online/dtm_test_bl/Rev.3.5) | For Public          |
| [GR5xx APP Log Application Note](https://docs.goodix.com/en/online/app_log_bl/Rev.3.2) | For Public          |
| [GR5xx Fault Trace Module Application Note](https://docs.goodix.com/en/online/fault_trace_bl/Rev.3.2) | For Public          |
| [GR5xx Firmware Encryption Application Note](https://docs.goodix.com/en/online/firmware_encryption_bl/Rev.3.0) | For Public          |
| [GRPLT Lite Config Tool Customized Firmware   Encryption Application Note](https://docs.goodix.com/en/online/grplt_lite_config_tool_customized_firmware_encryption/Rev.1.5) | For Public          |
| [GR5525 MCD](https://www.goodix.com/en/docview/GR5525 MCD_Rev.1.1?objectId=214&objectType=document&version=515) | For Public          |
| [GR5525 Reliability Test Report](https://docs.goodix.com/en/online/reliablity_report_bl_c/Rev.1.0) | For Public          |



### 6.3 GR5526 Documents
https://www.goodix.com/en/product/connectivity/ble/gr5526

| Document | Privileges |
| ------------------------------ | ---------- |
| [Getting Started with Bluetooth LE Device](https://docs.goodix.com/en/online/bluetooth_le_getting_started/Rev.2.6) | For Public          |
| [GR5526 Product Brief](https://www.goodix.com/en/docview/GR5526 Product Brief_Rev.1.2?objectId=100&objectType=document&version=309) | For Public          |
| [GR5526 Datasheet](https://docs.goodix.com/en/online/datasheet_bl_b/Rev.1.2) | For Public          |
| [GR5526 Starter Kit User Guide](https://docs.goodix.com/en/online/starter_kit_manual_bl_b/Rev.1.1) | For Public          |
| [GProgrammer User Manual](https://docs.goodix.com/en/online/gprogrammer_user_guide/Rev.3.2) | For Public          |
| [GR5xx IAR User Manual](https://docs.goodix.com/en/online/gr5xx_iar_guide/Rev.1.1) | For Public          |
| [GR5526 Hardware Design Guidelines](https://docs.goodix.com/en/online/hardware_design_guidelines_bl_b/Rev.1.2) | For Public          |
| [GRPLT Lite Config Tool User Manual](https://docs.goodix.com/en/online/grplt_lite_configuration_tool_user_guide/Rev.1.7) | For Public          |
| [GR5xx GCC User Manual](https://docs.goodix.com/en/online/gr5xx_gcc_guide/Rev.1.0) | For Public          |
| [GR5526 Display Refresh Module Guide](https://docs.goodix.com/en/online/display_refresh_guide_bl_b/Rev.1.0) | For Public          |
| [GR5526 Developer Guide](https://docs.goodix.com/en/online/developer_guide_bl_b/Rev.1.0) | For Public          |
| [GR5526 Reference Design](https://www.goodix.com/en/docview/GR5526 Reference Design_Rev.1.0?objectId=158&objectType=document&version=312) | Register Users Only |
| [GR5526-SK-BASIC-RevC](https://www.goodix.com/en/docview/GR5526-SK-BASIC-RevC_Rev.1.0?objectId=159&objectType=document&version=313) | For Public          |
| [GR5526 API Reference](https://docs.goodix.com/en/online/api/api_reference_bl_b/Rev.1.0.3) | For Public          |
| [GR5xx Sample Service Application and Customization](https://docs.goodix.com/en/online/custom_sample_service_bl/Rev.3.1) | For Public          |
| [GR5xx HID Mouse Example Application](https://docs.goodix.com/en/online/hid_mouse_bl/Rev.3.2) | For Public          |
| [GR5xx Serial Port Profile Example Application](https://docs.goodix.com/en/online/serial_port_bl/Rev.3.1) | For Public          |
| [GR5xx Power Consumption Profile Example Application](https://docs.goodix.com/en/online/power_consumption_bl/Rev.3.1) | For Public          |
| [GR5xx HRS RSCS Relay Example Application](https://docs.goodix.com/en/online/hrs_rscs_relay_bl/Rev.3.1) | For Public          |
| [GR5xx FreeRTOS Example Application](https://docs.goodix.com/en/online/freertos_bl/Rev.3.1) | For Public          |
| [GR5xx Throughput Example Application](https://docs.goodix.com/en/online/throughput_bl/Rev.3.1) | For Public          |
| [GR5xx AT Command Example Application](https://docs.goodix.com/en/online/at_command_bl/Rev.3.1) | For Public          |
| [GR5xx ANCS Profile Example Application](https://docs.goodix.com/en/online/ancs_profile_bl/Rev.3.1) | For Public          |
| [GR5xx AMS Profile Example Application](https://docs.goodix.com/en/online/ams_profile_bl/Rev.3.1) | For Public          |
| [GR5xx DFU Development Application Note](https://docs.goodix.com/en/online/firmware_upgrade_bl/Rev.1.6) | For Public          |
| [GR5xx DTM Test Application Note](https://docs.goodix.com/en/online/dtm_test_bl/Rev.3.5) | For Public          |
| [GR5xx APP Log Application Note](https://docs.goodix.com/en/online/app_log_bl/Rev.3.2) | For Public          |
| [GR5xx Fault Trace Module Application Note](https://docs.goodix.com/en/online/fault_trace_bl/Rev.3.2) | For Public          |
| [GR5xx Firmware Encryption Application Note](https://docs.goodix.com/en/online/firmware_encryption_bl/Rev.3.0) | For Public          |
| [GRPLT Lite Config Tool Customized Firmware   Encryption Application Note](https://docs.goodix.com/en/online/grplt_lite_config_tool_customized_firmware_encryption/Rev.1.5) | For Public          |
| [GR5526 Reliability Test Report](https://docs.goodix.com/en/online/reliablity_report_bl_b/Rev.1.0) | For Public          |
| [GR5526 MCD](https://www.goodix.com/en/docview/GR5526 MCD_Rev.1.1?objectId=156&objectType=document&version=310) | For Public          |



### 6.4 GR533x Documents
https://www.goodix.com/en/product/connectivity/ble/gr533x


| Document | Privileges |
| ------------------------------------- | ---------- |
| [GR533x Product Brief](https://www.goodix.com/en/docview/GR533x Product Brief_Rev.1.3?objectId=222&objectType=document&version=498) | For Public          |
| [GR533x Datasheet](https://docs.goodix.com/en/online/datasheet_bl_d/Rev.1.3) | For Public          |
| [GR5331 Starter Kit User Guide](https://docs.goodix.com/en/online/starter_kit_manual_bl_d/Rev.1.1) | For Public          |
| [GR533x Developer Guide](https://docs.goodix.com/en/online/developer_guide_bl_d/Rev.1.3) | For Public          |
| [GProgrammer User Manual](https://docs.goodix.com/en/online/gprogrammer_user_guide/Rev.3.2) | For Public          |
| [GR5xx IAR User Manual](https://docs.goodix.com/en/online/gr5xx_iar_guide/Rev.1.1) | For Public          |
| [GRPLT Lite Config Tool User Manual](https://docs.goodix.com/en/online/grplt_lite_configuration_tool_user_guide/Rev.1.7) | For Public          |
| [GR5xx GCC User Manual](https://docs.goodix.com/en/online/gr5xx_gcc_guide/Rev.1.0) | For Public          |
| [PLT Lite User Manual](https://docs.goodix.com/en/online/plt_lite_guide_bl/Rev.1.0) | For Public          |
| [PLT Lite Mass Production Programming Guide](https://docs.goodix.com/en/online/plt_lite_programming_guide_bl/Rev.1.0) | For Public          |
| [GR533x LCP Developer Guide](https://docs.goodix.com/en/online/lcp_bl_d/Rev.1.0) | For Public          |
| [GR533x Module Reference Design](https://www.goodix.com/en/docview/GR533x Module Reference Design_Rev.1.3?objectId=226&objectType=document&version=504) | Register Users Only |
| [GR533x Reference Design](https://www.goodix.com/en/docview/GR533x Reference Design_Rev.1.4?objectId=225&objectType=document&version=503) | Register Users Only |
| [GR533x Hardware Design Guidelines](https://docs.goodix.com/en/online/hardware_design_guide_bl_d/Rev.1.4) | For Public          |
| [GR5331-SK-BASIC-RevC](https://www.goodix.com/en/docview/GR5331-SK-BASIC-RevC_Rev.1.0?objectId=229&objectType=document&version=411) | For Public          |
| [GR533x API Reference](https://docs.goodix.com/en/online/api/api_reference_bl_d/Rev.1.0.6) | For Public          |
| [GR5xx Sample Service Application and Customization](https://docs.goodix.com/en/online/custom_sample_service_bl/Rev.3.1) | For Public          |
| [GR5xx HID Mouse Example Application](https://docs.goodix.com/en/online/hid_mouse_bl/Rev.3.2) | For Public          |
| [GR5xx Serial Port Profile Example Application](https://docs.goodix.com/en/online/serial_port_bl/Rev.3.1) | For Public          |
| [GR5xx Power Consumption Profile Example Application](https://docs.goodix.com/en/online/power_consumption_bl/Rev.3.1) | For Public          |
| [GR5xx HRS RSCS Relay Example Application](https://docs.goodix.com/en/online/hrs_rscs_relay_bl/Rev.3.1) | For Public          |
| [GR5xx FreeRTOS Example Application](https://docs.goodix.com/en/online/freertos_bl/Rev.3.1) | For Public          |
| [GR5xx Throughput Example Application](https://docs.goodix.com/en/online/throughput_bl/Rev.3.1) | For Public          |
| [GR5xx AT Command Example Application](https://docs.goodix.com/en/online/at_command_bl/Rev.3.1) | For Public          |
| [GR5xx ANCS Profile Example Application](https://docs.goodix.com/en/online/ancs_profile_bl/Rev.3.1) | For Public          |
| [GR5xx AMS Profile Example Application](https://docs.goodix.com/en/online/ams_profile_bl/Rev.3.1) | For Public          |
| [GR533x Mesh Simple On Off Models Example Application](https://docs.goodix.com/en/online/mesh_sso_bl_d/Rev.1.1) | For Public          |
| [GR533x Mesh Light Lightness Models Example   Application](https://docs.goodix.com/en/online/mesh_lln_bl_d/Rev.1.1) | For Public          |
| [GR533x RF PA Application Note](https://docs.goodix.com/en/online/rf_pa_bl_d/Rev.1.4) | For Public          |
| [GR533x Power Consumption Measurement User Guide](https://docs.goodix.com/en/online/power_measure_bl_d/Rev.1.4) | For Public          |
| [GR5xx DFU Development Application Note](https://docs.goodix.com/en/online/firmware_upgrade_bl/Rev.1.6) | For Public          |
| [GR5xx DTM Test Application Note](https://docs.goodix.com/en/online/dtm_test_bl/Rev.3.5) | For Public          |
| [GR5xx APP Log Application Note](https://docs.goodix.com/en/online/app_log_bl/Rev.3.2) | For Public          |
| [GR5xx Fault Trace Module Application Note](https://docs.goodix.com/en/online/fault_trace_bl/Rev.3.2) | For Public          |
| [GR533x Reliability Test Report](https://docs.goodix.com/en/online/reliablity_report_bl_d/Rev.1.1) | For Public          |
| [GR533x MCD](https://www.goodix.com/en/docview/GR533x MCD_Rev.1.0?objectId=223&objectType=document&version=405) | For Public          |
| [GR533x RF Matching Guidelines](https://docs.goodix.com/en/online/rf_matching_bl_d/Rev.1.2) | For Public          |



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




