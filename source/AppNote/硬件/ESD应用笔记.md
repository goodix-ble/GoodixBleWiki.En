## ESD应用笔记



### 1. GR5xx系列芯片ESD性能介绍

* GR551x系列芯片级ESD性能：HBM (Human Body Model) = 2000 V, CDM (Charged Device Model) = 500 V。

* GR5526系列芯片级ESD性能：HBM (Human Body Model) = 2000 V, CDM (Charged Device Model) = 500 V。
* GR533x系列芯片级ESD性能：HBM @ All pins = 2000 V, CDM @ All pins (excluding the antenna pin) = 500 V. The ESD CDM of GR533x is rated at 400 V on the antenna pin.

* GR5525系列芯片级ESD性能：HBM @ All pins = 2000 V, CDM @ All pins (excluding the antenna pin) = 500 V. The ESD CDM of GR5525 is rated at 400 V on the antenna pin.
* JEDEC document JEP157 states that 250-V CDM allows secure manufacturing with a standard ESD control process.

* 系统级ESD（Electrostatic Discharge）是一个产品整机的衡量指标，与电子产品设备的设计、制造和使用密切相关。为了能够满足整机系统级ESD需求，使用GR5xx系列芯片开发产品时，工程师在原理图、PCB和产品结构设计方面须遵循相应的设计规则，具体可以参考对应芯片系列《硬件设计指南》中“系统ESD防护设计”章节。

### 2. GR5xx系列芯片ESD应用笔记

* GR5xx系列芯片建议均采用单独LDO/DCDC供电。
* GR5xx系列芯片建议在产品电源输入接口处分别串接磁珠，可衰减静电能量，并在磁珠前端增加TVS管进行ESD防护处理。

* GR5xx系列芯片建议对于金属外壳的产品，应在金属外壳地与主板地之间连接磁珠，避免静电干扰直接进入主板。

* GR551x系列芯片，在针对手表、手环等产品场景，如果产品系统静电指标为空气放电±8 kV、接触放电±4 kV以上时，需要另外增加外部看门狗等复位机制来增强产品系统ESD防护能力。
  
* GR5525系列芯片建议在VBATL引脚并联一个TVS管（推荐：µClamp03301ZA），用于提高系统的静电放电（ESD）能力。

* GR5xx系列芯片PCB Layout设计要点参考对应芯片系列《硬件设计指南》中“系统ESD防护设计”章节。

* GR5xx系列芯片GND设计尤为重要，如DCDC的VSS_BUCK GND管脚需要靠近输入电容（10 µF）地脚，减少电源/GND回路阻抗抑制地噪声。

* GR5xx系列芯片打ESD的PIN脚，如外露的电源充电口、通信接口等，不能靠近时钟、Reset、通信等敏感信号，同时需要对其做包地隔离处理。

* GR5xx系列芯片除了在芯片设计上要注意，在产品结构设计以及生产、运输、调试阶段都要遵循相应的ESD注意事项。参考对应芯片系列《硬件设计指南》中“系统ESD防护设计”关于结构和生产的章节。

