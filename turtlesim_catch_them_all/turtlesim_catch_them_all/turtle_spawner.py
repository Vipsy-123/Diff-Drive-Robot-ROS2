
'''
    Turtle Spawner Node :
        Purpose Of the Node is spawn Turles in turtlesim 

    Publishers:
        /alive_turtles - Publish list of alive turtles with coordinates #TODO
    Subscribers:
        None
    Services:
        /spawn service client - To spawn a turtle on screen
        /kill service client - To remove a turtle form screen

'''

#!/usr/bin/env python3
# import sys
import rclpy
from rclpy.node import Node
# from my_robot_interfaces.srv import CatchTurtle
from turtlesim.srv import Spawn
import random

class TurtleSpawner(Node):
    def __init__(self):
        super().__init__("turtle_spawner")
        self.battery_client = self.create_client(Spawn,"spawn")
        while not self.battery_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Spawn Service not available ...')
        self.req = Spawn.Request()
        self.timer_ =self.create_timer(1.0,self.timer_callback)
        self.name = 2

    def send_request(self):
        self.req.x = random.uniform(0.0,11.0)
        self.req.y = random.uniform(0.0,11.0)  
        self.req.name = "turtle" + str(self.name)
        self.name += 1
        self.future = self.battery_client.call_async(self.req)

    def timer_callback(self):
        self.send_request()
        
def main(args=None):
    rclpy.init(args=args)

    minimal_client = TurtleSpawner()
    # minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                    'Turtle %s spawned at location %d,%d' %
                    (minimal_client.req.name, minimal_client.req.x, minimal_client.req.y))
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()