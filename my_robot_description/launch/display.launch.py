from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():

    urdf_path = os.path.join(get_package_share_path)

    robot_description = ParameterValue(Command(['xacro', urdf_path]),value_type=str)

    robot_state_publisher_node = 
    return LaunchDescription([


    ])