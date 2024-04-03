## GPTimer常见问题



### 1. app_tim.c与app_timer.c有什么区别？哪些定时器是低功耗定时器？哪些不是？
   - GR5xx SOC，基于系统时钟的定时器有timer和dual timer，这两个都不是低功耗定时器，在系统睡眠的时候不能工作；基于系统慢速时钟（频率一般32K左右）的定时器有Sleep Timer和RTC，他们是低功耗定时器，在系统睡眠的时候可以工作。

   - 基于timer构造的app驱动文件为app_tim.c; 
   
     基于dual timer构建的驱动文件为app_dual_tim.c;
   
     基于Sleep Timer构建的驱动文件为app_timer.c;
   
     基于RTC构建的驱动文件为app_rtc.c.



### 2. 使用Timer/Dual Timer定时，利用中断里翻转IO的方式测试定时准确度，发现误差比较大, 原因是什么

-   中断被抢占。检查一下有没有比timer/dual timer中断优先级更高的中断频繁来抢占,如果存在，需要提高timer中断的优先级。

- 中断响应慢。检查一下从进入TIMERx_IRQHandler到用户的回调函数的执行时间，建议所有的函数都放在RAMCODE执行。有必要的话，重新实现TIMERx_IRQHandler。

- IO翻转需要调用ll层的接口，这样IO控制的效率更高。



### 3. 使用Timer/Dual Timer定时，利用中断里翻转IO的方式测试定时准确度，发现第一个周期的误差很大，后面的周期符合要求。

- 其实每个定时周期时间到，响应中断都需要时间。而第一个周期响应时间显得更长，主要是响应过程有部分函数(比如用户的回调函数)是在flash上，第一次从flash加载到cache而需要更长时间。

- 定时时间到，中断响应需要从进入TIMERx_IRQHandler()开始一步一步执行到到用户设置的回调函数，然后在回调函数里面执行IO控制操作。为了提高效率，可以在app_tim.c/app_dual_tim.c重构TIMERx_IRQHandler，然后把要求优先响应的IO控制放在TIMERx_IRQHandler的最前面，以timer0为例：

    ```C
    #if 0
    #define TIMER_HANDLER(index, val) \
    SECTION_RAM_CODE void TIMER##index##_IRQHandler(void)\
    {\
        hal_timer_irq_handler(&p_tim_env[val]->handle);\
    }
    
    TIMER_HANDLER(0, APP_TIM_ID_0)
    TIMER_HANDLER(1, APP_TIM_ID_1)
    #endif
    
    SECTION_RAM_CODE void TIMER0_IRQHandler(void)
    {
        ll_gpio_toggle_pin(GPIO1,LL_GPIO_PIN_10);//add IO control here
        hal_timer_irq_handler(&p_tim_env[APP_TIM_ID_0]->handle);
    }
    
    SECTION_RAM_CODE void TIMER1_IRQHandler(void)
    {
        hal_timer_irq_handler(&p_tim_env[APP_TIM_ID_1]->handle);
    }
    ```


​      