
## GRPLT Lite工具

GRPLT Lite为离线量产板（PLT Lite）配套的配置工具。

### 1. GRPLT Lite基本功能介绍

- 支持GR5515/GR5526/GR5525/GR553x。
- 支持对设备进行晶体校准、RSSI功能测试、应用固件烧录、Flash资源烧录。
- 支持16个设备并联测试（需要多个PLT Lite板级联）。
- 支持端口电平检测启动测试。
- 支持使用QSPI协议直接烧录Flash。

### 2. GRPLT Lite应用笔记

- GRPLT Lite仅会记录烧录失败的结果信息，可通过配置工具读取Log查看。
- 为避免带电插拔导致芯片失效，建议PLT Lite板不测试时对UART断电。
- 应用固件烧录和Flash资源烧录不能混淆，应用固件烧录会更新imageinfo到SCA区域，且将设置的信息写入Boot。
- RSSI功能测试采用扫描方式获取RSSI值。GU开启广播，DUT扫描（GR533x不支持RSSI功能测试）。
- eFuse区域一旦写入，不可逆转，自定义加密信息与I/O LDO的配置需要确认无误后才写入。
- 预烧录模式需要预先将应用固件的.bin文件烧录到对应区域，并将固件的imageinfo烧录到SCA区域，没有imageinfo将无法通过测试。
- GRPLT Lite默认情况下不会对芯片进行全擦，仅对待烧录区域进行擦除。
- 由于GU只有两路UART，多个PLT Lite板级联测试时，GRPLT Lite配置工具不会打印测试信息。

