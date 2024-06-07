
'''
    Turtle Controller Node :
        Purpose Of the Node is to control "turtle1" to catch other spawned turtles

    Publishers:
        /turtle1/cmd_vel - Control speed of turtle1     Done   
    Subscribers:
        /turtle1/pose - Obtain current Position & Orientation of turtle1    Done
        /alive_turtles - Get list of current Turtles and their coordinates
    Services:
        /catch_turtle client - Call when a turtle has been caught master turtle 

    Testing : Target turtle2 is at (10.0,10.0,0.0)

'''
#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from my_robot_interfaces.msg import TurtleArray,Turtle


class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.target_x = 8.0
        self.target_y = 4.0

        self.pose_ = None
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(
            Pose, "turtle1/pose", self.callback_turtle_pose, 10)
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
        self.turtle_subscriber = self.create_subscription(TurtleArray,"alive_turtle",self.turtleArray_subscriber_callback,10)
        

    def turtleArray_subscriber_callback(self,msg):
         

    def callback_turtle_pose(self, msg):
        self.pose_ = msg

    def control_loop(self):
        if self.pose_ == None:
            return

        dist_x = self.target_x - self.pose_.x
        dist_y = self.target_y - self.pose_.y
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)

        msg = Twist()

        if distance > 0.5:
            # position
            msg.linear.x = 2*distance

            # orientation
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta
            if diff > math.pi:
                diff -= 2*math.pi
            elif diff < -math.pi:
                diff += 2*math.pi

            msg.angular.z = 6*diff
        else:
            # target reached!
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.cmd_vel_publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()