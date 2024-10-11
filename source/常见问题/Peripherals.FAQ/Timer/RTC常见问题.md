## RTC常见问题



### 1. RTC计时误差大的原因是什么？

- RTC是基于慢速时钟源工作的，所以它的精度与慢速时钟源的精度相关。

- 我们SDK都会对慢速时钟源进行校准。所谓的校准，其实是基于32M的高速精确时钟去测试获取慢速时钟的真正频率，修正32.768K这个数值。所以32M的精度也至关重要，RTC测试前需要先用Goodix在线或离线工具对32M晶振进行校准。

- 除GR551x以外的芯片，SDK默认每隔30s对慢速时钟进行校准；GR551x则在冷启动的时候校准一下，1.7.0及以前的SDK版本RTC校准方法有Bug，需要按照论坛方法进行修正，详见“[如何提高RTC的精度](https://developers.goodix.com/zh/bbs/detail/429620fdd9dc4d9787bf0e07b135bf1b)”。



### 2. 如何根据RTC获取到系统运行时间？

- 首先要确保RTC已经初始化，可调用app_rtc的初始化接口对RTC进行初始化。

- 调用hal_pwr_get_timer_current_value(PWR_TIMER_TYPE_CAL_TIMER, (x)) 获取原始的RTC数据，注意第一个入参是PWR_TIMER_TYPE_CAL_TIMER。

- 获取到RTC计数数据后，调用sys_lpclk_get()获取当前的慢速时钟频率，根据与慢速时钟频率的关系，转换为ms或者μs。



### 3. RTC不工作，或者调用app_rtc_get_time(&time)发现获取到的时间一直不变，原因是什么？

- 首先确认慢速时钟源的选择，是选择内部还是外部。
- 如果选择的是内部慢速时钟源，对于GR551x或者GR5526，RTC是基于Bluetooth LE Timer构造的，所以需要确保蓝牙协议栈已初始化。
- 如果选择的是外部慢速时钟源，确保32K晶振是否焊接正常。