## GR5xx Timers

### 1. Overview of GR5xx Timers

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


### 2. Clock configuration of GR5xx slow clock timers

GR5xx slow clock based timers are BLE_Timer, aon_wdt, sleep timer, RTC respectively.

The slow clock sources are external crystal clock and internal RC clock respectively.

The external crystal clock is a 32K crystal oscillator, also called LFXO-32K, characterized by better stability than the internal RC clock.

The internal RC clocks are RNG_OSC and LFRC-32K (also called RNG2).The RNG_OSC comes from the 2MHZ_RNG_OS on the clock tree, which is less stable, while the LFRC-32K has a better PPM compared to the RNG_OSC.However, when the LFRC-32K is used for the timing module on the GR551x and the GR5526, there is a problems with abrupt timing changes, so it can't be used. The slow clock configuration for each chip is as follows:

- For GR551x:

BLE TIMER: LFXO_32K if external clock source is selected, RNG2 if internal clock source is selected.
AON WDT:fixed to RNG (RNG2 is not supported, nor is external LFXO_32K) 
SLEEP TIMER:LFXO_32K for external, RNG2 for internal.
RTC: fixed to external LFXO_32K, no support for internal clock (so if the chip does not have external LFXO_32K, the SDK implements calendar timing based on ble timer, but the calendar does not have tick and alarm functions)

- For GR5526.

BLE Timer: use LFXO_32K if external clock source is selected, use LFRC_32K if internal clock source is selected.
AON WDT: LFXO_32K if external clock source is selected, RNG_OSC if internal clock source is selected (LFRC_32K cannot be used due to mutation in timing).
Sleep Timer: LFXO_32K if external clock source is selected, RNG_OSC if internal clock source is selected (cannot be used because LFRC_32K timing has mutation)
RTC0:if choose external clock source with LFXO_32K, if choose internal clock source when app_rtc.c will implement calendar simple time timing function based on ble_timer, no tick and alarm interrupt function.
RTC1: use LFXO_32K if external clock source is selected, use RNG_OSC if internal clock source is selected (can't use LFRC_32K timing since it has mutation).

- For GR5525/GR533x:

For GR5525/GR533x: For all BLE_Timer/aon_wdt/sleep timer/RTC.

For all BLE_Timer/aon_wdt/sleep timer/RTC, use LFXO_32K if external clock source is selected, and use LFRC_32K if internal clock source is selected (because LFRC-32K has better PPM than RNG_OSC).

### 3. RTOS tick implementation of each chip

- GR551x:

In MCU ACTIVE mode, the RTOS tick is realized based on Systick;

In MCU SLEEP mode, systick stops working and relies on the timing task of ble_timer to wake up, and compensates systick by reading the time of ble_timer after waking up.


- GR5525/GR5526

RTOS tick implementation based on RTC1. these two chips have two RTCs, so RTC0 is used for normal calendar functions.


- GR533x:

Implement RTOS tick based on RTC0. Since the chip has only one way RTC, the calendar function will be limited in RTOS scenario.