# Cloud Ether Lab Information

This document provides information about leveraging Cloud Ether Lab options (e.g., AWS, Azure instances) for computationally intensive tasks in the Physical AI & Humanoid Robotics course. While cloud resources can augment local workstations, the Edge AI Kit remains a core requirement for on-device deployment.

## Purpose of Cloud Ether Lab

*   **Accelerated Simulation**: Run large-scale Gazebo or Isaac Sim simulations with more powerful GPUs and CPUs than a local workstation.
*   **Distributed Training**: Train complex AI models (e.g., deep reinforcement learning policies) across multiple cloud instances.
*   **Data Processing**: Process vast amounts of sensor data or perform large-scale data analysis.

## Recommended Cloud Platforms

*   **AWS (Amazon Web Services)**: EC2 instances with NVIDIA GPUs (e.g., P3, P4 instances) for compute-intensive tasks. AWS RoboMaker for robotics development services.
*   **Azure (Microsoft Azure)**: NC-series VMs with NVIDIA GPUs. Azure Kubernetes Service (AKS) for container orchestration.

## Setup and Usage

1.  **Account Setup**: Create an account on your chosen cloud platform.
2.  **Instance Provisioning**: Launch a virtual machine with appropriate GPU and CPU resources, pre-configured with Ubuntu 22.04 and NVIDIA drivers.
3.  **Software Installation**: Install ROS 2, Isaac Sim, and other necessary software on the cloud instance, similar to the workstation setup.
4.  **Remote Access**: Configure SSH for secure remote access to your cloud instance.
5.  **Data Transfer**: Utilize cloud storage (e.g., AWS S3, Azure Blob Storage) for efficient data transfer between local and cloud environments.

## Important Note

While Cloud Ether Lab provides significant computational power, the **Edge AI Kit (Jetson Orin Nano/NX) is still required** for hands-on experience with deploying and testing AI models directly on embedded hardware, which is a core learning objective of this course.
