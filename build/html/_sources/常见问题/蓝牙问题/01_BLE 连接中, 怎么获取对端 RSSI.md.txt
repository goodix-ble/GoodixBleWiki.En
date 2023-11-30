# BLE 连接中, 怎么获取对端 RSSI?

- 适用芯片

| GR551x | GR5525 | GR5526 | GR533x |
| ------ | ------ | ------ | ------ |
| YES    | YES    | YES    | YES    |



1. 调用接口 ble_gap_conn_info_get(uint8_t conn_idx, ble_gap_get_conn_info_op_t opcode); opcode 支持 **BLE_GAP_GET_CON_RSS**I,    BLE_GAP_GET_CON_CHANNEL_MAP,    BLE_GAP_GET_PHY,   BLE_GAP_GET_CHAN_SEL_ALGO
2.  然后关注回调 app_gap_connection_info_get_cb

```c
static void app_gap_connection_info_get_cb(uint8_t idx, uint8_t status, const gap_conn_info_param_t * p_conn_info) {
    if(BLE_SUCCESS == status && GAP_GET_CON_RSSI == p_conn_info) {
    	// GET p_conn_info->info.rssi
    }
}
```

