# WDT应用笔记 #

## 1. GR5xx WDT 基本功能介绍

- 芯片内部有Always-on Watchdog（AON_WDT）  和 System Watchdog。区别在于前者在Always-On区域，基于芯片内部慢速时钟计时，芯片睡眠态可以继续工作；后者在mcu system域，基于芯片高速时钟计时，芯片睡眠时会该模块会掉电停止工作。在应用开发中推荐用AON_WDT。
- AON_WDT的时钟源是系统的慢速时钟，频率在30KHZ~50KHZ。我们SDK会对慢速时钟源频率进行校准（重新测算），所以对应的reload值可能不一样。
- WDT 的RESET功能：从设置的32bit Counter值往下计数，当Counter减到0时会产生系统reset的操作。
- WDT 的ALARM中断功能：当Counter值减到与设置的alarm相等时，会产生alarm中断，可以用来记录看门狗复位前的一些信息。注意，GR551x的alarm值只有5bit，对应的最大时间是1ms不到；其他芯片的alarm值是16bit，对应的最大时间有接近2S。因此，GR551x不能在alarm中断里做复杂操作，可能中断刚响应进去就到reset时间而产生芯片复位了。

## 2. GR5xx WDT 应用笔记

- 如何设置看门狗reset时间和alarm时间

  - 通过设置aon_wdt_init_t 结构体的counter成员变量和alarm_counter  成员变量，然后调用app_aon_wdt_init  接口来实现。
  - 注意GR551x的counter的单位是tick，根据与慢速时钟频率的关系可以转换得到对应的ms时间；其他芯片的counter单位是ms，根据与慢速时钟频率的关系可以转换得到对应的tick个数。alarm_counter的单位也是这样定义。tick与ms的互相转换公式，可参考头文件对aon_wdt_init_t  结构体的描述说明。
  - GR551x的alarm_counter在API接口无意义，内部实现用最大的5bit alarm_counter值（对应的具体时间大约为1ms）；其他芯片的alarm_counter的值受16bit范围的限制，对应单位为ms的数值不能超过2000.
  - 更多参数的设置和接口调用，参考《GR5xx APP用户驱动手册.pdf》的2.9章节。
- 如何判断系统复位是否为看门狗复位

  - GR551x系列可以通过查询AON_WDT Reboot Event Flag来判断是否产生了WDT复位，但是要注意，该标志在platform_init里面会被清除，所以需要在platform_init之前读取；

  - GR5525/GR5526/GR533x系列由于内部有复位原因寄存器，可以通过查询复位原因寄存器的方式来判断是否为WDT复位。

  - 以上判断复位原因的具体方法，可参考论坛上的经验分享《GR55xx 判断复位原因方法分享》https://developers.goodix.com/zh/bbs/detail/5ec2641ffd0a4afdb5103ad1ea4a3a3e

- 如何记录看门狗复位前的现场信息

  - 利用WDT的alarm中断功能，设置合理的alarm值，当系统繁忙来不及喂狗时，WDT的counter会减到alarm值，此时会触发alarm中断。在alarm中断里面可以记录现场信息，有助于分析系统来不及喂狗的原因。
  - 在WDT alarm中断里记录现场信息的方法，与在HardFault_Handler 里面记录死机现场信息的方法是一样的，用户可参考我们SDK的HardFault_Handler的处理方法进行记录；用户也可以把自己的记录方法在alarm中断里实现。
  - 需要注意的是，GR551x产生alarm中断的时刻离芯片复位的时间非常接近(1ms不到)，所以可能来不及记录就产生复位了。可以尝试在hal_aon_wdt_alarm_callback函数中进行喂狗后再进行记录。具体可参考社区问题讨论：https://developers.goodix.com/zh/bbs/detail/fb6ade9f85d84fbd8b3b596062b08fe3
- 看门狗复位是复位哪些域

  看门狗复位会把BLE域、MCU域、AON域等都复位，效果与硬件复位和冷启动是一样的。

