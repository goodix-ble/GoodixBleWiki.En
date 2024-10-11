## Usage of J-Link RTT


### 1. How to turn on the RTT function in the sample project

- Make sure that the file ${ SDK } \ external \ segger _ RTT \ SEGGER _ RTT. C is added to the project compilation.

- Change the macro APP _ LOG _ PORT value of the project profile _ custom _ config. H _ to 1.


  ```c
  // <o> APP log port type
  // <0=> UART
  // <1=> RTT
  // <2=> ITM
  #ifndef APP_LOG_PORT
  #define APP_LOG_PORT            1
  #endif
  ```

- Make sure that the function BSP _ log _ init in the file ${ SDK } \ platform \ boards \ board _ SK. C is called when the main peripheral is initialized (or make sure that the board _ init function of the sample project is called, which calls the BSP _ log _ init). Because the initialization of RTT function in SDK is placed in the function BSP _ log _ init.



### 2. The Skill of Obtaining the Compiler Address of _ SEGGER _ RTT;

- When using J-Link RTT, the address of the _ SEGGER _ RTT will be filled in, one is to fill in the scope tool for automatic search, and the other is to fill in the fixed address. This article introduces the second method:

  - First refer to the above to open the RTT function, and then compile the project.

  - After the compilation is completed, open the.map file to search for the variable address of the _ SEGGER _ RTT. The reference is as follows:


    ```c
    _SEGGER_RTT      0x2000c220   Data     120  segger_rtt.o(.bss)
    ```

  - Modify the definition of variables in the _ SEGGER _ RTT. C _, use the attribute at attribute to fix the variable address of the map file, so that the variable address of the subsequent _ SEGGER _ RTT will not change with the increase of engineering functions and variables.


    ```c
    SEGGER_RTT_CB _SEGGER_RTT __attribute__ ((at(0x2000c220))); 
    ```



### 3. When J-Link RTT prints the log, the log will not be printed after working for a while

- Check whether it works in Sleep mode. RTT is a non-AON module and is not friendly to Sleep mode support. Please use RTT in Active mode of the chip.

- If the RTT log stops printing in the Active mode, try to modify the RTT working mode to the SEGGER _ RTT _ MODE _ BLOCK _ IF _ FIFO _ FULL blocking mode. If it works normally, try to adjust the size of the RTT buffer.


  ```
  #define SEGGER_RTT_MODE_DEFAULT                   SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL 
  ```

  
