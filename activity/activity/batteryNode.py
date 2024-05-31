#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed

class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery_node")
        self.battery_client = self.create_client(SetLed,"set_led")
        while not self.battery_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Set Led service not available, waiting again...')
        self.req = SetLed.Request()

    def send_request(self):
        self.req.led_number = int(sys.argv[1])
        self.req.led_state = sys.argv[2]
        self.future = self.battery_client.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    minimal_client = BatteryNode()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                    'Got response from Server : LED %d , Success = %s  ' %
                    (minimal_client.req.led_number, response.success))
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()