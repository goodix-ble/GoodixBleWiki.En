## GR5526 (7)-Debugging rendering exceptions using savebin

[TOC]

### 1. Background

When using GUI frameworks such as LVGL to develop display applications, you may encounter the problem that the drawn UI or elements display abnormally on the screen. When troubleshooting exceptions, the analysis can be conducted in two stages:

- The first stage is the rendering stage: the GUI framework renders the UI elements and outputs them to the Frame Buffer.

- The second stage is the screen brushing stage, in which the screen brushing driver interface sends the data in the Frame Buffer to the screen.

By analyzing the content of Frame Buffer, it can be judged whether the exception occurs in the rendering stage or the screen brushing stage, and then further locate the cause of the problem.



### 2. Analyze Frame Buffer

#### 2.1 Get Frame Buffer Parameters

Before grabbing the Frame Buffer data, you need to get the following Frame Buffer parameters.

- Frame buffer start address: If double buffers are used, the addresses of both buffers are obtained. In general, you can print buffer space when the system starts to allocate it.


  ```c
  void lv_port_disp_init(void)
  {
      /*-------------------------
       * Initialize your display
       * -----------------------*/
      disp_init();
  
      /*-----------------------------
       * Create two fixed frame buffers for drawing and never release it
       *----------------------------*/
      static lv_disp_draw_buf_t draw_buf_dsc;
  
      lv_color_t* _draw_buf1 = app_graphics_mem_malloc(DISP_HOR_RES * DISP_VER_RES * DISP_PIXEL_DEPTH);
      lv_color_t* _draw_buf2 = app_graphics_mem_malloc(DISP_HOR_RES * DISP_VER_RES * DISP_PIXEL_DEPTH);
      ......
      // 可将 _draw_buf1 & _draw_buf2 的地址 printf出来
  }
      
  ```

  

- Frame Buffer Size: Determines the actual buffer size (length X width X pixel depth in bytes).



#### 2.2 Capture frame buffer data in debugging state

To reproduce the problem, you can choose to do the following when the target UI is ready to be refreshed after rendering:

- Write conditions on the program to let the program Halt before the screen is refreshed.
- Enter the debugging mode, and stop the breakpoint before the interface code that is ready to brush the screen after rendering.


```c
static void _disp_drv_flush(disp_drv_t * dev, void * buff, uint32_t buff_format, uint16_t w, uint16_t h) {
    graphics_hybrid_rm69330_flush(buff, buff_format, w, h); //lvgl 831 工程可在此增加断点暂停程序
}
```

After the program stops at the target position, connect the device through J-Link. After the connection is successful, use the `savebin` command to capture the frame buffer data. The reference example is as follows:


```c
//savebin <filename>, <addr>, <NumBytes> (hex)

J-Link>savebin D:/fb.rgba565 0x300A4A90 0x64A48
Opening binary file for writing... [D:/fb.rgba565]
Reading 412232 bytes from addr 0x300A4A90 into file...O.K.
```

The above example Dumps the framebuffer data with a starting address of 0x300A4A90 and a size of 0x64A48 (resolution of 454x454, format of RGB565, size of 454 X 454 X 2 bytes, and 0x64A48) into the file of the D disk *fb.rgba565*.

- Savebin calculates the Size and formats the file according to the format of the framebuffer:

|Common framebuffer format| 对应枚举值 | 缓冲区大小公式 | 文件后缀  |
| ---------------- | ---------- | -------------- | --------- |
| RGBA565          | 0x05       | W x H x 2      | \.rgba565 |
| RGBA8888         | 0x06       | W x H x 4      | .rgba8888 |
| TSC4             | 0x12       | W x H / 2      | .tsc4     |
|TSC6 or TSC6a| 0x13/0x14  | W x H x 6 / 32 | .tsc6     |

- The double buffer will switch the buffer every time the screen is refreshed. It can be determined according to the input parameters of the Fush interface. Do not Dump the error.



#### 2.3 Check buffer exception

1. Open the nema _ pixpresso software (located [GrLvglImageTool](https://developers.goodix.com/zh/bbs/blog_detail/2996e8f9f352491eb0ccca468f28f2ce)in the CmdTool directory of the software).

2. In the nema _ pixpresso, open the file that was Dumped using the savebin command in Section 2.2 (be careful to fill in the correct resolution when opening the file, otherwise an error will be displayed), as shown in the following figure:

![1714467382351](../../_images/savebin_gui_nema.png)

3. See if the rendered results are as expected.

- If the effect is not as expected, check the rendering stage.
- If the effect is in line with expectations, it can be judged that the problem occurs in the screen brushing stage.
- Another possibility is to accidentally modify the code that synchronizes rendering and screen brushing, causing the frame buffer to be brushed out before rendering is completed. To avoid this, synchronize the use of double buffering.















