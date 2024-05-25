#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsSubscriber : public rclcpp::Node
{
public:
    RobotNewsSubscriber() :  Node("robot_news_subscriber")
    {
        sub = this->create_subscription<example_interfaces::msg::String>
                                        ("robot_news", 10,
                                        std::bind(&RobotNewsSubscriber::callback, this,
                                        std::placeholders::_1)
                                        );   
        RCLCPP_INFO(this->get_logger(), "Robot News Subscriber started.");

    }

private:
    void callback(const example_interfaces::msg::String::SharedPtr msg){
        RCLCPP_INFO(this->get_logger(), "Hello got you message : %s" , msg -> data.c_str());
    }
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr sub;

};

int main(int argc, char **argv){
    rclcpp::init(argc,argv);
    auto node = std::make_shared<RobotNewsSubscriber>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}