#! /usr/bin/env python3 
import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String

class RobotStateSubscriber(Node):

    def __init__(self):
        super().__init__("robot_state_subscriber")
        self.subscriber = self.create_subscription(String,"robot_state",self.subscriber_callback,10)

    def subscriber_callback(self,msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = RobotStateSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()