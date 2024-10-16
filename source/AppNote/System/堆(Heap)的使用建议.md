## Suggestions for the use of Heap

In Goodix Bluetooth LE SDKs, there are the following heap managers, which can be used by the application layer according to the business needs.

| Heap Type | Description | General Suggestions | Usage Scope |
| ---------------- | ------------------------------------------------------------ | ---- | ---- |
| std   malloc     | Derived from the standard library provided by the compiler, it can be configured and enabled via SYSTEM_HEAP_SIZE  | recommended not to enable it in OS environments, and to use the OS Heap | all SoCs |
| FreeRTOS Heap    | Heap Manager by FreeRTOS                                            | under FreeRTOS | all SoCs |
| app_memory.c/.h  | simple heap management                   | Not recommended | Not recommended  |
| app_graphics_mem | For GR5526 only, the application's unused SRAM and PSRAM are synthesized into a Heap for management. | Recommended for Graphics and large block data caching scenarios, power down processing when hibernating | GR5526 |

- The standard library heap manager is not normally prioritized, but can be enabled as appropriate if the application algorithms require exclusive memory heap blocks or if there are special execution requirements.

- In addition, users can introduce other suitable heap managers on their own.

