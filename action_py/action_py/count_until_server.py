#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse,CancelResponse
from my_robot_interfaces.action import CountUntil
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
import time

class CountUntilServer(Node):
    def __init__(self):
        super().__init__("count_until_action_server")
        self.count_until_server_ = ActionServer(self,CountUntil,"count_until",
                                                goal_callback=self.goal_callback,
                                                cancel_callback=self.cancel_callback,
                                                execute_callback=self.execute_callback,
                                                callback_group=ReentrantCallbackGroup())
        self.get_logger().info("Action Server has started.")
    
    def goal_callback(self,goal_request : CountUntil.Goal):
        self.get_logger().info("Goal Recieved")
        # Goal Rejection or Acceptance
        if(goal_request.target_number <= 0):
            self.get_logger().info("Rejecting a Goal")
            return GoalResponse.REJECT
        self.get_logger().info("Accepting a Goal")
        return GoalResponse.ACCEPT
    
    def cancel_callback(self,goal_handle):
        self.get_logger().info("Recieved Cancel Request")
        return CancelResponse.ACCEPT # or Reject
    
    def execute_callback(self,goal_handle):
        #Get request from goal
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period

        #Execute the Action
        self.get_logger().info("Executing the Goal")
        counter = 0
        feedback = CountUntil.Feedback()
        result = CountUntil.Result()
        for i in range(target_number):
            if goal_handle.is_cancel_requested:
                self.get_logger().info("Canceling the Goal")
                goal_handle.canceled()
                result.reached_number = counter
                return result
            counter += 1
            self.get_logger().info(str(counter))
            feedback.current_number = counter
            goal_handle.publish_feedback(feedback)
            time.sleep(period)

        # Once done , set goal final state
        goal_handle.succeed()

        # and send the result
        result.reached_number = counter
        return result

def main(args=None):
    rclpy.init(args=args)
    node = CountUntilServer()
    rclpy.spin(node, MultiThreadedExecutor())
    rclpy.shutdown()

if __name__ == "__main__":
    main()