## RF常见问题



### 1. 射频的PI电路可以简化或移除吗？
* 靠近GR5xx端的PI电路用于匹配芯片内部PA，不能简化和移除。该电路的电感值和电容值不建议改变，建议保持和推荐电路一致，PCB设计遵循对应硬件设计指南相应的RF端口设计要求，如因结构等原因不能完全遵循PCB设计要求，回板后的RF性能不太理想，可以在射频或硬件工程师试验验证后适当地微调参数，通常可以按照PA Load Pull匹配方法来调整参数，详见《GR5xx RF匹配调试指南》。另外，从芯片PI出来后的RF通道上的阻抗是50 Ω，可以兼容市面上任意2.4 GHz频段的天线（2400 MHz～2484 MHz）。
* 靠近天线端的PI电路是用于匹配天线的，该电路可以根据所使用的天线进行更改。天线的匹配问题，可以通过矢量网络分析仪测试S11参数或史密斯圆图进行简单的匹配调节。但是天线的增益、方向性等其他指标则建议寻求专业的天线厂完成匹配测试。



### 2. GR551x如何扩展PA或FEM提高传输距离？

   * GR551x支持扩展外部PA。
   * GPIO2作为外置PA RX使能，GPIO3作为外置PA TX使能信号。
   * 需要在软件中配置对应功能，在RF电路动作TX或RX之前，会把对应的电平拉高，结束后会把电平拉低。
   * GR551x本身不使用这些信号来控制，仅用来控制外接的FEM。



### 3. GR5xx传导灵敏度、发射功率偏低有哪些原因？

   * RF匹配参数是否按照参考设计选型。
   * GR5xx RF布局匹配网络的第一个元器件放置在离RFIO引脚不超过1 mm的位置。
   * RF走线尽可能短而直，如结构限制需要转弯，则转角处要求倒圆弧。禁止出现直角或小于90°夹角走线。
   * RF线优选走表层，避免打过孔换层， 避免走线存在分支，RF走线下方必须保证完整参考地平面。RF线宽尽量设计和匹配器件焊盘一致，避免由于元器件的焊盘宽度与走线宽度不一致而破坏50 Ω传输线特性阻抗的连续性。
   * DC-DC纹波需要低于16 mV。
   * 32M XO晶体时钟需要校准。



### 4. 为什么GR5331/GR5330系列的第一颗匹配电容有两个？

   - 在FCC谐波测试中，需要在高次谐波位置做单独的滤波处理，比如参考设计的0.3 pF物料（GRM0335C1HR30WA01）是特殊选型，在7次谐波位置阻抗点最低（电容的自谐振点），2 pF物料（GRM0335C1H2R0BA01）在3次谐波阻抗位置最低，能够起到比较好的滤波效果。



### 5. 为什么GR533x系列VBAT_RF和GPIO0/1上面有小pF电容？

   - 在FCC谐波测试中，GR533x系列的高次谐波主要通过RF_TX脚及其附近的管脚辐射出来，尤其是VBAT_RF引脚，所以我们特意增加了pF电容在VBAT_RF上。该电容选型也是特挑自谐振点在需要滤波的频段，比如GR5332系列选型3.9 pF（自谐振点在2次谐波位置），GR5331/GR5330系列选型2.0 pF（自谐振点在3次谐波位置）。
   - GPIO0/1在实测过程中也可能存在高次谐波的辐射，不过一般情况下这两个脚的pF电容只是作为调试位置预留，根据实际FCC测试结果来决定是否需要增加pF级电容滤波。
   - 关于如何优化Layout来优化高次谐波，请参考《[GR533x硬件设计指南](https://docs.goodix.com/zh/online/hardware_design_guide_d/V1.2)》的RSE章节。



### 6. GR533x系列调制特性差怎么办？

   - GR533x系列测试若发现调制特性指标比较差（比如典型的df2 99%指标、max drift rate等），或者出现指标Fail蓝牙协议，首先建议切换到SYSLDO供电模式查看，一般情况下都是DCDC电源纹波过大导致。
   - 确定是DCDC电源问题之后建议调整VDD_RF滤波磁珠的参数，请参考《[GR533x Reference Design](https://www.goodix.com/zh/docview/GR533x Reference Design_V1.2?objectId=362&objectType=document&version=609)》推荐磁珠，选型时加大磁珠的DCR参数，一般情况下可以更好地抑制DCDC纹波。
   - 检查DCDC纹波变大的原因，首先检查DCDC Layout的环路，看是否是DCDC IN/OUT的环路过大导致，需要更改PCB Layout，DCDC电源布局请参考《[GR533x硬件设计指南](https://docs.goodix.com/zh/online/hardware_design_guide_d/V1.2)》的电源Layout章节。



### 7. GR533x不同的PCB板子使用参考设计匹配参数达不到GR533x SK板子功率或灵敏度，原因是什么？

   * 导致用户实际匹配参数和参考匹配参数差异的因素包括：
        * 《[GR533x Reference Design](https://www.goodix.com/zh/docview/GR533x Reference Design_V1.2?objectId=362&objectType=document&version=609)》中的匹配参数基于GR533x SK板调试。
        * PCB叠层结构可能会影响RF走线的阻抗和寄生参数。
        * 使用了与参考设计推荐BOM不同的RF射频器件。
        * PCB结构限制导致Layout差异。

   * 基于GR533x进行产品设计时，建议先参考《[GR533x Reference Design](https://www.goodix.com/zh/docview/GR533x Reference Design_V1.2?objectId=362&objectType=document&version=609)》中的推荐匹配器件贴片，然后根据实际产品的PCB叠层和布局，对匹配参数进行微调。详细的匹配调试指南请参考《[GR533x RF匹配调试指南](https://docs.goodix.com/zh/online/rf_matching_bl_d/V1.0)》。


















