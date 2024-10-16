## USB Introduction

### 1. Introduction to USB
GR5526 provides a Universal Serial Bus (USB) device controller compliant with the USB 2.0 full-speed specification. This USB device controller supports six endpoints and four data transfer modes: control transfer, bulk transfer, interrupt transfer, and isochronous transfer.

| Endpoint | Type                               | Main Parameters        |
| ---- | ---------------------------------- | ---------------------- |
| EP0  | Control endpoint with both input and output functions | 2 x 64 bytes FIFO      |
| EP1  | Output endpoint supporting interrupt and bulk transfers | 64 bytes FIFO          |
| EP2  | Input endpoint supporting interrupt and bulk transfers | 64 bytes FIFO          |
| EP3  | Input endpoint supporting interrupt and bulk transfers | 64 bytes FIFO    DMA √ |
| EP4  | Input endpoint supporting isochronous transfers | 1023 bytes FIFO  DMA √ |
| EP5  | Output endpoint supporting isochronous transfers | 1023 bytes FIFO  DMA √ |

### 2. Typical USB Applications
* Considering multi-chip and platform portability, as well as ease of use, the provided demos are built based on the TinyUSB open-source library;
 * No dynamic memory allocation is used;
 * Block all interrupt events and handle them in non-ISR task functions;
* The GR5526 adaptation, not included in TinyUSB, is publicly available. The adaptation file path in the GR5526 SDK is: `\external\TinyUSB\src\portable\goodix\gr552x\dcd_gr552x.c`;
* The demos provided by the GR5526 SDK all have a `tusb_config.h` file under the path `\Src\usbd_user`, which can configure MCU type, operating system type, and Class type, etc.;
* TinyUSB defines callback functions with the weak attribute. To avoid unexpected results during compilation and linking when using user-defined and weak callbacks, add the TU_ATTR_USED attribute to user-defined callback functions. For example, if "One ELF Section per Function" is checked in Keil, user-defined callbacks might be optimized out;
* TinyUSB uses some GNU features. When compiling in a non-GCC environment, ensure GNU support is enabled. For example, in Keil, add the --gnu configuration;
* Considering that existing computers and other devices are incompatible with USB 1.0 Host and at least support the USB 2.0 protocol, Speed Low is not yet adapted.