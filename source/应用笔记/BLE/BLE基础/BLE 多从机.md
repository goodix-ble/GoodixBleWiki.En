## BLE多从机 (Multi Slave)

### 1. GR5xx多从机基本概念介绍

1. BLE从设备简介
    - 通用访问规范GAP（Generic Access Profile）定义了四种设备角色：广播者（Broadcaster）、观察者（Observer）、中央设备（Central）以及外围设备（Peripheral）。
    - 低功耗蓝牙中的外围设备也称为 “从设备” 或 “从机”，广泛应用于需要低功耗和无线数据传输的健康医疗、工业监测、智能家居和IoT等应用领域。
2. BLE从设备功能介绍
    - 从设备（Peripheral）向外周期性发送广播数据，被动接收其它设备发起的物理连接。
    - 从设备等待主设备（Central）的连接请求，一旦建立连接，便可以向主机提供特定服务或数据信息。
    - 从设备作为GATT服务端，提供特征（Characteristic）和服务（Service），供主设备读取或写入数据。
    - 从设备向主设备发送通知（Notification）或指示（Indication）消息，并主动向主设备报告更新的数据。
    - 关于从设备涉及的通用属性规范GATT（Generic Attribute Profile）内容细节，请参考《[GR551x BLE Stack用户指南](https://docs.goodix.com/zh/online/gr55xx_ble_stack_user_guide)》。
3. GR5xx多从机简介
    - GR5xx多从机以BLE从设备为基础，能够在单颗SoC上开启多条独立的BLE广播（地址不同、广播数据不同）。
    - 多从机支持多路蓝牙连接，每路连接均可配对并绑定。
    - 与主机建连后，每路连接均可发现不同的蓝牙服务。
    - 多路连接支持同一个手机上的多个不同App。
4. GR5xx多从机的应用场景
    - 如果对端主机是多个实体设备，“多连接” 即可满足这种应用需求，多从机和传统意义上的多连接是有区别的。
    - 多从机允许GR5xx单颗蓝牙芯片与同一手机上的多个应用App同时连接并独立通信，且不会相互影响。
    - 每一路从机被手机多个App发现到的服务是不同的，相当于单颗SoC构建了多路虚拟从机来实现相互独立的BLE设备功能。


### 2. GR5xx多从机应用笔记

- 多从机示例，可参考SDK工程`SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave`。

- 双从机示例工程包含了从机1（HRS心率服务）和从机2（HID服务）与同一手机建连，实现心率传感器和键盘功能分别在两个蓝牙链路上的不同表现。

- 以双从机举例，说明多从机的实现方法：

  - 每个从机均包含一个或多个BLE Profile来实现特定的蓝牙功能。添加自定义Service，请参考《[GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl)》。

  - 每个从机需要开启一个BLE广播（地址不同，参数及Payload自行设置）。为保证广播相互独立，确保双从机的广播索引`adv_idx`不同。

  - 两条广播开启后，主机可以分别与双从机建连。此时需使用接口`void ble_gap_conn_local_addr_get(uint8_t conidx,uint8_t *p_addr)`判断当前连接是根据哪个广播建立的，记录连接索引`conn_idx`以便后续流程用。

  - 最后，通过接口`uint16_t ble_gatts_service_hide_set(uint8_t conn_idx, uint16_t handle)`配置服务的可见性。在每次建连时将对方从机的某些服务`Service Handles`隐藏，从而保证当前从机的服务可见。详细信息，请参考双从机示例工程中`void app_connected_handler(uint8_t conn_idx, const ble_gap_evt_connected_t *p_param)`函数。

- 总的来说，多从机中的单个从机就是一个标准的BLE设备，GR5xx在单颗SoC上虚拟了多个BLE实体，与同一主机以分时复用的方式，构建出了独立通信且互不影响的多条链路，可满足更加多元和客制化的BLE应用场景。

### 3.FAQ

**Q**：BLE从设备本来就支持多连接，那么多连接和多从机具体有什么区别呢？双从机或者多从机的具体应用场景是什么？

**A**：当前，GR5xx多从机主要应用于苹果查找网络配件产品。在该应用场景中，用户有以下需求：

- 苹果查找App仅限于配件的查询和定位，Apple Find My SPEC禁止添加其他指令，配件端开源但App端封闭，用户无权利用App进行其他操作。
- 日常使用带有查找网络功能的滑板车还有查里程、查电量和靠近解锁等诸多定制化需求。

   同时，基于以下几点技术限制，从设备多连接可能无法达到实际产品需求：
   
   - 同一BLE设备在蓝牙规范中无法与同一主设备（如手机）建立两条配对的加密连接。
   - 苹果查找网络配件不允许添加规范以外的BLE Service，并且非Owner手机连接时，配件会在10s后主动断连该设备。
   
   
   因此，GR5xx双从机中的一个从机用于支持Apple Find My服务，另一从机用于产品专属应用，例如OTA、设备状态查询及控制等丰富功能，助力客户产品轻松支持查找网络，并实现诸多定制化需求，且不会破坏苹果查找网络的安全规范。

**Q**：在实际应用双从机的工程中，每条链路的广播都是独立的，如果有频繁修改广播地址的应用场景，应该怎么实现呢？

**A**：为了确保双从机的广播相互独立，假设从机1已经成功开启广播1，从机2要启动一个地址不同的广播2，可采用如下方式实现：

1. 启动广播2之前，首先应该使用`uint16_t ble_gap_addr_get(ble_gap_bdaddr_t *p_addr)`函数保存广播1的地址到全局变量`ble_gap_bdaddr_t s_gap_default_addr`中。

2. 使用`uint16_t ble_gap_addr_set(ble_gap_bdaddr_t const *p_addr)`函数设置广播2的不同地址。

3. 当广播2成功开启后，在协议栈`BLE_GAPM_EVT_ADV_START`回调中使用保存的全局变量，恢复之前广播1地址的配置。

   下一次启动广播前同理，以此方式实现这一需求。

**Q**：同一个手机可以正常连接双从机，但是建连后每个从机发现的服务为什么不符合预期？

**A**：若每个从机均可发现两个从机所有的服务，则检查配置服务Service可见性的逻辑是否已添加并正常实现；若当前从机发现了另外一个从机的服务，自己本来应该具有的服务却没有，则检查连接索引`conn_idx`是不是判断有误，或者是刚好设置反了。

**Q**：双从机建连正常，服务发现也正常，但是从设备端发消息到手机，为什么手机却接收不到呢？

**A**：当主机建连后，变量`conn_idx`应该在全局维护好，它代表着当前的连接索引。

- 这个值不光区分主机在哪条链路下发数据，从机设备端也应该在对应的连接上回复或发送数据给主机。

- 从机到主机的数据传输，不论是指示（Indication）还是通知（Notification），都需要正确的连接索引。
- 请检查各个从机中`uint16_t ble_gatts_noti_ind(uint8_t conn_idx, const ble_gatts_noti_ind_t *p_param)`函数的第一个参数是否和建连时的`conn_idx`保持一致。

