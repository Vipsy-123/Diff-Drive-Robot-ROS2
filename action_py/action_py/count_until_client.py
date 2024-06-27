#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle,GoalStatus
from my_robot_interfaces.action import CountUntil

class CountUntilClient(Node):
    def __init__(self):
        super().__init__("count_until_action_server")
        self.count_until_client_ = ActionClient(self,CountUntil,"count_until")
        self.get_logger().info("Action Client sending goal.")

    # Function to Send Goal Request to Action Server
    def send_goal(self,target_number,period):
        # Wait for the Action Server
        self.count_until_client_.wait_for_server()

        # Create a Goal
        goal = CountUntil.Goal()
        goal.target_number = target_number
        goal.period = period

        # Send the Goal and call goal response callback
        self.get_logger().info("Sending Goal")
        self.count_until_client_. \
            send_goal_async(goal,feedback_callback=self.goal_feedback_callback). \
            add_done_callback(self.goal_response_callback)
        
        self.timer_ = self.create_timer(2.0, self.cancel_goal)
        
    # Check if Goal is Accepted & Send the request for the result
    def goal_response_callback(self,future):
        self.goal_handle_: ClientGoalHandle = future.result()
        if self.goal_handle_.accepted:
            self.get_logger().info("Goal Accepted")
            self.goal_handle_. \
                get_result_async(). \
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

        self.get_logger().info("Result: "+ str(result.reached_number))

    def cancel_goal(self):
        self.get_logger().info("Sending a Cancel request")
        self.goal_handle_.cancel_goal_async()
        self.timer_.cancel()

    def goal_feedback_callback(self,feedback_msg):
        number = feedback_msg.feedback.current_number
        self.get_logger().info("Feedback Number = " +str(number))


def main(args=None):
    rclpy.init(args=args)
    node = CountUntilClient()
    node.send_goal(6,1.0)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()