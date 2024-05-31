#! /usr/bin/env python3
import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String


class RobotStatePublisher(Node):
    def __init__(self):
        super().__init__("robot_state_publisher")
        self.declare_parameter("robo_state","GOOD")
        self.robot_state = self.get_parameter("robo_state")
        self.publisher = self.create_publisher(String,"robot_state",10)
        self.timer = self.create_timer(0.5,self.timer_callback)
        self.get_logger().info("Hello World")

    def timer_callback(self):
        msg = String()
        msg.data = "Robot state is " + str(self.robot_state.value) 
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotStatePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()