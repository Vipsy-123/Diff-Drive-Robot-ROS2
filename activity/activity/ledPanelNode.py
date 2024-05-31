#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
from my_robot_interfaces.msg import LedStates

class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_ = self.create_service(SetLed,"set_led",self.setLED_callback)
        self.timer_ = self.create_timer(1.0,self.led_panel_state_timer_callback)
        self.panel_publisher = self.create_publisher(LedStates,"led_panel_state",10)
        self.get_logger().info("Set LED service has Started")
        self.panel = [0,0,0]
        self.status = ""

    def setLED_callback(self,request,response):
        if(request.led_state == "on"):
            self.panel[request.led_number-1] = 1
            self.status = "ON"
        elif(request.led_state == "off"):
            self.panel[request.led_number-1] = 0
            self.status = "OFF"
        self.get_logger().info(" LED no. %d set as %s"%(request.led_number,self.status))
        response.success = True
        return response

    def led_panel_state_timer_callback(self):
        msg = LedStates()
        msg.led1 = self.panel[0]
        msg.led2 = self.panel[1]
        msg.led3 = self.panel[2]
        self.panel_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()