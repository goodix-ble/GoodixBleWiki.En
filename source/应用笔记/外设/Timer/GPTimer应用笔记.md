# GPTimer应用笔记 #

## 1. GPTimer 基本功能介绍
- GR5xx芯片内部分别有2路Timer和2路Dual Timer, 它们统称为GPTimer。与Sleep Timer的最大区别在于，GPTimer是基于系统时钟下的32-bit定时器，所以MCU睡眠的时候不能工作。

- 它们都是从设定的RELOAD值开始往下计数，减到0会产生中断。

- 它们都是属于MCU域，所以MCU睡眠的时候会掉电，不能正常工作。

- 它们的时钟源都是系统时钟SystemCoreClock。

- Timer与Dual Timer的主要区别：
  - Dual Timer可以基于SystemCoreClock进行1/16/256的分频。
  - Dual Timer可以配置为16-bit进行计时
  - Dual Timer除了Periodic  模式，还支持One-shot模式和Free-running模式（Free-running模式即减到0后从最大值重新开始）。
  -  GR5526/GR5525/GR533x的Dual Timer支持BG_Load设置功能（直接修改RELOAD会立即生效，从而破坏当前正在计时的周期；而修改BG_Load是需要等当前计时周期结束后才更新计时周期）。
  
- GR533x的GPTimer，新增了以下功能：
  - Timer新增了capture功能。每个Timer支持4-channel的capture；Capture模式支持：上升沿、下降沿，双边沿。
  - Dual Timer新增了IO Control功能，即满足一定条件后可以直接触发IO的动作。每个Dual Timer支持3路IO控制；每路IO可以绑定5种Dual Timer事件进行触发，分别是Start、Compare1，Compare2，Period、Stop；触发IO的动作支持：高电平、低电平和电平翻转。
  - Dual Timer新增了指定周期个数的设置。结合IO Control功能，就可以实现指定个数的方波的产生。

## 2. GPTimer 应用笔记
- 利用Timer或Dual Timer进行定时，要注意设置值与定时时间的关系。

  - 对于Timer

      ```c
      Expect_time (s) = RELOAD / (SystemCoreClock-1)
      ```

  -   对于Dual Timer

      ```c
      Expect_time (s) = RELOAD/(SystemCoreClock/PRE-1)  
      ```

      

  -   注意

      >   这里的SystemCoreClock要反映当前的系统主频，所以如果系统主频变化了，设置的定时value也要跟着变化。

      

- 利用Timer或Dual Timer进行定时，还要注意中断处理的及时性。对于BLE业务比较频繁的场景，中断频繁被抢占可能会导致定时有一定的误差；另外，如果要在定时器中断里面翻转IO进行定时测量等，建议用LL层的IO控制函数。

- 更新定时周期RELOAD值的时候，注意它的更新是即时生效的，所以可能会导致当前正在定时的周期被破坏。GR551x以外的几款芯片，在Dual Timer上新增了BG_Load的设置功能。如果在意定时周期的严谨性，建议用GR551x以外几款芯片的Dual Timer。

- GR533x使用Timer的捕获功能时，要注意用来捕获的IO要设置为输入模式（Capture不是特殊的第二功能，所以该IO配置MUX时依然是MUX为GPIO）。

- GR533x使用Timer的捕获功能时，我们往往会把前后两次捕获中断读取到的channel value的值相减，得到被捕获IO翻转的时间。这个时候要注意中断处理的及时性，否则上一次捕获对应的channel value可能会被下一次捕获事件对应的channel value所覆盖。

- GR533x使用Dual Timer的IO Control功能时，需要先把对应的IO mux为Dual Timer功能。

