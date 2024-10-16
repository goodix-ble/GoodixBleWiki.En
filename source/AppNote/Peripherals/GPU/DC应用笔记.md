## DC Application Note
> Description:
- In graphical contexts, "DC" refers to the Display Controller module. Note that this is distinct from Direct Current (DC).
- "DC" is an extended peripheral of the GR5526 SoC series chips (available in GR5526VGBIP and GR5526RGNIP packaging). Other chip series do not include DC.



### 1. Introduction to Basic Functions

The Display Controller is mainly used in conjunction with the GPU to send the rendered frame buffer to the display for graphical output. Typical frame buffer formats include RGBA8888, RGB565, TSCx, etc. The main supported screen interface specification is MIPI DBI (Display Bus Interface) Type-C, covering the following timing protocols:
1.  3-Wire SPI
    Includes three signal lines: SPI_CS (chip select signal), SPI_SCLK (clock signal), and SPI_SD (data output). The command word consists of 9 bits, including a 1-bit data/command indicator and an 8-bit command word. The data word consists of a 1-bit data/command indicator and several bits of pixel data.
2.  4-Wire SPI (extended DCX signal line)
    Includes four signal lines: SPI_CS (chip select signal), SPI_SCLK (clock signal), SPI_SD (data output), and SPI_DC (data/command indicator signal). The command word consists of 8 bits, while the data word consists of several bits of pixel data.
3.  Dual SPI
    Includes four signal lines: SPI_CS (chip select signal), SPI_SCLK (clock signal), SPI_SD (data output), and SPI_SD1 (data output 1). The command word is generally sent via the SPI_SD line, while data is sent via both SPI_SD and SPI_SD1. The command word consists of 9 bits, including a 1-bit data/command indicator and an 8-bit command word. The data word consists of a 1-bit data/command indicator and several bits of pixel data.
4.  Quad SPI
    Includes six signal lines: SPI_CS (chip select signal), SPI_SCLK (clock signal), SPI_SD (data output), SPI_SD19 (data output 1), SPI_SD2 (data output 2), and SPI_SD3 (data output 3). The command type can be transmitted by SPI_SD or all SPI_SDx. The timing generally consists of an 8-bit command header, a 24-bit command word, and several bits of pixel data.
> - The display controller has a built-in DMA to accelerate frame data transfer and is capable of transferring a complete frame of data at once.
> - The display controller (DC) is often abbreviated as DC, please distinguish it from DC (Direct Current).
>



### 2. Application Notes

- The DC module and QSPI2 module share the main IO pins (CSn, CLK, D0 to D3). When the QSPI signal lines of the screen are connected to these I/O pins:
    - If the Frame Buffer is in RGB565 uncompressed format, users can choose either the QSPI2 or DC module to drive the screen.
    - If the Frame Buffer is in TSCx compressed format, users can only use the DC module to drive the screen.
    - In product engineering that utilizes a GPU, it is recommended that users prioritize the DC module to drive the peripheral screen for better compatibility and refresh rate bandwidth.
- The DC screen refresh interface app_graphics_dc_send_single_frame supports both synchronous and asynchronous call modes:
    - In synchronous call mode, the CPU waits for the Frame Buffer screen refresh logic to complete before continuing with subsequent operations.
    - In asynchronous call mode, the CPU exits the interface after initiating the Frame Buffer screen refresh transmission. Users must manage the interface call lifecycle through callback events to prevent reentrant calls and avoid operations such as entering sleep mode before the screen refresh is completed.
    - Synchronous call mode is generally used for debugging. Ultimately, it is recommended to use asynchronous call mode to allow parallel task execution, maximizing the chip's computational capabilities and improving the refresh frame rate.
- For sleep management of the DC module:
    - When the system allows sleep, ensure that the app_graphics_dc_send_single_frame call is complete, then call app_graphics_dc_set_power_state(GDC_POWER_STATE_SLEEP) to allow the system to put the DC module to sleep.
    - Before the system wakes up and prepares to refresh the screen, call app_graphics_dc_set_power_state(GDC_POWER_STATE_ACTIVE) to wake up the DC module and prepare it for operation.
- The main timing interfaces provided by the DC module are described with images in the "[GR5526 Display Refresh Guide](https://docs.goodix.com/zh/online/display_refresh_guide_bl_b)". Refer to this document if there are any doubts about using the interface.
- The DC module provides an adjustment for the CS Setup Delay (Tcsu, Chip Select Setup Time) electrical parameter. If the peripheral screen requires a larger Tcsu, it can be adjusted through the tcsu_cycle parameter in the initialization structure app_graphics_dc_params_t.
- The Frame Buffer used by the DC module during screen refresh should correspond to the Frame Buffer used by the GPU. The DC module has an in-flight frame format conversion function, which can convert the frame format of the GPU Frame Buffer to another format for sending to the screen. For example:
    - If the GPU uses the RGBA8888 format for frame rendering, the DC can set the target frame format to RGB565 for screen display.
    - If the GPU uses the TSCx format for frame rendering, the DC can set the target frame format to RGB565 for screen display.