## FAQ for I/O



### 1. How to deal with the problem of high sleep power consumption due to IO leakage (how to properly configure and detect IOs before sleep)?

- It is necessary to correctly configure the pull-up and pull-down resistors of each IO according to the pull-up and pull-down resistor configuration principles introduced in the application notes.
- When analyzing the problem, the pull-up and pull-down configuration of each IO can be read out and checked one by one before sleep. The specific approach is to implement a function to detect the IOs before sleep, and inside the function, read out the pull-down configuration of GPIO, AON IO, and MSIO; and then register the function to the function hook io_dump_func_t before sleep through pwr_mgmt_register_io_dump_func(). so that before really going to sleep, the SDK will call the function of read pull-down configuration to read out the IO pull-down configuration before sleep for checking. For details, please refer to the forum discussion “[GR551x how to measure the GPIO pull-down status before sleep to analyze whether the GPIO configuration is correct or not](https://developers.goodix.com/zh/bbs/detail/66ed78f2b95140b0b8748a5f8f9aef80)”.



### 2. How to deal with IO interrupt loss?

- Check that in the interrupt callback function app_io_event_handler(), when determining the interrupt pin number based on p_evt, you can't use if... .else... The example code in the SDK is the correct structure for the judgment:

```c
    if (p_evt->pin == APP_GPIO_KEY0_PIN)
    {
    }
    if (p_evt->pin == APP_GPIO_KEY1_PIN)
    {
    }
```

- Pin interrupts are grouped, with GPIO0~15 responding to EXT0_IRQ, GPIO16~31 responding to EXT1_IRQ, GPIO32~33 responding to EXT2_IRQ, and the AON IO responding to AON_EXT_IRQ. pins in the same group may respond to both if their interrupt triggers are relatively close to each other. AON IO responds to AON_EXT_IRQ.



### 3. Does IO have push-pull output mode?

- There is no push-pull output mode for the IOs of the GR5xx series chips. Each IO has a limited drive current, which can be found in the Electrical Specifications section of the IO chapter of the Datasheet.



### 4. What is the reason for the large frequency error when outputting a square wave using IO flip-flop?

- Check if the function to set the IO level has slow execution efficiency. If you need to flip IO quickly, you can call LL level functions after initialization is done, such as ll_gpio_set_output_pin\ll_gpio_reset_output_pin, ll_gpio_toggle_pin, and the same for AON_GPIO\MSIO.
- In addition, the function can be placed in the SRAM execution can further improve the rate, in the function name before the addition of SECTION_RAM_CODE can be.