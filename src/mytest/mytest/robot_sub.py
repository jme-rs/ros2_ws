import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import nav2_action_send
# from nav2_action_send import nav2init, nav2goal


class TrialSub(Node):
    def __init__(self):
        super().__init__("robot_sub_node")
        self.create_subscription(String, "/speech_recog_result", self.sub_callback, 10)
        nav2_action_send.nav2init()

    def sub_callback(self, msg):
        self.get_logger().info("Received: {}".format(msg))
        if msg.data == "右":
            nav2_action_send.nav2goal(3, 0)


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
