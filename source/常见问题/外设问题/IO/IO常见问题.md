# I/O常见问题



## 1. 如何处理IO漏电导致睡眠功耗高的问题（睡眠前如何正确进行IO的配置和检测）?

- 需要按照应用笔记中介绍的上下拉电阻配置原则，正确配置每个IO的上下拉电阻。
- 在分析问题时，可以在睡眠前把每个IO的上下拉配置情况读取出来逐一检查。具体的做法是，实现睡眠前检测IO的函数，函数里面把GPIO、AON IO、MSIO的上下拉配置都读取出来；然后通过pwr_mgmt_register_io_dump_func（）把该函数注册到睡眠前的函数钩子io_dump_func_t。这样真正进入睡眠前，SDK就会调用一下上下拉配置读取的函数把睡眠前的IO上下拉配置读取出来供检查。具体方法可参考论坛链接https://developers.goodix.com/zh/bbs/detail/66ed78f2b95140b0b8748a5f8f9aef80



## 2. 如何处理I/O中断丢失的问题?

- 检查一下中断回调函数app_io_event_handler()中，根据p_evt判断中断 引脚号时，不能用if...else...的结构，因为可能存在几个引脚同时响应一个回调函数的情况。SDK的示例代码是正确的判断结构：

    ```c
    if (p_evt->pin == APP_GPIO_KEY0_PIN)
    {
    }
    if (p_evt->pin == APP_GPIO_KEY1_PIN)
    {
    }
    ```

- 引脚中断是分组的，GPIO0~15响应的是EXT0_IRQ，GPIO16~31响应的是EXT1_IRQ， GPIO32~33响应的是EXT2_IRQ，AON IO响应的是AON_EXT_IRQ。同一组的引脚如果它们的中断触发时间比较接近，那么它们可能就同时响应一个IRQ。



## 3. I/O有没有推挽输出模式?

- GR5xx系列芯片的IO没有推挽输出模式。各个IO的驱动电流有限，具体可参见datasheet关于IO章节的electrical specifications 部分。



## 4. 利用IO翻转输出方波，频率误差很大, 是什么原因?

- 检查是否设置IO电平的函数执行效率慢导致。如果需要快速翻转IO可以在初始化完成后调用ll层函数如：ll_gpio_set_output_pin\ll_gpio_reset_output_pin，ll_gpio_toggle_pin，AON_GPIO\MSIO同理。
- 此外，函数放在SRAM执行可以进一步提高速率，在函数名前加SECTION_RAM_CODE即可。