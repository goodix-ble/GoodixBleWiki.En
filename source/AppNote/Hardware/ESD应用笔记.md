## ESD Application Notes



### 1. GR5xx Series Chip ESD Performance Introduction

* GR551x Series Chip Level ESD Performance: HBM (Human Body Model) = 2000 V, CDM (Charged Device Model) = 500 V. * GR5526 Series Chip Level ESD Performance: HBM (Human Body Model) = 2000 V, CDM (Charged Device Model) = 500 V.

- GR5526 Series Chip Level ESD Performance: HBM (Human Body Model) = 2000 V, CDM (Charged Device Model) = 500 V. * GR533x Series Chip Level ESD Performance: HBM (Human Body Model) = 2000 V, CDM (Charged Device Model) = 500 V.

* GR533x Series Chip Level ESD Performance: HBM @ All pins = 2000 V, CDM @ All pins (excluding the antenna pin) = 500 V. The ESD CDM of GR533x is rated at 400 V on the antenna pin.

- The ESD CDM of GR533x is rated at 400 V on the antenna pin. * GR5525 series chip-level ESD performance: HBM @ All pins = 2000 V, CDM @ All pins (excluding the antenna pin) = 500 V. The ESD CDM of GR5525 is rated at 400 V on the antenna pin.
  The ESD CDM of GR5525 is rated at 400 V on the antenna pin. * JEDEC document JEP157 states that 250-V CDM allows secure manufacturing with a standard ESD control process.

* System-level ESD (Electrostatic Discharge) is a measure of a product's entirety and is closely related to the design, manufacture, and use of electronic devices. In order to meet the system-level ESD requirements of the whole machine, when developing products using GR5xx series chips, engineers should follow the corresponding design rules in the schematic, PCB and product structure design, which can be found in the “System ESD Protection Design” chapter of “Hardware Design Guide” of the corresponding chip series.

### 2. ESD Application Notes for GR5xx Series Chipsets

* GR5xx series chips are recommended to be powered by a separate LDO/DCDC.
* GR5xx series chips are recommended to connect a magnetic bead at the power input connector of the product to attenuate the electrostatic energy and add a TVS tube at the front of the magnetic bead for ESD protection.

* GR5xx series chips suggest that for products with metal case, a magnetic bead should be connected between the metal case ground and the motherboard ground to avoid electrostatic interference directly into the motherboard.

* GR551x series chips, for watches, bracelets and other product scenarios, if the product system electrostatic indicators for air discharge ± 8 kV, contact discharge ± 4 kV or more, you need to additionally increase the external watchdog and other reset mechanisms to enhance the product system ESD protection capabilities.
  
* GR5525 series chips are recommended to connect a TVS tube (recommended: µClamp03301ZA) in parallel with the VBATL pin to improve the electrostatic discharge (ESD) capability of the system.

* For GR5xx series PCB Layout, please refer to the chapter “System ESD Protection Design” in the Hardware Design Guide of the corresponding chip series.

* GR5xx series chips GND design is particularly important, such as DCDC VSS_BUCK GND pin needs to be close to the input capacitor (10 µF) ground pin, to reduce the power supply / GND loop impedance to suppress ground noise.

* GR5xx series chips fight ESD PIN pin, such as exposed power charging port, communication interface, etc., can not be close to the clock, Reset, communication and other sensitive signals, and at the same time need to do the packet ground isolation processing.

* GR5xx series chips should follow the corresponding ESD precautions not only in chip design, but also in product structure design, as well as in production, transportation, and debugging phases. Refer to the chapter on “System ESD Protection Design” in the Hardware Design Guide of the corresponding chip series regarding structure and production.
