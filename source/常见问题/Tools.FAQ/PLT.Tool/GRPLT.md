## FAQ for GRPLT


### 1. What is the principle of crystal calibration?
- The GU module starts the PWM at the beginning of the test and sends a specific square wave signal to the IO port corresponding to the DUT, and the DUT calibrates based on the square wave. Currently using a 40 Hz square wave to calculate the count in one cycle at a running rate of 64m, the expected count is:
  
$$
64M \times 1 \div 40 = 1.6M
$$

-   The corresponding card control threshold algorithm is:

$$
N = X \div 1.6
$$

-   Where N is the desired PPM and X is the count offset (i.e. ErrLimit in the job setup). The default card control threshold of the current work order is 60, and the PPM is 37.5. In principle, the offset value should not exceed 80 (i.e. 50 PPM). When the offset is large, Bluetooth is easily disconnected.

### 2. What is the RSSI test method?

- At the beginning of the test, the GU module will broadcast data as a Slave (the broadcast data value is a random value of 6 bytes to distinguish the broadcast signals of GUs at different stations), and the DUT will SCAN as a Master to obtain the RSSI value. (Neither the GR533x nor the GR5625 support RSSI, and there are no plans to support any future models.)

### 3. Where is the.bin file for the new version of the online tool (after V1.5.0.0.4)?

- The new work order generator will be saved in the memory when opening the.bin file. After saving the work order, all the contents will be saved in the work order, and the work order will be encrypted.

### 4. When do we need secondary development?

- Need to interface with MES or similar system
- Need to load custom dynamic Flash data
- Need to dynamically generate Bluetooth addr
- The SN code needs to be scanned and written to the machine
- Need to use a specific interface

### 5. How is custom encryption different from Goodix encryption?

- GOODIX encryption is hardware encryption, which uses the internal encryption module of the Goodix Bluetooth LE to encrypt the Flash and close the SWD. This operation is irreversible. The application firmware also needs to be encrypted to run, which is the automatic encryption of the hardware; Custom encryption is to encrypt some Flash data (such as NVDS data or Flash resource files) according to the information written by eFuse. If the customer wants to stop using encryption, it can be burned again.

### 6. Report 0x1A badness (test firmware operation failure), what is the possible reason?
- Check that the work order matches the module. For a DUT without an external 32.768 K crystal, do not use a work order with an external crystal.
- There is a problem with the SRAM. You can check whether the Flash data is consistent with the test firmware through the Dump Flash.
- If it is a hardware encryption environment and the DUT has been encrypted, it is possible that the KEY INFO in the DUT does not match the key of the test firmware and cannot be decrypted successfully.

### 7. The online tool reports 0xFC fault (test firmware download fails). What is the possible reason?
- Check whether the Dupont line from PLT to DUT UART is qualified. The line that is too thin is easy to be interfered.
- The fixture has interference, which can be checked through the flying line.
- If the plug-in Flash used is not suitable, it can be excluded by replacing the Flash of other brands.
- There is interference with the PCBA trace.
- The UART cable from PLT to DUT is too long. The current PLT can stably support a length of 1.5m. Communication beyond this length may be interfered.

### 8. 0x10 badness (abnormal crystal calibration) is reported. What is the possible reason?
- If most modules have this problem, it may be that the calibration port is not selected correctly or there is a problem with the calibration pin. The problem with the calibration pin may be that there is a capacitor on the jig or on the PCBA, which causes the PWM waveform to be inaccurate and the calibration to fail.
- If individual modules have this problem, it may be that the threshold card is too strict, the crystal oscillator error is too large, etc.


### 9. Report 0x 12 error (abnormal burning), what is the possible reason?
- 0x12 is the error code when the burning link is abnormal. See the attached error code for details.
- 0x15 or 0x16: This is a resource or firmware burning failure. Check the "LoadFW" column in the CSV Log file to see the specific reason for the failure. If it is "Error of Program Start", it is mostly caused by the transfer of external Flash download, and there is a problem with the configured port; if it is "Error of Program Data", this is an error in the process of burning Flash, which can be handled by referring to the problem of firmware download failure; If it is "Error of Program End", this is the final verification error, and contact the original factory personnel to check.
- There is no other error code attached: Check the "Fail Log" "in the CSV Log to see the specific error content. At present, most of them are" Product _ info Error "". This error indicates that there is a problem with the calibration value and Bluetooth address in eFuse. GRPLT's eFuse interface can be used to read the complete eFuse content for factory analysis.

### 10. After starting the GRPLT, when connecting the DUT, clicking "Start" does not respond. What is the possible reason?
- There is a problem with the design of the DUT, and the DC-DC circuit design does not meet the specifications, resulting in the DUT cannot start normally and cannot be identified.
- Fixture pin communication is poor, the DUT cannot return the command correctly, and it cannot be recognized.

### 11. After opening GRPLT, 16 small windows are not displayed. What may be the reason?
- PLT uses FTDI USB to serial port chip, and FTDI should be installed correctly before using PLT [驱动](http://www.ftdichip.cn/Drivers/VCP.htm). After the driver is downloaded, you can check whether it is recognized correctly through the port (COM and LPT) page of the Windows Device Manager. When the installation is successful, 17 or 18 com ports (USB Serial Port) will appear in the list. In case of installation failure, reinstall the driver if all of them cannot be identified; if some of them cannot be identified, right click the com port to manually update the driver.
