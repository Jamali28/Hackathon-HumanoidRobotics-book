# Edge AI Kit Setup Instructions (Jetson Orin Nano/NX)

This document provides detailed setup instructions for the Edge AI Kit, featuring the NVIDIA Jetson Orin Nano/NX, essential for deploying and testing AI models on the edge.

## Hardware Components

*   **NVIDIA Jetson Orin Nano/NX Developer Kit**
*   **Intel RealSense D435i** (Depth Camera)
*   **USB IMU** (e.g., BNO055)
*   **USB Microphone/Speaker**
*   **Power Supply** and **MicroSD Card** (64GB+)

## Setup Instructions

1.  **Jetson OS Flashing**: Flash the latest JetPack OS onto your Jetson Orin Nano/NX using NVIDIA SDK Manager. This includes Ubuntu, CUDA, cuDNN, and TensorRT.
2.  **ROS 2 Installation**: Install ROS 2 (Humble Hawksbill) on your Jetson. Follow the official ROS 2 documentation for ARM architecture.
3.  **RealSense SDK Installation**: Install the Intel RealSense SDK (librealsense) and ROS wrapper for your D435i camera.
4.  **IMU Driver**: Install necessary drivers or ROS packages for your USB IMU.
5.  **Audio Setup**: Configure the USB microphone and speaker for audio input/output.
6.  **Network Configuration**: Set up Wi-Fi or Ethernet connectivity for your Jetson.
