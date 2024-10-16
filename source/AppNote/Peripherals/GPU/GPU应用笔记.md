## GPU Application Notes
> Note: The GPU is an additional peripheral of the GR5526 SoC series chips: GR5526VGBIP and GR5526RGNIP packages. Other chip series do not include a GPU.



### 1. Introduction to Basic Functions

#### 1.1 Main Features of GPU
- Hardware components: Programmable shader engine, DMA-based command list to reduce CPU overhead, primitive rasterizer, texture mapping unit, blending unit
- Primitive drawing: Pixel/line drawing, filled rectangles, triangles (Gouraud Shaded), quadrilaterals
- Color formats: 32-bit RGBA8888/BGRA8888/ABGR8888, 24-bit RGB, 16-bit RGBA5551/RGB565, 8-bit A8/L8/RGB332, TSC™
- Compression schemes: TSC™4 (4 bits per pixel), TSC™6/TSC™6a (6 bits per pixel, with/without Alpha channel)
- Image transformations: Texture mapping, point sampling, bilinear filtering, bit blit, arbitrary angle rotation, mirroring, stretching (independent x-axis and y-axis), source and/or destination color keying, real-time format conversion, 2.5D perspective projection
- Text rendering support: Bitmap anti-aliasing A1/A2/A4/A8, font compression, Unicode (UTF8)
- Blending support: Fully programmable Alpha blending modes (source and destination), source/destination color keying
- Anti-aliasing: 8 x MSAA (Multi-Sampling Anti-Aliasing), edge anti-aliasing for quadrilaterals, edge anti-aliasing for triangles, anti-aliased thick lines, anti-aliased circles

#### 1.2 GPU Usage Key Points

##### 1.2.1 Frame Buffer
- The frame buffer is a memory buffer that contains data representing all the pixels in a complete video frame. On the GR5526, the frame buffer is typically placed in RAM. If the frame buffer is too large or there is more than one frame buffer, it can be placed in PSRAM. The read and write access rate of PSRAM is slower than RAM, but it has a larger capacity, which can provide sufficient capacity for frame and resource buffers.
- The frame buffer has an associated color format that applies to all entries in the buffer, with each entry referred to as a pixel. Each storage unit of the frame buffer corresponds to a pixel on the screen, and the entire frame buffer corresponds to one frame of the image.
In essence, the frame buffer is a storage space used to render and cache pixel data for drawing to the screen.

##### 1.2.2 Memory Allocation and Usage
The memory unit serves as the bridge for communication between various modules within the GPU and other modules. A typical GPU application involves three types of memory usage:
-   Command List Buffer: Used to store the command list for GPU execution and rendering. To ensure fast access, it is generally placed in the SRAM area.
-   Texture Cache: Persistently stored in Flash memory, it supports memory mapping for retrieval. It can also be loaded into the PSRAM area as needed during use.
-   Frame Buffer: The space for the frame buffer is generally the screen length x width x pixel depth. When using double buffering, this space requirement is doubled. It usually occupies a large space and can be placed in the SRAM/PSRAM area.

##### 1.2.3 Reference Recommendations
- We recommend that users prioritize developing graphical products based on the reference example projects provided by the GR5526 SDK. The example projects provide GPU integration for the LVGL GUI framework. Users do not need to concern themselves with the low-level driver adaptation and implementation of the GPU, and can focus solely on the application layer implementation of LVGL.
- For a more systematic understanding of GPU usage, refer to the "[GR5526 GPU Developer Guide](https://docs.goodix.com/zh/online/detail/gpu_guide_bl_b/V1.0/29bb32e1f0c19e8d6892784f5f2cbca4)".



### 2. Application Notes

- When developing graphical products using the GPU version of LVGL with the SDK, the recommended color depth parameters for optimal compatibility are as follows:
    - Set LVGL's COLOR_DEPTH to 32-bit.
    - LVGL uses a double buffering mechanism, with the frame buffer format being RGB565.
    - It is recommended to use RGB565 as the color format on the screen side.
- The GPU must work in conjunction with the Display Controller and PSRAM module. The graphical project requires a specific chip voltage strategy. During the main initialization phase, ensure to call the interface to initialize the voltage strategy.
    ```
    app_graphics_adjust_dcore_policy();
    ```
- Set the instruction buffer size to at least 10 KB. If you notice any random screen corruption during UI rendering, check if the buffer size is insufficient.
    ```
    #define HAL_GFX_RING_BUFFER_SIZE            (10*1024u)
    ```
- The GPU version of the LVGL framework supports the TSCx image compression format, which requires the image width to be a multiple of 4. If the screen buffer width is not a multiple of 4, consider rounding up the width to the nearest multiple of 4.
- When developing graphical products using the GPU version of LVGL, the project's image and font resources need to be generated using adapted tools, as referenced below:
    - [Generate image resources compliant with the GPU-adapted version of LVGL](https://developers.goodix.com/zh/bbs/blog_detail/2996e8f9f352491eb0ccca468f28f2ce)
    - [Generate font resources compliant with the GPU-adapted version of LVGL](https://developers.goodix.com/zh/bbs/blog_detail/6b29cdf5923247029f4357a65de1b065)