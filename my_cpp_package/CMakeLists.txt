cmake_minimum_required(VERSION 3.8)
project(my_cpp_package)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

#add executables here
add_executable(cpp_publisher src/cpp_publisher.cpp)
ament_target_dependencies(cpp_publisher rclcpp example_interfaces)

add_executable(cpp_subscriber src/cpp_subscriber.cpp)
ament_target_dependencies(cpp_subscriber rclcpp example_interfaces)

install(TARGETS
  cpp_publisher
  cpp_subscriber
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
