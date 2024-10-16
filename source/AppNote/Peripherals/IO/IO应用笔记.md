# I/O Application Notes

## 1. I/O Basic Functions Introduction
- The I/O system of the GR5xx includes three types: GPIO, AON IO, and MSIO. GPIO belongs to the MCU domain and cannot generate interrupts during system sleep, only maintaining its state before sleep; AON IO belongs to the Always On power domain and can generate interrupts and wake up the system during sleep; MSIO can transmit both digital and analog signals.
- I/O power domains: GPIO0 to GPIO15 are powered by VDDIO_1; other GPIOs and all AON IOs are powered by VDDIO_0; MSIO is powered by VBATL. The high level voltage when used as output and the maximum input level voltage when used as input are determined by the voltage of their respective power domains.
- I/O interrupts: MSIO does not have interrupt functionality, while other I/Os do; the interrupt trigger mode can be configured as high level triggering, low level triggering, rising edge triggering, falling edge triggering, and both edges triggering (GR51xx does not support both edges triggering).
- I/O supports MUX for other peripheral functions. Each I/O of the GR533x can be individually MUXed to one of all peripheral ranges; for other chips except GR533x, each I/O can only be MUXed to one of the specific peripheral ranges for that I/O. Refer to the Pin Mux section of the Datasheet for details, which includes a Pin Mux Table listing the MUX relationships between each I/O and other peripherals.
- I/O default state: MSIO defaults to analog attribute I/O upon power-up; other I/Os default to input with pull-down upon power-up.
- I/O drive capability: ~2.5 mA for GR551x, ~5 mA for GR552x, and ~12 mA for GR533x. Refer to the Electrical Specifications section of the Datasheet's I/O chapter for details.
- I/O has internal pull-up and pull-down resistors that can be configured to enable pull-up, enable pull-down, or disable both. Note that pull-up and pull-down resistors cannot be enabled simultaneously, otherwise the I/O will leak. The internal structure block diagram of the I/O is as follows, with the resistance value of a single resistor varying among different chip models. Refer to the Electrical Specifications section of the Datasheet's I/O chapter for details:
  ![](../../../_images/io/IO-1.PNG)

## 2. I/O Application Notes
- How to configure and use I/O
  - Set the four parameters for the I/O input: pin (pin number), mode (input/output/interrupt/analog), pull (pull-up/pull-down selection), and mux (select the mux for I/O function). Then call app_io_init() for initialization (the first parameter is the type of I/O, and the second parameter is the structure parameter configured above).
  - Output: Call app_io_write_pin() to set the high level and low level of the I/O, or call app_io_toggle_pin() to toggle the I/O level. Please note that if you want to quickly set the I/O level, you can also call the LL layer interface (in the LL layer header files of various types of I/O), such as ll_gpio_set_output_pin(GPIO0, LL_GPIO_PIN_4).
  - Input: Call app_io_read_pin() to get the I/O level.
- How to configure interrupt I/O and use it as a wake-up source
  - When configuring interrupt I/O, the mode parameter should be set to a mode with the _IT suffix, and an appropriate interrupt trigger method should be selected, such as io_init.mode = APP_IO_MODE_IT_FALLING to set an interrupt triggered by the falling edge.
  - When configuring interrupt I/O, you need to call app_io_event_register_cb() for interrupt I/O initialization and interrupt callback function setting.
  - If you need to configure several interrupt I/Os at the same time, after setting the parameters, you can also call app_gpiote_init() for unified initialization.
  - Several I/Os can point to the same interrupt callback function; in the interrupt callback function, determine whether it is the desired I/O response interrupt based on p_evt->type and p_evt->pin.
  - For I/O as a wake-up source, configuring the interrupt of AON IO also has the wake-up function; GPIO does not have the wake-up function; MSIO neither has the interrupt function nor the wake-up function.
   For the use of the above functions, you can refer to the example project SDK\projects\peripheral\gpio\app_gpio.
- Configuration Principles for Pull-up and Pull-down Resistors
  - When a GPIO pin is set as an output, the internal pull-up/pull-down resistors should be disabled.
  - When a GPIO pin is set as an input and the connected external device is in a high-impedance state, the internal pull-up or pull-down resistors should be enabled (note: both pull-up and pull-down resistors cannot be enabled simultaneously).
  - When a GPIO pin is set as an input and the pin is pulled high/low by an external device, the internal pull-up/pull-down resistors should be disabled.
  - When a GPIO pin is not in use, the internal pull-down resistor should be enabled.
  - When a GPIO pin is in a floating state and there is external interference voltage on the pin, the internal pull-up/pull-down resistors should be enabled.
- How to Set the Voltage of I/O High Level
  - The voltage of the I/O high level is determined by the voltage provided by VDDIO_0 or VDDIO_1 (whether a specific I/O is controlled by VDDIO_0 or VDDIO_1 is mentioned in the "Basic I/O Function Introduction" section above).
  - Some chip models expose VDDIO_0 or VDDIO_1, allowing users to connect the voltage output from an external circuit LDO (e.g., 3.3 V or 1.8 V) to VDDIO_0/VDDIO_1 to determine whether the high level voltage of the I/O controlled by this domain is 3.3 V or 1.8 V.
  - Users can also connect VDDIO_0/VDDIO_1 to the IO_LDO_OUT pin of the chip, in which case the high level voltage of the I/O controlled by this domain is determined by the internal IO_LDO voltage.
  - For some chip models where VDDIO_0 or VDDIO_1 is not exposed, the VDDIO is internally bound to the IO_LDO, so the high level voltage of the I/O controlled by this domain is also determined by the internal IO_LDO voltage.
- Precautions When Using MSIO
  - MSIO is by default an analog port, and when there is no signal input, the analog port is in a high-impedance state.
  - MSIO is used to transmit analog signals to the ADC or comparator, so it is internally connected to the ADC and comparator through gate switches. At this time, it should be noted that the voltage on the MSIO should not exceed VBATL! Excessive voltage can easily damage the gate switches, potentially damaging the ADC or comparator module.
  - MSIO does not have interrupt functionality.
  - When MSIO is used as a high-speed digital I/O (e.g., when mux is set to SPI), it is recommended to increase the drive current of the MSIO by calling app_io_set_strength() to set the drive current.
- How to configure the drive strength (drive current) of I/O
  - Only GR5525 and GR533x can configure the drive current of I/O.
  - Call the interface uint16_t app_io_set_strength(app_io_type_t type, uint32_t pin, app_io_strength_t strength) to configure the drive current of I/O.
  - The configurable drive current levels are:
    `APP_IO_STRENGTH_LOW, /*< Select low output driver strength. ~ 2mA */ APP_IO_STRENGTH_MEDIUM, /*< Select medium output driver strength. ~ 4mA */ APP_IO_STRENGTH_HIGH, /*< Select high output driver strength. ~ 8mA*/ APP_IO_STRENGTH_ULTRA, /*< Select high output driver strength. ~ 12mA*/`