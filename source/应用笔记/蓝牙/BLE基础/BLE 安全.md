## BLE安全



### 1. BLE SM基本概念介绍

- BLE SM定义了协议和行为来管理低功耗蓝牙设备之间的配对、认证和加密。
- 配对流程，是指两个陌生设备建立连接后，根据自身安全配置，进行的一系列相互验证确认的流程。
- 配对流程完成后，可以确保当前连接后续数据交互在自身认可的安全环境下进行，防止重要数据被第三方窃取。
- 配对流程中，可以选择是否对当前设备进行绑定。绑定完成后会对当前设备的秘钥和特征值进行保存，直到绑定解除或是被重新覆盖。
- 配对流程中，会对当前连接进行加密，本次加密行为会持续到本次连接断开。
- 配对流程中，根据安全配置，两个连接的设备会向对方分发秘钥，这些秘钥用于后续链路加密、数据鉴权以及地址解析等场景。
- 已完成配对并且相互绑定的设备，在后续的重新连接中，会使用之前分发的秘钥直接对链路进行加密。
- 配对流程，分为`LE legacy pairing`和`LE Secure Connections pairing`两种。
- `LE legacy pairing`是应用最广泛，同时也是目前最稳定的配对流程，目前我们推荐这种配对流程。
- `LE Secure Connections pairing`由于配对流程和算法不同，安全等级更高，但是在大部分Android手机上无法正常使用。
- 概念细则，请参考蓝牙规范《[Core Specification 5.4](https://www.bluetooth.com/specifications/core54-html/)》 “Part H: Security Manager Specification”。



### 2. GR5xx BLE SM应用笔记

- 如需启动加密配对，应先设置隐私策略`uint16_t ble_gap_privacy_params_set(uint16_t renew_dur, bool enable_flag)`，例如`ble_gap_privacy_params_set(900, true)`。
- LE legacy pairing安全配置，可参考SDK工程`SDK_Folder\projects\ble\ble_peripheral\ble_app_hrs`，API: `ble_sec_params_set `入参配置。
- LE Secure Connections pairing使用方法，需要将接口`uint16_t ble_sec_params_set(ble_sec_param_t *p_sec_param)`的入参设置为：`p_sec_param->level`大于或等于`BLE_SEC_MODE1_LEVEL2`，`p_sec_param->auth`字段置位`BLE_SEC_AUTH_SEC_CON`，其他参数参考LE legacy pairing安全配置。
- BLE在使用LE Secure Connections pairing的前提下，可以利用BLE流程生成BT Link Key。参考[BLE生成Link key使用方法说明（适用于GR5525/GR5526/GR533x）](https://developers.goodix.com/zh/bbs/blog_detail/58dd05d850bf47b8972f8ef3d146713d)。不同平台配置可能略有不同。
- 如果主动发起配对流程，需要调用接口`uint16_t ble_sec_enc_start(uint8_t conn_idx)`。
- 在Apple手机端，App没有主动发起BLE配对接口的情况下，需要设备端主动调用接口`uint16_t ble_sec_enc_start(uint8_t conn_idx)`，才能发起配对流程。而Android手机的App不存在该问题。
- 白名单以及隐私使用方式，请参考[GR551X 蓝牙应用开发如何开启白名单过滤机制](https://developers.goodix.com/zh/bbs/detail/7b5e08fd60234fc8b7d10e2cb34a6f90)。



### 3. FAQ

**Q**：BLE配对有问题，应该如何解决？

**A**：如果存在配对问题，可按以下方法处理：

1. 优先检查是否打开配对`ble_gap_pair_enable(true)`。

2. 检查隐私策略`ble_gap_privacy_params_set`是否配置为`true`。

3. Apple应用，需要设备侧主动调用接口`ble_sec_enc_start`，才能发起配对流程。

4. 安全参数的配置，建议优先参考论坛问题[BLE配对部分手机配对会出现0x03错误](https://developers.goodix.com/zh/bbs/detail/2039bcd4ef2941deaa289ff5968a95a8 "BLE配对部分手机配对会出现0x03错误")。

5. 如果是LE Secure Connections pairing，请确认手机是否支持该配对模式。

**Q**：BLE蓝牙连接，怎么直接连接不需要提示配对请求？

**A**：有以下两种情形：

- 如果使用手机设置中的蓝牙进行连接，那么应该是没有办法的，因为对于设置中的蓝牙，App是需要配对的，否则连接会断开。 
- 如果是第三方自己开发的App，则主要取决于App端的逻辑。

**Q**：在例程ble_app_hids_keyboard中哪部分代码知道蓝牙配对码？如何输入蓝牙配对密码？密钥配对的例程？

**A**：`ble_sec_params_set(&sec_param)`入参中，`sec_param.io_cap`选择带有keyoard capability的选择，即`BLE_SEC_IO_KEYBOARD_ONLY`或`BLE_SEC_IO_KEYBOARD_DISPLAY`，可能会需要输入密码。

- 在示例工程 `ble_app_hids_keyboard`中，密码由Uart输入，即`app_uart_evt_handler`中 `pair_code`为密码。
- 参考 `uint16_t ble_sec_enc_cfm(uint8_t conn_idx, const ble_sec_cfm_enc_t *p_cfm_enc)` 调用的部分。
- 参考代码如下：

````
cfm_enc.req_type = BLE_SEC_TK_REQ;
cfm_enc.accept   = true;
memset(cfm_enc.data.tk.key, 0, 16);
cfm_enc.data.tk.key[0] = (uint8_t)((pair_code & 0x000000FF) >> 0);
cfm_enc.data.tk.key[1] = (uint8_t)((pair_code & 0x0000FF00) >> 8);
cfm_enc.data.tk.key[2] = (uint8_t)((pair_code & 0x00FF0000) >> 16);
cfm_enc.data.tk.key[3] = (uint8_t)((pair_code & 0xFF000000) >> 24);
ble_sec_enc_cfm(now_connect_indx, &cfm_enc);
```



**Q**：设备每次连接，都会弹出配对框，按理说只有第一次配对会弹框，后面就不会弹框了。请问这个问题如何解决？

**A**：导致该问题的原因应该是：安全参数配置时没有打开绑定。解决该问题，需将安全参数配置*sec_param.auth*中的`BLE_SEC_AUTH_BOND`置为1。

**Q**：请问GR5xx蓝牙外设如何防止被抓包？通讯数据如何加密？

**A**：开启蓝牙配对，通过链路加密，即可有效防范数据被窃听。参考示例工程`SDK_Folder\projects\ble\ble_peripheral\ble_app_hrs`或 `SDK_Folder\projects\ble\ble_peripheral\ble_app_hids_keyboard`。

**Q**：配对后，如何获取对端设备（如手机）的MAC地址？

**A**：绑定后，可调用`ble_gap_bond_dev_addr_get`获取对端地址。

**Q**：设备绑定后，iOS设备地址会发生变化，如何保证更改地址的设备能连接上？

**A**：手机端通常是用随机地址（每次均会改变）进行连接，在配对绑定过程中会分发身份地址（固定不变的）。

- 在后续回连过程中，手机端的随机地址会被irk解析出来，获取到对应的身份地址。通过身份地址查找到绑定信息进行链路加密，即可回连成功。
- 设备端的安全参数配置需要绑定并分发ltk和irk, 同时需要开启隐私。




