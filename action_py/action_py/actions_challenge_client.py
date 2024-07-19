#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle,GoalStatus
from my_robot_interfaces.action import PoseGoal
from example_interfaces.msg import Bool

class ActionChallengeClient(Node):
    def __init__(self): 
        super().__init__("action_challenge_client")
        self.client_ = ActionClient(self,PoseGoal,"pose_goal")
        self.get_logger().info("Action Client sending goal.")
        self.create_subscription(Bool,"cancel_move",self.cancel_move_callback,10)

    # Function to Send Goal Request to Action Server
    def send_goal(self,target_number,velocity):
        # Wait for the Action Server
        self.client_.wait_for_server()

        # Create a Goal
        goal = PoseGoal.Goal()
        goal.target_position = target_number
        goal.velocity = velocity

        # Send the Goal and call goal response callback
        self.get_logger().info("Sending Goal")
        self.client_. \
            send_goal_async(goal,feedback_callback=self.goal_feedback_callback). \
            add_done_callback(self.goal_response_callback)

    # Check if Goal is Accepted & Send the request for the result
    def goal_response_callback(self,future):
        self.goal_handle_: ClientGoalHandle = future.result()
        if self.goal_handle_.accepted:
            self.get_logger().info("Goal Accepted")
            self.goal_handle_.get_result_async(). \
                add_done_callback(self.goal_result_callback)
        else:
            self.get_logger().warn("Goal got Rejected")

    # Result request callback to Check the end result
    def goal_result_callback(self,future):
        status = future.result().status
        result = future.result().result

        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info("Accepted")
        elif status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error("Aborted")
        elif status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warn("Canceled")

        self.get_logger().info("Result: "+ str(result.reached_position))

    def cancel_goal(self):
        self.get_logger().info("Sending a Cancel request")
        self.goal_handle_.cancel_goal_async()
        self.timer_.cancel()

    def goal_feedback_callback(self,feedback_msg):
        number = feedback_msg.feedback.current_position
        self.get_logger().info("Feedback Number = " +str(number))

    def cancel_move_callback(self,msg):
        self.timer_ = self.create_timer(1.0, self.cancel_goal)
        
def main(args=None):
    rclpy.init(args=args)
    node = ActionChallengeClient()
    node.send_goal(15,2)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()