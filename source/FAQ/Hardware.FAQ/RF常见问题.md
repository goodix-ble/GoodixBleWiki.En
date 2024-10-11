## FAQ for RF



### 1. Can the PI circuit for RF be simplified or removed?
* The PI circuit near the GR5xx end is used to match the internal PA of the chip and cannot be simplified and removed. It is not recommended to change the inductance value and capacitance value of the circuit, and it is recommended to keep consistent with the recommended circuit. The PCB design follows the corresponding RF port design requirements of the corresponding hardware design guide. If the PCB design requirements cannot be fully followed due to structural and other reasons, and the RF performance after returning to the board is not ideal, the parameters can be properly fine-tuned after the RF or hardware engineer's test verification. The parameters can usually be adjusted according to the PA Load Pull matching method. See the GR5xx RF Matching and Commissioning Guide for details. In addition, the impedance on the RF channel coming out of the chip PI is 50 Ω, which is compatible with any 2.4 GHz band antenna on the market (2400 MHz to 2484 MHz).
* The PI circuit near the antenna end is used to match the antenna, and the circuit can be changed according to the antenna used. The matching of the antenna can be adjusted simply by testing the S11 parameters of the vector network analyzer or Smith chart. However, the gain, directivity and other indicators of the antenna are recommended to seek a professional antenna factory to complete the matching test.



### 2. How does GR551x extend PA or FEM to improve transmission distance?

   * The GR551x supports extended external PAs.
   * GPIO2 is used as the external PA RX enable signal and GPIO3 is used as the external PA TX enable signal.
   * The corresponding function needs to be configured in the software. Before the RF circuit acts on TX or RX, the corresponding level will be pulled up, and after that, the level will be pulled down.
   * The GR551x itself does not use these signals to control, but only to control the external FEM.



### 3. What are the reasons for the low conducted sensitivity and transmit power of the GR5xx?

   * Whether the RF matching parameters are selected according to the reference design.
   * The first component of the GR5xx RF layout matching network is placed no more than 1 mm from the RFIO pin.
   * The RF wiring shall be as short and straight as possible. If the structural restriction requires turning, the inverted arc shall be required at the corner. The right angle or the included angle less than 90 ° is prohibited.
   * The surface layer is preferred for the RF line to avoid punching holes and changing layers, and to avoid the existence of branches in the line. The complete reference ground plane must be ensured below the RF line. The RF line width shall be designed to be consistent with the pad of the matching device as far as possible, so as to avoid damaging the continuity of the characteristic impedance of the 50 Ω transmission line due to the inconsistency between the pad width of the component and the trace width.
   * DC-DC ripple needs to be less than 16 mV.
   * The 32m XO crystal clock needs to be calibrated.



### 4. Why are there two first matching capacitors in the GR5331/GR5330 series?

   - In the FCC harmonic test, it is necessary to make a separate filtering treatment at the position of higher harmonics. For example, the 0.3 pF material (GRM0335C1HR30WA01) of the reference design is a special selection, and the impedance point at the 7th harmonic position is the lowest (the self-resonance point of the capacitor). 2 pF material (GRM0335C1H2R0BA01) has the lowest impedance in the third harmonic, which can play a better filtering effect.



### 5. Why are there small pF capacitors on the GR533x series VBAT _ RF and GPIO0/1?

   - In the FCC harmonic test, the high-order harmonics of the GR533x series are mainly radiated through the RF _ TX pin and its nearby pins, especially the VBAT _ RF pin, so we deliberately added a pF capacitor on the VBAT _ RF. The capacitor is also specially selected to have the self-resonance point at the frequency band to be filtered. For example, the GR5332 series is selected to have 3.9 pF (the self-resonance point is at the 2nd harmonic position), and the GR5331/GR5330 series is selected to have 2.0 pF (the self-resonant point is at the 3rd harmonic position).
   - GPIO0/1 may also have higher harmonic radiation in the actual measurement process, but in general, the pF capacitor of these two pins is only reserved as a debugging position, and whether pF capacitor filtering needs to be added is determined according to the actual FCC test results.
   - Refer to the RSE section of the [GR533x Hardware Design Guide](https://docs.goodix.com/zh/online/hardware_design_guide_d/V1.2)for how to optimize Layout to optimize higher harmonics.



### 6. What about the poor modulation characteristics of GR533x series?

   - In the GR533x series test, if it is found that the modulation characteristic index is relatively poor (such as the typical df2 99% index, Max drift rate, etc.), or the index Fail Bluetooth protocol appears, it is recommended to switch to the SYSLDO power supply mode first. In general, it is caused by the excessive ripple of the DCDC power supply.
   - It is recommended to adjust the parameters of the VDD _ RF filter bead after it is confirmed that the problem is caused by the DCDC power supply. Please [GR533x Reference Design](https://www.goodix.com/zh/docview/GR533x Reference Design_V1.2?objectId=362&objectType=document&version=609)refer to the recommended bead. Increase the DCR parameter of the bead when selecting the type. In general, the DCDC ripple can be better suppressed.
   - Check the reason for the increase of DCDC ripple. First, check the loop of DCDC Layout to see if it is caused by the excessive loop of DCDC IN/OUT. It is necessary to change the PCB Layout. For the DCDC power supply layout, please refer to [GR533x Hardware Design Guide](https://docs.goodix.com/zh/online/hardware_design_guide_d/V1.2)the power supply layout section of.



### 7. What is the reason why the GR533x SK board power or sensitivity cannot be matched to the GR533x different PCB boards using reference design matching parameters?

   * Factors that cause differences between the user's actual match parameters and the reference match parameters include:
        * The matching parameters [GR533x Reference Design](https://www.goodix.com/zh/docview/GR533x Reference Design_V1.2?objectId=362&objectType=document&version=609)in are based on GR533x SK board debugging.
        * The PCB stack structure may affect the impedance and parasitic parameters of the RF traces.
        * RF components that differ from the reference design recommendation BOM are used.
        * Layout differences due to PCB structure limitations.

   * When designing products based on GR533x, it is recommended to refer to the recommended matching device patches in the [GR533x Reference Design](https://www.goodix.com/zh/docview/GR533x Reference Design_V1.2?objectId=362&objectType=document&version=609), and then fine-tune the matching parameters according to the PCB stack and layout of the actual product. For detailed matching and debugging guidelines, please refer to [GR533x RF Matching Commissioning Guide](https://docs.goodix.com/zh/online/rf_matching_bl_d/V1.0).


















