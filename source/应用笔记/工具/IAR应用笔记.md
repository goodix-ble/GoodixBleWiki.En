## IAR应用笔记

### 1. 基本介绍

 - IAR Embedded Workbench（下文简称IAR）是IAR Systems提供的一款专为嵌入式系统开发设计的集成开发环境，包括编译器、调试器和优化器等工具，帮助开发人员快速高效地开发嵌入式软件。

 - GR5xxx系列SDK支持通过IAR进行构建与调试。但不同芯片的SDK对IAR不同版本的支持程度不一样，具体支持情况见下表：

芯片型号 | SDK版本号 | 推荐IAR版本
--------|----------|-----------
GR551x  | 全部版本 | IAR 8.42.1
GR5525  | 全部版本 | IAR 8.42.1
GR5526  | 全部版本 | IAR 8.42.1
GR533x  | 全部版本 | IAR 9.40.1

### 2. 在IAR中使用GR5xxx SDK

下面将以**GR533x SDK**与**IAR Embedded Workbench 9.40.1**为例，借助SDK中的`projects\ble\ble_peripheral\ble_app_template_freertos`示例工程来介绍如何在IAR中使用GR5xxx SDK。

#### 2.1 基于Keil工程生成IAR工程

GR5525 SDK，GR5526 SDK与GR533x SDK在发布时都已经默认集成了IAR工程文件，对于GR551x SDK与用户自己的工程，则需要通过SDK提供的脚本工具将Keil工程转换为IAR工程。具体的转换步骤请参考[GR5xx IAR用户手册 - 生成IAR工程](https://docs.goodix.com/zh/online/detail/gr5xx_iar_guide/V1.0/bba656ecb2c1491ee3372c1baa7c9e33)。

#### 2.2 配置调试与下载

首先来配置Flash Loader。在IAR安装目录下找到`arm/config/flashloader`文件夹，在里面创建一个`Goodix`文件夹，如图所示：

![](../../_images/IAR/img-20240402163215.png) 

在SDK中找到`${SDK_Folder}/build/iar`文件夹，将文件夹中的`GR5xxx_IAR_16M.board`, `GR5xxx_IAR_16M.flash`, `GR5xxx_IAR_flashloader_16M.out`三个文件拷贝到刚才创建的`Goodix`文件夹中。如图所示：

![](../../_images/IAR/img-20240402164639.png)

> 如果使用的是GR551x SDK，则需要拷贝的文件为`GR55xx_IAR_8M.board`, `GR55xx_IAR_8M.flash`, `GR55xx_IAR_flashloader_8M.out`。

在SDK下找到演示用的`ble_app_template_freertos`IAR工程，并在工程目录下创建一个`gr5xxx.mac`文件：

![Img](../../_images/IAR/img-20240402165530.png)

在`gr5xxx.mac`文件中写入如下内容并保存：

```c
execUserReset()
{
    #SP = __readMemory32(0x00000000, "Memory");
    #PC = __readMemory32(0x00000004, "Memory");
    __writeMemory32(0xE000ED08, 0x00000000, "Memory");
}
```

使用IAR打开示例工程目录下`IAR`文件夹中的工程，如图所示：

![Img](../../_images/IAR/img-20240402162207.png)

使用IAR打开`ble_app_template_freertos.eww`工程文件。在IAR中右键单击构建目标，点击`Options...`打开工程设置窗口：

![Img](../../_images/IAR/img-20240402165126.png)

在设置窗口中，在左侧`Category`中找到并单击`Debugger`选项，将`Driver`设置为`J-Link/J-Trace`，勾选`Use macro file(s)`，并在下面的文件选择框中填入`$PROJ_DIR$\gr5xxx.mac`。如图所示：

![Img](../../_images/IAR/img-20240402170418.png)

切换到`Download`选项卡，勾选`Use flash loader(s)`, 勾选`Override default .board file`, 并在下面的文件选择框中填入`$TOOLKIT_DIR$\config\flashloader\Goodix\GR5xxx_IAR_16M.board`。如图所示：

![Img](../../_images/IAR/img-20240402170708.png)

> 如果使用的是GR551x SDK，则需要将上述路径中的`GR5xxx_IAR_16M.board`替换成`GR55xx_IAR_8M.board`。

点击`OK`完成设置。等待IAR更新工程后即可进行编译，下载与调试。在IAR工具栏中找到并点击`Download and Debug`按钮，或使用快捷键`Ctrl+D`来一键触发编译下载和调试：

![Img](../../_images/IAR/img-20240402171111.png)

编译完成后，IAR会自动下载固件并开始调试。第一次使用IAR进行调试下载可能会弹窗提示`The first time that you debug a project in C-SPY, you must setup or review the memory configuration`，此时点击`OK`，并在接下来的窗口继续点击`OK`即可：

![Img](../../_images/IAR/img-20240402171815.png)

![Img](../../_images/IAR/img-20240402171826.png)

等待IAR完成固件下载并开始调试。在开始调试时，可能会弹窗提示`Warning: Stack pointer is setup to incorrect alignment. Stack addr = 0xf105'4605`，此时直接点击OK即可，正确的栈指针会在设置的`gr5xxx.mac`文件中加载。等待IAR完成调试窗口初始化后，可以看到此时已经正确进入了调试模式，可以对应用程序进行调试了：

![Img](../../_images/IAR/img-20240402172140.png)
