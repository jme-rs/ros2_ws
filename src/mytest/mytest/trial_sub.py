import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TrialSub(Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(String, "helloworld", self.sub_callback, 10)

    def sub_callback(self, msg):
        self.get_logger().info("Received: {}".format(msg))


def main(args=None):
    try:
        rclpy.init(args=args)
        listener = TrialSub()
        rclpy.spin(listener)
    except KeyboardInterrupt:
        pass
    finally:
        listener.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
