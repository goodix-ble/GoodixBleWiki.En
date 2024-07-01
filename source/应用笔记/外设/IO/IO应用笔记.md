# I/O应用笔记 #


## 1. I/O基本功能介绍

- GR5xx的I/O系统分别有GPIO、AON IO和MSIO三种。其中GPIO属于MCU域，系统睡眠时不能产生中断、只能维持睡眠前的电平状态；AON IO属于Always On电源域，系统睡眠时能够产生中断和唤醒系统；MSIO既能传递数字信号也能传递模拟信号。

- I/O的供电域：GPIO0～GPIO15由VDDIO_1供电；其他GPIO以及所有的AON IO由VDDIO_0供电；MSIO由VBATL供电。它们作为输出时高电平的电压、作为输入时的最大输入电平电压，都是由其供电域的电压决定。

- I/O的中断：MSIO没有中断功能，其他I/O都有中断功能；中断触发方式可以配为高电平触发、低电平触发、上升沿触发、下降沿触发和双边沿触发（GR51xx没有双边沿触发功能）。

- I/O支持MUX为其他外设功能的I/O。GR533x的每个I/O都能单独MUX为所有外设范围中的某一种；除GR533x外的其他芯片，每个I/O只能MUX为该I/O特定几种外设范围中的某一种。具体参见Datasheet关于Pin Mux章节的描述，其中有一个Pin Mux Table，详细列举了每个I/O与其他外设的Mux对应关系。

- I/O默认状态：MSIO上电默认是模拟属性I/O；其他I/O上电默认状态是输入、下拉。

- I/O的驱动能力：GR551x在2.5 mA左右，GR552x在5 mA左右，GR533x在12 mA左右。具体参见Datasheet关于I/O章节的Electrical Specifications部分的描述。

- I/O内部有上下拉电阻可以配置，分别可配置为使能上拉、使能下拉、上下拉均不使能。注意不能同时使能上下拉电阻，否则I/O会漏电。I/O内部的结构框图如下，其中单个电阻的阻值在各个芯片型号中有差异，具体参见Datasheet关于I/O章节Electrical Specifications部分的描述：

  ![](../../../_images/io/IO-1.PNG)
  
  
## 2. I/O应用笔记

- 如何配置和使用I/O

  - 分别设置好I/O入参的pin（引脚号）、mode（输入/输出/中断/模拟）、pull（上下拉选择）、mux（选择作为I/O功能的mux）这四个参数，然后调用app_io_init()进行初始化（第一个入参是I/O的类型，第二个入参是上面配置的结构体参数）。
  
  - 输出：调用app_io_write_pin()进行I/O的高电平和低电平设置，也可调用app_io_toggle_pin()进行I/O电平的翻转。请注意，如果要快速设置I/O电平，也可以调用LL层的接口（在各种类型I/O的LL层头文件里），如ll_gpio_set_output_pin(GPIO0, LL_GPIO_PIN_4)。
  
  - 输入：调用app_io_read_pin()获取I/O电平。
  
- 如何配置中断I/O和作为唤醒源
  - 配置中断I/O时，上面参数的mode要设置为带_IT的模式，并选择合适的中断触发方式，如io_init.mode = APP_IO_MODE_IT_FALLING表示设置下降沿触发的中断。
  - 配置中断I/O时，需要调用app_io_event_register_cb()进行中断I/O的初始化，以及中断回调函数的设置。
  - 如果需要同时配置好几个中断I/O，设置好参数后，也可调用app_gpiote_init()统一进行初始化。
  - 几个I/O可以指向同一个中断回调函数；在中断回调函数里，根据p_evt->type和p_evt->pin来判断是否为想要的I/O响应的中断。
  - 对于I/O作为唤醒源，配置了AON IO的中断，也就具有唤醒的功能；GPIO没有唤醒功能；MSIO既没有中断功能，也没有唤醒功能。

   对于以上功能的使用，具体代码可以参考SDK\projects\peripheral\gpio\app_gpio示例工程。

- 上下拉电阻的配置原则
  
  - GPIO管脚设为输出时，应禁能内部上/下拉电阻。
  
  - GPIO管脚作为输入且连接的外部设备处于高阻抗状态时，应使能内部上拉或下拉电阻（注意：不能同时使能上拉和下拉）。
  
  - GPIO管脚设为输入且该管脚被外部设备拉高/低时，应禁能内部上/下拉电阻。
  
  - GPIO管脚未使用时，应使能内部下拉电阻。
  
  - GPIO管脚处于浮空状态，当引脚上有外部干扰电压时，GPIO管脚应使能内部上/下拉电阻。
  
- 如何设置I/O高电平的电压
  - I/O高电平的电压由VDDIO_0或VDDIO_1的电压决定（具体的I/O是受控于VDDIO_0还是VDDIO_1，上文“I/O基本功能介绍”章节有提到）。
  - 有些芯片型号会把VDDIO_0或VDDIO_1引出来，用户可以把外部电路LDO出来的电压（比如3.3 V或1.8 V）接到VDDIO_0/VDDIO_1上，来决定该域管控的I/O高电平电压是3.3 V还是1.8 V。
  - 用户也可以把VDDIO_0/VDDIO_1接到芯片的IO_LDO_OUT引脚，这样该域管控的I/O高电平电压就由内部的IO_LDO电压决定。
  - 有些芯片品型号的VDDIO_0或VDDIO_1没有引出来，对于没有引出来的VDDIO，其在芯片内部已经跟IO_LDO绑定在一起了，所以该域管控的I/O高电平电压也是由内部的IO_LDO电压决定。
  
- 使用MSIO时的注意事项
  - MSIO默认是模拟口，模拟口在没有信号输入时是高组态。
  
  - MSIO用于向ADC或比较器传递模拟信号，所以其内部通过门电路开关与ADC和比较器进行连接。此时要注意，MSIO上的电压不能超过VBATL！过高的电压容易把门电路冲击破坏，可能会损坏ADC或比较器模块。
  
  - MSIO没有中断功能。
  
  - MSIO作为数字高速I/O时（比如mux为SPI），建议提升MSIO的驱动电流，调用app_io_set_strength()进行驱动电流的设置。
  
- 如何配置IO的驱动能力（驱动电流大小）
  
  - 只有GR5525和GR533x可以配置IO的驱动电流大小。
  
  - 调用接口 uint16_t app_io_set_strength(app_io_type_t type, uint32_t pin, app_io_strength_t strength) 来配置IO的驱动电流大小。
  
  - 可配置驱动电流的档位分别有：
  
    `APP_IO_STRENGTH_LOW, /*< Select low output driver strength. ~ 2mA */ 	     APP_IO_STRENGTH_MEDIUM, /*< Select medium output driver strength. ~ 4mA */ APP_IO_STRENGTH_HIGH, /*< Select high output driver strength. ~ 8mA*/ APP_IO_STRENGTH_ULTRA, /*< Select high output driver strength. ~ 12mA*/`
