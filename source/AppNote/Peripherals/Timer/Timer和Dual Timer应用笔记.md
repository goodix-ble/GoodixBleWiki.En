# Application Note for Timer and Dual Timer

## 1. Introduction to Timer and Dual Timer Basic Functions
- The GR5xx chips feature 2 Timers and 2 Dual Timers. The main difference from the Sleep Timer is that the Timer and Dual Timer are 32-bit timers based on the system clock, so they cannot operate when the MCU is in sleep mode.
- They count down from the set RELOAD value and generate an interrupt when they reach 0.
- They belong to the MCU domain, so they power down and cannot function when the MCU is in sleep mode.
- Their clock source is the system clock, SystemCoreClock.
- The main differences between Timer and Dual Timer:
  - Dual Timer can divide the SystemCoreClock by 1/16/256.
  - Dual Timer can be configured to count in 16-bit mode.
  - In addition to Periodic mode, Dual Timer supports One-shot mode and Free-running mode (in Free-running mode, it restarts from the maximum value after reaching 0).
  - The Dual Timer in GR5526/GR5525/GR533x supports the BG_Load setting function (BG_Load setting function means that when updating the timer period value, the new period value is first stored in the BG_LOAD register. The new period value takes effect after the current period ends, ensuring the integrity of the current period. If the period value is updated directly in the RELOAD register, the timer will immediately start counting down from the RELOAD value, and the new period will take effect immediately, potentially disrupting the integrity of the previous period).
- The GR533x's GPTimer has added the following features:
  - Timer has added a Capture function. Each Timer supports 4-channel Capture; Capture mode supports rising edge, falling edge, and both edges.
  - Dual Timer has added an IO Control function, which can directly trigger IO actions under certain conditions. Each Dual Timer supports 3 IO controls; each IO can be bound to 5 types of Dual Timer events for triggering: Start, Compare1, Compare2, Period, and Stop. The IO actions support high level, low level, and level toggle.
  - Dual Timer has added a setting for a specified number of periods. Combined with the IO Control function, it can generate a specified number of square waves.

## 2. Application Notes for Timer and Dual Timer
- When using Timer or Dual Timer for timing, pay attention to the relationship between the set value and the timing period.
  - For Timer
      ```c
      Expect_time (s) = RELOAD / (SystemCoreClock-1)
      ```
  - For Dual Timer
      ```c
      Expect_time (s) = RELOAD/(SystemCoreClock/PRE-1)  
      ```
  - Note
      > The SystemCoreClock here should reflect the current system frequency. Therefore, if the system frequency changes, the set timing value should also change accordingly.
- When using Timer or Dual Timer for timing, also pay attention to prompt interrupt handling. In scenarios where Bluetooth LE operations are frequent, frequent interrupt preemption may cause some timing inaccuracies. Additionally, if you need to toggle IO in the timer interrupt for timing measurements, it is recommended to use low-level IO control functions.
- When updating the RELOAD value of the timing period, note that its update takes effect immediately, which may disrupt the current timing period. For chips other than GR551x, a BG_Load setting function has been added to the Dual Timer. If the precision of the timing period is important, it is recommended to use the Dual Timer of chips other than GR551x.
- When using the capture function of the Timer on GR533x, note that the IO used for capture should be configured as GPIO and set to input direction.
- When using the capture function of the Timer on GR533x, we often subtract the Channel Value read from the previous capture interrupt from the Channel Value read from the subsequent capture interrupt to obtain the time when the captured IO toggled. Pay attention to prompt interrupt handling in this case, otherwise, the Channel Value corresponding to the previous capture may be overwritten by the Channel Value corresponding to the next capture event.
- When using the IO Control function of the Dual Timer on GR533x, you need to first configure the corresponding IO to the Dual Timer function.