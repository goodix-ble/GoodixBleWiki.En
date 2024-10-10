## Apple Find My技术方案 #




- 本技术方案适用于Goodix蓝牙全系列芯片GR5xxx。
- 更多有关于苹果Find My的详细介绍，请参考官网[Apple Find My](https://www.goodix.com/zh/product/connectivity/ble/apple_find_my)页面。
- 其中技术细节仅针对MFi成员开放，如需获取汇顶科技支持Apple Find My Network技术的SDK开发资料，请提供公司名称和MFi编号等基本信息，通过官网“[获得支撑](https://developers.goodix.com/zh/bbs/support)”获取相关资源和技术支持。



### 1. Apple FMNA简介

1. FMNA基本概况
    - FMNA方案：苹果官方Spec称为`Apple Find My Network Accessory`，中文是苹果“`查找我的`”网络配件，也可以叫做`苹果Find-My`。
    - 它是由苹果公司推出的、由全球数十亿台苹果设备组成的`众包网络`。
    - 每个苹果设备相当于一个基站，采用`蓝牙无线技术`检测附近丢失物品，并将其大致位置报告给所有者。
    - 整个过程是端到端`加密和匿名`的，旨在保护用户隐私安全；同时，查找功能也十分高效，无需担心电池续航或流量消耗。
2. FMNA优势
    - 完善生态
        - 庞大的全球查找网络：全球数十亿计的Apple设备都可以为丢失物品提供定位服务，设备越多查找网络的定位精度就越高。
        - 查找App内嵌入苹果生态：“查找”App在苹果系统官方预装，是IOS系统的一个功能，默认开启了相关权限，无需品牌方维护。
        - 多设备添加：同一`Apple ID`下的配件是互通的，并且每个账号可以绑定最多16个配件。
    - 智能查找
        - 近距离查找：Bluetooth LE近距离连接范围内直接让配件播放声音寻物。
        - 远距离查找：查找网络中的“附近设备”可追踪配件的蓝牙信号，如被检测到，加密位置后上传至苹果服务器，物主就可在“查找”应用中实时定位丢失物品的位置。
        - 丢失联系：主动开启配件的“丢失模式”，让捡到的人知道失主信息。
    - 开放适配
        - 支持第三方配件接入（MFi）：2021年4月上旬，苹果官方宣布查找网络配件功能开源，开放提供给打算将产品接入苹果“查找”网络的第三方配件开发商，并且这一计划隶属于MFi计划。
3. FMNA产品类别
    - 独立防丢配件
    - 服装
    - 个人物品
    - 旅行装备
    - 运动器材
    - 电子设备
    - 医疗设备
4. FMNA应用场景介绍
    - 关于Apple Find My的应用场景，请观看官网页面“培训和活动”中的[视频一](https://www.goodix.com/zh/product/connectivity/ble/apple_find_my)（15:25时间点）。

### 2. 第三方品牌厂商的FMNA项目整体流程
1. 第三方品牌厂商量产流程（产品及硬件）
    - 正式立项，FMNA产品定义确认。
    - 硬件原理图设计。
    - 打板测试。
    - 确认产线流程，小规模硬件试产。
    - 硬件就绪确认送样版本号。
2. 第三方品牌厂商量产流程（软件）
    - 获取Goodix Find-My SDK开发资料。
    - 外设及传感器适配，客户定制双从机应用开发。
    - Find My软件功能适配。
    - 产品测试流程。
    - 软件就绪，确认送样苹果的版本号。
    - 准备苹果认证测试报告（FMCA），填写送样前流程表格。
    - 提交苹果测试实验室自测报告、FCC测试报告、QDIO和产品说明书等材料。
3. 苹果MFi流程
    - 无MFi资质需认证企业MFi会员账号。
    - 有MFi资质后申请查找网络配件PPID。
    - 搭建服务器，从Apple批量拉取Token。
    - 寄送样品至第三方实验室，进行查找网络配件合规性认证。
    - 产品包装及营销传播认证。
4. 法规认证流程
    - BQB测试，列名QDID。
    - FCC认证。
    - 大规模量产。

### 3. 苹果查找网络Features及原理简述
1. 查找我的网络配件FMNA Spec
    - **F**ind **M**y **N**etwork **A**ccessory Specification：该文档定义了配件如何与Apple设备进行通信的所有标准，帮助所有者使用Find My网络私密且安全地找到他们的配件。
    - 有关于FMNA的所有Spec均由苹果制定，开放在MFi门户网站，获取Apple的MFi资质，就可以在个人中心查看并下载“查找网络”相应的规格书。
2. FMNA核心角色
    - Accessory：查找网络配件，通过实施Apple Find My网络协议，可借助查找网络及服务器进行定位，并需与所有者设备上的Apple ID配对。
    - Owner device：物主苹果设备，配件与Apple设备通过“查找”应用配对后，会与设备上的Apple ID关联，此设备及所有同一Apple ID登录的设备视为Owner设备。
    - Find My Network：苹果查找网络，使用启用“查找我的”功能的Apple设备组成众包网络来定位配件，附近Apple设备检测到配件的Bluetooth LE信号后，会上报加密位置信息，指示大致位置。
    - Apple server：Apple服务器，接收并暂存加密位置数据，但只有Owner设备才能解密获取原始位置。
3. FMNA Features
    - Pairing（与Owner设备配对）
        - 配件须先与Owner设备配对，然后才能定位。
        - Owner设备将在访问“查找我的”网络服务之前启动标准Bluetooth LE加密。
    - Play sound（近距离查找、防跟踪响铃）
        - 播放声音功能允许配件响铃以定位配件。
        - 用户可以在Owner设备上的“查找”应用程序播放声音，Apple设备会创建Bluetooth LE连接或使用与配件的现有连接并发送播放声音指令。
        - 当设备上出现UT（防跟踪）警报时，被跟踪者可以从非Owner的苹果设备控制配件播放声音。
    - 远距离定位（遗落提醒）
        - 当Owner Apple设备与配件距离较远（超过配件Bluetooth LE通信范围）时，可点击查找APP中“路线”菜单，由“地图”导航至配件大概位置。
        - 此时配件位置记录为Owner Apple设备或其他Apple设备最近监测到的位置。
    - Unwanted tracking detection（防跟踪）
        - 防跟踪（UT）手机侧业务：苹果设备随着时间的推移持续检测到随身携带一个无法识别的配件，会推送消息通知用户，并允许被跟踪者在设备上采取各种行动，如让恶意跟踪的配件播放声音等。
        - 防跟踪（UT）配件侧业务：配件如果检测到自己处于长时间移动状态，就会启动防跟踪声音报警，提醒被跟踪者随身携带了一个别人的配件。
    - Lost mode（丢失模式）
        - Owner可以使用“查找”应用程序将自己的配件手动置于丢失模式，并留下联系方式。
        - 当有人捡到这个丢失的配件时，可以通过NFC或Bluetooth LE途径来获取失主设置的详细信息，以联系失主找回丢失的物品。
    - UARP（苹果查找网络配件OTA方式）
        - 使用统一配件恢复协议（UARP）来更新配件上的固件。
        - 该协议由苹果设计，使用固件更新服务在配件和Owner设备之间传输UARP OTA消息。
4. FMNA状态机
    - UnPaired：待配对状态，配件首次启动或解配完成时的状态，发出待配对广播，包含每个产品PPID的特定Payload，苹果设备扫描到就可以弹窗进行配对，将配件注册进查找网络中。
    - Connected：在与苹果设备进行Bluetooth LE连接的中间态（瞬时状态），之后由状态机的轮转进入下一状态。
    - Nearby：临近状态，在与Owner手机断开连接后立即进入此状态，短时间内持续广播，方便Owner手机再次回连。
    - Separated：分离状态，Nearby状态超时或者已配对的配件重新上电进入的状态，广播包含长期公钥的分离广播，配件在一天中的大部分时间都处于这个状态。
    - 目前针对使用Goodix FMNA库形式的交付件，用户无需关心底层状态机的轮转。
    - 应用层要获取状态机状态，请使用以下接口：`fmna_state_machine_t fmna_application_state_machine_get(void)`。
5. FMNA工作流程
    - 近距离&远距离查找
        - 配件配对：配件和所有者的Apple设备在“查找我的”网络配对时，手机下发消息并按照流程和配件协商出一个加密密钥对，Owner设备保存私钥和公钥，配件保存公钥。
        - 近距离查找：配件作为Bluetooth LE Beacon，不断广播一个变化的秘钥（由公钥轮转衍生），如果配件在附近但一时无法发现，此时Owner手机可以发起Bluetooth LE连接，下发响铃指令让配件播放声音来查找位置。
        - 远距离查找：如果配件意外丢失，周围的Apple Find My网络（周边经过的其它苹果设备）协寻设备检测到这个广播后，会把自身的定位信息用当前的秘钥打包上传至苹果服务器。
        - “查找”App定位：Owner设备上的“查找”应用程序从服务器上拿到这些定位报告，会使用私钥将相关的定位信息解析出来，从而获取到自己配件的位置。
        - 加密/匿名：因为私钥仅存储在Owner设备上，只有物主才可以解密并访问位置信息，所以经过Apple服务器中的数据也是端到端加密的。
    - 丢失模式
        - 标记丢失状态：物主可以使用“查找”应用程序将自己的配件手动设置为丢失模式，这样会在苹果服务器上标记这个Tag为丢失状态。
        - NFC或Bluetooth LE获取物主信息：当有人捡到这个丢失的配件时，可以通过NFC碰一碰或Bluetooth LE途径从配件获取SN，通过配件SN即可从苹果服务器上查到失主设置的详细信息。
        - 联系失主：捡到配件的人可以通过手机上弹出的URL查看信息，之后直接联系失主。

### 4. 基于Goodix GR551x & GR533x系列的Apple Find My解决方案介绍
1. Apple查找网络开发文档
    - 苹果MFi官网提供一系列Find My相关文档指导用户开发。
    - 大致包括以下几类：规范类、自测试类、UARP类、Token管理类和产品计划类。
    - Startup请参考《查找我的网络参考实施验证指南》。
    - MFi成员需要在项目开发前仔细阅读Apple Find My Spec。如果您直接使用Goodix FMNA解决方案，不仅可以拿到SDK源码进行开发，Goodix还总结并提供以下交付件文档助力客户项目落地：
        - 《Goodix GR5xxx FMNA开发手册》
        - 《GR5515 SK FMNA Demo介绍》
        - 《GR5xxx FMNA自测用例》
        - 《Find My功耗模型及关键场景实测》
2. 基于Goodix GR5xxx平台`查找我的网络配件`开发流程
    - MFi资质申请：具有Apple MFi资质的伙伴才可以正式开始Find My Network产品的研发。
    - Goodix FMNA交付件获取：提供公司名称和MFi编号，通过销售、官网或FAE等途径获取支持。
    - 配件计划提交：在MFi Portal提交配件产品计划以获取Apple分配的信息，如PPID、Token、UUID、Product Value、Product Category等字段。
    - Goodix FMNA SDK集成。
    - FMNA外设完善。
    - 自定义Bluetooth LE应用开发（双从机）。
    - FMNA自测试流程。
    - FMNA认证流程。
3. Tag类查找网络配件产品通用硬件外设
    - 针对市面上主流的防丢器和Tag类查找网络配件产品，Goodix进行了多个拆解，并总结出通用的硬件外设需求，可以从中选择适合各类产品形态的不同外设。
    - 必需器件：
        - Goodix Bluetooth LE SoC、外部晶振（32M）及Bluetooth LE天线
        - Battery（不可充电电池如CR2032 / 可充电电池）及ADC采样电池电压
        - G-Sensor（I2C）
        - Speaker Driver（PWM）及Speaker（压电片发声器 / 蜂鸣器）
    - 可选器件：
        - 外部晶振（32.768K）
        - LED（GPIO）
        - 按键（AON GPIO）（推荐添加外部按键）
        - NFC（I2C）（Bluetooth LE获取SN的方式能完全代替NFC功能）
        - UWB（QSPI / SPI）
4. Goodix FMNA解决方案 -- SDK介绍
    - Goodix FMNA SDK在Apple Find My Network ADK基础工程上适配了Goodix平台相关代码，同时将各个组件二次开发，以回调函数形式留给客户实现上层交互逻辑。
    - Goodix FMNA DK代码以Lib形式交付，包含：
        - release & debug library
        - Keil Lib & gcc .a for GR551x
        - Keil Lib for GR533x
    - 苹果UARP OTA Feature：
        - gr_fmna_dk_uarp1.lib包含UARP所有业务，只需划分好Flash规划，添加`app_bootloader`即可进行升级。
        - gr_fmna_dk_uarp0.lib不包含UARP代码，节省Code Size，可以使用Goodix OTA或客制化OTA。
    - custom_board文件夹中包含Find My常用外设的示例代码，简单修改即可适配产品，如Battery_det、button、G-Sensor、Speaker、NFC等。
    - findmy_slave和vendor_slave双从机示例：
        - 调用`fmna_ret_code_t fmna_application_startup(void)`即可开启Find My业务。
        - `vendor_slave`演示另一个自定义蓝牙双从机的业务，有需求的客户可以直接在这个框架上进行二次开发。
5. Goodix FMNA解决方案 -- SDK工程结构
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
6. Goodix FMNA解决方案 -- SDK工程配置
    - fmna_application.h
        - Goodix FMNA DK Lib的头文件
        - 包含Find My库文件的启动及对外使用函数
    - fmna_config.h
        - Goodix FMNA DK Lib的内部配置文件，主要对于Find My Network Accessory的各类Feature进行配置
        - DEBUG、NFC、UARP、BATT_TYPE等配置
    - findmy_platform_port.h
        - Goodix FMNA DK Lib的platform适配接口
        - Flash擦和读写
        - 内存malloc及free
        - 消息队列
    - fmna_application_config.h
        - 配置不同FMNA产品PPID相关的具体项目
        - 在`《Goodix GR551x FMNA开发手册》`的“工程配置”表格中详细说明，标绿配置需根据自身产品进行修改
        - 包含但不限于以下内容：
            - 生产厂商名称
            - 模组代号
            - 芯片代号
            - 固件版本号
            - 产品信息类别
            - PPID产品信息（提交产品计划由Apple分配）
            - Token在Flash的保存位置
            - 是否使能双从机等
7. Goodix FMNA解决方案 -- Flash规划及资源消耗
    - Goodix FMNA DK基于GR551x平台的资源消耗统计：
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
    - 用户可以根据成本和应用复杂度考虑在以下平台进行开发：
        - GR5513 (512  KB Flash, 128 KB RAM)
        - GR5515 (1 MB Flash, 256 KB RAM)
        - GR533x (512 KB Flash, 96 KB RAM)
    - 某量产客户，在GR5513BENDU平台上Find My方案Flash规划如下：
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
8. Goodix FMNA解决方案 -- FMNA外设完善
    - 查找网络配件需由Speaker、NFC、G-Sensor等外设实现查找、找回、防跟踪等功能：
        - 查找：近距离查找通过控制配件播放声音进行定位，需加入声音播放模块，如Speaker。
        - 找回：当配件启用丢失模式，其他人拾取后需获取配件Serial Number查询失主信息，可通过NFC贴近获取。
        - 防跟踪：配件检测自身是否移动，来提示是否被用于恶意跟踪，需加入运动检测模块，如G-Sensor等。
    - GR5xxx FMNA SDK针对NFC、Play Sound、Motion Detection、Battery等模块均已实现软件框架和逻辑，产品开发时只需针对使用的外设进行初始化和API调用即可。
    - custom_board中也已实现一套外设示例代码，可以直接在此基础上开发。
9. Goodix FMNA解决方案 -- 自定义Bluetooth LE应用开发（双从机）
    - 关于双从机的详细内容，可阅读`《Bluetooth LE多从机应用笔记》`文档。
    - 当前，在苹果查找网络的应用场景中，用户有以下需求：
        - 苹果查找App仅限于配件的查询和定位，Apple Find My Spec禁止添加其他指令，配件端开源但App端封闭，用户无权利用App做其他操作。
        - 但是，日常使用带有查找网络功能的滑板车却还有查里程、查电量、靠近解锁等诸多定制化需求。
     - 同时，基于以下几点技术限制，从设备多连接也不能达到实际产品需求：
        - 同一Bluetooth LE设备在蓝牙规范中无法与同一主设备（如手机）建立两条配对的加密连接。
        - 苹果查找网络配件不允许添加规范以外的Bluetooth LE Service，并且非Owner手机连接时，配件会在10s后主动断连该设备。
    - GR5xxx双从机简介：
        - GR5xxx双从机以Bluetooth LE从设备为基础，能够在单颗SoC上开启两条独立的Bluetooth LE广播（地址不同、广播数据不同）。
        - 双从机支持两路蓝牙连接，每路连接均可配对并绑定。
        - 在被主机建连后每路连接均可发现不同的蓝牙服务。
        - 两路连接甚至支持同一个手机上的两个不同App。
    - 因此，GR55xx & GR533x FMNA SDK的双从机，一个从机用于支持Apple Find My服务，另一从机用于产品专属应用，例如OTA、设备状态查询及控制等丰富功能，助力客户产品轻松支持查找网络，并实现诸多定制化需求，且不会破坏苹果查找网络的安全规范。
10. Goodix FMNA解决方案 -- FMNA自测流程
    - Find My Certification Assistant（FMCA Test Case自测助手）：
        - FMCA是一个在iOS设备上运行的应用程序，用于进行Find My Network配件的开发和测试。
        - FMCA支持通过蓝牙发现、连接Find My Network的配件并与之交互，下发测试命令。
        - 相当于苹果官方的一个自测试App，如果通过认证，需要在此App上生成基础测试报告。
    - Find My Network Reference Implementation Test Cases（参考实施自测试用例）：
        - 实施自测试用例是苹果给出的全功能测试用例指导文档，用于验证查找我的认证助手（FMCA）和查找我的网络附件规范。
        - 其中包含类别、测试用例ID、测试用例描述和测试详细步骤。
        - 用户按照此文档的所有用例ID测试完成，即可验证查找网络配件侧的所有功能符合规范要求。
        - 认证实验室也是按照此测试用例条目进行认证测试。
    - Goodix已经完成FMNA的所有测试。更多测试流程详情，可查看文档`《GR551x FMNA自测用例》`。
11. Goodix FMNA解决方案 -- FMNA认证流程
    - 苹果规定第三方查找网络类配件在上市之前需要通过实验室认证，其目的是为了确保配件的所有功能符合Find My Network Accessory Specification。
    - 汇顶科技GR551x系列低功耗蓝牙SoC已于2023年Q2成功通过Apple授权第三方测试机构的各项合规性验证，标志着该系列SoC已全面兼容Find My Network Accessory的最新规格和功能要求，详情见[官网页面](https://www.goodix.com/zh/about_goodix/newsroom/company_news/detail/15598)。
    - Find My实验室认证大致流程如下：（有关认证的详细信息，请通过FAE获取支持）
        - 完成FMCA和参考实施测试用例，导出测试结果。
        - 联系Apple MFi代表或专员，请求认证实验室联系信息。
        - 联系实验室获得报价并安排测试服务。
        - 填写“查找我的网络参考实施合规性调查问卷”。
        - 准备认证材料（蓝牙证书、产品、英文说明书、测试固件等）。
        - 填写“查找我的参考实施装箱单”并将所有物品邮寄实验室。
        - 等待认证测试完成或交流测试结果（可能需要重测）。
        - 测试通过。
        - 提供Marketing/PR Materials至Apple评审。
12. Goodix FMNA解决方案 -- 量产Token烧录
    - 在线GRPLT量产烧录测试工具支持Token烧录。
    - 多个客户已使用Goodix原厂Token烧录方案量产，产线使用支持导入Token文件，保存于db文件中，运行时再生成token.bin进行烧录。
    - GRPLT工具也支持客户使用.dll库进行二次开发。
    - 有关于量产Token烧录和产线工具的详细内容，请通过FAE获取支持。



### 5. GR5xxx Apple Find My开发案例经验分享

1. Tag类查找网络配件产品功耗模型
    - 按照Apple FMNA Spec，制定`关键场景工作动态表格`，方便横向对比各类Tag产品的工作情况。
    - 仿照AirTag，每天进行四次近距离查找响铃，并且全天大部分时间保持在分离模式下，制定`查找配件Tag类产品通用功耗模型`。
    - 购买市面上比较火爆的几款Tag，拆机挂功耗仪实测关键场景下的工作电流，带入同一功耗模型，横向对比各个Tag产品的功耗数据。
    - 实测Tuya SmartTag（GR5513BENDU SoC）电流，并且带入功耗模型得出该产品**续航371.11天**。
    - **结论：Goodix FMNA解决方案在国产芯片中的功耗表现应该是很优秀的。**
    - 有关于GR551x芯片应用于Tag防丢器产品上的功耗实际表现，可参考我爱音频网的拆解报告：[优秀射频性能，信号稳定，汇顶科技低功耗蓝牙SoC应用于Smart tag无线定位器](https://www.52audio.com/archives/175903.html)，表格`汇顶科技GR5513BENDU芯片关键场景功耗测试数据表`。
    - 更多有关于Tag类查找网络配件产品功耗模型的详细内容，请通过FAE获取支持。
2. Goodix FMNA解决方案的优势
    - 整体方案稳定，且有很多量产的大中小类客户，对于Find My产品的各项流程积累了很多经验。
    - Goodix FMNA DK代码简单、高效、易用，下层Find My整体业务无需过多关注，只要开发客制化的内容即可，无需投入过多的开发资源，开发效率很高。
    - 对于Find My产品的各类Feature已经完全适配，客户想要什么功能只需开启相关宏，极大地减少了客户的开发工作量。
    - 整体功耗水平在国产芯片中较为优秀，对于Tag类不可充电功耗敏感的产品有很大的优势。
    - Goodix FMNA解决方案的交付件众多，开发文档和手册比较详实，且有一套成熟的量产方案。
    - 双从机的Feature已经在多个量产产品中稳定使用，给客户拓展了Bluetooth LE更多的应用场景和产品形态。
    - Goodix本身对于苹果查找网络这一套架构有很多积累，方便帮助客户快速解决各类问题。



### 6. 常见问题答疑（FAQ）

1. 在测试Goodix FMNA Demo时，有时会出现配件在手机上位置定位不准的问题，这是什么原因呢？
    - 从本质上来说，蓝牙配件本身不具备任何定位的能力，它作为一个蓝牙Beacon，向外广播，远距离查找时只会依托其它苹果的设备作为蓝牙基站，如果手机等设备检测到了特定的蓝牙广播，才会上报位置至苹果服务器，所以查找的位置是否精确，都依托查找网络中在这个配件附近的苹果设备数量。
    - 并且手机自身的定位，也会和手机是否开启了GPS、是否开启了流量、是否连接到了某个无线网络、信号是否正常、是否在室内等诸多问题相关，所以手机自身的定位准确性也会影响到查找App上配件物品的定位精度。
    - 最后，目前在室内测试时，也发现了室内定位不准或定位轨迹会一直移动的问题，这也是手机本身在室内定位不准所造成的。
2. 完成产品开发后，配件在首次和Owner苹果设备进行配对时却提示“发生未知错误，请几分钟后再试一次，如果问题继续存在，您可能需要与生产企业联系”，为什么会出现这种配对不上的情况呢？
    - 配件要正常绑定到苹果设备上，需要在Flash的特定位置烧录Token，首次配对会通过Token进行滚动令牌方案的身份验证流程，以此方式来授权配件与Apple设备进行通信，并绑定加入Apple查找网络。
    - 所以出现这条提示大概率是Token异常，请确保：
        - Apple Token及其相应的UUID与产品信息相关联，由苹果下发。
        - Token和UUID须经Base64解码后使用，通过工厂产线预烧录进配件Flash中储存。
        - Token仅供一次性使用，生命周期持续到下一次配对流程，每次重新配对时都会由苹果服务器下发更新Token及其相应的UUID，配件需更新存储。
3. 在近距离操作配件响铃时，有时候会响铃失败，显示“配件地址不可用”或“无法连接物品”，这是什么原因呢？
    - FMNA配件有长连接和多连接机制：
        - 配件长连接：Apple ID登录单一苹果设备并操作配对的配件，此时配件和Owner手机一直保持连接，手机不会主动断连，只会有调整连接间隔的策略（比如将连接间隔从30 ms调整为990 ms）。
        - 配件多连接：不同苹果设备登录相同Apple ID并操作同一个查找网络配件，每次手机会在给配件发送指令后主动断连（0xA3断连），此时配件会经历快速临近广播（广播间隔 30ms）、慢速临近广播（2s）最后到分离广播的状态变化（2s）。
    - 长连接或多连接状态主要取决于手机是否会主动断连我们配件，当前Find My SDK中配件侧没有主动Bluetooth LE断连的业务逻辑。
    - 在多连接情况下，每次手机下发响铃指令均会经历一遍扫描广播和蓝牙建连过程，如果在这个过程中没有立即连上，会出现地址不可用，或者显示“无法连接物品，请四处走动以连接”等情况。
4. 解除配件绑定时，查找App等待一段时间，显示“找不到物品”，这是什么原因呢？
    - 手机主动移除配件时，在异常情况下没有建立蓝牙连接，手机下发不了解配指令，在UI上就会出现这个提示。
    - 如果配件在手机旁边，并确认广播已经正常发出，此时可以多次尝试。
    - 如果配件不在Owner手机旁边，手机根本建立不了Bluetooth LE连接，此时点击“找不到物品”中的红色移除按钮，Owner手机就会在苹果服务器标注这个配件已经强行解绑了，配件下次若要正常使用就需要通过物理方式将设备恢复出厂设置，之后再配对即可。
5. 手机触发防跟踪业务后，会将恶意跟踪的Tag位置显示出来，在监控打点时，打点间隔有些点很远，有些点很密，有时还出现距离定位偏差大的问题，这是什么原因呢？
    - 手机触发防跟踪业务后，除了非Owner响铃这一项指令会和配件交互之外，其余的所有业务和配件均无直接关系。
    - 这里路程上的监控打点，也完全是查找App的业务，是手机自行计算的结果，所以监控打点的间隔和整体定位准确度，和手机定位机制有关。
6. Goodix FMNA DK使用注意事项：
    - 最终Find My库生效的Feature，应用层需要在`fmna_config_t fmna_config`结构体中进行配置。
    - 苹果UARP升级依托`Second Boot`或者是`App Bootloader`方案，如果在大固件完成正常升级后，没有`BootLoader`小固件也不能正常完成固件校验、搬运和跳转的逻辑。
    - 应用层需注册有关于UARP OTA固件的Blank 1区域起始地址，使用宏`FMNA_UARP_DFU_FW_SAVE_ADDR`，并确保4K对齐。

