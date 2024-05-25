#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32

class NumPublisher(Node):
    def __init__(self):
        super().__init__("num_publisher")
        self.pub = self.create_publisher(Int32,"number",10)
        self.timer = self.create_timer(0.5,self.timer_callback)
        self.count = 0
        self.get_logger().info("Number Publisher has started.")

    def timer_callback(self):
        msg = Int32()
        msg.data = self.count
        self.pub.publish(msg)
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = NumPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()