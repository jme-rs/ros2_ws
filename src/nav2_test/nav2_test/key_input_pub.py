import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class KeyInputPub(Node):
    def __init__(self):
        super().__init__("key_input_pub")
        self.publisher_ = self.create_publisher(String, "key_input", 10)
        timer_period = 1.0  # Frequency of publishing
        self.timer = self.create_timer(timer_period, self.pub_callback)

    def pub_callback(self):
        msg = String()
        msg.data = input("Enter a point: ")
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing: {}".format(msg))


def main(args=None):
    try:
        rclpy.init(args=args)
        talker = KeyInputPub()
        rclpy.spin(talker)
    except KeyboardInterrupt:
        pass
    finally:
        talker.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
