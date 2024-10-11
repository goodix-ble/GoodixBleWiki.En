## FAQ for Memory 



### 1. How does Keil limit the compiled firmware size?

- You can modify the maximum size of the firmware load domain, such as the size that GR551x can modify `FLASH_SIZE` in the _ flash _ scatter _ config. H _ file, to limit the size of the firmware. When the firmware is greater than this value, the ARMCC linker reports the following error:

    ```
    .\Objects\ble_app_cts.axf: Error: L6220E: Load region LR_FLASH size (84604 bytes) exceeds limit (4096 bytes). Region contains 263 bytes of padding and 910 bytes of veneers (total 1173 bytes of linker generated content).
    Finished: 0 information, 0 warning and 1 error messages.
    ".\Objects\ble_app_cts.axf" - 1 Error(s), 0 Warning(s).
    ```



### 2. How to fix a variable at a specified address?

- You can refer to how the SDK fixes the variable ```BUILD_IN_APP_INFO```at the specified address.
- However, when the address is fixed, it should not conflict with the address space inside the SDK. For details of the layout of SDK Flash and SRAM, see the corresponding chip developer guide. For example, for the layout of Flash and SRAM of GR551x, please refer to [GR551x Developer's Guide](https://docs.goodix.com/zh/online/gr551x_develop_guide/V2.7)the sections "Flash Memory Mapping" and "RAM Memory Mapping".


