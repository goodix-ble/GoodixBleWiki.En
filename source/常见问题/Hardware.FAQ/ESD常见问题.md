## FAQ for ESD



### 1. Why is the system-level ESD performance degraded when IO pins are near the edge of the PCB?
* Ground path instability: If the IO pin is close to the edge of the PCB, the ground path may become unstable, which increases the uncertainty of the ground loop, resulting in the current can not effectively flow back through the ground loop when ESD events occur, which reduces the ESD protection performance.
* ESD leakage path: IO pins near the edge of the PCB may increase the length of the ESD leakage path, so that the leakage current during ESD impact cannot be discharged quickly, which affects the ESD performance.
* EMI/EMC effects: IO pins near the edge of the PCB are more susceptible to external electromagnetic interference (EMI) and electromagnetic compatibility (EMC). These EMI/EMC disturbances may affect the normal operation of IO pins, resulting in poor ESD performance, especially sensitive signals that are susceptible to interference, such as clock, reset, and so on.
* Therefore, in PCB design, it is recommended that the communication signal network should be laid out in the middle layer of the PCB as far as possible and shielded with GND. In particular, sensitive signals that are vulnerable to interference should not be routed close to the edge of the PCB, and it is recommended to wrap the ground to ensure a stable grounding path, reduce the ESD leakage path, and reduce the impact of external interference on IO pins, so as to improve the ESD protection performance.















