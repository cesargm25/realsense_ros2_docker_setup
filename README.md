# Docker Scripts for ROS 2 Workspace (ws_moveit)
This repository includes Docker scripts to simplify the development and deployment of your ROS 2 projects inside a containerized environment.

🐳 Docker Setup
# 1. Install Docker (with optional NVIDIA support)
bash
# Use the -n flag to enable NVIDIA driver support (recommended if using GPU).

bash install_docker.sh -n     # Install or reinstall Docker
bash build_docker.sh -n       # Build the Docker image
bash run_docker.sh -n         # Run the Docker container

# 2. Access the Docker container

bash
bash into_docker.sh

# Setting Up the ROS 2 Workspace (ws_moveit)
All the following commands should be executed inside the container and within the ws_moveit folder.

# 2. Install Dependencies
bash

rosdep install -i --from-path src --rosdistro $ROS_DISTRO --skip-keys=librealsense2 -y

# 3. Build the Workspace

bash
colcon build
# 4. Source the Setup File

bash
source install/setup.bash

# Running the RealSense Node
Once the workspace is built and sourced, you can launch the Intel RealSense camera node using one of the following methods:

bash
Copy
Edit
ros2 run realsense2_camera realsense2_camera_node

# or with a launch file:
ros2 launch realsense2_camera rs_launch.py
