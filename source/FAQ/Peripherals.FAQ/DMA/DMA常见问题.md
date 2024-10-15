

## FAQ for DMA

### 1. DMA transfers use the concept of beat, what is a beat?

- Beat is a term commonly used at IC level to indicate the bit width used for a single data access, which is generally 8bit, 16bit, 32bit in embedded field, corresponding to the basic data types of char, short and int (32bit) in C program. If the access data bit width is 8bit (char), one bit is used to access the data, and one bit is used to access the data. 
    - If the access data bit width is 8bit (char), 1 beat corresponds to a data length of 1 byte.
    - If the access data bit width is 16 bit (short), the length of the data is 2 bytes per beat.
    - If the access data bit width is 32bit (int), the length of data for 1 beat is 4 bytes.



### 2. Can the same DMA channel of the same DMA instance be configured for use by different peripherals at the same time?

- No. Only DMA instances and channels configured as Memory to Memory can be used between various Memories (such as SRAM, PSRAM, and NOR Flash address spaces that have completed Memory Mapped configuration).
- In other DMA transfer modes, the current driver framework does not support assigning the same channel of the same DMA instance to different peripherals at the same time; however, it can be used in a time-sharing manner, with initialization and de-initialization of the peripheral and the DMA before and after each use (this is not recommended unless there are not enough DMA channels to go around, as it can easily lead to a bug if you are not familiar with the situation).
