# Workstation Hardware Setup Instructions

This document outlines the recommended hardware specifications and setup instructions for your high-performance workstation required for the Physical AI & Humanoid Robotics course.

## Recommended Hardware

*   **GPU**: NVIDIA RTX 4070 Ti+ (RTX 3090/4090 preferred) for demanding simulations and AI workloads.
*   **CPU**: Intel Core i7 13th Gen+ / AMD Ryzen 9+ for robust multi-threaded performance.
*   **RAM**: 64GB DDR4/DDR5 RAM for large datasets and complex simulations.
*   **Storage**: 1TB NVMe SSD for fast loading times and ample storage for datasets and software.
*   **Operating System**: Ubuntu 22.04 LTS (64-bit).

## Setup Instructions

1.  **OS Installation**: Install Ubuntu 22.04 LTS. Ensure all system updates are applied.
2.  **NVIDIA Driver Installation**: Install the latest proprietary NVIDIA drivers compatible with your GPU. Refer to NVIDIA's official documentation for detailed steps.
3.  **ROS 2 Installation**: Install the Humble Hawksbill distribution of ROS 2. Follow the official ROS 2 documentation for Ubuntu 22.04.
4.  **Docker and NVIDIA Container Toolkit**: Install Docker and the NVIDIA Container Toolkit to run GPU-accelerated containers for Isaac Sim and other AI tools.
5.  **Python Environment**: Ensure Python 3.10 is installed and configured as outlined in `configure_python.sh`.
6.  **Development Tools**: Install common development tools, including `git`, `build-essential`, `colcon-common-extensions`.
