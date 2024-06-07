from launch import LaunchDescription
from launch.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    remap_number_topic = [("number", "number2")]

    number_publisher_node = Node(
        package="activity",
        executable="number_publisher",
        name="my_number_publisher",
        remappings=remap_number_topic
    )

    number_subscriber_node = Node(
        package="activity",
        executable="number_counter",
        name="my_number_counter",
        remappings=[
        remap_number_topic ,
          ("number_count", "my_number_count")
        ] 
    )

    ld.add_action(number_publisher_node)
    ld.add_action(number_subscriber_node)
    return ld