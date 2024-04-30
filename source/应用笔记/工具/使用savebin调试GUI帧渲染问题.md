## 使用savebin调试GUI帧渲染问题



### 1. 背景

使用Lvgl 等GUI框架开发显示类应用时, 有时会遇到绘制UI或元素在屏幕上显示异常. 这时候需要排查异常的原因, 从渲染到刷屏有两个独立阶段, 第一阶段是GUI框架将UI元素进行渲染, 输出到帧缓冲区FrameBuffer; 第二阶段是刷屏驱动接口将帧缓冲区的数据送显到屏幕.

这个时候, 我们可以通过分析FrameBuffer的内容, 来判断异常发生在渲染阶段还是刷屏阶段. 确认后再进一步定位问题原因. 



### 2. 分析FrameBuffer

#### 2.1 获取帧缓冲参数

在抓取Frame Buffer数据之前, 需要先获取 帧缓冲区主要参数:

- 帧缓冲区起始地址 - 如果用的双缓冲区, 则将两个缓冲区的地址都获取到, 一般可在系统启动分配缓冲区空间时将其打印出来

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

  

- 帧缓冲区大小 - 确定实际的缓冲区大小, 缓冲区的长x宽x像素深度, 单位字节



#### 2.2 调试状态下抓取帧缓冲区数据

确定问题出现的复现方法, 可以选择在目标UI渲染后准备刷屏时:

- 程序上写入条件让程序在刷屏前 halt住
- 进入调试模式, 在渲染完成后准备刷屏的接口代码前断点停住

```c
static void _disp_drv_flush(disp_drv_t * dev, void * buff, uint32_t buff_format, uint16_t w, uint16_t h) {
    graphics_hybrid_rm69330_flush(buff, buff_format, w, h); //lvgl 831 工程可在此增加断点暂停程序
}
```

​	待程序在目标位置停住后, 通过jlink 连接设备, 完成后, 使用 savebin 命令抓取帧缓冲区数据, 参考:

```c
//savebin <filename>, <addr>, <NumBytes> (hex)

J-Link>savebin D:/fb.rgba565 0x300A4A90 0x64A48
Opening binary file for writing... [D:/fb.rgba565]
Reading 412232 bytes from addr 0x300A4A90 into file...O.K.
```

示例为 将起始地址为 0x300A4A90、大小为 0x64A48 (分辨率454x454, 格式为RGB565, 大小为 454x454x2 字节, 合 0x64A48 ) 的帧缓冲区数据 dump 到D盘 fb.rgba565 文件. 

- 注意, savebin 计算size和设置文件格式 时候要注意 帧缓冲区的格式. 如下:

| 常用帧缓冲区格式 | 对应枚举值 | 缓冲区大小公式 | 文件后缀  |
| ---------------- | ---------- | -------------- | --------- |
| RGBA565          | 0x05       | W x H x 2      | \.rgba565 |
| RGBA8888         | 0x06       | W x H x 4      | .rgba8888 |
| TSC4             | 0x12       | W x H / 2      | .tsc4     |
| TSC6 或 TSC6a    | 0x13/0x14  | W x H x 6 / 32 | .tsc6     |

- 另外, 双缓冲区注意每次刷屏都会切换缓冲区, 可以根据 flush 的接口入参确定, 不要 dump错误



#### 2.3 检查缓冲区异常

- 打开 nema_pixpresso 软件,  位于GrLvglImageTool 软件的 CmdTool下.   [GrLvglImageTool下载](https://developers.goodix.com/zh/bbs/blog_detail/2996e8f9f352491eb0ccca468f28f2ce)

- 将 2.2 章节使用 savebin 命令, dump的文件, 使用 nema_pixpresso 打开, 示意如图 (打开时候注意填写正确的分辨率, 否则显示错误)

![1714467382351](../../_images/savebin_gui_nema.png)

通过上图, 查看渲染结果是否符合预期.



- 如果效果不符合预期, 则检查渲染侧.
- 如果效果符合预期, 则问题应该出在刷屏侧
- 另外注意还有一种可能, 就是不小心修改了渲染和刷屏同步的代码, 造成刷出去的帧缓冲区, 其实还没完成渲染. 这个地方, 注意双缓冲的使用同步即可.















