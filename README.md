Docker Scripts for ROS 2 Workspace (ws_moveit)
This repository includes Docker scripts to simplify the development and deployment of your ROS 2 projects inside a containerized environment.

🐳 Docker Setup
1. Install Docker (with optional NVIDIA support)
bash
Copy
Edit
# Use the -n flag to enable NVIDIA driver support (recommended if using GPU).
bash install_docker.sh -n     # Install or reinstall Docker
bash build_docker.sh -n       # Build the Docker image
bash run_docker.sh -n         # Run the Docker container
2. Access the Docker container
bash
Copy
Edit
bash into_docker.sh
🚀 Setting Up the ROS 2 Workspace (ws_moveit)
All the following commands should be executed inside the container and within the ws_moveit folder.

1. Install Dependencies
bash
Copy
Edit
rosdep install -i --from-path src --rosdistro $ROS_DISTRO --skip-keys=librealsense2 -y
2. Build the Workspace
bash
Copy
Edit
colcon build
3. Source the Setup File
bash
Copy
Edit
source install/setup.bash
📷 Running the RealSense Node
Once the workspace is built and sourced, you can launch the Intel RealSense camera node using one of the following methods:

bash
Copy
Edit
ros2 run realsense2_camera realsense2_camera_node

# or with a launch file:
ros2 launch realsense2_camera rs_launch.py
