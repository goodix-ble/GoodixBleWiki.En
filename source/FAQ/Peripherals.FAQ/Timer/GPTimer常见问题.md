## FAQ for GPTimer



### 1. What is the difference between _app_tim.c_ and _app_timer.c_? Which timers are low power timers? Which ones are not?
   - GR5xx SoC, the timers based on system clock are Timer and Dual Timer, both of which are not low-power timers and can't work when the system sleeps; the timers based on system slow clock (the frequency is usually around 32K) are Sleep Timer and RTC, they are low-power timers and can work when the system sleeps.

        - The App driver file constructed based on Timer is  app_tim.c.
        
        - The driver file constructed based on Dual Timer is  app_dual_tim.c.
        
        - The driver file constructed based on Sleep Timer is  app_timer.c.
        
        - The driver file built based on RTC is  app_rtc.c.



### 2. Using Timer/Dual Timer timing, test the timing accuracy by flipping the IO in interrupt, and found the error is relatively large, what is the reason?

- Interrupts are being preempted: check if there are interrupts with higher priority than Timer/Dual Timer interrupts that are frequently preempted, if there are, you need to increase the priority of Timer interrupts.

- Slow interrupt response: check the execution time from entering TIMERx_IRQHandler to the user's callback function, it is recommended that all functions are placed in RAMCODE for execution. If necessary, reimplement TIMERx_IRQHandler.

- The IO flip-flop needs to call the LL layer interface so that the IO control is more efficient.



### 3. Using Timer/Dual Timer timing, test the timing accuracy by flipping the IO in the interrupt, and found that the error of the first cycle is very large, and the later cycles meet the requirement, what is the reason?

- In fact, each timing cycle time to respond to the interrupt will take time. In fact, it takes time to respond to the interrupt when the time of each timing cycle comes, but the response time of the first cycle is longer, mainly because some functions (such as user callback functions) are on Flash, and it takes longer time to load them from Flash to Cache for the first time.

- When the timer is up, the interrupt response needs to be executed step by step from entering TIMERx_IRQHandler() to the callback function set by the user, and then the IO control operation is executed inside the callback function. To improve efficiency, you can refactor TIMERx_IRQHandler in _app_tim.c/app_dual_tim.c_, and then put the IO control that requires a priority response at the top of TIMERx_IRQHandler; take Timer0 as an example:


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
