## Ellisys User Guide

[TOC]

### 1. Important Note

Ellisys packet grabber is a valuable equipment, the value of a 15W~50W range, replacement and maintenance costs are high, and the repair needs to be sent back to the original Swiss factory for repair, which takes a long time. In order to avoid disputes, please remember to use the device in a standardized way to avoid power failure, falling and other abnormalities.



### 2. Preface

Ellisys Bluetooth Analyzer is a packet grabbing tool that needs to be used together with Ellisys Bluetooth Analyzer.

Classic Bluetooth packet capture requires packet capturing hardware support, the software is still consistent. As our main business is BLE, solid this document mainly to BLE packet capture as an example.

The latest version of the software download address https://www.ellisys.com/better_analysis/bta_latest.htm

The software will be updated synchronously according to the protocol update, so it is recommended to keep using the latest version as much as possible.

This document is only a brief explanation of how to start quickly and typical problems in the process of using the software. For comprehensive and detailed instructions, please refer to the official user guide document in the installation directory of the software: install_patch\Ellisys\Ellisys Bluetooth Analyzer\Documentation\Ellisys Bluetooth Analyzer User Manual.pdf



### 3. About the hardware

- The ellisys packet grabbers we use come in three main models, as shown below from left to right: Vanguard, Explorer, Tracker.

  ![抓包器型号](../../_images/elisys/MACHINE_MODEL.bmp)

- Both Vanguard and Explorer must be powered externally by a dedicated power adapter, and the USB cable is for data transfer only. Both packet grabbers can be used to grab Bluetooth dual-mode over-the-air packets.

- The Tracker can be powered using the USB connection cable, i.e. USB can be used for both data transfer and power supply. Laptop USB ports may also be underpowered, so you may need to plug the laptop into a power source or try a different computer.

- Bluetooth packet grabber data transmission volume is large, please try to use high-quality USB cable, to avoid insufficient power supply or packet grabbing abnormal interruptions.

- All packet grabbers need an external antenna, please make sure the antenna is functioning properly and has been screwed tightly.



### 4. Getting Started

#### 4.1 Main Interface

Open Ellisys Bluetooth Analyzer as below.

![抓包软件主界面](../../_images/elisys/MACHINE_UI.bmp)

1~5 Function Introduction:

1. software configuration:
   - File: Open the history capture file. You can also double-click the .btt file to open it directly.
   - View: open/close the small window of various functions of packet capture.
   - Record: capture a variety of parameter configuration. This entry is the most commonly used.
   - Help: open the user guide document, download the latest software version, view the current software version information.
2. window selection:
   - Welcome: the default interface.
   - Low Energy Overview: BLE packet capture is in this interface.
   - BR/EDR Overview: BT capture packets are in this interface. 3.
3. Historical Packet Files: Quickly open the recently opened packet files. 4.
4. Native packet capture file, which exists by default after the software is installed and is used to demonstrate the packet capture style. LowEnergyXXXX.btt is the BLE capture file. 5.
5. User Manual, which is the official user guide document. 6.
6. some other official documents.



#### 4.2 Quick Start

This section describes how to quickly start capturing packets sequentially.

1. Open Ellisys Bluetooth Analyzer software. 2.
2. Connect the packet grabber to the power supply, connect the USB to the packet grabber and the computer, and wait for half a minute for the device to initialize; the initialization of the Vanguard device may take 1-2 minutes. 3.
3. Click Record to start capturing packets, and the interface will automatically jump to the packet capturing display interface; for BLE devices, it will jump to Low Energy Overview, and for dual-mode devices, it will jump to BR/EDR Overview. 4. After a short initialization period, the device will be connected to the power supply of the packet capturing device.
4. After a short initialization, the device starts to capture packets. At this time, the Record button is grayed out, and the Stop and Restart buttons next to it become clickable.
5. The Low Energy Overview interface lists the captured empty port signals and parses them out automatically.
6. When the capture is finished, click Stop to stop the capture.
7. After stopping the capture, the captured data is still in the cache and is not saved. To save the data, you need to click the Save button or click Save in the popup box when you close the interface. 8.
8. If the data is not good, you can tap Restart to clear the current data and restart the packet capture. Please note that restart operation will not save any data. 9.
9. In the case of more Bluetooth data around, the packet capture data may accumulate very quickly. Capturing packets for a long time will not only take up a lot of system hard disk space, but also may not be easy to move because of the large size of the capture file. Therefore, if you need to capture packets for a long time, please make sure to set up the auto-save location and size of the captured packets, see Auto-save Configuration under Capture Management interface in the following section.

The above process involves several buttons as shown below:

![快速开始](../../_images/elisys/QUICK_START.bmp)

#### 4.3 Packet Catching Configuration

Usually, we can just quickly start and catch the desired air port packets. However, there are cases where we may need some simple configurations to make our packet capture more accurate.

These configurations usually can't take effect during the packet capture process, so please do the configuration operation before clicking Record.

The following figure opens the packet capture configuration interface:

![打开配置](../../_images/elisys/OpenConfig.bmp)

The following are common configuration operations:

1. Wireless interface:

   - Classic Bluetooth (BR/EDR) : Configured to catch classic Bluetooth air packets (hardware support required).
   - Bluetooth Low Energy : Configured to capture BLE packets. The following three options are usually all checked.
     - Bluetooth 5 Low Energy 2 Mbps : Support to capture 2 M PHY packets.
     - Bluetooth 5 Low Energy Coded (long range) : Support to capture Coded PHY packets.
     - Bluetooth 5 Low Energy Advertising Extension : Support to capture extended broadcast.
   - Bluetooth Radio: Adjust the antenna gain. The air port signal is not the higher the better, you need to adjust the gain value, so that the air port signal is at the right strength to achieve the best results.
     - RF Gain: Default is 0 dB, positive number is to increase the gain, used when the target signal is far away and the signal is weak. Negative number is to decrease the gain, which is used when the target distance is too close and the signal is too strong.

   ![Wireless界面](../../_images/elisys/Wireless_UI.bmp)

2. Wired interface:

   - Logic Transitions and inputs: There are some problems involving timing, you may need to pull the chip signal line, together with the air port packet to observe the timing and analyze the problem.
     - Add signal input (Alt+S) : Add a signal analysis line
     - Add bus input (Alt+B): Add a set of signal analyzing lines, multiple signal lines are used to represent multiple states or numbers.
     - Please refer to the official user's guide document, section “24. Flying Leads Probe - Explorer” and section “25. - Tracker and Vanguard”.

   ![Wired界面](../../_images/elisys/Wired_UI.bmp)

3. Capture Management interface: Automatically save relevant settings.

   - Capture storage: Capture automatically save the location and naming rules.
   - Automatic Segmentation: For long time packet capture, please make sure to set automatic segmentation to save the packet, so that only the segmented packet will be kept after the problem is found.

   ![Capture management](../../_images/elisys/Capture_management.bmp)

4. Save configurations and read configurations:

   - Save settings: You can save the current configuration locally by using the button at the bottom of the configuration screen.
   - Load Setting from file: Click to restore the saved configuration, which can be used when you need to configure fast recovery or reinstall the software.

#### 4.4 Only lip packet filtering

With the popularity of the current Bluetooth technology, we live and work, many devices with Bluetooth functionality, resulting in the capture of packets, we may capture many of our unwanted null packets, these packets will cause some interference in our analysis of the problem, affecting the efficiency of our analysis of the problem.

To deal with this situation, we can filter the empty port packets by simple configuration.

The following ways can be done at any moment before the capture starts, while the capture is in progress, and after the capture stops. Either of the two ways can be selected:

- Choose according to the device address:

  1. Click Filtering : Exclude Background--> configure on the upper right side of the packet capture interface to enter the device selection interface. 2.
  2. In the Device Database area, find your device address. You can enter the device address or name in the Search box to quickly search for it. 3.
  3. Double-click the target address to see it added to the Traffic Filtering Criteria. 4.
  4. If you add only one address, it will filter out the air packets sent from and to this address. If you add more than one address, only the packets sent from those addresses will be filtered.
  5. Click Apply to take effect, and then you can see that the broadcast air packets have been filtered in the Low Energy Overview window.
  6. The schematic is shown below.

  ![地址过滤](../../_images/elisys/ADDR_FILTER.bmp)

- To select filtering based on air packets

  1. Switch to the Null Packets screen.
  2. Select the empty packet you want to filter out and right-click to select it.
  3. Right-click to bring up a pop-up menu, the top three options are filter by protocol, and the next three options are filter by device. 4.
  4. In the following figure, select the ATT air packets during the connection of two devices, and click the right drop-down menu to select.

  ![空口选择过滤](../../_images/elisys/AIR_FILTER.bmp)



### 5. FAQ

1. 如何判断空口包的信号质量？如何提高抓包质量？

   - 点击需要查看的空口包，在右侧的Details窗口，Link-Layer Information中，可以看到Sniffer Radio-->RSSI。
   - RSSI在-30dBm~-70dBm应该是比较理想信号强度，这个强度下的空口包不容易出现误包和漏包。
   - Sniffer Radio-->RF Gain即为Record-->Wireless界面下，设置的Bluetooth Radio增益。
   - 根据RSSI空口强度，调节增益，来使抓包器达到最理想的工作信号强度。

2. 抓包时，只能抓一小段，抓包设备和软件都在正常运行，但是后面就没有包了，是怎么回事？

   - 可能是抓包软件没有配置抓2M PHY空口包，请参考 开始使用-->抓包配置章节中，Wireless界面配置。
   - 可能是连接过程中，Master设备出现异常，没有继续发包，导致连接异常。观察程序后续有没有连接超时之类的错误上报。
   - 可能是过滤策略导致，尝试将过滤策略取消，看看所有完全的空口包中有没有需要的包。

3. 只能抓到经典广播，无法抓到扩展广播，是怎么回事？

   - 请先更新抓包软件Ellisys Bluetooth Analyzer至最新版本。
   - 请参考 开始使用-->抓包配置章节中，Wireless界面配置，勾选Bluetooth 5 Low Energy Advertising Extension。

4. 程序运行起来了，可以在抓包器上看到广播包，但是通过手机工具无法扫描到设备，或是发现设备后连接成功概率很低，这是什么问题？

   - 可能是设备的RF信号太弱导致，请将抓包器放置与手机相同位置抓包，观察抓到空口包的RSSI是否处于理想信号强度。信号弱请尝试靠近设备或是检查天线，信号过强请远离设备。
   - 可能是设备时钟不准，导致的RF性能问题，尝试检查设备XO是否有校准。
   - 作为专业抓包器，抓包器RF性能远优于手机RF性能，信号弱或是信号质量差，抓包器大多数情况可以正常抓取。

5. 抓包器如何在抓空口包的同时，拉程序中的信号？

   - 找到抓包器Logic 或是 Logic Analyzer接口，连接信号号。另一侧连接设备对应IO口。
   - 参考抓包配置章节，Wired界面-->Logic Transitions and inputs相关说明

6. 为什么有的加密的空口包可以解密，有的加密的空口包无法解密？

   - 根据蓝牙协议，使用LE Legacy Pairing方式中的Just Works，并且在初次配对阶段，完整抓取了整个配对过程的数据包，抓包软件才能自动解密。
   - 其他解密包均是要在知道密钥的前提下，才能解密成功。
   - 选择加密空口包，在主界面章节中，Mesh点击View-->Mesh Security，其他空口包点击View-->Security，按照提示填入密钥即可解密。
   - 正确填写Key底色会变成绿色，空口密文包变成明文包。否则为红色，空口内容无变化。

7. 抓包软件运行起来非常卡是怎么回事？

   - 抓包软件Ellisys Bluetooth Analyzer更新很快，可能会出现中间版本有bug的情况，尝试更新版本后大概率能解决。
   - 更新方法：点击主界面 Help-->Download offline installer即可下载最新版本

8. 抓包软件长时间抓包后，非常卡，而且把我们的系统盘占满了，我应该怎么办？

   - 在未保存之前，抓包软件抓的包，均是通过缓存的方式，存在系统盘中。如果周围蓝牙设备较多，抓包软件可能短时间即抓起大量数据，导致大量占用系统盘空间。这时只要停止抓包，并关闭抓包软件，即可将缓存释放，系统盘空间就会被释放出来。
   - 这里请注意：直接关闭抓包软件，并不会自动保存当前的抓包。
   - 因此长时间抓包之前，为避免单个抓包数据过大，同时也为了避免内存使用过大而导致电脑卡顿，请务必提前设置自动保存抓包文件。
   - 具体设置方法，请参考开始使用-->抓包配置-->Capture Management界面章节内容

9. 如何通过空口包查看当前广播周期或是连接周期，以此来对照我们的代码配置符合预期？

   - 打开主界面，点击View-->Timing，打开时序界面。
   - 点击选择Low Energy Overview界面的空口数据包。
   - 在Timing界面，鼠标左键按住左右拉动，即可出现量时序的标识线。
   - 对齐到需要量取的区间即可。
   - 可以右键下拉菜单中，点击Keep，将目前的量测线保留下来，继续量测其他时间区间。
   - 如下示例图，点击选择Low Energy Overview界面的广播空口数据包1，量测出广播周期大约是378ms。点击选择Low Energy Overview界面的连接空口数据包2，量测出连接周期为是20ms。
   
   ![量时序](../../_images/elisys/MEASURE_TIMING.bmp)

10. 我想确定我的广播数据是否设置正确，或是想确定连接数据发出来没有，应该在哪里看发出来的空口数据？

    - 在主界面，点击View-->Data，打开Data界面，查看原始数据。
    
    - 选中Low Energy Overview界面想要查看的空口数据包，即可在Data界面看到原始数据。
    
    - 注：加密数据需解密成功后，通过明文数据才能与自己的实际发送的数据比对。揭秘之前默认显示为密文原始数据。
    
    - 广播与连接数据查看方式一致，以下图以查看连接数据为例：
    
      - ​	02 07为LL层包头；
    
      - ​	03 00为ATT数据长度；
    
      - ​	04 00为ATT数据信道；
    
      - ​	0A 0E 00为ATT数据；
    
      - ​	3E B5 B1为数据CRC校验位。
    
    ![RAW_Data](../../_images/elisys/RAW_Data.bmp)
