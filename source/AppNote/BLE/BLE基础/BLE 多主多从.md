## BLE多主多从 (Multi Role)


### 1. GR5xx多主多从基本概念介绍

1. BLE主从设备简介
    - BLE通用属性规范`GATT (Generic Attribute Profile)`定义了两个设备之间的数据通信。当两个设备处于连接状态时，一个设备作为`GATT服务端（从设备或从机）`，另一个设备作为`GATT客户端（主设备或主机）`。
    - GATT客户端：设备发起命令、请求，并接收响应、通知和指示。
    - GATT服务端：设备接收命令、请求，并发送响应、通知和指示。
    - BLE设备可以同时担当主机和从机两种角色，这一功能被称为`多主多从(Multiple Roles)`。
    - 单个BLE设备可开启这种模式，即**主从一体**。它具有主机和从机的双重身份，可以作为主机搜索、连接和管理其他BLE从机，同时也能以从机的身份被其他BLE主机设备发现、连接和管理。
    - 关于多主多从涉及到的`GAP与GATT`内容细节，请参考《[GR551x BLE Stack用户指南](https://docs.goodix.com/zh/online/detail/gr55xx_ble_stack_user_guide)》。
2. GR5xx多主多从简介
    - GR5xx多主多从以BLE主从设备为基础，能够在单颗SoC上实现多角色（从机Peripheral & 主机Central）、多连接的应用场景。
    - GR5xx主机支持的功能：
        - 扫描：主机可以不断扫描并监听外围设备的广播，搜索、发现和筛选周边设备。
        - 发起连接：主机可以对选定的从机发起连接请求，并与之建立一个或多个连接。
        - GATT Client：主机作为GATT客户端的角色，通过读取、写入服务端的特性来控制从机或与之交换数据。
        - 连接管理：主机负责与多个从机的连接管理，用户可以针对不同从机开发定制化功能。
        - 连接参数更新：主机可以修改当前连接的参数，提升通信效率或降低功耗。
    - GR5xx从机支持的功能：
        - 广播：从机设置包含特定广告数据（如设备名称、服务和功能）的广播包，并发起周期性广播。
        - 接受扫描并响应连接：从机可以被主机扫描、发现并被请求连接。
        - GATT Server：从机作为GATT服务端的角色，定义了BLE设备提供的服务和特性，允许主机读取或写入。
        - 数据上报：从机通过向主机发送Notification或Indication消息，主动发送数据。
        - 连接参数更新请求：从机可以请求主机更改现有的连接参数，以优化传输效率和功耗。
3. GR5xx多主多从应用场景
    - 典型应用场景：带有健康跟踪功能的智能手表可作为BLE主机收集其他多个穿戴设备，比如胸带心率血氧传感器的数据；与此同时，也可作为从机将数据同步至用户手机App。
    - 其它应用场景包括不限于：
        - 运动和健康追踪设备
        - 智能穿戴设备
        - 智能家居
        - 物联网（IoT）网关



### 2. GR5xx多主多从应用笔记

- 多主多从：
    - 可参考SDK示例工程`SDK_Folder\projects\ble\ble_multi_role\ble_app_hrs_rscs_relay`。
    - 该工程演示了将GR5xx芯片应用于多角色、多连接的场景，实现了心率传感器和跑速与步频传感器中继设备功能。
- 主从一体：
    - 可参考SDK工程`SDK_Folder\projects\ble\ble_multi_role\ble_app_uart_multi_link`。
    - 该工程演示了将单个GR5xx芯片同时作为主机和从机，支持一主多从的功能。
- 多主多从的多角色场景下，**主机**功能实现的方法：
    - 设置扫描参数并开启传统或扩展扫描，扫描流程的实现请参考[蓝牙连接后开启主动扫描示例说明](https://developers.goodix.com/zh/bbs/blog_detail/dc587d956a1a431c9021d6a9be8c52cb)。
    - 当扫描到目标设备后，设置合理的连接参数，主动发起扩展连接（BT Core Spec 5.0及以上）流程或传统连接流程。
    - 连接设备成功，在协议栈`BLE_GAPC_EVT_CONNECTED`回调中可发现对端从机的主要服务和特征。
    - 服务发现完成，通过写入对端的CCCD特征配置值使能通知功能，执行GATT客户端（主机）Write下发消息的过程。
    - 主机还需要处理从机发送的`ATT_WRITE_RSP`数据包和发过来的通知消息。
- 多主多从的多角色场景下，**从机**功能实现的方法：
    - GATT服务端（从机）包含一个或多个BLE Profile来实现特定的蓝牙功能。添加自定义Service，请参考《[GR5xx应用及自定义Sample Service](https://docs.goodix.com/zh/online/custom_sample_service_bl)》。
    - 设置广播数据、扫描响应数据、参数和模式，开启广播。
    - 从机处理主机的读写请求。详细内容，请参考《[GR551x BLE Stack用户指南](https://docs.goodix.com/zh/online/gr55xx_ble_stack_user_guide)》。
    - 从机可使用`uint16_t ble_gatts_noti_ind(uint8_t conn_idx, const ble_gatts_noti_ind_t *p_param)`函数主动发送“通知"和"指示"给主机。



### 3. FAQ

**Q**：GR5xx设计主从一体的应用场景时，最大可支持多少个连接呢？

**A**：GR5xx系列芯片最多可以同时支持12个activity（资源业务）。一个可扫描的广播占用2个activity，不可扫描广播占用1个activity，连接占用1个activity。通过宏`CFG_MAX_CONNECTIONS`可配置最大连接数为1～10。

举例说明：
- 在无广播业务时，最多可支持10个连接。
- 在2个可扫描的广播业务时，最多可支持 12 - 2 * 2 = 8个连接。
- 在1个扫描和1个普通广播业务时，最多可支持10个连接。

**Q**：在ble_app_uart_multilink主从一体示例中，如何区分从机？怎么修改默认连接的从机设备设置？

**A**：在示例工程中，首先通过协议栈`BLE_GAPM_EVT_ADV_REPORT`回调过滤扫描到的广播包，确认其携带数据是否符合规范；然后使用已有的MAC地址（参见`first_slave_target_addr`数组）与Slave地址进行对比，若是期望的地址，则进行连接。

- 如果要区分从机，可在连接回调函数的连接参数中获取配对从机地址，使用`conn_idx`进行从机的分辨。
- 详细业务，请参考`void app_connected_handler(uint8_t conn_idx, const ble_gap_evt_connected_t *p_param)`函数。

**Q**：BLE多业务场景下开启广播或扫描失败的常见问题分析。

用户在开发过程中可能经常会遇到一些多业务场景下，协议栈报错的问题。例如以下场景：

- 广播开启成功之后，再去开启扫描，结果扫描开启失败。

- 建立连接之后，再开启广播，结果广播开启失败。

- 建立连接之后，再开启扫描，结果扫描开启失败。

**A**：详细解决方法，请参考[BLE 多业务场景下开启失败的常见问题分析](https://developers.goodix.com/zh/bbs/blog_detail/213844795e8a45d59a4501fa80d519c4)。

**Q**：在一主多从场景下，一对一设备主从通信没有问题，但一对十设备主从通信时，通过conn_idx向从机逐一发送命令，在数据量很大的情况下从机无法接收到数据，这是因为蓝牙传输调度的问题吗？

**A**：这可能是连接参数配置不合理导致的，请参考如下建议进行调整，配置详情参考[多连接参数优化说明](https://developers.goodix.com/zh/bbs/detail/87e8f3be6c9b464496381ac8f8ff4893)：

- 请确保CE_LEN之和小于CI_Min。
- 考虑到精度转换以及扩窗机制，配置Slave设备的CE_LEN应当保留一定的裕量，建议比理论值至少小2.5 ms。例如，若CE_LEN可配的理论值为100 ms，则实际应配置成为97.5 ms。
- 请确保各链路CI成倍数关系。
- 根据各条链路的传输数据量配置合适的CE_LEN，以调整各链路在CI_Min内所占带宽。

