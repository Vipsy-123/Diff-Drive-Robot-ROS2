# ROS2 Repository for ROS2 Concepts and Differential Drive Robot Simulation

This repository contains multiple robotics projects implemented in both Python and C++. Each project is organized into its respective directory with the following structure:

## Directories Overview

### action_py
This directory contains Python implementations of various action-related functionalities, including clients and servers for different challenges and counting tasks.

- [`actions_challenge_client.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/action_py/action_py/actions_challenge_client.py): Client for actions challenge.
- [`actions_challenge_server.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/action_py/action_py/actions_challenge_server.py): Server for actions challenge.
- [`count_until_client.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/action_py/action_py/count_until_client.py): Client for counting until a certain number.
- [`count_until_server.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/action_py/action_py/count_until_server.py): Server for counting until a certain number.

### actions_cpp
This directory contains C++ implementations for action-related tasks.

- [`count_until_client.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/actions_cpp/src/count_until_client.cpp): C++ client for counting tasks.
- [`count_until_server.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/actions_cpp/src/count_until_server.cpp): C++ server for counting tasks.
- [`count_until_server_queue_goals.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/actions_cpp/src/count_until_server_queue_goals.cpp): C++ server with goal queuing functionality.

### activity
This directory contains Python nodes for various activities.

- [`batteryNode.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/activity/activity/batteryNode.py): Node to monitor battery status.
- [`ledPanelNode.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/activity/activity/ledPanelNode.py): Node to control an LED panel.
- [`number_counter.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/activity/activity/number_counter.py): Node for counting numbers.
- [`number_publisher.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/activity/activity/number_publisher.py): Node to publish numbers.

### components_cpp
This directory contains C++ components for various functionalities.

- [`manual_composition.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/components_cpp/src/manual_composition.cpp): Example of manual component composition.
- [`number_publisher.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/components_cpp/src/number_publisher.cpp): Component to publish numbers.

### components_py
This directory contains Python components for various functionalities.

- [`manual_composition.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/components_py/components/manual_composition.py): Example of manual component composition.
- [`node1.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/components_py/components/node1.py): First example node.
- [`node2.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/components_py/components/node2.py): Second example node.

### executors_cpp
This directory contains C++ executors.

- [`multi_threaded_executor.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/executors_cpp/src/multi_threaded_executor.cpp): Multi-threaded executor example.
- [`single_threaded_executor.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/executors_cpp/src/single_threaded_executor.cpp): Single-threaded executor example.

### executors_py
This directory contains Python executors.

- [`multi_threaded_executor.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/executors_py/executors/multi_threaded_executor.py): Multi-threaded executor example.
- [`single_threaded_executor.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/executors_py/executors/single_threaded_executor.py): Single-threaded executor example.
- [`number_publisher.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/executors_py/executors/number_publisher.py): Example of a node publishing numbers.

### final_project
This directory contains the final project implementations in C++.

- [`final_project.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/final_project/src/final_project.cpp): Main final project implementation.
- [`final_project_step1.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/final_project/src/final_project_step1.cpp): Step 1 of the final project.
- [`final_project_step2.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/final_project/src/final_project_step2.cpp): Step 2 of the final project.
- [`final_project_step3.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/final_project/src/final_project_step3.cpp): Step 3 of the final project.
- [`final_project_turtlebot.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/final_project/src/final_project_turtlebot.cpp): Final project for Turtlebot.

### lifecycle_cpp
This directory contains C++ lifecycle nodes.

- [`number_publisher.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/lifecycle_cpp/src/number_publisher.cpp): Lifecycle node to publish numbers.

### lifecycle_py
This directory contains Python lifecycle nodes.

- [`actions_challenge_client.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/lifecycle_py/lifecycle/actions_challenge_client.py): Lifecycle client for actions challenge.
- [`actions_challenge_server.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/lifecycle_py/lifecycle/actions_challenge_server.py): Lifecycle server for actions challenge.
- [`lifecycle_node_manager.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/lifecycle_py/lifecycle/lifecycle_node_manager.py): Node manager for lifecycle nodes.
- [`number_publisher.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/lifecycle_py/lifecycle/number_publisher.py): Lifecycle node to publish numbers.

### my_cpp_package
This directory contains custom C++ packages.

- [`add_two_ints_client.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_cpp_package/src/add_two_ints_client.cpp): Client for adding two integers.
- [`add_two_ints_server.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_cpp_package/src/add_two_ints_server.cpp): Server for adding two integers.
- [`cpp_publisher.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_cpp_package/src/cpp_publisher.cpp): Publisher node in C++.
- [`cpp_subscriber.cpp`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_cpp_package/src/cpp_subscriber.cpp): Subscriber node in C++.

### my_py_pkg
This directory contains custom Python packages.

- [`add_two_ints_client.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_py_pkg/src/add_two_ints_client.py): Client for adding two integers.
- [`add_two_ints_server.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_py_pkg/src/add_two_ints_server.py): Server for adding two integers.
- [`py_publisher.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_py_pkg/src/py_publisher.py): Publisher node in Python.
- [`py_subscriber.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_py_pkg/src/py_subscriber.py): Subscriber node in Python.

### my_robot_bringup
This directory contains launch files and configurations for bringing up the robot.

- [`components.launch.py`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_robot_bringup/launch/components.launch.py): Launch file for components.
- [`final_project.launch.xml`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_robot_bringup/launch/final_project.launch.xml): Launch file for the final project.
- [`my_robot_gazebo.launch.xml`](https://github.com/Vipsy-123/Diff-Drive-Robot-ROS2/blob/main/my_robot_bringup/launch/my_robot_gazebo.launch.xml): Launch file for Gazebo simulation.
