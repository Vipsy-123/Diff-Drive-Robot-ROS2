cmake_minimum_required(VERSION 3.5)
project(activities)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(example_interfaces REQUIRED)


# Install Python scripts
install(PROGRAMS
  src/number_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
