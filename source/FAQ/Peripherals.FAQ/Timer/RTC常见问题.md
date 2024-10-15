## FAQ for RTC



### 1. What are the reasons for the large RTC timing errors?

- RTC works based on a slow clock source, so its accuracy is related to the accuracy of the slow clock source.

- Our SDK will calibrate the slow clock source. The so-called calibration is actually based on the 32M high-speed accurate clock to test to get the real frequency of the slow clock, and correct the value of 32.768K. So the accuracy of 32M is also crucial, and the 32M crystal needs to be calibrated with Goodix online or offline tool before RTC test.

- For chips other than GR551x, SDK calibrates the slow clock every 30s by default; GR551x calibrates it during cold start. 1.7.0 and previous SDK versions have bugs in the RTC calibration method, which need to be corrected according to the forum method, for details, please refer to “[How to Improve RTC's Accuracy](https://developers.goodix.com/zh/bbs/detail/429620fdd9dc4d9787bf0e07b135bf1b)”.



### 2. How to get the system runtime according to RTC?

- First of all, make sure the RTC has been initialized, you can call the initialization interface of app_rtc to initialize the RTC.

- Call hal_pwr_get_timer_current_value(PWR_TIMER_TYPE_CAL_TIMER, (x)) to get the raw RTC data, note the first input is PWR_TIMER_TYPE_CAL_TIMER.

- After getting the RTC count data, call sys_lpclk_get() to get the current slow clock frequency, which is converted to ms or μs depending on the relationship with the slow clock frequency.



### 3. The RTC does not work, or call app_rtc_get_time(&time) and find that the time obtained remains the same, what is the reason?

- First confirm the selection of the slow clock source, whether internal or external is selected.
- If you choose internal slow clock source, for GR551x or GR5526, the RTC is constructed based on Bluetooth LE Timer, so you need to make sure the Bluetooth stack is initialized.
- If the choice is external slow clock source, make sure the 32K crystal is soldered properly.