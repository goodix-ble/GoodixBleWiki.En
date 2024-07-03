## GR5526(4)-将Lvgl字体位图合并为bin

[TOC]

### 1. 使用背景及说明

- 在 Goodix GR5526使用的Lvgl 工程中,为加速字体的渲染速度, 将Lvgl 原生的Font渲染层适配到GR5526 的图形处理器GPU上, 适配后的位图格式(glyph_bitmap) 与Lvgl原生的位图格式存在差异, 因此不再支持使用 Lvgl 官网提供的 lv_font_conv.exe 软件生成的字体数据. 我们基于 lv_font_conv.exe 工具进行了对应的适配修改, 推出了适用于 GR5526 Lvgl 字体渲染的工具 gdx_font_conv.exe.

- 工具能输出两种可供Lvgl 字体渲染器支持的格式:

  - **bin 格式 **: 将位图数据、字体描述信息等所有信息整体打包正一个bin文件, 在这种格式下, cpu/gpu 等主控单元不能对位图进行直接寻址访问, 需要实现bin 的加载器, 将字体的位图数据及描述信息全部加载到RAM区域再进行访问. 由于下述两个原因, 目前在GR5526 中不支持 bin格式访问
    - Lvgl 源码bin加载器是从 v9.0 版本后才开始支持的, 我们目前适配的最新版本为 v8.31, 不支持bin 加载器
    - bin 加载器将整个bin 的位图数据和描述信息加载到RAM空间, 这会极大的浪费 RAM空间, 对GR5526来说是难于接受的.
  - **Lvgl 格式** : 会生成一个 .c 的源码文件, 在源码文件中定义了位图数组 glyph_bitmap 和其他的字体描述信息, 需要将整个.c 源文件放在工程中进行编译, 这样所有的字体数据就放置在了代码空间. 目前 GR5526 SDK参考工程使用的是这样的方式, 但这个方式存在一个缺点, 当字体文件越来越大时, 会很快耗尽 GR5526 的源码存储空间. 

  

- 本文就是基于上述Lvgl格式进行优化, 将 Lvgl 格式中占据空间最大的 位图数据(glyph_bitmap) 放置到外部Flash空间, 将字体其他描述信息还是放置到 源码空间.

  

### 2. Lvgl格式位图数据转换为bin文件

#### 2.1 生成适用于Lvgl字体的方式

在GR5526 Lvgl的产品环境中, 字体文件的生成和使用需要经过以下步骤:

1. 使用 gdx_font_conv.exe 工具, 将ttf等格式的字体源文件生成多个不同字体不同字号的lvgl 格式的.c 源文件

2. 将多个字体源文件中的glyph_bitmap 数组, 手工导出为 .txt 数组文件群

3. 使用提供的 goodix_lvgl_font_to_bin.py 脚本文件, 将 .txt 位图文件群, 按规则合并为一个 goodix_lvgl_font.bin文件, 同时输出各个字体位图在bin的基础信息, 包括对齐调整后的长度、偏移等

4. 确定goodix_lvgl_font.bin 文件在外部Nor Flash的烧写偏移地址, 用下述公式确定每个字体位图在总线地址空间的偏移地址:

   ```c
   glyph_bitmap_AHB_ADDR = QSPIx_XIP_BASE + Flash_Offset + glyph_bitmap_offset
   ```

   - QSPIx_XIP_BASE 是Flash 挂载模块的逻辑基地址, 如果挂载在QSPI0模块, 则为QSPI0_XIP_BASE, 以此类推

   - Flash_Offset 是将goodix_lvgl_font.bin 烧写到 Nor Flash 的空间偏移, 比如从0地址开始烧写, 则 为 0x00000000

   - glyph_bitmap_offset 是当前字体位图文件的glyph_bitmap 数据在 bin文件中的偏移。举例：

     ```c
     goodix_lvgl_font_to_bin.py 脚本输出信息:
     
     OrderedDict([('file', '.\\raw\\lv_font_montserrat_48_gdx.txt'),
                  ('align_len', 37376),
                  ('offset', 0),
                  ('offset_hex', '0x0')])
     OrderedDict([('file', '.\\raw\\lv_font_msyh_20_gr552x.txt'),
                  ('align_len', 19200),
                  ('offset', 37376),
                  ('offset_hex', '0x9200')])
     OrderedDict([('file', '.\\raw\\lv_font_msyh_26_gr552x.txt'),
                  ('align_len', 25856),
                  ('offset', 56576),
                  ('offset_hex', '0xdd00')])
        
     offset(十进制)或offset_hex(十六进制)的值, 即为glyph_bitmap_offset的值
     ```

   5. 将生成的 goodix_lvgl_font.bin 文件烧写到外部的Nor Flash, 注意在Flash空间的偏移地址和上述提到的Flash_Offset 对应
   6. 将计算得到的各个字体文件的 glyph_bitmap_AHB_ADDR 地址重新赋值给 lv_font_fmt_txt_dsc_t 的成员变量glyph_bitmap, 并移除原来的glyph_bitmap数组即可. 
   7. 完成上述步骤, glyph_bitmap 就索引到Nor Flash 的地址空间



本文适用于 Goodix 蓝牙SoC GR5526的Lvgl 工程, 用于将Lvgl 字体的位图数组



#### 2.2 生成符合GPU适配版Lvgl规范的字体资源

**2.1 章节** 第1步生成Lvgl 格式字体资源的方法, 请参考专门的文章. 如下:

- [GR5526 GUI专题(2) - 生成符合GPU适配版Lvgl规范的字体资源 | 技术文章 | 汇顶科技开发者社区 (goodix.com)](https://developers.goodix.com/zh/bbs/blog_detail/6b29cdf5923247029f4357a65de1b065)

**2.1 章节** 第5步烧写bin文件到Nor Flash的方法, 请使用GProgrammer 工具和参考相关的使用说明

**2.1 章节** 第2~4步请参考下述  **2.3 生成字体位图bin文件的方法** 章节 



#### 2.3 生成字体位图bin文件的方法

- 获取 **GoodixLvglFontToBin** 脚本压缩包, 在压缩包中有一个 goodix_lvgl_font_to_bin.py 脚本和 raw 目录

- raw 目录用于存放各字体源文件的 glyph_bitmap 位图数据, 一般操作建议如下:

  - 删除raw 目录下的测试文件 (用于演示目的, 可以备份下)

  - 在 raw目录下命名一个跟 .c 字体源文件同名的 .txt文件, 如字体源文件 lv_font_msyh_26_gr552x.c 对应的位图数据文件命名为  lv_font_msyh_26_gr552x.txt

  - 将 .c 源文件中 static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[] 数组内容拷贝到对应的txt文件, 如下(拷贝 {}中的内容, 不包含{}) :

    ```c
        /* U+0020 " " */
    
        /* U+0021 "!" */
        0xe, 0xf1, 0xe, 0xf1, 0xd, 0xf0, 0xd, 0xf0,
        0xd, 0xf0, 0xc, 0xf0, 0xc, 0xf0, 0xc, 0xf0,
        0xb, 0xe0, 0xb, 0xe0, 0x8, 0xa0, 0x0, 0x0,
        0x3, 0x50, 0x1f, 0xf4, 0xc, 0xe2, 0x0, 0x0,
    
        。。。。。。。。。
    
        /* U+989D "额" */
        0x0, 0x0, 0x51, 0x0, 0x0, 0x0, 0x0, 0x0,
        0x0, 0x0, 0x0, 0x0, 0xe9, 0x0, 0x0, 0x45,
        0x55, 0x55, 0x55, 0x52, 0x3, 0x33, 0x9f, 0x33,
        0x32, 0xef, 0xff, 0xff, 0xff, 0xf6, 0x3f, 0xff,
        0xff, 0xff, 0xfb, 0x0, 0x5, 0xf2, 0x0, 0x0,
        0x3f, 0x16, 0x20, 0x0, 0xcb, 0x0, 0x8, 0xe0,
        0x0, 0x0, 0x18, 0x4f, 0x63, 0x33, 0x85, 0x48,
        0x8d, 0xe8, 0x88, 0x60, 0x0, 0xbf, 0xff, 0xff,
        0xa0, 0x8f, 0xaa, 0xaa, 0xad, 0xc0, 0x6, 0xf2,
        0x0, 0x3f, 0x50, 0x8d, 0x0, 0x10, 0x9, 0xc0,
        0x3f, 0x7a, 0x41, 0xdb, 0x0, 0x8d, 0x1, 0xf5,
        0x9, 0xc0, 0x3a, 0x1a, 0xfe, 0xe1, 0x0, 0x8d,
        0x0, 0xf5, 0x9, 0xc0, 0x0, 0x4, 0xef, 0xfb,
        0x30, 0x8d, 0x1, 0xf4, 0x9, 0xc0, 0x3, 0xaf,
        0xa0, 0x5d, 0xf9, 0x8d, 0x1, 0xf4, 0x9, 0xc0,
        0x8f, 0xe6, 0x22, 0x22, 0x73, 0x8d, 0x3, 0xf3,
        0x9, 0xc0, 0x23, 0xff, 0xff, 0xff, 0x60, 0x8d,
        0x5, 0xf1, 0x9, 0xc0, 0x0, 0xf5, 0x11, 0x1e,
        0x60, 0x8d, 0x9, 0xf0, 0x9, 0xc0, 0x0, 0xf4,
        0x0, 0xe, 0x60, 0x12, 0x2f, 0xfc, 0x21, 0x10,
        0x0, 0xf4, 0x0, 0xe, 0x60, 0x1, 0xdf, 0x5d,
        0xf5, 0x0, 0x0, 0xff, 0xff, 0xff, 0x60, 0x5e,
        0xf4, 0x0, 0xaf, 0x90, 0x0, 0xf7, 0x44, 0x4e,
        0x6c, 0xfc, 0x20, 0x0, 0x7, 0xf8, 0x0, 0x20,
        0x0, 0x0, 0x5, 0x50, 0x0, 0x0, 0x0, 0x40,
    
        /* U+FF0C "，" */
        0x2, 0x30, 0xf, 0xc0, 0x2f, 0x70, 0x6f, 0x20,
        0xad, 0x0, 0xd8, 0x0
    ```

  - 按照上述步骤, 完成所有 .c 源文件 位图数据文件的创建

  - 提前安装好Python 环境, 命令行进入到 GoodixLvglFontToBin 目录下. 执行脚本命令 **python goodix_lvgl_font_to_bin.py** :

    ```
    D:\03_Software\LvglFont\GoodixLvglFontToBin>python goodix_lvgl_font_to_bin.py
    
    Handle Font File : .\raw\lv_font_montserrat_48_gdx.txt
    Handle Font File : .\raw\lv_font_msyh_20_gr552x.txt
    Handle Font File : .\raw\lv_font_msyh_26_gr552x.txt
    
    OrderedDict([('file', '.\\raw\\lv_font_montserrat_48_gdx.txt'),
                 ('align_len', 37376),
                 ('offset', 0),
                 ('offset_hex', '0x0')])
    OrderedDict([('file', '.\\raw\\lv_font_msyh_20_gr552x.txt'),
                 ('align_len', 19200),
                 ('offset', 37376),
                 ('offset_hex', '0x9200')])
    OrderedDict([('file', '.\\raw\\lv_font_msyh_26_gr552x.txt'),
                 ('align_len', 25856),
                 ('offset', 56576),
                 ('offset_hex', '0xdd00')])
    
    Bin File length:82432 bytes, (hex:0x14200)
    
    Genqerate Lvgl Binary-Font File Successful!
    ```

  - 脚本执行完毕后, 会生成一个 goodix_lvgl_font.bin 文件, 并输出文件的合并信息.

    - file - 位图源文件名
    - align_len - 源字体数组进行对齐后的长度, 默认按照 Flash Page(256字节) 进行对齐. 
    - offset 和 offset_hex 分别是十进制/十六进制格式表示的当前位图在 bin文件中的偏移起始地址, 对应前文 **2.1 章节** 的glyph_bitmap_offset 变量
    - 最后输出 bin 文件的总大小

- 将上述生成的bin 烧写到外部 Nor Flash 空间

- 更新 static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[]  变量定义:

  - 删除 glyph_bitmap[] 数组

  - 重新定义glyph_bitmap:

    ```c
    const uint8_t * glyph_bitmap = (const uint8_t * ) (QSPIx_XIP_BASE + Flash_Offset + glyph_bitmap_offset)
    ```

    - 如Nor Flash 挂载到 QSPI0, flash 烧写偏移为 0x10000, 位图数据偏移为举例 lv_font_msyh_26_gr552x.txt 的 0xdd00. 则:

      ```c
      const uint8_t * glyph_bitmap = (const uint8_t * ) (QSPI0_XIP_BASE + 0x10000 + 0xdd00)
      ```

  - 各个字体文件 glyph_bitmap 变量更新雷同