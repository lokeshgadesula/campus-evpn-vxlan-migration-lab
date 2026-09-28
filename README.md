# Campus EVPN-VXLAN Migration & Micro-Segmentation Deployment
Synthetic 2-spine/12-leaf EVPN-VXLAN architecture lab with CORP/IOT/GUEST VRFs, L2/L3 VNIs, BFD uplinks, Type-2/Type-5 design intent, Docker, CI and validation tests.

The repository proves **12-leaf configuration/design coverage**, not deployment to twelve physical switches. BFD timers are modeled; claim **sub-second convergence** only after measuring an actual emulator/lab failure and recovery below 1000 ms.
