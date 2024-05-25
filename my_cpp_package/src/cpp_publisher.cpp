#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotStatePublisher : public rclcpp::Node {
public:
    RobotStatePublisher() : Node("robot_state_publisher"), robot_name("Bot") {
        pub = this->create_publisher<example_interfaces::msg::String>("robot_news", 10); 
        timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&RobotStatePublisher::timer_callback, this));
        RCLCPP_INFO(this->get_logger(), "Robot News Station has been started.");
    }

private:
    void timer_callback() {
        auto msg = example_interfaces::msg::String();
        msg.data = "Robot says " + robot_name + " is chilling.";
        pub->publish(msg);
    }
    
    std::string robot_name;
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr pub;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char* argv[]){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotStatePublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
