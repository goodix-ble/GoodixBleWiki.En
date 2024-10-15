## FAQ for I2C


### 1. During I2C transmission, the SDA is abnormal and is forced down all the time by the slave and cannot be recovered, what is the reason?

- Problem Analysis

    SCL is pulled high during the first half cycle of ACK and the host no longer pulls down SCL (e.g., the host generates a reset, peripherals are restored to their default state, etc. during this period, and a full CLK cannot be issued normally).

- Handling Methods
    1. counter-initialize I2C after the problem occurs.
    2. initialize the I2C SCL pin to a normal IO port.
    3. simulate the I2C SCL flip-flop, i.e., pull down and pull up for 9 cycles, with the flip-flop frequency not higher than that of normal I2C communication, refer to the following Code:

```c
    for(uint8_t i=0; i<9; i++)
    {
      app_io_write_pin(...,SET)
      delay_us(1);
      app_io_write_pin(...,RESET)
      delay_us(1); }
    }
```

4. Initialize I2C and check if it communicates normally.



### 2. During I2C transfer, SCL is abnormal and stuck at low level.

The following are common I2C SCL exception stuck at low level cases and solutions:

- Situation 1:
    - Slave must call the Receive function of I2C first. If the Master calls the I2C Transmit function first, it is equivalent to the Slave is not ready, according to the I2C protocol, the SCL will be pulled low at this time.

- Solution 1:
    - This cause is an application error. you need to ensure the timing of Master Transmit and Slave Receive.

 

- Scenario 2:
    - Bus Arbitration The I2C interface of the GR5515 is designed as a master-slave interface that allows multiple hosts to share a single I2C bus. the I2C interface continuously detects the levels and jumps of SCL and SDA when it is enabled. When a low level pulse (hardware interference) is detected on SCL or SDA, the bus is considered to have entered a busy state (this interference is equivalent to an additional Master). At this point the GR5515 considers the bus occupied and refuses to send signals to the bus.

- Solution 2:
    - Re-initializing I2C (initializing the I2C state machine) or sending another STOP signal (releasing the bus) solves the problem.

 

- Scenario 3:
    - Call the I2C initialization interface directly during normal transmission. In the process of transmitting data, the initialization interface is re-called, causing the transmission to be interrupted, but the actual transmission is not aborted, and the Slave is still receiving data, holding the SCL line, so that the next time the Master transmits data, it will find that the I2C is in the state of Active and returns Busy, causing the SCL to be stuck at a low level.

- Solution 3:
    - Call deinit() function before calling Init() function, the deinit() of I2C has been done to deal with this problem, in addition, you should avoid calling the initialization interface during transmission in the application process.



- Case 4:
    - In the normal transmission process, there are some abnormalities that can cause the I2C to be stuck at a low level (e.g. SCL suffers from noise). Previously, a customer encountered in the pressure test, occasionally I2C is stuck in the low level of the situation, about one day pressure test can be reproduced once.

- Solution 4:
    - By in the exception handling (to determine the return value of the send function is an exception), anti-initialization and then initialize the GR5515 I2C + reset the slave + GR5515 sends the STOP signal, the purpose of all these steps is to release the I2C bus. When an unknown exception occurs, it is recommended to add all the recovery methods first, and then find a suitable recovery method by combining them.
