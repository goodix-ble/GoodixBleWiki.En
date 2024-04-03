## Memory常见问题



### 1. Keil怎么限制编译固件大小?

- 可以修改固件加载域的最大大小，如GR551x可在`flash_scatter_config.h`文件修改`FLASH_SIZE`的大小，从而限制固件的大小，当固件大于此值时，ARMCC链接器会报以下错误：
    ```
    .\Objects\ble_app_cts.axf: Error: L6220E: Load region LR_FLASH size (84604 bytes) exceeds limit (4096 bytes). Region contains 263 bytes of padding and 910 bytes of veneers (total 1173 bytes of linker generated content).
    Finished: 0 information, 0 warning and 1 error messages.
    ".\Objects\ble_app_cts.axf" - 1 Error(s), 0 Warning(s).
    ```



### 2. 怎么把一个变量固定在指定地址?

- 可参考SDK怎么把变量```BUILD_IN_APP_INFO```固定在指定的地址；
- 但是在固定地址的时候，不要和SDK内部的地址空间冲突，SDK Flash和SRAM布局详情见对应芯片开发者指南，如GR551x的Flash和SRAM布局可参考：https://docs.goodix.com/zh/online/detail/developer_guide_bl_b/V1.0/07010db64eec6b3d6fc75a8407382a46