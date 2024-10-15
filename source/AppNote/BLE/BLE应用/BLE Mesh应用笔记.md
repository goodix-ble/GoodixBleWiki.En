## BLE Mesh



### 1. Introduction to BLE Mesh Basic Concepts

- The BLE Mesh Profile specification defines the basic requirements to support an interoperable mesh networking solution for Bluetooth low power wireless technology.
- The Mesh Profile is a protocol based on the BLE Stack protocol.
- Mesh Stack is called Mesh Profile in V1.0 and Mesh Protocol in V1.1.Currently Goodix BLE Mesh supports Mesh Profile V1.0.
- Mesh Profile is divided into three roles, Provisioner, Unprovisioned device and Node.
  - The Provider is used to manage the conversion between Unprovisioned device and Node.
  - Unprovisioned devices are devices that are not connected to the mesh network.
  - Nodes are devices that are connected to the mesh network.
  - After the allocator allocates a mesh to an unallocated device, the unallocated device is transformed into a node.
- Mesh Stack usually refers to the part of Mesh Profile, while the user-oriented application part of Mesh is usually called Mesh Model.



### 2. BLE Mesh Application Notes

- Goodix BLE Mesh currently supports Mesh Profile V1.0, and the supported chips are GR533x series.
- The version of Mesh Model protocol supported by Goodix BLE Mesh is Mesh Model V1.0.
- The SDK for GR533x series supports all the base Models included in Mesh Model V1.0.
- In Goodix BLE SDK, the function of Mesh Profile has been realized and included in SDK Lib; Mesh Model is presented in the form of source code in SDK. Users can refer to the Model source code to implement customized Model functions.
- In the SDK package of GR533x series, the `SDK_Folder\projects\mesh` directory stores the Mesh projects, in which the SIG directory is the standard Model project defined by Mesh Model, and the Vendor directory is the Mesh custom Model project.
- The custom model can be realized by modifying the project in the Vendor directory. If you want to introduce a standard model, please refer to the SIG directory which has the implementation code for introducing multiple models.
- Goodix BLE Mesh provides Demo Android App as the mesh provisioning end (Provisioner), with the mesh project provided in the SDK, it can demonstrate the functions of mesh networking, mesh node control and so on, for users' development reference.
- Please contact FAE for the corresponding SDK version and related information.



### 3. FAQ

#### 3.1 Where can I find the introduction of Mesh principle and protocol?

**A**: Please refer to [official website protocol list](https://www.bluetooth.com/specifications/specs/?types=all), Mesh Model, Mesh Profile/Mesh Protocol.



#### 3.2 Are BLE legacy features and BLE Mesh already included in the BLE stack library file? Or is BLE Mesh a separate protocol stack library file? Is there some documentation and information related to BLE Mesh development?

**A**: BLE Mesh software stack is built on top of low-power Bluetooth technology and communicates based on the low-power Bluetooth stack. Goodix BLE chips support BLE Mesh, and the `GR533x_Mesh_SDK` development kit is currently available for support, please contact FAE to provide the specific development kit.



#### 3.3 How many operating modes does GR533x Mesh low power support? What is the power consumption of different operating modes?Does GR533x support specific micro-operating system?

**A**: Depending on the power supply and processing capability, nodes can serve the following roles: relay node, low power node, friend node, and agent node. Different node current consumption is recommended to be measured using the SK development board based on the application settings.

The GR533x SDK provides FreeRTOS sample projects. In addition, other RTOS supporting Cortex M4 platform can be easily ported to GR533x.



#### 3.4 What is the maximum number of BLE nodes that can be connected to the mesh? Is there any kind of mesh topology, or is it just a star structure?

**A**: BLE Mesh network theoretically supports up to 32,767 nodes. In BLE Mesh networking, network flooding is used and message propagation is multi-path in nature, so a failure at a single point in the network will not fatally affect the entire network transmission. This makes the network more reliable as compared to star network. Refer to the official website article: [mesh-in-large-scale-network](https://www.bluetooth.com/blog/mesh-in-large-scale-networks/).



#### 3.5 Is there a Goodix Mesh SDK application development brief?

**A**: Please refer to: [GR533x SDK Mesh Application Profile](https://developers.goodix.com/zh/bbs/blog_detail/11d69fb8aff346de99a8010377d5cb93).