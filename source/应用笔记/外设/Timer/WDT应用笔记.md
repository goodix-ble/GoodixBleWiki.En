# WDT应用笔记 #

## 1. GR5xx WDT基本功能介绍

- 芯片内部有Always-on Watchdog（AON_WDT）和System Watchdog。区别在于前者在Always-On区域，基于芯片内部慢速时钟计时，芯片睡眠态可以继续工作；后者在MCU System域，基于芯片高速时钟计时，芯片睡眠时该模块会掉电停止工作。在应用开发中推荐用AON_WDT。
- AON_WDT的时钟源是系统的慢速时钟，频率在30 kHz～50 kHz。我们SDK会对慢速时钟源频率进行校准（重新测算），所以对应的Reload值可能不一样。
- WDT的Reset功能：从设置的32bit Counter值往下计数，当Counter减到0时会产生系统Reset操作。
- WDT 的Alarm中断功能：当Counter值减到与设置的Alarm相等时，会产生Alarm中断，可以用来记录看门狗复位前的一些信息。注意，GR551x的Alarm值只有5bit，对应的最大时间是1 ms不到；其他芯片的Alarm值是16bit，对应的最大时间接近2s。因此，GR551x不能在Alarm中断里做复杂操作，可能中断刚响应进去就到Reset时间而产生芯片复位了。

## 2. GR5xx WDT应用笔记

- 如何设置看门狗Reset时间和Alarm时间

  - 通过设置aon_wdt_init_t结构体的Counter成员变量和alarm_counter成员变量，然后调用app_aon_wdt_init接口来实现。
  - 注意GR551x的Counter单位是Tick，根据与慢速时钟频率的关系可以转换得到对应的ms时间；其他芯片的Counter单位是ms，根据与慢速时钟频率的关系可以转换得到对应的Tick个数。alarm_counter的单位也是这样定义。Tick与ms的互相转换公式，可参考头文件对aon_wdt_init_t结构体的描述说明。
  - GR551x的alarm_counter在API接口无意义，内部实现用最大的5bit alarm_counter值（对应的具体时间约为1 ms）；其他芯片的alarm_counter值受16bit范围的限制，对应单位为ms的数值不能超过2000。
  - 更多参数的设置和接口调用，参考《[GR5xx APP用户驱动手册](https://docs.goodix.com/zh/online/detail/app_driver_bl/V1.4/cca9c0c5cf27f9dde90a1aa5d875e1af)》的“APP AON_WDT驱动”章节。
- 如何判断系统复位是否为看门狗复位

  - GR551x系列可以通过查询AON_WDT Reboot Event Flag来判断是否产生了WDT复位，但是要注意，该标志在platform_init里面会被清除，所以需要在platform_init之前读取。

  - GR5525/GR5526/GR533x系列由于内部有复位原因寄存器，可以通过查询复位原因寄存器来判断是否为WDT复位。

  - 以上判断复位原因的具体方法，可参考论坛上的经验分享“[GR55xx 判断复位原因方法分享](https://developers.goodix.com/zh/bbs/detail/5ec2641ffd0a4afdb5103ad1ea4a3a3e)”。

- 如何记录看门狗复位前的现场信息

  - 利用WDT的Alarm中断功能，设置合理的Alarm值，当系统繁忙来不及喂狗时，WDT的Counter会减到Alarm值，此时会触发Alarm中断。在Alarm中断里可以记录现场信息，有助于分析系统来不及喂狗的原因。
  - 在WDT Alarm中断里记录现场信息的方法，与在HardFault_Handler里记录死机现场信息的方法是一样的，用户可参考我们SDK的HardFault_Handler处理方法进行记录；用户也可以在Alarm中断里实现自己的记录方法。
  - 需要注意的是，GR551x产生Alarm中断的时刻离芯片复位的时间非常接近（1 ms不到），所以可能来不及记录就产生复位了。可以尝试在hal_aon_wdt_alarm_callback函数中喂狗后再进行记录。具体可参考社区问题讨论“[如何记录复位原因](https://developers.goodix.com/zh/bbs/detail/fb6ade9f85d84fbd8b3b596062b08fe3)”。
- 看门狗复位是复位哪些域

  看门狗复位会把Bluetooth LE域、MCU域、AON域等都复位，效果与硬件复位和冷启动是一样的。

