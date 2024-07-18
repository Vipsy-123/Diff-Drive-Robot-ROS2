#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
import threading
from rclpy.action import ActionServer, GoalResponse,CancelResponse
from rclpy.action.server import ServerGoalHandle
from my_robot_interfaces.action import CountUntil
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
import time

class ActionChallengeServer(Node):
    def __init__(self):
        super().__init__("action_challange_server")
        self.goal_handle_ : ServerGoalHandle = None
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
        
        # Policy : Preempt current goal when receiving new goal
        with self.goal_lock:
            if self.goal_handle_ is not None and self.goal_handle_.is_active:
                self.get_logger().info("Abort current goal and accept new goal")
                self.goal_handle_.abort()

        self.get_logger().info("Accepting a Goal")
        return GoalResponse.ACCEPT