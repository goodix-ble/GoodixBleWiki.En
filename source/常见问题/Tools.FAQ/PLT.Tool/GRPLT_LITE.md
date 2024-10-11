## FAQ for GRPLT Lite 



### 1. What is the principle of crystal calibration?

-   The GU module starts the PWM at the beginning of the test and sends a specific square wave signal to the IO port corresponding to the DUT, and the DUT calibrates based on the square wave. Currently using a 40 Hz square wave to calculate the count in one cycle at a running rate of 64m, the expected count is:

    
    $$
    64M \times 1 \div 40 = 1.6M
    $$

-   The corresponding card control threshold algorithm is:
    

    $$
    N = X \div 1.6
    $$
    
    
    
-   Where N is the desired PPM and X is the count offset (i.e. ErrLimit in the job setup). The default card control threshold of the current work order is 60, and the PPM is 37.5. In principle, the offset value should not exceed 80 (i.e. 50 PPM). When the offset is large, Bluetooth is easily disconnected.

### 2. What is the RSSI test method?

-   At the beginning of the test, the GU module will broadcast data as a Slave (the broadcast data value is a random value of 6 bytes to distinguish the broadcast signals of GUs at different stations), and the DUT will SCAN as a Master to obtain the RSSI value. (Neither the GR533x nor the GR5625 support RSSI, and there are no plans to support any future models.)

### 3. How is custom encryption different from Goodix encryption?

-   GOODIX encryption is hardware encryption, which uses the internal encryption module of the Goodix Bluetooth LE to encrypt the Flash and close the SWD. This operation is irreversible. The application firmware also needs to be encrypted to run, which is the automatic encryption of the hardware; Custom encryption is to encrypt some Flash data (such as NVDS data or Flash resource files) according to the information written by eFuse. If the customer wants to stop using encryption, it can be burned again.

### 4. Test Firmware failed to run (0x39), what could be the cause?

- Check that the work order matches the module. For a DUT without an external 32.768 K crystal, do not use a work order with an external crystal.
- There is a problem with the SRAM. You can check whether the Flash data is consistent with the test firmware through the Dump Flash.
- If it is a hardware encryption environment and the DUT has been encrypted, it is possible that the KEY INFO in the DUT does not match the key of the test firmware and cannot be decrypted successfully.

### 5. Test firmware download failed (0x37, 0x38), what could be the cause?

- Check whether the Dupont line from PLT-Lite to DUT UART is qualified. The line which is too thin is easy to be interfered.
- The fixture has interference, which can be checked through the flying line.
- If the plug-in Flash used is not suitable, it can be excluded by replacing the Flash of other brands.
- There is interference with the PCBA trace.

### 6. Crystal calibration exception (0x3A, 0x3B, 0x3C), what could be the cause?

- If most modules have this problem, it may be that the calibration port is not selected correctly or there is a problem with the calibration pin. The problem with the calibration pin may be that there is a capacitor on the jig or on the PCBA, which causes the PWM waveform to be inaccurate and the calibration to fail.
- If individual modules have this problem, it may be that the threshold card is too strict, the crystal oscillator error is too large, etc.

### 7. How to solve the time-consuming problem of port self-starting test?

- The self-start test is fool-proof, which will detect the port status for the second time, and the default time of this interval is 1.5s. If the user wants to speed up, the inspection interval can be shortened according to the field situation.


