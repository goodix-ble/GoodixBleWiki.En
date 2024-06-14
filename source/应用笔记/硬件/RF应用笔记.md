## RF应用笔记




### 1. GR5xx RF介绍

* GR551x系列芯片RF指标

  * Bluetooth LE Connectivity：Bluetooth LE 5.1
  * 支持数据传输速率：1 Mbps、2 Mbps、LR（500 kbps、125 kbps）
  * 发射功率：–20 dBm ～ +7 dBm
  * 96 dBm接收灵敏度（1 Mbps模式下）
  * –93 dBm接收灵敏度（2 Mbps模式下）
  * –99 dBm接收灵敏度（LR 500 kbps模式下）
  * –102 dBm接收灵敏度（LR 125 kbps模式下）
  * TX功耗：5.6 mA @ 0 dBm, 1 Mbps
  * RX功耗：4.8 mA @ 1 Mbps

* GR5526系列芯片RF指标

  * Bluetooth LE Connectivity：Bluetooth LE 5.3
  * 支持数据传输速率：1 Mbps、2 Mbps、LR（500 kbps、125 kbps）
  * 发射功率：–20 dBm ～ +7 dBm
  * –98 dBm接收灵敏度（1 Mbps模式下）
  * –94 dBm接收灵敏度（2 Mbps模式下）
  * –101 dBm接收灵敏度（LR 500 kbps模式下）
  * –104 dBm接收灵敏度（LR 125 kbps模式下） 
  * TX功耗: 4.0 mA @ 0 dBm, 1 Mbps
  * RX功耗: 3.5 mA @ 1 Mbps
  * AoA/AoD、LE同步通道

* GR5525系列芯片RF指标

  * Bluetooth LE Connectivity：Bluetooth LE 5.3
  * 支持数据传输速率：1 Mbps、2 Mbps、LR（500 kbps、125 kbps）
  * 发射功率：–20 dBm ～ +7 dBm
  * –97 dBm接收灵敏度（1 Mbps模式下）
  * –93 dBm接收灵敏度（2 Mbps模式下）
  * –101 dBm接收灵敏度（LR 500 kbps模式下）
  * –103 dBm接收灵敏度（LR 125 kbps模式下）
  * TX功耗：6.3 mA @ 0 dBm输出功率（64 MHz系统时钟）
  * RX功耗：5.3 mA @ 1 Mbps（64 MHz系统时钟）  

* GR533x系列芯片RF指标

  * Bluetooth LE Connectivity：Bluetooth LE 5.3

  * 支持数据传输速率：1 Mbps、2 Mbps、LR（500 kbps、125 kbps）

  * 发射功率：
    GR5330/GR5331：高达6 dBm
    GR5332：高达15 dBm

  * 接收灵敏度：

    GR5330/GR5331：–97.5 dBm @ 1 Mbps
    GR5332：–99 dBm @ 1 Mbps

  * GR5330/GR5331功耗 @ 3.3 V VBAT输入：
    TX功耗：3.8 mA @ 0 dBm输出功率（DC-DC供电、16 MHz系统时钟）
    RX功耗：4.7 mA @ 1 Mbps（DC-DC供电、16 MHz系统时钟）

  * GR5332功耗 @ 3.3 V VBAT：
    TX功耗：5.9 mA @ 0 dBm输出功率（DC-DC供电、16 MHz系统时钟）
    TX功耗：86.3 mA @ 15 dBm输出功率（SYS_LDO供电、64 MHz系统时钟）
    RX功耗：4.9 mA @ 1 Mbps（DC-DC供电、16MHz系统时钟）

### 2. GR5xx RF应用笔记

- GR533x系列不同型号支持不同的PA类型，GR5332系列支持HPA（–10 dBm～+15 dBm）和SPA（–20 dBm～+5 dBm），GR5331/GR5330系列支持SPA（–20 dBm～+6 dBm）和UPA（–15 dBm～+2 dBm）。
- GR5332系列使用HPA工作时，只能使用SYSLDO供电模式。
- GR5331/GR5330仅使用UPA模式的情况下可以简化匹配BOM数量。
- GR533x的RF PA介绍详情请参考《[GR533x RF PA应用指南](https://docs.goodix.com/zh/online/rf_pa_bl_d/V1.2)》。
- RF端口匹配器件布局应遵循PCB设计要求，匹配网络中的元器件应尽可能地靠近RF引脚（即RF_RX与RF_TX），并将匹配网络的第一个元器件放置在离RF引脚不超过1 mm的位置。
- RF走线尽可能短而直，如结构限制需要转弯，则转角处要求倒圆弧。禁止出现直角或小于90°夹角走线。
- RF线优选走表层，避免打过孔换层，避免走线存在分支，RF走线下方必须保证完整参考地平面。RF走线与芯片Pin之间建议走渐变线，并且RF线宽尽量设计和匹配器件焊盘一致，避免由于元器件的焊盘宽度与走线宽度不一致而破坏50 Ω传输线特性阻抗的连续性。
- DCDC纹波对RF性能影响较大，不合理的DCDC接地回路会影响RF性能指标，建议按照设计指南要求合理设计DCDC外围器件布局，尽可能减小接地回路路径，将DCDC纹波控制在小于16 mV。
- RF指标需要校准晶体后再进行测试。

