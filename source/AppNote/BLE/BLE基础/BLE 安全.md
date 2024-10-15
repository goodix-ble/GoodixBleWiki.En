## BLE Security



### 1. Introduction to basic BLE SM concepts

- BLE SM defines protocols and behaviors to manage pairing, authentication, and encryption between low-power Bluetooth devices.
- The pairing process is a series of mutual authentication and confirmation processes performed by two unfamiliar devices according to their own security configurations after they establish a connection.
- After the pairing process is completed, it can ensure that the subsequent data interactions of the current connection are carried out under its own recognized security environment, preventing important data from being stolen by a third party.
- In the pairing process, you can choose whether to bind the current device or not. After the binding is completed, the secret key and feature values of the current device are saved until the binding is lifted or overwritten.
- During the pairing process, the current connection is encrypted, and the encryption behavior continues until the connection is disconnected.
- During the pairing process, based on the security configuration, the two connected devices distribute secret keys to each other, which are used in subsequent scenarios such as link encryption, data authentication, and address resolution.
- Devices that have completed pairing and are bound to each other will use the previously distributed secret keys to directly encrypt the link in subsequent reconnections.
- The pairing process is categorized into `LE legacy pairing` and `LE Secure Connections pairing`.
- `LE legacy pairing` is the most widely used and the most stable pairing process, and we recommend this pairing process.
- `LE Secure Connections pairing` has a higher security level due to different pairing process and algorithm, but it doesn't work properly on most Android phones.
- For conceptual details, please refer to the Bluetooth specification “[Core Specification 5.4](https://www.bluetooth.com/specifications/core54-html/)” “Part H: Security Manager Specification”.



### 2. GR5xx BLE SM Application Notes

- To enable encrypted pairing, the privacy policy `uint16_t ble_gap_privacy_params_set(uint16_t renew_dur, bool enable_flag)` should be set first, e.g. `ble_gap_privacy_params_set(900, true)` .
- LE legacy pairing security configuration, refer to SDK project `SDK_Folder\projects\ble\ble_peripheral\ble_app_hrs`, API: `ble_sec_params_set ` entry parameter configuration.
- LE Secure Connections pairing usage requires the entry parameter of interface `uint16_t ble_sec_params_set(ble_sec_param_t *p_sec_param)` to be set to: `p_sec_param->level` is greater than or equal to `BLE _SEC_MODE1_LEVEL2`, the `p_sec_param->auth` field is set to `BLE_SEC_AUTH_SEC_CON`, and the other parameters refer to the LE legacy pairing security configuration.
- BLE can utilize the BLE process to generate the BT Link Key under the premise of using LE Secure Connections pairing. refer to [BLE Generate Link key usage instructions (for GR5525/GR5526/GR533x)](https://developers. goodix.com/zh/bbs/blog_detail/58dd05d850bf47b8972f8ef3d146713d). Configurations may vary slightly from platform to platform.
- If you initiate the pairing process, you need to call the interface `uint16_t ble_sec_enc_start(uint8_t conn_idx)`.
- On the Apple phone side, the App does not initiate the BLE pairing interface, you need to call the interface `uint16_t ble_sec_enc_start(uint8_t conn_idx)` on the device side to initiate the pairing process. The app for Android phones does not have this issue.
- For whitelisting and how to use privacy, please refer to [How to enable whitelist filtering mechanism for GR551X Bluetooth app development](https://developers.goodix.com/zh/bbs/detail/7b5e08fd60234fc8b7d10e2cb34a6f90).



### 3. FAQ

#### 3.1 There is a problem with BLE pairing, what should I do to solve it?

**A**: If there is a pairing problem, it can be handled as follows:

1. Prioritize checking if pairing is turned on `ble_gap_pair_enable(true)`.

2. check if the privacy policy `ble_gap_privacy_params_set` is configured to `true`.

3. Apple application, need device side to actively call interface `ble_sec_enc_start` to initiate pairing process.

4. For the configuration of security parameters, it is recommended to prioritize and refer to the forum question [BLE pairing of some phones pairing will show 0x03 error](https://developers.goodix.com/zh/bbs/detail/2039bcd4ef2941deaa289ff5968a95a8 “BLE pairing of some phones Pairing will show 0x03 error").

5. In case of LE Secure Connections pairing, please check whether the phone supports this pairing mode.



#### 3.2 BLE Bluetooth connection, how to connect directly without prompting pairing request?

**A**: There are two scenarios:

- If you use the Bluetooth in the settings of the phone to connect, then there should be no way, because for the Bluetooth in the settings, the App needs to be paired, otherwise the connection will be disconnected. 
- If it is a third party's own developed app, then it mainly depends on the logic of the app side.



#### 3.3 Which part of the code in the routine ble_app_hids_keyboard knows the Bluetooth pairing code? How to enter the Bluetooth pairing code? The key pairing routine?

**A**: `ble_sec_params_set(&sec_param)` entry, `sec_param.io_cap` selects the selection with KEYBOARD CAPABILITY, i.e., `BLE_SEC_IO_KEYBOARD_ONLY` or `BLE_SEC_IO_ KEYBOARD_DISPLAY`, a password may be required.

- In the example project `ble_app_hids_keyboard`, the password is entered by Uart, i.e. `app_uart_evt_handler` where `pair_code` is the password.
- Refer to `uint16_t ble_sec_enc_cfm(uint8_t conn_idx, const ble_sec_cfm_enc_t *p_cfm_enc)` for the part of the call.
- The reference code is below:

````
cfm_enc.req_type = BLE_SEC_TK_REQ;
cfm_enc.accept = true;
memset(cfm_enc.data.tk.key, 0, 16);
cfm_enc.data.tk.key[0] = (uint8_t)((pair_code & 0x000000FF) >> 0); cfm_enc.data.tk.key[0] = (uint8_t)((pair_code & 0x000000FF) >> 0);
cfm_enc.data.tk.key[1] = (uint8_t)((pair_code & 0x0000FF00) >> 8);
cfm_enc.data.tk.key[2] = (uint8_t)((pair_code & 0x00FF0000) >> 16);
cfm_enc.data.tk.key[3] = (uint8_t)((pair_code & 0xFF000000) >> 24);
ble_sec_enc_cfm(now_connect_indx, &cfm_enc);
```



#### 3.4 Every time the device connects, the pairing box pops up, and it is reasonable to say that only the first pairing will pop up the box, but not the subsequent ones. How to solve this problem?

**A**: The cause of this problem should be: the security parameters are configured without opening the binding. To solve this problem, you need to set `BLE_SEC_AUTH_BOND` in the security parameter configuration *sec_param.auth* to 1.



#### 3.5 How to prevent GR5xx Bluetooth peripheral from being captured? How is the communication data encrypted?

**A**: Enabling Bluetooth pairing and encrypting through the link can effectively prevent the data from being eavesdropped. Refer to the example project `SDK_Folder\projects\ble\ble_peripheral\ble_app_hrs` or `SDK_Folder\projects\ble\ble_peripheral\ble_app_hids_keyboard`.



#### 3.6 How to get the MAC address of the opposite device (e.g. cell phone) after pairing?

**A**: After binding, you can call `ble_gap_bond_dev_addr_get` to get the address of the opposite end.



#### 3.7 After device bonding, the iOS device address will change, how to make sure the device with changed address can connect?

**A**: The cell phone side usually connects with a random address (which changes every time), and the identity address (which is fixed and unchanged) is distributed during the pairing and binding process.

- During the subsequent reconnection process, the random address on the cell phone side will be parsed out by irk to get the corresponding identity address. The identity address will be used to find the binding information and encrypt the link, and then the connection will be successful.
- The security parameter configuration of the device needs to bind and distribute ltk and irk, and also needs to enable privacy.



