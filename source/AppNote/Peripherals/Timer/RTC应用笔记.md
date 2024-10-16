# APP RTC Application Note

## 1. Introduction to RTC Basic Functions
- GR551x/GR533x System on Chips (SoCs) have only one RTC; GR5525/GR5526 SoCs have two RTCs, one of which is dedicated to providing Tick interrupts for the RTOS.
- Based on the low-speed clock source, you can choose between the external low-speed clock LF_XO32K and the internal low-speed clock LF_RC32K, depending on your needs.
- The system's low-speed clock source can be divided, supporting NO_DIV, DIV_2, DIV_4, DIV_8, DIV_16, DIV_32, DIV_64, and DIV_128.
- RTC Tick interrupt function: Set a time interval, and an interrupt will be generated when the interval is reached. The Tick interval cannot be less than a millisecond. Since the RTC can continue to work during sleep, the RTC Tick interrupt function is often used to provide ticks for the RTOS.
- RTC Alarm interrupt function: Set an alarm time, which can be configured to repeat daily or weekly.

## 2. APP RTC Application Note for GR5xx
- When calling `app_rtc_setup_tick` to set the Tick, note that the Tick value cannot be too small. Since the RTC operates based on a slow clock source, it cannot achieve a Tick below milliseconds. For GR551x, the Tick must be greater than 5 ms.
- The accuracy of RTC timing is related to the slow clock source. Our SDK calibrates the slow clock source by using the high-speed 32M clock to test and obtain the actual frequency of the slow clock, correcting the 32.768K value. Therefore, the accuracy of the 32M clock is also crucial. Before RTC testing, the 32M crystal oscillator needs to be calibrated using Goodix online or offline tools.
- GR5525/GR5526 has two RTCs, one of which is dedicated to providing Tick functionality for RTOS, while GR551x and GR533x have only one RTC internally. In RTOS scenarios, if RTOS uses RTC for Tick (except for GR551x, which provides Tick to RTOS based on `ble_timer` in the SDK), and if this RTC has already been initialized by RTOS to a 1 ms Tick interrupt, the application layer should avoid conflicts with RTOS when using RTC.
- For GR551x and GR5526, due to poor compatibility of the RTC module with the internal slow clock source, if the user selects the internal slow clock source, the SDK's App Driver will construct the RTC interface based on `ble_timer`. However, such interfaces only have timing functionality, meaning they can only obtain the RTC Timer without Tick interrupt and Alarm functionality. Additionally, since it is constructed based on `ble_timer`, ensure that the protocol stack has been initialized.