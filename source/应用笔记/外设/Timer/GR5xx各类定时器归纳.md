## GR5xx各类定时器归纳

### 1. GR5xx各类定时器特征概览

|             名字              |    模块属性     | AON域 |                 个数                 |           时钟源            | 计数模式和计时精度 | 驱动参考                                                     | 典型特点                                                     | 应用场景                                                     |
| ----------------------------- | --------------- | ----- | ------------------------------------ | --------------------------- | ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
|            SysTick            |     ARM系统     |  NO   |                  1                   |        System Clock         |    递减，24-bit    | 标准的CMSIS 驱动                                             | 24位系统硬件定时器, 注意使用时预防溢出                       | 1. 可作为OS的Tick心跳, 方便不同Cortex核之间移植<br />2.在GR551x 的FreeRTOS 工程中的Active模式, 作为 OS的Tick 驱动使用; <br />3.在非GR551x芯片系列的FreeRTOS工程 没有使用SysTick（用RTC）, 所以Systick可以根据需要提供给应用层使用 |
|              DWT              |     ARM系统     |  NO   |                  1                   |        System Clock         |    递增，32-bit    | HAL_TIMEOUT_INIT<br />HAL_TIMEOUT_GET_TICK<br />HAL_TIMEOUT_DEINIT | 不算标准Timer, 主要用于 系统tick 计数                        | 1.可以使用 DWT的Tick来辅助计算片段代码的运行时间<br />2.注意溢出时间, 举例96MHz主频下, 溢出时间约 U32_Max/96M = 44秒. 使用场景一般都先重置再使用, 尽量不要跨越复杂的上下文环境使用 |
|             Timer             |     ARM系统     |  NO   |                  2                   |        System Clock         |    递减，32-bit    | HAL：gr55xx_hal_tim.c/h<br />APP:app_tim.c/h                 | 1.32-bit硬件定时器<br />2.MCU睡眠定时器不能工作，所以调用接口初始化了系统不会睡眠，反初始化才允许系统睡眠<br />3.GR533x的timer有IO捕获功能 | MCU ACTIVE模式下高精度定时场景<                              |
|          Dual Timer           |     ARM系统     |  NO   |                  2                   |        System Clock         |    递减，32-bit    | HAL:gr55xx_hal_dual_tim.c/h<br />APP:app_dual_tim.c/h        | 1.可用作16/32 位定时器<br />2.MCU睡眠定时器不能工作，所以调用接口初始化了系统不会睡眠，反初始化才允许系统睡眠<br />3.有周期模式、自由模式、一次到达等多种定时模式<br />4.GR533x的dual timer拥有IO联动功能 | 1. MCU ACTIVE模式下高精度定时场景<br />2.用于捕获IO电平变化信息<br />3.用于产生时序严格的IO方波 |
|            ARM-WDT            |     ARM系统     |  NO   |                  1                   |        System Clock         |    递减，32-bit    | CMSIS驱动                                                    | ARM 看门狗, 不能在Sleep模式工作                              | 基本弃用状态                                                 |
|            AON-WDT            | SOC always on域 |  YES  |                  1                   | 慢速时钟源，具体配置见项目2 |    递减，32-bit    | HAL gr55xx_hal_aon_wdt.c/h<br />APP app_aon_wdt.c/h          | 1. 32Bit硬件计数器, 触发系统复位, MCU 睡眠也可继续工作<br />2.在复位前可以配置一个过期提醒ALARM中断 | 1. 用作系统的软件看门狗<br />2.用作特别设计的系统复位接口<br />3.ALARM中断可以用来记录看门狗复位前的现场信息供分析 |
|  Sleep Timer<br />APP Timer   | SOC always on域 |  YES  |                  1                   | 慢速时钟源，具体配置见项目2 |    递减，32-bit    | HAL gr55xx_hal_sleep_timer.c/h<br />APP app_timer.c/h        | 1. 32Bit 硬件计数器<br />2.模式0 - 休眠模式计数活动模式停止工作<br />3.模式1 - 单次计数,完成停止, 无论是休眠还是活动模式<br />4.模式2 - 类似模式1, 自动重载计数 | 1. 可用作将CPU从休眠状态唤醒 <br />2. 基于sleep timer构建的应用层timer （即app timer）, 可广泛应用在对时间精度要求不是很高的场景做定时器(支持休眠下工作). <br />3. 应用层Timer 用软件链表管理, 因此存在一定的时延 |
|       RTC<br />Calendar       | SOC always on域 |  YES  | GR551x/GR533x:1<br />GR5525/GR5526:2 | 慢速时钟源，具体配置见项目2 |    递增，32-bit    | HAL gr55xx_hal_rtc.c/h<br />APP  app_rtc.c/h                 | 1.采用外部晶振时候计时精度等于晶振ppm<br />2.GR551x 如果采用RNG2做时钟源, Calendar无法使用, 因为其无法正常设置RNG2为时钟源<br />3.5526用RNG2为时钟源也无法使用Calendar, 因为RNG2计数有时突变到0xffffffff | 1. 一个替代SysTick作为 OS的Tick心跳（Active下周期性, Sleep 单次计时）<br />2.另一个 实现日历，有计时、tick中断和闹钟设置功能 |
|              PWM              |   SOC外围模块   |  NO   |                  2                   |        Serial Clock         |    递增，32-bit    | HAL gr55xx_hal_pwm.c/h<br />APP app_pwm.c/h                  | 为外设提供PWM 信号                                           | 电机、LED控制或信号发生等场景                                |
| BLE_Timer<br />ble comm timer |   SOC ble模块   |  YES  |                  1                   | 慢速时钟源，具体配置见项目2 |         /          | ble_time.c/h                                                 | ble core 里面的定时器                                        | 为协议栈提供广播间隔等时隙，系统也可以调它的接口获取睡眠时间 |


### 2. GR5xx慢速时钟定时器的时钟配置

GR5xx基于慢速时钟的定时器分别有BLE_Timer，aon_wdt, sleep timer, RTC.

慢速时钟源分别有外部的晶体时钟和内部的RC时钟。

外部晶体时钟是32K晶振，也叫LFXO-32K，特点是相比内部的RC时钟有更好的稳定性。

内部的RC时钟分别有RNG_OSC和LFRC-32K（也叫RNG2）。RNG_OSC来源于时钟树上的2MHZ_RNG_OS，不太稳定；LFRC-32K相比RNG_OSC则有更好的PPM.但在GR551x和GR5526上，LFRC-32K用于计时模块时，会出现计时突变的问题，所以不能用。各个芯片的慢速时钟配置如下：

- 对于GR551x：

BLE TIMER:如果选择外部时钟源用LFXO_32K，如果选择内部时钟源用RNG2。
AON WDT:固定到RNG(不支持RNG2，也不支持外部LFXO_32K) 
Sleep TIMER:外部用LFXO_32K，内部用RNG2
RTC:固定到外部LFXO_32K，不支持内部时钟(所以如果芯片没有外挂LFXO_32K，SDK基于ble timer实现了日历的计时功能，但日历没有tick和alarm功能)

- 对于GR5526:

BLE Timer：如果选择外部时钟源用LFXO_32K，如果选择内部时钟源用LFRC_32K.
AON WDT：如果选择外部时钟源用LFXO_32K，如果选择内部时钟源用RNG_OSC(由于LFRC_32K计时有突变，所以不能用）
Sleep Timer：如果选择外部时钟源用LFXO_32K，如果选择内部时钟源用RNG_OSC(由于LFRC_32K计时有突变，所以不能用）
RTC0:如果选择外部时钟源用LFXO_32K，如果选择内部时钟源时，app_rtc.c会基于ble_timer实现日历简单的时间计时功能，没有tick和alarm中断功能。
RTC1:如果选择外部时钟源用LFXO_32K，如果选择内部时钟源用RNG_OSC(由于LFRC_32K计时有突变，所以不能用）.

- 对于GR5525/GR533x：

对所有BLE_Timer/aon_wdt/sleep timer/RTC来讲，

如果选择外部时钟源用LFXO_32K；如果选择内部时钟源时用LFRC_32K（因为LFRC-32K相比RNG_OSC则有更好的PPM）。

### 3.各款芯片RTOS tick的实现方式

- GR551x：

MCU ACTIVE模式下，是基于Systick实现 RTOS的tick；

在MCU Sleep 模式下，systick停住工作，依靠ble_timer的定时任务进行唤醒，唤醒后通过读取ble_timer时间对systick进行补偿。


- GR5525/GR5526

基于RTC1实现RTOS的tick。这两款芯片有两路RTC，所以RTC0用于正常的日历功能。


- GR533x：

基于RTC0实现 RTOS的tick。由于芯片只有一路RTC，所以在RTOS场景下，日历功能会受限。
