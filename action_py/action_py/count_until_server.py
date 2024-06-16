#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from example_interfaces.action import CountUntil
import time

class CountUntilServer(Node):
    def __init__(self):
        super().__init__("count_until_action_server")
        self.count_until_server_ = ActionServer(self,CountUntil,"count_until",
                                                execute_callback=self.execute_callback)
        self.get_logger().info("Action Server has started.")
    
    def execute_callback(self,goal_handle):
        #Get request from goal
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period

        #Execute the Action
        self.get_logger().info("Executing the Goal")
        counter = 0
        for i in range(target_number):
            counter += 1
            self.get_logger().info(str(counter))
            time.sleep(period)

        # Once done , set goal final state
        goal_handle.succeed()

        # and send the result
        result = CountUntil.Result()
        result.reached_number = counter
        return result

def main(args=None):
    rclpy.init(args=args)
    node = CountUntilServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()