
## GRPLT LITE工具

### 1. GRPLT LITE基本功能介绍
- 支持GR5515/GR5526/GR5525/GR553x
- 支持对设备进行晶体校准、RSSI功能测试、应用固件烧录、Flash资源烧录
- 支持16个设备并联测试（需要多个PLT-LITE）
- 支持端口电平检测启动测试
- 支持使用QSPI协议直接烧录Flash

### 2. GRPLT LITE应用笔记

- PLT-LITE仅会记录烧录失败的记录，可通过配置工具读取LOG查看
- 为避免带电插拔导致芯片失效，PLT-LITE不测试时对UART断电
- 应用固件烧录和Flash资源烧录不能混淆，应用固件烧录会更新imageinfo到SCA区域，且将设置的信息写入boot
- RSSI功能测试采用扫描的方式获取RSSI值，GU开启广播，DUT扫描
- eFuse区域一旦写入，不可逆转，自定义加密信息与I/O LDO的配置需要确认无误才写入
- 预烧录模式需要预先将应用固件的bin文件烧录到对应的区域，同时将固件的imageinfo烧录到SCA区域，没有imageinfo将无法通过测试
- PLT-LITE默认情况不会对芯片进行全擦，仅对需要烧录的区域进行擦除
- PLT-LITE在并联时不会打印测试信息，这是因为GU只有两路UART
