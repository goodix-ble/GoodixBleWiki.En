## ADC Application Notes



### 1. Introduction to ADC Basic Functions

This chapter mainly introduces the overall framework and basic functions of the GR5xx ADC, helping users quickly understand the basic usage of the ADC.
![](../../../_images/adc/1-1-1.png)
The internal ADC of the GR5xx is an analog-to-digital converter based on the Successive Approximation Register (SAR) method. It features a multiplexer at its input end, providing multiple analog signal inputs. By selecting through the multiplexer, it can sample the selected signal at a given time. Among the supported multiple analog inputs, two channels are used for internal VBAT and temperature monitoring, which can be used for PMU adjustment and RF circuit configuration adjustment within the chip to achieve optimal performance. The ADC can be configured in single-ended input mode or differential input mode to perform single-ended or differential measurements. The reference voltage of the ADC supports both internal and external reference voltages. The internal reference voltage can be set to 0.8 V, 1.2 V, or 1.6 V; the external reference voltage can be input through MSIO0 to MSIO3. For any set reference voltage (Vref), the maximum analog input voltage for the ADC should be twice the reference voltage (2 x Vref).

#### 1.1 ADC Function Overview
- **About ADC Input Sources**
  - For the P channel, it supports MSIO0 to MSIO7 and Internal VRef input.
  - For the N channel, it supports MSIO0 to MSIO7, Temperature Sensor, VBAT Sensor, and Internal VRef input.
  - In single-ended mode, the N channel is used for signal input, and the output is the signal from the N channel.
  - In differential mode, the P and N channels are used for differential signal input, and the output is the differential signal of P-N.
- **About ADC Reference Voltage**
  ![](../../../_images/adc/1-1-2.png)
  - External reference voltage can only be input through MSIO0 to MSIO3.
  - The internal reference voltage is obtained by a constant current source passing through resistors of different values, resulting in different reference voltage settings.
  - Since only the 0P8, 1P2, and 1P6 settings are calibrated at the factory, it is recommended to use only these three settings.
  - Due to process differences between different chips and variations in internal resistance R0 of the same chip at different temperatures, the specific value of the internal reference voltage may vary, which is why factory calibration is necessary.
- **About ADC Clock**
  - Every 15 ADC Clocks generate 1 Code value, with the first 2 Clocks being the signal sampling hold time and the remaining 13 Clocks performing 13-bit quantization encoding. Therefore, the relationship between the sampling rate and the ADC clock is: 1sps = ADC clock/15.
  - Setting the ADC clock frequency is equivalent to setting the sampling rate.
  - Once the clock frequency is selected, the signal sampling hold time of 2 Clocks is determined. This requires that the charging time of the RC charging circuit, composed of the external circuit impedance R and the ADC internal capacitor C (2 pF; see Datasheet), does not exceed the signal sampling hold time.
- **About Internal Temperature Sensor**
  ![](../../../_images/adc/1-1-3.png)
  - The temperature sensor converts the temperature signal into an analog voltage signal, which is generally in the mV range.
  - The measurable range of the temperature sensor is –40℃ to 80℃.
  - The GR55xx internally uses the temperature measurement function to adjust RF parameters and implement DC power supply strategies.
- **About Vbat Sensor**
  ![](../../../_images/adc/1-1-4.png)
  - The Vbat Sensor is essentially a voltage divider circuit that divides the chip's supply voltage Vbat.
  - At room temperature, the typical voltage division ratio is 3.854, so Vsensor = VBAT/3.854.
  - Note that this voltage division ratio is a typical value, and there may be individual differences between different chips; factors affecting the voltage division ratio include device process and ambient temperature.
- **About the Conversion Formula Between ADC Code and Actual Voltage**
  - code — V conversion formula: ***V = (code + offset) / slope***
  The slope and offset are calibration parameters, and different reference voltages correspond to different parameters.
- code — Temperature conversion formula: ***Temp = ((code – temp_offset) / adc_slope) / (0.00175) + temp_vref***
    The code here is the code measured for the TempSensor based on the internal 0P8 reference voltage; temp_vref is the ambient temperature during calibration; temp_offset is the code value output by the ADC at the calibration temperature; slope is the slope corresponding to the 0P8 reference voltage.
  - code — V conversion formula: ***VBat = (code + offset) / slope x 3.854***
  The offset and slope correspond to the internal 0P8 reference voltage; 3.854 is an empirical value, and this ratio coefficient can be recalibrated if higher accuracy is required. Additionally, it can be seen that the measurement error for VBAT is magnified by 3.854 times compared to the error for the 0P8 reference voltage.

#### 1.2 Single-Ended Mode Measurement
Steps for single-ended mode measurement using ADC:
1) Configure ADC parameters.
- pin_cfg should specify the type and number of the input signal pin.
- The channel_n in the init structure should specify the channel number of the input signal.
- Configure input_mode for single-ended operation.
- Set the appropriate reference voltage type, reference voltage value, and ADC clock frequency.
- If data transfer using DMA is required, specify the DMA handle and channel through dma_cfg.
2) Call app_adc_init to complete the initialization. In asynchronous mode, a callback function needs to be specified.
3) If DMA mode is required, call app_adc_dma_init to complete the initialization.
4) Invoke the conversion interface to initiate ADC sampling.
5) For the synchronous interface, the function returns after collecting the number of codes specified by the input parameter; for the asynchronous interface, a callback is triggered after collecting the number of codes specified by the input parameter.
6) Call the voltage convert interface to convert each code value to the corresponding voltage value. The interface utilizes the slope and offset parameters calibrated during production, and then calculates based on the single-ended mode formula if the ADC handle is in single-ended mode.
Refer to the SDK's ADC example project in the void adc_single(void) function for key code.

#### 1.3 Differential Mode Measurement
Steps for differential mode measurement using ADC:
1) First, configure the ADC parameters.
- `pin_cfg` needs to specify the pin type and pin number for the differential signals P and N.
- The `init` structure's `channel_p` and `channel_n` need to specify the channel numbers corresponding to the input differential signals P and N.
- Set `input_mode` to differential mode.
- Configure the appropriate reference voltage type, reference voltage value, and ADC clock frequency.
- If DMA is needed to transfer data, specify the DMA handle and channel through `dma_cfg`.
2) Call `app_adc_init` to complete the initialization. For asynchronous mode, a callback function needs to be specified.
3) If DMA mode is required, call `app_adc_dma_init` to complete the initialization.
4) Call the conversion function to start ADC sampling.
5) For the synchronous interface, the function returns after collecting the number of codes specified by the input parameter; for the asynchronous interface, a callback is triggered after collecting the number of codes specified by the input parameter.
6) Call the voltage conversion interface to convert each code value to the corresponding voltage value. The interface will use the slope and offset parameters calibrated during production, and then calculate based on the differential mode formula if the ADC handle is in differential mode.
7) Note that the result of the differential measurement is the difference between P and N.
In the key code, apart from the configuration part, other parts are similar to the single-ended measurement mode. The configuration part can refer to the following code:
![](../../../_images/adc/1-3-1.png)

#### 1.4 How to Select External Reference Voltage for Measurement
Steps to measure using ADC with an external reference voltage:
1) Configure ADC parameters.
- In pin_cfg, specify the input signal, and also the pin type and pin number for the reference voltage input (extern_ref).
- The init structure's channel_p and channel_n specify the channel numbers for the input signal.
- Set the input mode to the required sampling mode.
- Note that the reference voltage source (ref_source) should be set to the external input channel number. The reference voltage value in the initialization parameters is not relevant, so configure the appropriate sampling clock frequency.
- If using DMA for data transfer, specify the DMA handle and channel through dma_cfg.
2) Call app_adc_init to complete the initialization. For asynchronous mode, specify a callback function.
3) If using DMA mode, call app_adc_dma_init to complete the initialization.
4) Call the conversion function to start ADC sampling.
5) For the synchronous interface, the function returns after collecting the number of codes specified in the input parameters; for the asynchronous interface, a callback is generated after collecting the number of codes specified in the input parameters.
6) Call the voltage conversion function to convert each code value to the corresponding voltage value. Note that you need to call the app_adc_voltage_extern function and specify the reference voltage value in the input parameters.
In the key code, apart from the configuration part, other parts are similar to the single-ended measurement mode. Refer to the following code for the configuration part:
![](../../../_images/adc/1-4-1.png)

#### 1.5 How to Measure Chip Supply Voltage
Steps for measuring chip supply voltage using ADC:
1) Configure ADC parameters.
- pin_cfg is not relevant at this stage.
- The channel_n in the init structure needs to specify the VBAT channel as ADC_INPUT_SRC_BAT.
- Set input_mode to single-ended mode.
- Set the reference voltage to internal 0.8V.
- If DMA is required for data transfer, specify the DMA handle and channel through dma_cfg.
2) Call app_adc_init to complete initialization. In asynchronous mode, a callback function needs to be specified.
3) If DMA mode is required, call app_adc_dma_init to complete initialization.
4) Call the conversion interface to start ADC sampling.
5) For synchronous interfaces, the specified number of codes will be returned after sampling; for asynchronous interfaces, a callback will be triggered after sampling the specified number of codes.
6) Call the app_adc_vbat_conv interface to convert each code value to the corresponding chip supply voltage value. The interface will use the voltage division relationship between the sampled voltage and the chip supply voltage to convert it to the chip's supply voltage.
Key code can be found in the SDK's ADC example project in the void battery_measure (void) function.

#### 1.6 How to Measure Internal Chip Temperature
Steps for measuring the internal temperature of the chip using ADC:
1) Configure ADC parameters.
- pin_cfg is not relevant at this stage.
- The channel_n in the init structure needs to specify the channel ADC_INPUT_SRC_TMP for the temperature signal.
- Set input_mode to single-ended mode.
- Set the reference voltage to the internal 0.8V range.
- If DMA is needed to transfer data, specify the DMA handle and channel through dma_cfg.
2) Call app_adc_init to complete the initialization. In asynchronous mode, a callback function needs to be specified.
3) If DMA mode is needed, call app_adc_dma_init to complete the initialization.
4) Call the conversion interface to start ADC sampling.
5) If using a synchronous interface, the interface will return after collecting the number of codes specified in the input parameter; if using an asynchronous interface, a callback will be triggered after collecting the specified number of codes.
6) Call the app_adc_temperature_conv interface to convert each code value to the corresponding temperature value. The interface will use the relationship between the sampled voltage and the actual temperature to convert it to a temperature value.
Key code can be referenced in the SDK's ADC example project in the void temperater_measure (void) function.

#### 1.7 How to Perform Multi-Channel Measurement
The GR5xx ADC has only one physical entity and a single corresponding FIFO, so it cannot simultaneously acquire data from multiple channels. However, it can acquire data from multiple channels sequentially. Using the SDK's multi-channel acquisition interface, there is no need to reinitialize the ADC after acquiring data from one channel before moving to another. Channel switching is managed by the SDK within interrupts.
> Note: The current multi-channel acquisition interface provided by the SDK requires that all channels use the same acquisition mode, reference voltage, and sampling clock frequency.
Steps to perform multi-channel measurement using the ADC:
1) Configure and initialize the ADC according to the first channel's parameters.
2) Initialize the node parameters for each channel. The node parameters mainly include the buffer address for the acquired data, the length of the acquired data, and the channel number.
3) Link each channel's node to form a linked list.
4) Call the `app_adc_multi_channel_conversion_async()` interface to start multi-channel acquisition. The input parameters are the head address of the linked list and the number of nodes.
5) When the data acquisition for all specified channels is complete, the callback function set during initialization will be called.
6) Use the voltage interface to convert the code values in each channel's buffer to voltage values.
Key reference code is as follows:
![](../../../_images/adc/1-7-1.png)
Benefits of using the multi-channel acquisition interface:
1) No need to repeatedly deinitialize and initialize the ADC to switch channels.
2) Channel switching is managed by the SDK Low Layer, resulting in faster speed.
3) By utilizing the multi-channel acquisition interface and pointing all nodes to the same channel, a large amount of data can be acquired with a single interface call, avoiding the limitation of the asynchronous acquisition interface's one-time data acquisition length.



### 2. Typical ADC Applications

This chapter discusses the metrics and applications of ADC through real project scenarios.



#### 2.1 How to Evaluate Whether the Measurement Range Meets the Requirements

In actual project evaluations, we often encounter customers who provide the maximum or minimum value of a measured signal and then need to assess whether the ADC's measurement range meets the requirements. Here, it is necessary to consider both single-ended mode and differential mode.
1) Measurement Range in Single-Ended Mode
The reference voltage primarily affects the ADC's measurement range in single-ended mode. The internal structure of the ADC determines that the maximum measurement voltage in single-ended mode is twice the reference voltage (VREF). For example, if the chosen reference voltage is 0P8, the maximum measurement range can reach approximately 1.6 V. Due to variations in chip manufacturing processes, the actual reference voltage corresponding to the nominal 0P8 may vary slightly, so the specific maximum measurement range may also vary. Below are the typical values for each reference voltage level and the corresponding maximum measurement range of 2VREF.

| Typical Value | Reference Voltage | Max Range 2VREF |
| ------------- | ----------------- | --------------- |
| 0.85 V        | 0P8               | 1.7 V           |
| 1.28 V        | 1P2               | 2.56 V          |
| 1.6 V         | 1P6               | 3.2 V           |
In single-ended mode, another factor that limits the measurement range is the ADC's upper and lower saturation voltages. Within the lower saturation voltage range, the ADC code value does not start to change with the increase in signal; within the upper saturation voltage range, the ADC code value cannot continue to change with the increase in signal. The typical values for the upper and lower saturation voltages for each reference voltage level are as follows:

| Reference Voltage | Lower Saturation Voltage | Upper Saturation Voltage |
| ----------------- | ------------------------ | ------------------------ |
| 0P8               | 0.033 V                  | 1.567 V                  |
| 1P2               | 0.052 V                  | 2.348 V                  |
| 1P6               | 0.072 V                  | 3.128 V                  |
**Therefore, the upper and lower saturation voltages for each reference voltage level are the true measurement range of the ADC in single-ended mode.**
When evaluating a customer's project, it is first necessary to ensure that the settings fall within the upper and lower saturation voltage range of the reference voltage. Additionally, to achieve better linearity in measurements, it is best to choose an appropriate reference voltage so that the measured signal falls near VREF.
2) Measurement Range in Differential Mode
The reference voltage primarily affects the measurement range in differential mode. The internal structure of the ADC determines that the differential result needs to fall within the range of ±2VREF, i.e., (-2VREF) < (P-N) < (+2VREF). Similarly, due to variations in chip manufacturing processes, the actual value corresponding to the reference voltage may vary, and the typical values for each reference voltage level are the same as in single-ended mode.
Secondly, differential mode has a common-mode limitation, i.e., the common-mode voltage limit. Assuming the common-mode voltage limit is Vmode, each end of the differential input (P or N) must be above the common-mode voltage Vmode and below (2VREF - Vmode); otherwise, the ADC code value will not change with the input signal. The common-mode voltage limits corresponding to different reference voltages are also different. Below are the typical values for the common-mode voltage limit Vmode for each reference voltage level.

| Reference Voltage | Common Mode Limit Vmode Typical Value |
| ----------------- | ------------------------------------- |
| 0P8               | 0.4 V                                 |
| 1P2               | 0.55 V                                |
| 1P6               | 0.7 V                                 |
Therefore, for differential mode, to evaluate whether the ADC can cover the range of the measured signal, the following conditions must be met:
**1)  (-2VREF) < (P-N) < (+2VREF)**
**2)  Vmode < P or N input < (2VREF - Vmode)**

#### 2.2 How to Evaluate Whether the Resolution Meets the Requirements
Many developers prefer to use ENOB to evaluate the resolution of an ADC, which is reasonable if the measured signal is an AC signal. ENOB, or Effective Number of Bits, is derived from the ADC's Signal-to-Noise and Distortion Ratio (SNDR) and is related to the noise of the signal. With the ENOB known, we can determine the ADC's actual resolution based on the precision of the effective bits.
*Example:*
*ENOB = 10 bits, if the maximum measurement range of the signal is Vfull, then the actual resolution is Vfull/(2^10).*
However, for DC measurement signals, it is more appropriate to use INL to evaluate the ADC's resolution, as DC signals are primarily affected by quantization error. INL, or Integral Non-Linearity, is the main indicator for measuring quantization error. Based on INL, we can determine the maximum linear error of the signal, which is the maximum measurement error. Since INL is often measured in LSB, we need to convert 1 LSB to its corresponding voltage to determine the resolution. According to the definition of LSB, assuming the maximum measurement range of the signal is Vfull and the physical quantization bits are 13 bits, then 1 LSB = Vfull/(2^13) V. Finally, based on INL and LSB, we can determine the actual resolution of the ADC.
*Example:*
*INL = 4 LSB, if the maximum measurement range of the signal is Vfull and the physical quantization bits are 13 bits, then the actual resolution of the ADC is 4 x Vfull / (2^13), unit: V.*
It should be noted that the maximum measurement range Vfull differs between differential mode and single-ended mode, as discussed in section 2.1 above. The INL indicator marked in our Datasheet is measured in differential mode, so the maximum measurement range in differential mode should be used for calculation.

#### 2.3 How to Improve Measurement Accuracy
To improve the actual measurement accuracy of the ADC, the following methods can be referenced: oversampling followed by mean filtering, oversampling followed by jitter suppression, and piecewise interpolation fitting. Among these, oversampling followed by mean filtering mainly improves accuracy by reducing noise; oversampling followed by jitter suppression mainly improves accuracy by eliminating outlier data points. These two methods can be used in combination. Piecewise interpolation fitting mainly involves recalibrating the slope and offset in segments to achieve better linearity and thus improve accuracy. Users can take corresponding measures based on the specific conditions of their projects to improve measurement accuracy.
1) **Oversampling Followed by Mean Filtering**
Increase the sampling rate to obtain more data points within the same time frame. For example, if the previous sampling clock was 1M, increasing the sampling clock to 16M will result in 16 times more data points within the same time frame. Then, average every 16 code values collected. The resulting code values, having reduced some noise through averaging, can achieve better measurement accuracy, specifically reflected in an improvement in Effective Number of Bits (ENOB).
The number of oversampling points varies under different reference voltages, and the potential for ENOB improvement also varies. Below are the results from our internal experiments (based on GR533x testing):
![](../../../_images/adc/2-3-1.png)
It is worth noting that although oversampling requires collecting more data points, and the collection time remains the same, the higher sampling clock configuration will slightly increase power consumption. However, this is the power consumption in MCU working mode and does not affect the current in sleep mode.
2) **Oversampling Followed by Dynamic Programming Jitter Suppression**
If a large number of data points are collected continuously (128 codes or more), some code values may exhibit significant jumps due to signal interference. For these jump points, mean filtering cannot achieve good results. The dynamic programming (DP) jitter suppression method introduced here is a better filtering method for such scenarios.
To suppress jitter using the dynamic programming (DP) algorithm, first define a jitter factor, for example, set it to 6, which satisfies:
![](../../../_images/adc/clip_image002.gif)
We consider the current point ![](../../../_images/adc/clip_image003.gif) as a jitter point. The DP algorithm first needs to find the initial conditions. Based on sample observations, usually, no more than three numbers will jitter simultaneously. First, traverse the data sample to find three non-jitter numbers as the starting point. Subsequently, according to the DP algorithm, compare each number with the previous two to determine if the current number is not a jitter point. Define a valid function ![](../../../_images/adc/clip_image004.gif), if it satisfies:
![](../../../_images/adc/clip_image005.gif)
then ![](../../../_images/adc/clip_image006.gif) is True, otherwise False. The DP algorithm can be written as:
![](../../../_images/adc/clip_image007.gif)
where i is the first pointer in ![](../../../_images/adc/clip_image008.gif) that satisfies ![](../../../_images/adc/clip_image009.gif). Considering low sampling rates or significant data changes, if no three consecutive non-jitter points are found during the first data traversal, or only one set of non-jitter data is found, it can be simplified as insufficient sampling rate, degrading to ordinary mean filtering:
![](../../../_images/adc/clip_image010.gif)
Otherwise, filter according to the DP algorithm:
![](../../../_images/adc/clip_image011.gif)
The time complexity of this algorithm is O(n), and the space complexity is O(n). Considering the limited resources of the GR5xx chip, the algorithm is optimized. Except for the debugging stage where DP raw data needs to be printed, only the mean value is needed in actual use, so DP data does not need to be saved. When determining ![](../../../_images/adc/clip_image012.gif), only the previous two valid values or pointers need to be saved, while recording the cumulative sum and total number of all DP numbers. After optimization, the space complexity can be reduced to O(1).
The fitting code is as follows, first find the DP head and record the pointer.
![](../../../_images/adc/2-3-2.png)
Determine whether the current pointer meets the requirements. If no pointer is found, or the pointer directly points to the last node, it is considered that the current sampling rate is insufficient, and it degrades to mean filtering.
![](../../../_images/adc/2-3-3.png)
If the requirements are met, first record the sum of the current three data and the total number, then proceed with subsequent traversal.
![](../../../_images/adc/2-3-4.png)
Finally, output code_aver as the DP algorithm output.
3) **Piecewise Interpolation Fitting**
The calibration method for the BLE production line is to take one point at 20% of the measurement range and another at 80%, then connect these two points. The slope and offset of this line are used for calibration. If a user requires very high measurement accuracy for a certain signal segment, the slope and offset calibrated by the production line may not meet the requirements. In this case, the user can recalibrate based on the piecewise interpolation fitting method for a specific signal range.
For example, if a user requires a measurement accuracy of 1.5 mV for signals less than 80 mV, the user can divide the signal below 80 mV into 8 segments, calibrate each segment, and save the slope and offset of each segment and the code range of that segment into the chip. After ADC collection, determine the signal range based on the collected code values, then use the corresponding slope and offset from the corresponding range for calculation. This way, better accuracy can be achieved.
Below is a comparison of the measurement accuracy after re-fitting for signals less than 80 mV and greater than 80 mV based on the GR533x SK board, compared to the measurement accuracy calibrated by the production line:
![](../../../_images/adc/2-3-5.png)

#### 2.4 Calibration Method for Selecting Special External Reference Voltage
The BLE production line calibration is mainly based on the internal reference voltage. Although 1 V external reference voltage calibration parameters are also provided, these parameters are based on the 1 V reference voltage generated in the production line environment, which may differ from the reference voltage actually used by the user. Therefore, if the user chooses a special external reference voltage, it is recommended to recalibrate to achieve higher measurement accuracy. The specific calibration method is as follows:
1) Select the external reference voltage as the reference source and configure the single-ended mode to initialize the ADC.
2) Input a clean external reference voltage to the reference source input pin (note that only MSIO0 to MSIO3 can be selected), and record the reference voltage value as z.
3) Connect another clean input source to the N-end input of the ADC, adjust the input voltage to be approximately 20% of 2Vref, and record the input voltage value as y0.
4) Start the ADC to collect 1024 points, then average these points, and record the average value as x0.
5) Change the input voltage to be around 80% of 2Vref, and record the value as y1.
6) Using the above method, obtain the average of 1024 points, and record it as x1.
7) Based on the formula ![](../../../_images/adc/clip_image013.gif), substitute the above (x0, y0) and (x1, y1) to calculate the slope and offset.
The slope and offset obtained here correspond to the slope and offset of the external reference voltage selected by the user, and are saved in the chip.
Later, when measuring based on this calibrated external reference voltage, the actual voltage can be converted from the obtained code value using the following formula:
![](../../../_images/adc/clip_image014.gif)
The slope and offset in the formula are the slope and offset calibrated above, and z is the specific value of the selected external reference voltage.