## GR5526(2)-生成Lvgl规范的图片资源

[TOC]

本文主要介绍使用 LvglImageTool 生成符合 GR5526 GPU 适配版Lvgl 规范的图片资源, 进行 GUI 图片资源的准备和开发.

### 1. 工具介绍

Lvgl 官方提供了一个图片转换工具
![在这里插入图片描述](https://img-blog.csdnimg.cn/08a4ccda4dfe4ba39854dc6f3dc6db7b.png) 

但由于不方便批量转换、不能同时支持多种格式转换、不能同时生成bin 和描述符文件等原因, 相对只适合用于Demo性环境, 不适合于生产性环境。 因此额外提供了一个小工具 GrLvglImageTool。
![在这里插入图片描述](https://img-blog.csdnimg.cn/441df0b97e1d4c5dbeae3ebd29455cd2.png) 


具备以下特点:

- 可以同时支持大量的图片转换
- 可以同时支持多种图片格式转换
- 配合GR5526 优化版Lvgl, 在原生Lvgl上扩展了压缩图片格式支持, 方便用户进一步节省资源存储空间
- 根据项目需要, 支持配置存储偏移地址
- 支持同时生成 用于烧写的bin文件和用于代码使用的图片描述符源码文件
- GR5526 用户可以使用这个工具, 进行图片资源和描述性源码的快速生成, 然后应用到Lvgl 项目。



### 2. 生成图片资源

用户通过如下步骤, 进行图片资源的生成

#### 2.1 准备图片资源数据
GR5526 优化版Lvgl, 为了渲染性能的优化处理，对图片有如下要求:

原始的图片资源, 请UI工程师, 根据项目的需要, 准备为 PNG或 JPG格式. 如果图片有 alpha 图层及透明混合的需要, 准备为PNG 格式
图片的输出格式, 典型有以下几种:
![在这里插入图片描述](https://img-blog.csdnimg.cn/728558dd6f494dd4be453f6fea0222e9.png)



输入图片的宽度和高度, 需要满足以下需求
为了突破资源方便管理, 请提前为图片素材准备好一套命名规范. 后面生成图片的源码描述文件时候, 会依赖图片名

#### 2.2 组织图片目录格式

图片资源准备好后, 再按照如下要求, 放置到不同的目录下

![在这里插入图片描述](https://img-blog.csdnimg.cn/711defae3e084bfb9bd92052e12247ff.png)


创建一个命名格式为 0x{ADDR}_{DirName} 的目录. 0x{ADDR} 表示bin 文件初始地址下载到 外部Flash 的偏移地址； {DirName} 表示目录名, 可以较随意的取名, 符合目录规范即可。 比如 0x4000_WatchDemo, 就表示资源是准备下载到 外部Flash 偏移 0x4000 开始的地址空间
在0x{ADDR}_{DirName} 目录下, 根据项目对输出图片格式的需要, 再创建 RGBA8888、RGB (用于放置RGB565格式)、TSC4、TSC6A 的目录名. 工具会根据目录名, 将目录下的图片生成对应格式的bin 资源.
将先前准备好的图片资源, 根据创建的目录, 依次放置好, 比如将包含alpha 信息的PNG格式图片放到 RGBA8888 目录下
示意:

#### 2.3 进行资源生成

对于工具, 只需要使用 图中勾选的 GdPath 行功能即可. 其他功能不需要关心或已弃用



点击 GdPath 行的 Browse 按钮, 将准备好的图片资源目录选中. 这里有一些原则需要遵守
目录路径不要过深, 最好不包含中文字符, 以免不同环境的兼容性问题
选中路径要在 0x{ADDR}_{DirName} 目录的父层, 且同目录不要存在其他干扰目录.
导入路径后, 软件会在左侧列出子目录和图片资源
![在这里插入图片描述](https://img-blog.csdnimg.cn/8db50c7e75f54ce18fd93d8c23672251.png)


点击Parse, 等待若干时间, 就会成功 生成 bin文件和资源描述源码文件(.c 和.h). 如图
![在这里插入图片描述](https://img-blog.csdnimg.cn/13472a5fcbe9432393eac299bda51eb3.png)

### 3. 生成资源文件的使用

#### 3.1 烧写 .bin 文件
这个操作很简单, 将上文生成的.bin 文件, 使用 Goodix 提供的资源烧写工具 Gprogrammer 烧写到外部Flash 相应的偏移地址即可. （0x0000 就是从0地址开始烧写）. Gprogrammer 工具可以从Goodix官网下载到, 其使用也有专门的文档进行介绍说明.

只需要注意这个实际烧写的Flash设备和偏移地址要和源码描述符文件对应上, 否则可能得不到预想的效果.

#### 3.2 根据项目实际情况调整 源码描述符文件

截图源码描述符文件部分代码如下:

lv_img_dsc_list.h

```c
 #ifndef
  __LV_IMG_DSC_LIST_H__ 
  #define
  __LV_IMG_DSC_LIST_H__
  #define  ADDR_OFFSET_0000  0x00
  #define  ADDR_BLACK_CLOCK_FACE  (ADDR_OFFSET_0000 + 0x04)
  #define  ADDR_BLACK_CLOCK_THUMBNAIL  (ADDR_OFFSET_0000 + 0x3F488)
  #define  ADDR_DAY_CALORIE  (ADDR_OFFSET_0000 + 0x55A54)
  …
  LV_IMG_DECLARE(wd_img_black_clock_face);
  LV_IMG_DECLARE(wd_img_black_clock_thumbnail);
  LV_IMG_DECLARE(wd_img_day_calorie);
  ….
  #endif  
```

lv_img_dsc_list.c

```c
#include
  "lvgl.h"
  #include
  "gr55xx_hal.h"
  #include
  "lv_img_dsc_list.h"
  const
  lv_img_dsc_t  wd_img_black_clock_face =
  {
      .header.always_zero = 0,
      .header.w = 360,
      .header.h = 360,
      .data_size = 259200, 
      .header.cf = LV_IMG_CF_GDX_RGB565,
      .data = (uint8_t*)(QSPI0_XIP_BASE + ADDR_BLACK_CLOCK_FACE),
      };
  …
  const
  lv_img_dsc_t  wd_img_APPLIST_06_SLEEP =
  {
      .header.always_zero = 0,
      .header.w = 72,
      .header.h = 72,
      .data_size = 20736, 
      .header.cf = LV_IMG_CF_TRUE_COLOR,
      .data = (uint8_t*)(QSPI0_XIP_BASE + ADDR_APPLIST_06_SLEEP),
      };
  …
  const
  lv_img_dsc_t  wd_img_APPLIST_00_MENU =
  {
      .header.always_zero = 0,
      .header.w = 72,
      .header.h = 72,
      .data_size = 2592, 
      .header.cf = LV_IMG_CF_GDX_TSC4,
      .data = (uint8_t*)(QSPI0_XIP_BASE + ADDR_APPLIST_00_MENU),
      };
  …
  const
  lv_img_dsc_t 
  wd_img_APPLIST_03_HEARTRATE = {
      .header.always_zero = 0,
      .header.w = 72,
      .header.h = 72,
      .data_size = 31104/8, 
      .header.cf = LV_IMG_CF_GDX_TSC6a,
      .data = (uint8_t*)(QSPI0_XIP_BASE + ADDR_APPLIST_03_HEARTRATE),
      };
```

- .h 文件进行了图片资源的声明和地址索引. 其中 ADDR_OFFSET_0000 就是 0x{ADDR} 定义的地址偏移
- .c 文件中, RGBA 8888 的格式 (.header.cf), 使用 LV_IMG_CF_TRUE_COLOR 或 LV_IMG_CF_GDX_RGBA8888都可以。其中, LV_IMG_CF_GDX_RGBA8888、LV_IMG_CF_GDX_RGB565等 LV_IMG_CF_GDX_* 是GR5526 扩展支持的格式
- 源码默认支持的 Flash 为外部QSPI0 所连接的Nor Flash (要求支持 XIP 寻址). 如果是内部Flash 或者 QSPI1或者QSPI2 连接的Flash, 就需要根据实际情况, 人工手动全局修改下 这个 宏 QSPI0_XIP_BASE.
1）QSPI0_XIP_BASE 表示 QSPI0 的 XIP 总线起始地址
2）QSPI1_XIP_BASE 表示 QSPI1 的 XIP 总线起始地址
3）QSPI2_XIP_BASE 表示 QSPI2 的 XIP 总线起始地址
4）如果是 使用 内部X-Flash, 则需要定义一个实际使用的起始地址宏.

#### 3.3 将源码.c/.h 文件嵌入Lvgl 工程

就可以进行图片资源的使用和索引了. 其用法和 Lvgl 官方的用法一致.

```c
lv_obj_t* img1 =  lv_img_create(obj);
lv_img_set_src(img1,  &wd_img_digital2_heart_small);
lv_obj_set_pos(img1,  160, 270);
```



#### 3.4 相关工具下载地址

- LvglImageTool 工具: [LvglImageTool](https://developers.goodix.com/zh/bbs/download/comment/47ff0c4dfed64681bb65551bd2d7b3c2/upload_2516870ad68f2c74c94e48a5ea94cff9)
- Gprogrammer 工具下载地址: [GProgrammer](https://www.goodix.com/zh/software_tool/gprogrammer_ble)
- GR5526 SDK 下载地址:  [GR5526_SDK]([GR5526 SDK丨软件资源丨汇顶科技 (goodix.com)](https://www.goodix.com/zh/software_tool/gr5526_sdk))

