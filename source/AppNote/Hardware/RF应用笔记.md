## RF Application Notes



### 1. Introduction to GR5xx RF

* GR551x Series Chip RF Metrics

  * Bluetooth LE Connectivity: Bluetooth LE 5.1
  * Supported Data Rate: 1 Mbps, 2 Mbps, LR (500 kbps, 125 kbps)
  * Transmit power: -20 dBm ~ +7 dBm
  * 96 dBm receive sensitivity (in 1 Mbps mode)
  * -93 dBm receive sensitivity (in 2 Mbps mode)
  * -99 dBm receive sensitivity (in LR 500 kbps mode)
  * -102 dBm receive sensitivity (LR 125 kbps mode)
  * TX power consumption: 5.6 mA @ 0 dBm, 1 Mbps
  * RX power consumption: 4.8 mA @ 1 Mbps

* GR5526 Series Chip RF Metrics

  * Bluetooth LE Connectivity: Bluetooth LE 5.3
  * Supported data rate: 1 Mbps, 2 Mbps, LR (500 kbps, 125 kbps)
  * Transmit power: -20 dBm ~ +7 dBm
  * -98 dBm receive sensitivity (in 1 Mbps mode)
  * -94 dBm receive sensitivity (in 2 Mbps mode)
  * -101 dBm receive sensitivity (in LR 500 kbps mode)
  * -104 dBm receive sensitivity (LR 125 kbps mode) 
  * TX power consumption: 4.0 mA @ 0 dBm, 1 Mbps
  * RX power consumption: 3.5 mA @ 1 Mbps
  * AoA/AoD, LE synchronization channel

* GR5525 Series Chip RF Specifications

  * Bluetooth LE Connectivity: Bluetooth LE 5.3
  * Supported Data Rate: 1 Mbps, 2 Mbps, LR (500 kbps, 125 kbps)
  * Transmit power: -20 dBm ~ +7 dBm
  * -97 dBm receive sensitivity (in 1 Mbps mode)
  * -93 dBm receive sensitivity (in 2 Mbps mode)
  * -101 dBm receive sensitivity (in LR 500 kbps mode)
  * -103 dBm receive sensitivity (LR 125 kbps mode)
  * TX power consumption: 6.3 mA @ 0 dBm output power (64 MHz system clock)
  * RX power consumption: 5.3 mA @ 1 Mbps (64 MHz system clock)  

* GR533x Series Chip RF Metrics

  * Bluetooth LE Connectivity: Bluetooth LE 5.3

  * Supported Data Rate: 1 Mbps, 2 Mbps, LR (500 kbps, 125 kbps)

  * Transmit power:
    GR5330/GR5331: up to 6 dBm
    GR5332: up to 15 dBm

  * Receive sensitivity:

    GR5330/GR5331: -97.5 dBm @ 1 Mbps
    GR5332: -99 dBm @ 1 Mbps

  * GR5330/GR5331 power consumption @ 3.3 V VBAT input:
    TX power consumption: 3.8 mA @ 0 dBm output power (DC-DC supply, 16 MHz system clock)
    RX power consumption: 4.7 mA @ 1 Mbps (DC-DC powered, 16 MHz system clock)

  * GR5332 power consumption @ 3.3 V VBAT:
    TX power consumption: 5.9 mA @ 0 dBm output power (DC-DC supply, 16 MHz system clock)
    TX power consumption: 86.3 mA @ 15 dBm output power (SYS_LDO supply, 64 MHz system clock)
    RX power consumption: 4.9 mA @ 1 Mbps (DC-DC powered, 16 MHz system clock)



### 2. GR5xx RF Application Notes

- Different models of GR533x series support different PA types, GR5332 series support HPA (-10 dBm to +15 dBm) and SPA (-20 dBm to +5 dBm), GR5331/GR5330 series support SPA (-20 dBm to +6 dBm) and UPA (-15 dBm to +2 dBm).
- The GR5332 series can only use the SYSLDO power supply mode when operating with HPA.
- The GR5331/GR5330 can simplify the number of matching BOMs when using only the UPA mode.
- For details of RF PA introduction of GR533x, please refer to “[GR533x RF PA Application Guide](https://docs.goodix.com/zh/online/rf_pa_bl_d/V1.2)”.
- The RF port matching device layout should follow the PCB design requirements. Components in the matching network should be placed as close as possible to the RF pins (i.e., RF_RX vs. RF_TX), and the first component in the matching network should be placed no more than 1 mm away from the RF pins.
- RF alignments should be as short and straight as possible, and if structural constraints require a turn, the corner should be chamfered. Right angle or less than 90° angle alignment is prohibited.
- RF line is preferred to go to the surface layer, to avoid punching holes to change the layer, to avoid branching of the alignment, RF alignment must be guaranteed below the complete reference ground plane. RF alignment and chip Pin between the proposed gradient line, and RF line width as far as possible to design and match the device pad consistent, to avoid the components of the pad width and the width of the alignment is inconsistent with the disruption of the continuity of the 50 Ω transmission line characteristics of the impedance.
- DCDC ripple has a large impact on RF performance, unreasonable DCDC ground loop will affect RF performance indicators, it is recommended to follow the design guidelines to rationally design the layout of the DCDC peripheral devices, minimize the ground loop path, the DCDC ripple control at less than 16 mV.
- RF indicators need to calibrate the crystal before testing.
