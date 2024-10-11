# RTC应用笔记 #

## 1. RTC基本功能介绍

- GR551x/GR533x内部只有1路RTC；GR5525/GR5526内部有2路RTC，其中一路专门用于给RTOS提供Tick中断。
- 基于慢速时钟源，其中可选择外部慢速时钟LF_XO32K和内部慢速时钟LF_RC32K，用户根据实际情况来选择。
- 可以对系统的慢速时钟源进行分频，支持NO_DIV、DIV_2、DIV_4、DIV_8、DIV_16、DIV_32、DIV_64和DIV_128。
- RTC的Tick中断功能：设定一个时间间隔，到达时间间隔后会产生中断。Tick的间隔不能小于ms。由于RTC在睡眠时可以继续工作，所以往往利用RTC的Tick中断功能为RTOS提供Tick。
- RTC的Alarm中断功能：设定一个闹钟时间，该时间可选择按天循环或按周循环。

## 2. GR5xx RTC应用笔记

- 调用app_rtc_setup_tick设置Tick时，要注意Tick不能太小。由于RTC是基于慢速时钟源进行工作，所以它不能实现ms以下的Tick。对于GR551x，Tick还要求大于5 ms。
- RTC计时的精度与慢速时钟源有关。我们SDK都会对慢速时钟源进行校准，这里所谓的校准，其实是基于32M的高速精确时钟去测试获取慢速时钟的真正频率，修正32.768K这个数值。所以32M的精度也至关重要，RTC测试前需要先用Goodix在线或离线工具对32M晶振进行校准。
- GR5525/GR5526有2路RTC，其中一路专用于给RTOS提供Tick功能，而GR551x和GR533x内部只有1路RTC。所以在RTOS的场景，要注意如果RTOS用了RTC进行Tick（GR551x以外，GR551x在SDK上是基于ble_timer给RTOS提供Tick），该路RTC如果已经被RTOS初始化设置为1 ms的Tick中断，应用层使用RTC的时候要注意避免与RTOS的冲突。
- 对于GR551x和GR5526，由于RTC模块对内部慢速时钟源的兼容性不好，所以，对于GR551x和GR5526，如果用户选择的慢速时钟源是内部的，那么SDK的App Driver里面会基于ble_timer来构建RTC的接口。但是此类接口只有计时功能，即只能获取RTC的Timer，没有Tick中断和Alarm功能。同时要注意，由于是基于ble_timer构建，所以要确保协议栈已经初始化。

