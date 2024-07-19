#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
import threading
from rclpy.action import ActionServer, GoalResponse,CancelResponse
from rclpy.action.server import ServerGoalHandle
from my_robot_interfaces.action import PoseGoal
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
import time

class ActionChallengeServer(Node):
    def __init__(self):
        super().__init__("action_challenge_server")
        self.goal_handle_ : ServerGoalHandle = None
        self.goal_lock = threading.Lock()
        self.count_until_server_ = ActionServer(self,PoseGoal,"pose_goal",
                                                goal_callback=self.goal_callback,
                                                cancel_callback=self.cancel_callback,
                                                execute_callback=self.execute_callback,
                                                callback_group=ReentrantCallbackGroup())
        self.get_logger().info("Action Server has started.")
    
    def goal_callback(self,goal_request : PoseGoal.Goal):
        self.get_logger().info("Goal Recieved")

        # Goal Rejection or Acceptance
        if(goal_request.target_position <= 0):
            self.get_logger().info("Rejecting a Goal")
            return GoalResponse.REJECT
        
        # Policy : Preempt current goal when receiving new goal
        with self.goal_lock:
            if self.goal_handle_ is not None and self.goal_handle_.is_active:
                self.get_logger().info("Abort current goal and accept new goal")
                self.goal_handle_.abort()

        self.get_logger().info("Accepting a Goal")
        return GoalResponse.ACCEPT  

    def cancel_callback(self,goal_handle: ServerGoalHandle):
        self.get_logger().info("Recieved Cancel Request")
        return CancelResponse.ACCEPT # or Reject
    
    def execute_callback(self,goal_handle : ServerGoalHandle):
        target_pos = goal_handle.request.target_position
        velocity = goal_handle.request.velocity

        # Using a Lock while accessing a variable that is shared among different threads
        with self.goal_lock:
            self.goal_handle_ = goal_handle

        feedback = PoseGoal.Feedback()
        result = PoseGoal.Result()
        for i in range(0,target_pos,velocity):
            # print(i)        
            if goal_handle.is_cancel_requested:
                self.get_logger().info("Canceling the Goal")
                goal_handle.canceled()
                result.reached_position = i
                return result
            
            if i + velocity > target_pos:
                i += i + velocity - target_pos
            else:
                i += velocity
            feedback.current_position = i 

            goal_handle.publish_feedback(feedback)
            time.sleep(1.0)

        # Once done , set goal final state
        goal_handle.succeed()

        result.reached_position = feedback.current_position
        return result

def main(args=None):
    rclpy.init(args=args)
    node = ActionChallengeServer()
    rclpy.spin(node, MultiThreadedExecutor())
    rclpy.shutdown()

if __name__ == "__main__":
    main()
