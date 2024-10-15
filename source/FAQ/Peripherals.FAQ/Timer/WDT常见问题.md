## FAQ for WDT



### 1. What are the reasons why the watchdog does not work (or does not feed the dog for a predetermined period of time, but does not generate a reset)?

- First check the return value of the watchdog initialization interface to make sure whether the initialization is successful. Often the value of alarm_counter is out of range and the initialization is not successful. Please refer to the chapter “APP AON_WDT Driver” in [GR5xx APP Driver User's Manual](https://docs.goodix.com/zh/online/app_driver_bl/V1.4) for the details of the initialization parameters.
- Check whether the watchdog is enabled or not by calling ll_aon_wdt_is_enabled() interface, and whether the watchdog will be abnormally shut down due to software tampering.
- Check if the watchdog counter is running by calling the ll_aon_wdt_get_counter() interface.
- If the watchdog counter is not running, check that the slow clock is normal, provided that the watchdog is enabled. If the slow clock source is an external 32K crystal, you need to check if the 32K crystal is normal.



### 2. The watchdog reset time is not correct, what is the reason?

- Check if the value of Counter is correct, note that the unit of GR551x Counter is Tick of slow clock, and the unit of Counter of other chips is ms.
- Print out the slow clock frequency SystemCoreLowClock and check whether the slow clock frequency deviates greatly from the understanding.
- GR5525/GR5526/GR533x series chips will re-calibrate the value of SystemCoreLowClock every 30s by default on the SDK. If the slow clock frequency changes greatly within 30s, it will lead to a large deviation of the actual counting time of the watchdog because of the frequency deviation as it hasn't had time to calibrate yet.