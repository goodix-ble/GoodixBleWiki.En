## BLE Broadcasting


### 1. Introduction to the basic functions of BLE broadcasting
- It is used to inform other devices that they have discovered their presence. Among them, traditional broadcast sends broadcast packets on channels 37, 38 and 39; extended broadcast can send broadcast packets on the remaining 37 channels.
- The maximum application data length of a traditional broadcast packet is 31 Bytes, and a three-byte ADV Flag is added by default in the SDK, so the length available to the user is 28 Bytes.
- Extended Broadcast can transmit 254 Bytes of broadcast data.
- The broadcast interval can be set in the range of 20 ms ~ 10.24 s. The broadcast channel can be set individually in the range of 37 Bytes.
- Broadcast channels can be set individually to broadcast on channels 37, 38 or 39, or you can choose to cull a channel and broadcast on the remaining two channels.
- Broadcast can be turned on manually. After the broadcast is turned on, trigger the callback event `BLE_GAPM_EVT_ADV_START` to check whether the broadcast is turned on successfully by status.
- Broadcast can be stopped manually or automatically by setting a timeout period. After the broadcast stops, trigger the callback event `BLE_GAPM_EVT_ADV_STOP` to see if the broadcast stops successfully by status.



### 2. Broadcast Application Notes

- The broadcast mode (adv_mode) usually uses the non-directional scannable mode `BLE_GAP_ADV_TYPE_ADV_IND`. For other mode usage scenarios, refer to the LE Broadcast chapter in [Core Specification 5.4](https://www.bluetooth.com/specifications/core54-html/).
- The broadcast discovery mode (disc_mode) typically uses the general discoverable mode `BLE_GAP_DISC_MODE_GEN_DISCOVERABLE`. For other mode usage scenarios, refer to the LE Broadcast chapter in [Core Specification 5.4](https://www.bluetooth.com/specifications/core54-html/).
- For the usage of broadcast whitelist, please refer to `SDK_Folder\projects\ble\ble_peripheral\ble_app_hids_keyboard` project.
- Broadcast data needs to be placed in LTV format, i.e. 1 Byte Length, 1 Byte Type, N Byte data. For example, {0x0b, BLE_GAP_AD_TYPE_COMPLETE_NAME, 'G', 'o', 'o', 'd', 'i', 'x', '_', 'H', 'R', 'M',} .
- In the Broadcast parameter, you can set the broadcast duration duration. when duration is set to 0, the broadcast will stay on and need to be turned off manually; and when duration is set to any other value, the broadcast will be stopped automatically at the end of the duration.
- GR551x can turn on up to 5 broadcasts at a time, GR5526 can turn on up to 4 broadcasts at a time, and GR5525 and GR533x can turn on up to 2 broadcasts at a time.
- GR5xx broadcast channels support configuration of private channels. Please consult with FAE for the detailed configuration method.



### 3. FAQ

#### 3.1 Can the broadcast data be modified all the time?

  **A**: The broadcast data can be continuously modified and scanned for reply data via `ble_gap_update_adv_data`, and there is no need to stop broadcasting during this period. **It should be noted that `ble_gap_update_adv_data` must be called after the broadcast has been turned on successfully in order to be effectively modified. **

#### 3.2 How do I turn on two broadcasts at the same time?

  **A**: Turn on one broadcast when the other one is turned on successfully, i.e. turn on another broadcast with different adv_idx after receiving `BLE_GAPM_EVT_ADV_START` event. For specific method, please refer to `SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave` project.

#### 3.3 How to enable multi broadcast?

  **A**: refer to `SDK_Folder\projects\ble\ble_peripheral\ble_app_multi_slave` project while using random address

  `ble_gap_adv_param_set(uint8_t adv_idx, gap_own_addr_t own_addr_type, gap_adv_param_t* p_adv_param)` Configure the broadcast parameter with own_addr_type using the `BLE_GAP_OWN _ADDR_GEN_RSLV`.

#### 3.4 Is dynamic modification of the broadcast interval supported?

  **A**: dynamic modification is not supported. You must stop the broadcast to reset the broadcast parameters and then start the broadcast.

#### 3.5 How to set the broadcast power?

  **A**: After the broadcast is turned on successfully, call `ble_gap_tx_power_set()` to set it.

#### 3.6 How to set broadcast for HID device to make system bluetooth display device name?

  **A**: If you need to display the keyboard icon in Android system Bluetooth, add the descriptor `BLE_APPEARANCE_HID_KEYBOARD ` field in the broadcast package; if you need to display the device name in iOS system Bluetooth, add the descriptor `BLE_ATT_SVC_HID ` field in the broadcast package.

#### 3.7 How to set the broadcast packet can use 31 Bytes instead of 28 Bytes?

  **A**: Configuring `CFG_MAX_ADV_DATA_LEN_SUPPORT` to 1 and disc_mode to ` GAP_DISC_MODE_NON_DISCOVERABLE` removes the default 3 Bytes flag.