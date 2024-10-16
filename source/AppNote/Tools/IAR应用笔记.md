## IAR Application Notes



### 1. Basic Introduction

 - IAR Embedded Workbench (hereinafter referred to as IAR) is an integrated development environment (IDE) designed for embedded system development provided by IAR Systems, including compiler, debugger, optimizer and other tools, which can help developers to develop embedded software quickly and efficiently.

 - GR5xx series SDK supports building and debugging through IAR. Different chipset SDKs have different levels of support for different versions of IAR, see the table below for specific support:

Chip Series | SDK Version | Recommended IAR Version
--------|----------|-----------
GR551x | All versions | IAR 9.40.1 
GR5525 | All Versions | IAR 9.40.1 
GR5526 | All Versions | IAR 9.40.1 
GR533x | All Versions | IAR 9.40.1 



### 2. Using GR5xx SDK in IAR

The following is an example of using the **GR533x SDK** with **IAR Embedded Workbench 9.40.1**, based on the `projects\ble\ble_peripheral\ble_app_template_freertos` sample project in the SDK, which describes how to use the GR5xx SDK.

#### 2.1 Generating an IAR project based on a Keil project

The GR5525 SDK, GR5526 SDK and GR533x SDK all integrate IAR project files by default. For GR551x SDK with user's own project, you need to convert Keil project to IAR project by the script tool provided by SDK. Please refer to “[GR5xx IAR User's Manual](https://docs.goodix.com/zh/online/detail/gr5xx_iar_guide/V1.0/bba656ecb2c1491ee3372c1baa7c9e33)” for the specific conversion steps. “Generate IAR Project” section.

#### 2.2 Configuration Debugging and Downloading

1. Configure Flash Loader. locate the `arm/config/flashloader` folder under the IAR installation directory, and then create a new `Goodix` folder under the folder, as shown below:

  ![](../../_images/IAR/img-20240402163215.png ) 

2. Go to the `${SDK_Folder}/build/iar` folder (where SDK_Folder is the root directory of the SDK) and copy the _GR5xxx_IAR_16M.board_, _GR5xxx_IAR_16M.flash_, _GR5xxx_IAR_flashloader_, and _GR5xxx_IAR_16M.out_ in the folder. 16M.out_ files to the `Goodix` folder created earlier, as shown below:

![](../../_images/IAR/img-20240402164639.png)

> If you use GR551x SDK, the files you need to copy are _GR55xx_IAR_8M.board_, _GR55xx_IAR_8M.flash_, and _GR55xx_IAR_flashloader_8M.out_.

3. Go to the IAR project directory for the `ble_app_template_freertos` example and create a _gr5xxx.mac_ file in that project directory.

![Img](../../_images/IAR/img-20240402165530.png)

Write the following in the _gr5xxx.mac_ file and save it:

```c
execUserReset()
{
    #SP = __readMemory32(0x00000000, "Memory");
    #PC = __readMemory32(0x00000004, "Memory");
    __writeMemory32(0xE000ED08, 0x00000000, "Memory");
}
```

4. Use IAR to open the project in the `IAR` folder in the sample project directory as shown below:

![Img](../../_images/IAR/img-20240402162207.png)

5. Open the _ble_app_template_freertos.eww_ project file using IAR. Right mouse click on the build target in IAR and click `Options... ` to open the project settings window.

![Img](../../_images/IAR/img-20240402165126.png)

6. In the `Category` on the left side of the setup window, click to check the `Debugger` option, set `Driver` to `J-Link/J-Trace`, check `Use macro file(s)` and enter `$PROJ_DIR$\gr5xxx.mac` in the file selection box below, as shown below:

![Img](../../_images/IAR/img-20240402170418.png)

Switch to the `Download` tab, check `Use flash loader(s)`, check `Override default .board file`, and enter `$TOOLKIT_DIR$\config\flashloader\Goodix\GR5xxx_ in the file selection box below. IAR_16M.board`, as shown below:

![Img](../../_images/IAR/img-20240402170708.png)

> If you are using GR551x SDK, you need to replace _GR5xxx_IAR_16M.board_ with _GR55xx_IAR_8M.board_ in the above path.

7. Click `OK` to complete the setup. Wait for IAR to update the project and then you can compile, download and debug it. Click the `Download and Debug` button in the IAR toolbar, or use the shortcut key `Ctrl+D` to trigger compile, download and debug in one click:

![Img](../../_images/IAR/img-20240402171111.png)

8. After the compilation is complete, IAR will automatically download the firmware and start debugging. The first time that you use IAR for debugging download, there may be a popup window prompting `The first time that you debug a project in C-SPY, you must setup or review the memory configuration`. Click `OK` at this point and continue to click `OK` in the next window.

![Img](../../_images/IAR/img-20240402171815.png)

![Img](../../_images/IAR/img-20240402171826.png)

9. Wait for the IAR firmware to finish downloading and then start debugging. When you start debugging, there may be a popup window prompting `Warning: Stack pointer is setup to incorrect alignment. Stack addr = 0xf105'4605`, just click the `OK` button, and the correct stack pointer will be loaded in the setup _gr5xxx.mac_ file. Wait for the IAR to complete the initialization of the debug window and enter the debug mode correctly, then you can debug the application.

![Img](../../_images/IAR/img-20240402172140.png)
