## Power Consumption Debugging Reference for GR5526 Watch Demo 


> Note: This document applies to the reference project ${GR5526_SDK}\projects\peripheral\graphics\graphics_lvgl_831_gpu_demo


### 1. Reference Project Description 

- The Watch Demo project is a smart watch demo project based on GR5526 SK. The project adopts Lvgl 8.31 GUI framework, which is optimized based on GR5526's GPU porting, featuring high frame rate, good interaction effect, fast development efficiency, etc. Users can carry out the secondary development of watch or display products based on this project: add and modify the UI layout and interaction, increase the processing of peripheral devices, increase the logic of business interactions, and add and modify the BLE Profile, etc. This project can accelerate the user's product development. It can accelerate the product cycle of users. 

- Because different products will design different product operating modes, and the state transition conditions between modes are different, so the product power consumption (operating) mode design has a variety. This Watch Demo project provides a basic working mode management strategy, which on the one hand provides an initial reference for users to design working modes, and on the other hand helps users to understand and debug the low-power modes of the product quickly.



### 2. Background on Low Power Modes

- If you need to evaluate the power consumption of the GR5526 at the chip level, it is recommended to use the ${SDK}\rojects\ble\ble_peripheral\ble_app_pcs project. And refer to the document “GR5526 Power Consumption Mode and Power Consumption Measurement Description”, the online web link of the document is: [GR5526 Power Consumption Mode and Power Consumption Measurement Description](https://docs.goodix.com/zh/online/detail/power_application_bl_b/V1.0/61ae20c6ecf2d6ea57ef7e7b77f80c08), this document is also relied upon for the background knowledge of the power consumption in this article, please read it first.
- If you want to learn about power consumption business logic in OS environment, please check out the project ${SDK}\projects\ble\ble_peripheral\ble_app_template_freertos, which is based on GR5526 ported FreeRTOS system, adapted to hibernation policy, and turned on the base of the BLE broadcast, suitable as a starting point from OS to zero. It can be used as a template project for IOT products built from scratch. The online reference document for this project is [GR5xx FreeRTOS Sample Manual](https://docs.goodix.com/zh/online/detail/freertos_bl/V3.1/1018832044f1b7ff252f659fd41a50a2).
- For GR5xxx series chips, there is a difference between the low power hibernation strategy in FreeRTOS environment and Bare Metal environment, the former is based on the Tickless mode of FreeRTOS idle tasks, while the latter hibernation bare metal is managed in the main loop of the main stack. The former is based on FreeRTOS Idle Tasks Tickless mode, while the latter is managed by the main loop of the main stack.



### 3. Low-power debugging based on Watch Demo

#### 3.1 Principle

Since the low-power debugging is based on GR5526 SK development board, which is very different from the product environment, such as different I/O arrangement, different mounted peripherals, different working mode design, incomplete business logic of the demo project, etc., this section mainly describes the general method of debugging, and does not describe in detail the debugging methods of peripheral hibernation processing method, leakage finding and analysis, and other business scenarios related to debugging. This section mainly describes the general method of debugging, about the peripheral sleep processing method, leakage analysis and some other business scenarios are strongly related to debugging, and will not be described carefully. 

 

#### 3.2 Test Environment Setup

- This test uses the current loop measurement method to determine the power consumption of the system, and the voltage supply method can also be used. 

- The following hardware configuration applies to both the GR5526 SK Rev. B and Rev. C. Click here for the GR5526 SK Rev. C circuit diagram (https://www.goodix.com/zh/docview/GR5526-SK-BASIC-RevC_V1.0?objectId=278&objectType=document&version=449).

  - KeySight set to current measurement mode

  - Remove the jumper cap from J1. Connect KeySight Output+ to J1.Pin1; KeySight Output- to J1.Pin2. String KeySight into current loop.

  - Dipswitch S1 Dipswitch mode: Pin2 is connected to Pin3, Pin4 is connected to Pin5.

  - DIP Switch S10 Dialing Mode: VBAT side.

  - Dip Switch S11 Dialing Mode: VCC side

  - JLink-USB port connects to PC USB, used for circuit power supply and Jlink debugging.

  - JLink-USB port is connected to the PC USB port for powering the circuit and connecting to Jlink.
  
  - ![1705548135991](../../_images/app/measure_power.png)

    

#### 3.3 Main tasks of the Watch Demo project related to hibernation

- Starts the BLE stack from the main function, opens a broadcast called “SmartWatch” (earlier version of the broadcast was called: “5526_SK.X”), and creates a couple of reference BLE Profiles

- Touch detection task, mainly used to periodically detect Touch input, as the driver event input for GUI rendering task; in addition, extends the application-level work state management (users can redesign the work state management logic according to the product).
- Lvgl GUI rendering task, which handles the rendering and display of the entire UI.
- UI external event handling task, responsible for distributing generated key events to GUI tasks.
- FreeRTOS Idle task, which handles the system idle and sleep-wake logic entries.

 

#### 3.4 Working Mode Design of Watch Demo

In this reference project, three working modes are designed for the application layer.  

- Active on-screen working mode: all application services are in working state, GUI tasks are rendered in real time, and the screen is always on.

- Screen-off mode: In this mode, all other application services are running normally, only the screen display is turned off, and the GUI rendering and screen-swiping behaviors are suspended for a certain number of seconds. If in this time period, the system detects the behavior of touching the screen, it will directly light up the screen, back to Active mode; if more than the time period does not detect the touch behavior, into the system's off screen hibernation mode

- Screen off sleep mode: In this mode, the GUI related tasks do not work, the screen goes off, all peripherals enter into power-down or cyclic execution state according to the product design, and the chip stops working and goes to sleep. Screen off sleep mode does not prevent the execution of cyclic tasks. When the cyclic task is executed, the chip will wake up again and continue to enter Sleep mode after completion.  In the Sleep mode of this reference project, because the Touch stops working (not realize the sleep interrupt triggered wake-up, users need to realize it according to the needs of the product), the additional key to wake up. Users can use the K1 & K2 buttons of SK to wake up the screen, power on or wake up all peripherals, and put the system back into the active on-screen operation mode.

  

Generally speaking, the currents of the above three modes are in descending order, and depending on the product, the bottom current of the screen off hibernation mode should be in the range of tens~hundreds of uA (Note: the hibernation current of the chip itself is only a few uA, and the examples here include other kinds of power consuming peripherals).

  

#### 3.5 Hibernation Mode Debugging

##### 3.5.1 Principles

The general principles of the system hibernation policy are. 

- The general principles of the system sleep policy are: the system non-Idle task has finished running, the BLE has finished its current work, all peripherals have finished their work and are in the Idle state, and the next executable task is at least 5ms away from the current time. When entering the Idle task of the FreeRTOS, the chip will be allowed to enter the Sleep mode. 



##### 3.5.2 General Conditions

The general preconditions for a system to enter low-power sleep are.

- Check if there is a task that is always working, and make sure that the task is designed according to the product logic.
- Check if there is a periodic event less than 5ms.
- Ensure that the BLE application complies with the specification
- Ensure that all peripherals are not working in the Idle state.  

In general, the first three conditions are easy to check and fulfill, and are less likely to be the reason why the chip fails to sleep. More likely is the last condition: **Any peripheral is still in working state**. 



##### 3.5.3 Determining whether a peripheral is working or not

The way to find out whether a peripheral is in working state is also very simple, the SDK provides 2 u32 variables with bit bits to record whether each peripheral is currently working. 

- The variables themselves are defined within the SDK, with extern references in the header file ${SDK}\drivers\inc\hal\gr55xx_hal_pwr_mgmt.h. Here are the variable names and corresponding bits. 
- The following is an enumeration of the variable names and corresponding bits. The bit of the enumeration value indicates the current state of the corresponding peripheral: if the bit is 1, the peripheral is being used; if it is 0, the peripheral is in idle mode. 
- When all the bits of both variables are 0, it indicates that the condition for the peripheral to be allowed to sleep has been fulfilled.


```
extern volatile uint32_t g_devices_state; 
```

The number of managed peripherals is 32, the lowest bit characterizes whether [DMA0] is working or not, and the highest bit characterizes whether [USB] is working or not. 


```c
		typedef enum
		{
		    PERIPH_DEVICE_NUM_DMA0 = 0,
		    PERIPH_DEVICE_NUM_DMA1,     //NO.=1
		    PERIPH_DEVICE_NUM_ISO7816,  //NO.=2
		    PERIPH_DEVICE_NUM_PKC,      //NO.=3
		    PERIPH_DEVICE_NUM_QSPI0,    //NO.=4
		    PERIPH_DEVICE_NUM_QSPI1,    //NO.=5
		    PERIPH_DEVICE_NUM_QSPI2,    //NO.=6
		    PERIPH_DEVICE_NUM_SPIM,     //NO.=7
		    PERIPH_DEVICE_NUM_SPIS,     //NO.=8
		    PERIPH_DEVICE_NUM_DSPI,     //NO.=9
		    PERIPH_DEVICE_NUM_I2C0,     //NO.=10
		    PERIPH_DEVICE_NUM_I2C1,     //NO.=11
		    PERIPH_DEVICE_NUM_I2C2,     //NO.=12
		    PERIPH_DEVICE_NUM_I2C3,     //NO.=13
		    PERIPH_DEVICE_NUM_I2C4,     //NO.=14
		    PERIPH_DEVICE_NUM_I2C5,     //NO.=15
		    PERIPH_DEVICE_NUM_UART0,    //NO.=16
		    PERIPH_DEVICE_NUM_UART1,    //NO.=17
		    PERIPH_DEVICE_NUM_UART2,    //NO.=18
		    PERIPH_DEVICE_NUM_UART3,    //NO.=19
		    PERIPH_DEVICE_NUM_UART4,    //NO.=20
		    PERIPH_DEVICE_NUM_UART5,    //NO.=21
		    PERIPH_DEVICE_NUM_I2S_M,    //NO.=22
		    PERIPH_DEVICE_NUM_I2S_S,    //NO.=23
		    PERIPH_DEVICE_NUM_PDM,      //NO.=24
		    PERIPH_DEVICE_NUM_HMAC,     //NO.=25
		    PERIPH_DEVICE_NUM_RNG,      //NO.=26
		    PERIPH_DEVICE_NUM_AES,      //NO.=27
		    PERIPH_DEVICE_NUM_PWM0,     //NO.=28
		    PERIPH_DEVICE_NUM_PWM1,     //NO.=29
		    PERIPH_DEVICE_NUM_SNSADC,   //NO.=30
		    PERIPH_DEVICE_NUM_USB,      //NO.=31
		    MAX_PERIPH_DEVICE_NUM
		} periph_device_number_t;
```



 ```c
extern volatile uint32_t g_extra_devices_state;
 ```

The corresponding managed peripherals are as follows.

```
		typedef enum
		{
		    EXTRA_DEVICE_NUM_CLK_CALIB = 0,
		    EXTRA_DEVICE_NUM_GPU,          //NO.=1
		    EXTRA_DEVICE_NUM_DC,           //NO.=2
		    EXTRA_DEVICE_NUM_OSPI,         //NO.=3
		    MAX_EXTRA_DEVICE_NUM
		} extra_device_number_t;
```



##### 3.5.4 Example

- If you do a state check before entering the Idle to hibernate, and find that the value of the g_extra_devices_state variable is 2, the corresponding bit is EXTRA_DEVICE_NUM_GPU, which indicates that the current GPU has not completed its work. Therefore, it cannot sleep yet.

After finding the peripheral that affects hibernation, further analyze the reason why it is still working, and if it should not be working at this time, then find out the reason why it is not working properly and solve the problem.

When hibernation fails, the following methods can be used to check the value of the peripheral working status variable.

- Use Keil's Debug mode, breakpoint at the pwr_mgmt_enter_sleep_with_cond function in port_pm.c, and check the values of the two variables. This method is inefficient 
- Get the SRAM addresses of the two variables from the Map table, and use Jlink to connect to the SK board to view them.
- Use Ozone debugging tool to add timed refresh monitoring to the variables. Use Ozone debugging tool to add timed refresh monitoring to the variables. Further analyze the peripherals that are working abnormally by determining which bits are 1. 

When the chip can sleep periodically, the connected JLink will be disconnected automatically due to sleep, which can also be used as a condition to assist in determining whether the chip has entered sleep.



#### 3.6 Current Waveforms for Each Operation Mode

The waveforms are measured using the KeySight current loop method, but the waveforms will be different if the voltage supply method is used. The waveforms mainly reflect the order of magnitude difference of the current in each mode, which is used to judge whether the working mode is switched normally or not, and does not reflect the actual current accuracy (without carefully doing the operations involving specific business layers such as shutting down the peripheral devices and checking the leakage of electricity).



##### 3.6.1 Current Waveforms for Operating Mode Switching

- Waveform 1: Change of current waveform from **Active mode** to **Screen off mode** to **Hibernate mode** after power on.

  ![1705548617340](../../_images/app/sk_watch_demo_current_1.png)



##### 3.6.2 Current waveform with BLE broadcast hibernation

- Waveform 2: Expanded current waveform in hibernation mode

  > Periodic waveform for BLE broadcast

  ![1705548693897](../../_images/app/sk_watch_demo_current_2.png)



Once the system power consumption has been debugged at the mode level, we can enter the detailed debugging phase, including optimizing the hibernation strategy of each peripheral, checking the system leakage, and improving the overall power consumption tuning of the system.





