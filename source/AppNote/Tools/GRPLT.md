## GRPLT Tool

> GRPLT is a configuration tool for in-line mass production boards (PLT).



### 1. GRPLT basic function introduction

- Support GR551x/GR5526/GR5525/GR553x.
- Supports crystal calibration, RSSI function test, application firmware burning, Flash resource burning, etc. for the device.
- Supports up to 1 tow 16 simultaneous burn-in.
- Support customized encryption information burning.
- Support secondary development, users can set the Bluetooth information and Flash resources in real time while burning.



### 2. GRPLT Application Notes

- GRPLT will record all the burning result information, but not including the device that can not be found. The default save directory is the LOG directory under the DLL path, users can modify this path through GRPLT, or modify the LogDir in the *cfg.ini* file (*cfg.ini* is automatically generated after GRPLT starts).
- In order to avoid the chip failure caused by plugging and unplugging with electricity, it is recommended to power off the UART when the PLT board is not tested.
- Application firmware burning and Flash resource burning should not be confused. Application firmware burning will update imageinfo to SCA area and write the set information to Boot.
- RSSI function test adopts scanning method to get RSSI value. GU turns on broadcasting, DUT scanning (GR533x does not support RSSI function test).
- Once the eFuse area is written, it is irreversible. Customized encryption information and I/O LDO configuration information need to be confirmed to be correct before writing.
- There is no guarantee that the Bluetooth address will not be duplicated without using secondary development. Interference such as Bluetooth address file replacement, computer hardware failure, etc. may cause Bluetooth address duplication.
- The pre-burn mode requires pre-burning the .bin file of the application firmware to the corresponding area and burning the imageinfo of the firmware to the SCA area, without imageinfo it will not pass the test.
- GRPLT will not fully erase the chip by default, only the area to be burned is erased.
- The PLT board's power-up/down operations are unified, and cannot be operated for individual DUTs.
- The RST_PLT button in the upper left corner of the PLT board is used to reset all serial ports. Pressing this button during the test will result in a test exception, which can be recovered by reopening the host computer program.
