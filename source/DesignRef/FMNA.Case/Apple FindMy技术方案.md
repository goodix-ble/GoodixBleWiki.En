## Apple Find My Technical Solution #




- The technical scheme is applicable to a full series of chips GR5xxx of Goodix Bluetooth.
- For more details about Apple Find My, please refer to the official website [Apple Find My](https://www.goodix.com/zh/product/connectivity/ble/apple_find_my)page.
- The technical details are only open to MFi members. If you need to obtain the SDK development materials of Huiding Technology supporting Apple Find My Network technology, please provide basic information such as company name and MFi number, and [获得支撑](https://developers.goodix.com/zh/bbs/support)obtain relevant resources and technical support through the official website "".



### 1. Introduction to Apple FMNA

1. Basic overview of FMNA
    - FMNA program: Apple official Spec called `Apple Find My Network Accessory`, Chinese is Apple " `查找我的` " network accessories, can also be called `苹果Find-My`.
    - It was launched by Apple and consists of billions of Apple devices around the world `众包网络`.
    - Each Apple device acts as a base station, `蓝牙无线技术` detecting nearby missing items and reporting their approximate location to the owner.
    - The entire process is end-to-end `加密和匿名`, designed to protect users' privacy and security, and the lookup function is efficient, with no need to worry about battery life or traffic consumption.
2. FMNA Advantage
    - Improve the ecology
        - Huge global search network: Billions of Apple devices around the world can provide location services for lost items, and the more devices, the higher the location accuracy of the search network.
        - The search app is embedded in the Apple ecosystem: "Search" app is officially pre-installed in the Apple system. It is a function of the IOS system. It opens the relevant permissions by default and does not need to be maintained by the brand.
        - Add multiple devices: The same `Apple ID` accessories are interoperable, and each account can bind up to 16 accessories.
    - Intelligent search
        - Proximity search: Bluetooth LE allows the accessory to play sound search directly within the proximity connection range.
        - Long-distance search: Search for "nearby devices" in the network to track the Bluetooth signal of the accessory. If it is detected, encrypt the location and upload it to Apple's server. The owner can locate the location of the lost item in real time in the "search" application.
        - Lost contact: Take the initiative to open the "lost mode" of accessories, so that the person who finds it knows the owner's information.
    - Open adaptation
        - Support for third-party accessory access (MFi): In early April 2021, Apple officially announced that the search network accessory function is open source and available to third-party accessory developers who intend to connect their products to Apple's "search" network, and this plan belongs to the MFi plan.
3. FMNA Product Category
    - Independent anti-loss accessories
    - Clothing
    - Personal effects
    - Travel gear
    - Sports equipment
    - Electronic equipment
    - Medical equipment
4. Introduction to FMNA Application Scenario
    - For the application scenario of Apple Find My, please watch (15:25 time point) in "Training and Activities" [Demo Video](https://www.goodix.com/zh/product/connectivity/ble/apple_find_my) on the official website page.

### 2. Overall process of FMNA project of third-party brand manufacturer
1. Mass production process of third-party brand manufacturers (products and hardware)
    - Formal project establishment and FMNA product definition confirmation.
    - Hardware schematic design.
    - Punching board test.
    - Confirm the production line process and conduct small-scale hardware trial production.
    - The hardware is ready to confirm the version number of the sample.
2. Mass production process of third-party brand manufacturer (software)
    - Get Goodix Find-My SDK development materials.
    - Peripheral and sensor adaptation, custom dual slave application development.
    - Find My software function adaptation.
    - Product testing process.
    - The software is ready to confirm the version number of the sample apple.
    - Prepare the Apple Certified Test Report (FMCA) and complete the Pre-Sample Procedure form.
    - Submit materials such as Apple Test Lab Self-Test Report, FCC Test Report, QDIO and Product Specification.
3. Apple MFi process
    - Without MFi qualification, it is necessary to certify the MFi member account of the enterprise.
    - Apply to find PPID of network accessories after having MFi qualification.
    - Set up a server to pull Tokens from Apple in batches.
    - Send samples to a third party lab for network accessory compliance certification.
    - Product packaging and marketing communication certification.
4. Regulatory Certification Process
    - BQB test, column name QDID.
    - FCC certification.
    - Mass production.

### 3. Apple Search Network Features and Principles
1. Find My Network Accessories FMNA Spec
    -  **F**ind y etwork ccessory Specification **M****N****A**: This document defines all the standards for how an accessory communicates with an Apple device. Help owners find their accessories privately and securely using the Find My Network.
    - All specs on FMNA are developed by Apple and are open on the MFi portal. After obtaining Apple's MFi qualification, you can view and download the corresponding specifications of "Find Network" in the personal center.
2. FMNA Core Role
    - Accessory: Find network accessories. By implementing the Apple Find My network protocol, you can locate them by finding networks and servers, and you need to pair them with the Apple ID on the owner's device.
    - Owner device: The owner of the Apple device. When an accessory is paired with an Apple device through the Find app, it is associated with the Apple ID on the device. This device and all devices with the same Apple ID are considered Owner devices.
    - Find My Network: Apple finds the network and uses "Find My" enabled Apple devices to form a crowd-sourced network to locate accessories. When nearby Apple devices detect the Bluetooth LE signal of accessories, they will report encrypted location information to indicate the approximate location.
    - Apple Server: The Apple server receives and temporarily stores the encrypted location data, but only the Owner device can decrypt and obtain the original location.
3. FMNA Features
    - Pairing (with Owner device)
        - The accessory must be paired with the Owner device before it can be located.
        - The Owner device will initiate standard Bluetooth le encryption before accessing the Find My network service.
    - Play sound (proximity search, anti-tracking ringing)
        - The Play Sound feature allows the accessory to ring to locate the accessory.
        - Users can play sounds in the Find application on the Owner device, and the Apple device creates a Bluetooth LE connection or uses an existing connection to the accessory and sends a command to play the sound.
        - When the UT (anti-tracking) alarm appears on the device, the tracked person can control the accessory to play sound from the non-Owner's Apple device.
    - Remote positioning (lost reminder)
        - When the Owner Apple device is far away from the accessory (beyond the Bluetooth LE communication range of the accessory), you can click the "Route" menu in the search APP to navigate to the approximate location of the accessory from the "Map".
        - At this point, the accessory location is recorded as the most recent location monitored by the Owner Apple device or another Apple device.
    - Unwanted tracking detection (anti-tracking)
        - Anti-tracking (UT) mobile side business: Apple devices continue to detect an unrecognized accessory over time, push messages to notify users, and allow the tracked person to take various actions on the device, such as making the maliciously tracked accessory play sound.
        - Anti-tracking (UT) accessory side service: If the accessory detects that it has been moving for a long time, it will start the anti-tracking sound alarm to remind the tracked person that he or she is carrying someone else's accessory.
    - Lost mode
        - Owners can use the Find application to manually place their accessories in lost mode and leave contact information.
        - When someone finds the lost accessory, they can get the details of the owner's settings through NFC or Bluetooth LE to contact the owner to recover the lost item.
    - UARP (Apple's OTA way to find network accessories)
        - Use the Unified Accessory Recovery Protocol (UARP) to update the firmware on the accessory.
        - The protocol, designed by Apple, uses a firmware update service to transmit UARP OTA messages between the accessory and the Owner device.
4. FMNA state machine
    - UnPaired: the status of the accessory when it is started for the first time or when the unpairing is completed. It sends out a broadcast of the accessory to be paired, which contains a specific Payload of each product PPID. When the Apple device scans it, it can pop up a window to pair and register the accessory into the search network.
    - Connected: In the intermediate state (transient state) of the Bluetooth LE connection with the Apple device, then the next state is entered by the rotation of the state machine.
    - Nearby: near state. It will enter this state immediately after disconnecting from the Owner's mobile phone. It will continue to broadcast in a short time to facilitate the Owner's mobile phone to connect again.
    - Separated state. The Nearby state times out or the paired accessory repowers into the state. The broadcast contains a separate broadcast of the long-term public key. The accessory is in this state for most of the day.
    - Currently, for deliverables in the form of Goodix FMNA libraries, users do not need to be concerned about the rotation of the underlying state machine.
    - Application layer To obtain the state machine state, use the following interface: `fmna_state_machine_t fmna_application_state_machine_get(void)`.
5. FMNA Workflow
    - Near & Far Find
        - Accessory pairing: When the accessory and the owner's Apple device are paired in the "Find My" network, the phone sends a message and negotiates an encryption key pair with the accessory according to the process. The Owner device saves the private key and public key, and the accessory saves the public key.
        - Proximity search: The accessory, as a Bluetooth LE Beacon, continuously broadcasts a changing secret key (derived from the public key rotation). If the accessory is nearby but cannot be found for a while, the Owner phone can initiate a Bluetooth LE connection and issue a ring command to let the accessory play a sound to find the location.
        - Remote search: If the accessory is accidentally lost, the surrounding Apple Find My network (other Apple devices passing by) will upload its own location information to the Apple server with the current secret key package after detecting the broadcast.
        - "Find" App location: The "Find" application on the Owner device gets these location reports from the server, and will use the private key to parse out the relevant location information, so as to obtain the location of its accessories.
        - Encryption/anonymity: Because the private key is stored only on the Owner device, and only the owner can decrypt and access the location information, the data passing through Apple's servers is also encrypted end-to-end.
    - Lost mode
        - Tag lost status: Owners can use the Find app to manually set their accessory to lost mode, which will mark the Tag as lost on Apple's servers.
        - NFC or Bluetooth LE to obtain the owner's information: When someone finds the lost accessory, you can get the SN from the accessory through NFC or Bluetooth LE, and you can check the detailed information of the owner's settings from the Apple server through the accessory SN.
        - Contact the owner: The person who finds the accessory can view the information through the URL that pops up on the mobile phone, and then contact the owner directly.

### 4. Apple Find My Solution Based on Goodix GR551x & GR533x Series
1. Apple Find Web Development Documentation
    - Apple MFi official website provides a series of Find My related documents to guide users to develop.
    - It generally includes the following categories: specification, self-test, UARP, Token management, and product planning.
    - Startup Refer to the Find My Network Reference Implementation Validation Guide.
    - MFi members need to read the Apple Find My Spec carefully before developing the project. If you directly use the Goodix FMNA solution, not only can you get the SDK source code for development, but Goodix also summarizes and provides the following deliverable documents to help customers land their projects:
        - Goodix GR5xxx FMNA Development Manual
        - Introduction to GR5515 SK FMNA Demo.
        - GR5xxx FMNA Self-Test Case
        - Find My Power Consumption Model and Key Scenario Measurement
2. Development process based on Goodix GR5xxx platform `查找我的网络配件`
    - MFi qualification application: Only partners with Apple MFi qualification can officially start the research and development of Find My Network products.
    - Goodix FMNA deliverable acquisition: provide the company name and MFi number, and obtain support through sales, official website or FAE.
    - Accessory plan submission: Submit the accessory product plan on the MFi Portal to get the information assigned by Apple, such as PPID, Token, UUID, Product Value, Product Category and other fields.
    - Goodix FMNA SDK integration.
    - The FMNA peripheral is perfect.
    - Custom Bluetooth LE application development (dual slaves).
    - FMNA self-test process.
    - FMNA Certification Process.
3. Tag Class Search Network Accessories Products General Hardware Peripherals
    - In view of the mainstream anti-loss device and Tag search network accessories products on the market, Goodix has carried out a number of disassembly, and summarized the general hardware peripheral requirements, from which different peripherals suitable for various product forms can be selected.
    - Required components:
        - Goodix Bluetooth LE SoC, external crystal (32m), and Bluetooth antenna
        - Battery (non-rechargeable battery such as CR2032/rechargeable battery) and ADC sample battery voltage
        - G-Sensor（I2C）
        - Speaker Driver (PWM) and Speaker (piezoelectric sounder/buzzer)
    - Optional components:
        - External crystal (32.768 K)
        - LED（GPIO）
        - Key (AON GPIO) (external key is recommended)
        - NFC (I2C) (Bluetooth LE obtains SN in a way that completely replaces the NFC function)
        - UWB（QSPI / SPI）
4. Goodix FMNA Solution-SDK Introduction
    - The Goodix FMNA SDK adapts the relevant code of Goodix platform on the basis of Apple Find My Network ADK engineering, and at the same time, the secondary development of each component is left to the customer in the form of callback function to realize the upper interaction logic.
    - The Goodix FMNA DK code is delivered in Lib form and consists of:
        - release & debug library
        - Keil Lib & gcc .a for GR551x
        - Keil Lib for GR533x
    - Apple UARP OTA Feature:
        - The gr _ fmna _ DK _ uarp1.lib contains all the services of UARP. You only need to divide the Flash plan and add it `app_bootloader` to upgrade.
        - The gr _ fmna _ DK _ uarp0.lib does not contain the UARP code. Save Code Size and use Goodix OTA or Customized OTA.
    - The custom _ board folder contains the sample code of Find My common peripherals, which can be adapted to products such as Battery _ det, button, G-Sensor, Speaker, NFC, etc. With simple modifications.
    - Findmy _ slave and vendor _ slave Dual Slave Example:
        - Call `fmna_ret_code_t fmna_application_startup(void)` to open the Find My service.
        -  `vendor_slave` Demonstrate another custom Bluetooth dual slave business. Customers who need it can directly carry out secondary development on this framework.
5. Goodix FMNA Solution-SDK Engineering Structure

```
工程Group名称      描述
gr_startup        系统启动文件
gr_arch           System Core、PMU初始化配置及系统中断接口实现
gr_soc            芯片依赖核心源文件
gr_board          板载支持源文件
gr_stack_lib      GR551x SDK lib文件
gr_app_drivers    App驱动源文件
gr_driver_ext     外设驱动源文件
gr_libraries      常用辅助软件模块
gr_profiles       FMNA或双从机所需的SIG标准Service
gr_fmna_dk        Goodix FMNA DK Lib
findmy_slave      Find My的配置及启动框架代码
vendor_slave      针对客户定制化双从机应用场景的支持框架代码
custom_board      查找网络配件常用外设的示例代码
main              main源文件及工程配置文件
```
6. Goodix FMNA Solution-SDK Engineering Configuration
    - fmna_application.h
        - Header file for Goodix FMNA DK Lib.
        - Contains the startup and external functions of the Find My library file
    - fmna_config.h
        - The internal configuration file of the Goodix FMNA DK Lib is mainly used to configure various Features of the Find My Network Accessory.
        - DEBUG, NFC, UARP, BATT _ TYPE, etc.
    - findmy_platform_port.h
        - Goodix FMNA DK Lib platform adapter
        - Flash erase and read and write
        - Memory malloc and free
        - Message queue
    - fmna_application_config.h
        - Configure specific items related to PPID for different FMNA products
        - It is described in detail in the `《Goodix GR551x FMNA开发手册》` "Engineering Configuration" table, and the configuration marked in green needs to be modified according to its own products.
        - Including but not limited to the following:
            - Name of the manufacturer
            - Module code
            - Chip code
            - Firmware version number
            - Product information category
            - PPID Product Information (Submitted Product Plan is assigned by Apple)
            - Token's location in Flash
            - Whether dual slaves are enabled, etc.
7. Goodix FMNA Solution-Flash Planning and Resource Consumption
    - Resource consumption statistics of Goodix FMNA DK based on GR551x platform:
    - Flash：112.7 KB + 4 KB (Token saving) = 116.7 KB

        ```
        Wolfssl加解密库：42281
        UARP OTA：35814
        FMNA内核代码：24561
        FMNA Platform适配代码：12724
        Total：115380 Bytes
        ```
    - RAM：21.5 KB

        ```
        Wolfssl加解密库：7596
        UARP OTA：1937
        FMNA内核代码：3671
        FMNA Platform适配代码：619
        Malloc Heap：8192
        Total：22015 Bytes
        ```
    - Users can consider developing on the following platforms based on cost and application complexity:
        - GR5513 (512  KB Flash, 128 KB RAM)
        - GR5515 (1 MB Flash, 256 KB RAM)
        - GR533x (512 KB Flash, 96 KB RAM)
    - For a mass production customer, the Find My solution Flash plan on the GR5513BENDU platform is as follows:

        ```
        -------------------------------
        --[         NVDS 8K         ]--
        --[   UserData & Token 8K   ]--
        --[     APP Backup 224K     ]--
        --[       APP FW 224K       ]--
        --[     Second Boot 32K     ]--
        --[    DFU Image Info 4K    ]--
        --[    APP Image Info 4K    ]--
        --[      SCA Backup 4K      ]--
        --[         SCA 4K          ]--
        -------------------------------
        ```
8. Goodix FMNA Solutions-FMNA Peripheral Perfection
    - To find network accessories, Speaker, NFC, G-Sensor and other peripherals are required to realize the functions of finding, retrieving and anti-tracking:
        - Search: Close-range search locates by controlling the sound played by the accessories. A sound playing module, such as Speaker, needs to be added.
        - Retrieve: When the lost mode is enabled for the accessory, other people need to obtain the Serial Number of the accessory to query the owner's information after picking it up, which can be obtained through NFC.
        - Anti-tracking: The accessory detects whether it is moving to indicate whether it is used for malicious tracking. It is necessary to add a motion detection module, such as G-Sensor.
    - GR5xxx FMNA SDK has implemented software framework and logic for NFC, Play Sound, Motion Detection, Battery and other modules, and only needs to initialize and call API for the peripherals used during product development.
    - A set of peripheral sample code has also been implemented in custom _ board and can be developed directly on top of it.
9. Goodix FMNA Solution-Custom Bluetooth LE Application Development (Dual Slave)
    - For more information on dual slaves, read `《Bluetooth LE多从机应用笔记》` the documentation.
    - At present, in the application scenario of Apple's search network, users have the following needs:
        - Apple Find App is limited to the query and location of accessories. Apple Find My Spec prohibits the addition of other instructions. The accessory side is open source but the App side is closed. Users have no right to use the App for other operations.
        - However, the daily use of scooters with network search function still has many customized needs, such as checking mileage, checking power, approaching unlocking and so on.
     - At the same time, based on the following technical limitations, multi-connection of slave devices can not meet the actual product requirements:
        - The same Bluetooth LE device cannot establish two paired encrypted connections with the same master device (such as a cell phone) in the Bluetooth specification.
        - Apple Discovery Network accessories do not allow the addition of Bluetooth LE Service outside the specification, and when a non-Owner phone is connected, the accessory will actively disconnect the device after 10 seconds.
    - GR5xxx Dual Slave Introduction:
        - Based on the Bluetooth LE slave device, the GR5xxx dual slave can enable two independent Bluetooth LE broadcasts (with different addresses and broadcast data) on a single SoC.
        - Dual slaves support two Bluetooth connections, each of which can be paired and bound.
        - After the connection is established by the host, different Bluetooth services can be found for each connection.
        - Two-way connections even support two different apps on the same phone.
    - Therefore, the dual slaves of GR55xx & GR533x FMNA SDK, one slave is used to support Apple Find My service, and the other slave is used for product-specific applications, such as OTA, device status query and control, to help customers easily support network search and achieve many customization needs. And does not break the security specifications of Apple's search network.
10. Goodix FMNA Solution-FMNA Self-Test Flow
    - Find My Certification Assistant (FMCA Test Case Self Test Assistant):
        - FMCA is an application that runs on iOS devices for the development and testing of Find My Network accessories.
        - FMCA supports finding, connecting and interacting with accessories of Find My Network through Bluetooth, and issuing test commands.
        - It is equivalent to an official self-test App of Apple. If it passes the certification, it is necessary to generate a basic test report on this App.
    - Find My Network Reference Implementation Test Cases:
        - The Implementation Self Test Case is a full-featured test case guidance document given by Apple to verify the Find My Certified Assistant (FMCA) and Find My Network Attachment specifications.
        - It contains the category, test case ID, test case description, and test detail steps.
        - The user can verify that all functions on the search network accessory side meet the specification requirements by completing the test according to all the use case IDs in this document.
        - The certification laboratory also conducts certification tests according to this test case entry.
    - Goodix has completed all testing for FMNA. For more details on the testing process, see the documentation `《GR551x FMNA自测用例》`.
11. Goodix FMNA Solutions-FMNA Certification Proc
    - Apple stipulates that third-party search network accessories need to pass laboratory certification before they go on the market, in order to ensure that all the functions of the accessories meet Find My Network Accessory Specification.
    - GR551x series low-power Bluetooth SoC of Huiding Technology has successfully passed the compliance verification of Apple authorized third-party testing institutions in Q2 2023, which indicates that this series of SoC has been fully compatible with the latest specifications and functional requirements of Find My Network Accessory. For details, see [官网页面](https://www.goodix.com/zh/about_goodix/newsroom/company_news/detail/15598).
    - The general process of the Find My Lab certification is as follows: (For more information about the certification, please get support from FAE)
        - Complete FMCA and reference implementation test cases and export test results.
        - Contact an Apple MFi representative or officer to request certified lab contact information.
        - Contact the lab for a quote and to schedule testing services.
        - Complete the Find My Network Reference Implementation Compliance Questionnaire.
        - Prepare certification materials (Bluetooth certificate, product, English manual, test firmware, etc.).
        - Complete the Find My Reference Implementation Packing List and mail all items to the laboratory.
        - Wait for the certification test to be completed or communicate the test results (retest may be required).
        - The test passed.
        - Provide Marketing/PR Materials to Apple review.
12. Goodix FMNA Solution-Token Burning for Mass Production
    - Online GRPLT mass production burning test tool supports Token burning.
    - Many customers have used the Goodix original Token burning solution for mass production. The production line supports importing Token files, saving them in db files, and generating token. Bin for burning during operation.
    - The GRPLT tool also supports secondary development using the.dll library.
    - For details on mass production Token burning and production line tools, please get support from FAE.



### 5. GR5xxx Apple Find My Development Case Experience Sharing

1. Power consumption model for searching network accessory products based on Tag class
    - According to the Apple FMNA Spec, it is formulated `关键场景工作动态表格` to facilitate the horizontal comparison of the working conditions of various Tag products.
    - Modeled after AirTag, perform four close-up look-up rings per day, and remain in breakaway mode `查找配件Tag类产品通用功耗模型` for most of the day.
    - Buy several popular Tags on the market, dismantle the machine and hang the power consumption meter to measure the working current in key scenarios, bring the same power consumption model, and compare the power consumption data of each Tag product horizontally.
    - The current of Tuya SmartTag (GR5513BENDU SoC) is measured and the product **371.11 days of endurance**is obtained by power consumption model.
    -  **Conclusion: The power consumption performance of Goodix FMNA solution in domestic chips should be excellent.**
    - For the actual performance of power consumption of GR551x chip applied to Tag anti-loss device products, please refer to the disassembly report of I Love Audio Network: [With excellent RF performance and stable signal, Huiding Low Energy Bluetooth SoC is applied to Smart tag wireless locator](https://www.52audio.com/archives/175903.html)? Table `汇顶科技GR5513BENDU芯片关键场景功耗测试数据表`.
    - For more details about the Tag class to find the power consumption model of network accessories products, please get support from FAE.
2. Benefits of the Goodix FMNA Solution
    - The overall solution is stable, and there are many large, medium and small customers in mass production, who have accumulated a lot of experience in the various processes of Find My products.
    - The Goodix FMNA DK code is simple, efficient and easy to use. The overall business of Find My in the lower layer does not need too much attention. It only needs to develop customized content. It does not need to invest too much development resources. The development efficiency is high.
    - All kinds of Features of Find My products have been fully adapted, and customers only need to open relevant macros for any function they want, which greatly reduces the development workload of customers.
    - The overall power consumption level is excellent in domestic chips, and it has great advantages for Tag products which are sensitive to non-rechargeable power consumption.
    - The Goodix FMNA solution has a large number of deliverables, detailed development documents and manuals, and a mature mass production plan.
    - The Feature of dual slaves has been used stably in many mass-produced products, expanding more application scenarios and product forms of Bluetooth LE for customers.
    - Goodix itself has a lot of accumulation for Apple's search network architecture, which is convenient to help customers solve all kinds of problems quickly.



### 6. Frequently Asked Questions (FAQ)

1. When testing the Goodix FMNA Demo, sometimes there will be a problem of inaccurate positioning of accessories on the mobile phone, what is the reason?
    - Essentially, the Bluetooth accessory itself does not have any positioning capability. As a Bluetooth Beacon, it broadcasts outward. When searching from a long distance, it will only rely on other Apple devices as Bluetooth base stations. If the mobile phone and other devices detect a specific Bluetooth broadcast, they will report the location to the Apple server. Therefore, whether the location of the search is accurate or not? It relies on finding the number of Apple devices near the accessory in the network.
    - And the positioning of the mobile phone itself will also be related to whether the GPS is turned on, whether the traffic is turned on, whether it is connected to a wireless network, whether the signal is normal, whether it is indoor and many other issues, so the positioning accuracy of the mobile phone itself will also affect the positioning accuracy of finding accessories on App.
    - Finally, in the current indoor test, it is also found that the indoor positioning is not accurate or the positioning track will always move, which is also caused by the inaccurate indoor positioning of the mobile phone itself.
2. After completing the product development, when the accessory is paired with the Owner Apple device for the first time, it prompts "An unknown error has occurred. Please try again in a few minutes. If the problem continues, you may need to contact the manufacturer." Why does this happen?
    - In order for the accessory to be bound to the Apple device normally, it is necessary to burn a Token in a specific location of the Flash. For the first pairing, the authentication process of the rolling token scheme will be carried out through the Token, so as to authorize the accessory to communicate with the Apple device and bind to join the Apple search network.
    - Therefore, this prompt is likely to be a Token exception. Please make sure that:
        - The Apple Token and its corresponding UUID are associated with the product information and are issued by Apple.
        - Token and UUID must be used after being decoded by Base64, and stored in the accessory Flash through pre-burning in the factory production line.
        - The Token is only for one-time use, and its life cycle lasts until the next pairing process. Every time the Token is re-paired, the Apple server will send the updated Token and its corresponding UUID, and the accessories need to be updated and stored.
3. When the accessory ring is operated at close range, the ring sometimes fails to ring, showing "accessory address is not available" or "item cannot be connected". What is the reason?
    - FMNA accessories are available with long and multiple connection mechanisms:
        - Long accessory connection: The Apple ID logs in to a single Apple device and operates the paired accessory. At this time, the accessory and the Owner's phone remain connected all the time. The phone will not actively disconnect. There will only be a policy to adjust the connection interval (for example, adjust the connection interval from 30 ms to 990 ms).
        - Accessory multi-connection: Different Apple devices log in to the same Apple ID and operate the same search network accessory. Each time, the phone will actively disconnect (0xA3 disconnection) after sending instructions to the accessory. At this time, the accessory will experience a state change from fast proximity broadcast (broadcast interval 30 ms), slow proximity broadcast (2 s), and finally separate broadcast (2S).
    - Long connection or multi-connection status mainly depends on whether the mobile phone will actively disconnect our accessories. Currently, there is no business logic for active Bluetooth LE disconnection on the accessory side of Find My SDK.
    - In the case of multiple connections, every time the phone sends a ring command, it will go through a process of scanning the broadcast and establishing Bluetooth connection. If it is not connected immediately during this process, the address will be unavailable, or it will show "unable to connect items, please walk around to connect" and so on.
4. When unbinding accessories, find App and wait for a period of time, showing "no items found", what is the reason for this?
    - When the mobile phone actively removes the accessories, the Bluetooth connection is not established in an abnormal situation, and the mobile phone sends a command that it does not know how to configure, this prompt will appear on the UI.
    - If the accessory is next to the phone and it is confirmed that the broadcast has been sent out normally, it can be tried several times.
    - If the accessory is not next to the Owner phone, the phone cannot establish a Bluetooth LE connection at all. At this time, click the red removal button in "Item not found", and the Owner phone will mark on the Apple server that the accessory has been forcibly unbound. If the accessory is to be used normally next time, it is necessary to restore the device to the factory settings by physical means. And then match them.
5. After the mobile phone triggers the anti-tracking service, it will display the Tag location of malicious tracking. When monitoring the dots, some dots are very far apart, some dots are very dense, and sometimes there is a problem of large distance positioning deviation. What is the reason?
    - After the mobile phone triggers the anti-tracking service, all other services are not directly related to the accessories, except that the command of non-owner ringing will interact with the accessories.
    - The monitoring and management on the journey here is also entirely the business of finding App, which is the result of the mobile phone's own calculation, so the interval of monitoring and management and the overall positioning accuracy are related to the mobile phone positioning mechanism.
6. Precautions for use of Goodix FMNA DK:
    - The application layer needs to be configured in the `fmna_config_t fmna_config` struct for the effective Feature of the final Find My library.
    - Apple UARP upgrade relies on `Second Boot` or is a `App Bootloader` scheme. If the large firmware is upgraded normally, the logic of firmware verification, handling and jumping cannot be completed normally without `BootLoader` the small firmware.
    - The application layer needs to register the start address of the Blank 1 area with the UARP OTA firmware, use the macro `FMNA_UARP_DFU_FW_SAVE_ADDR`, and ensure 4K alignment.

