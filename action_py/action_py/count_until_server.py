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

class CountUntilServer(Node):
    def __init__(self):
        super().__init__("count_until_action_server")
        self.goal_handle_ : ServerGoalHandle = None
        # Implmenting a Lock so that Goal handle can be accessed one at a time by different threads
        self.goal_lock = threading.Lock()
        self.goal_queue = []
        self.count_until_server_ = ActionServer(self,CountUntil,"count_until",
                                                goal_callback=self.goal_callback,
                                                handle_accepted_callback=self.accept_callback,
                                                cancel_callback=self.cancel_callback,
                                                execute_callback=self.execute_callback,
                                                callback_group=ReentrantCallbackGroup())
        self.get_logger().info("Action Server has started.")
    
    def goal_callback(self,goal_request : CountUntil.Goal):
        self.get_logger().info("Goal Recieved")

        # # Policy : Refuse new Goal if current goal is still active and it not the First Goal
        # with self.goal_lock:
        #     if self.goal_handle_ is not None and self.goal_handle_.is_active:
        #         self.get_logger().info("A goal is already running. Rejecting new goal")
        #         return GoalResponse.REJECT
        
        # Goal Rejection or Acceptance
        if(goal_request.target_number <= 0):
            self.get_logger().info("Rejecting a Goal")
            return GoalResponse.REJECT
        
        # # Policy : Preempt current goal when receiving new goal
        # with self.goal_lock:
        #     if self.goal_handle_ is not None and self.goal_handle_.is_active:
        #         self.get_logger().info("Abort current goal and accept new goal")
        #         self.goal_handle_.abort()

        self.get_logger().info("Accepting a Goal")
        return GoalResponse.ACCEPT
    
    def accept_callback(self,goal_handle : ServerGoalHandle):
        with self.goal_lock:
            if self.goal_handle_ is not None:
                self.goal_queue.append(goal_handle)
            else:
                goal_handle.execute()

    def cancel_callback(self,goal_handle: ServerGoalHandle):
        self.get_logger().info("Recieved Cancel Request")
        return CancelResponse.ACCEPT # or Reject
    
    def execute_callback(self,goal_handle: ServerGoalHandle):
        #Get request from goal
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period

        # Using a Lock while accessing a variable that is shared among different threads
        with self.goal_lock:
            self.goal_handle_ = goal_handle

        #Execute the Action
        self.get_logger().info("Executing the Goal")
        counter = 0
        feedback = CountUntil.Feedback()
        result = CountUntil.Result()
        for i in range(target_number):
            if not self.goal_handle_.is_active:
                result.reached_number = counter
                self.process_next_goal_in_queue()
                return result
        
            if goal_handle.is_cancel_requested:
                self.get_logger().info("Canceling the Goal")
                goal_handle.canceled()
                result.reached_number = counter
                self.process_next_goal_in_queue()
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
        self.process_next_goal_in_queue()
        return result
    
    # Queue Goals
    def process_next_goal_in_queue(self):
        with self.goal_lock:
            if len(self.goal_queue):
                self.goal_queue.pop(0).execute()
            else:
                self.goal_handle_ = None

def main(args=None):
    rclpy.init(args=args)
    node = CountUntilServer()
    rclpy.spin(node, MultiThreadedExecutor())
    rclpy.shutdown()

if __name__ == "__main__":
    main()