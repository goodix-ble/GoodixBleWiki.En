
## GRPLT Lite Tool

>  GRPLT Lite is a configuration tool for offline mass production boards (PLT Lite).



### 1. GRPLT Lite basic function introduction

- Support GR5515/GR5526/GR5525/GR553x.
- Supports crystal calibration, RSSI function test, application firmware burn-in, Flash resource burn-in for devices.
- Supports parallel testing of 16 devices (cascading of multiple PLT Lite boards is required).
- Support port level detection startup test.
- Supports direct flash burning using QSPI protocol.



### 2. GRPLT Lite Application Notes

- GRPLT Lite will only record the result information of burn-in failure, which can be viewed by reading the Log through the configuration tool.
- In order to avoid the chip failure caused by power plugging and unplugging, it is recommended to power off the UART when the PLT Lite board is not under test.
- Application firmware burning and Flash resource burning should not be confused, application firmware burning will update imageinfo to SCA area and write the set information to Boot.
- RSSI function test adopts scanning method to get RSSI value, GU turns on broadcasting, DUT scanning (GR533x does not support RSSI function test).
- Once written, the eFuse area is irreversible. Customized encryption information and I/O LDO configuration need to be confirmed to be correct before writing.
- The pre-burn mode requires pre-burning the .bin file of the application firmware to the corresponding area and burning the imageinfo of the firmware to the SCA area, without imageinfo it will not pass the test.
- GRPLT Lite will not fully erase the chip by default, only the area to be burned will be erased.
- Since the GU has only two UARTs, the GRPLT Lite configuration tool will not print test information when multiple PLT Lite boards are cascaded for testing.
