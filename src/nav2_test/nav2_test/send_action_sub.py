import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator


class SendActionSub(Node):
    def __init__(self):
        super().__init__("send_action_sub")
        self.create_subscription(String, "key_input", self.sub_callback, 10)
        send_initial_pose()

    def sub_callback(self, msg):
        self.get_logger().info("Received: {}".format(msg))
        data = msg.data
        if data == "p1":
            send_goal_pose(0.0, 1.0)
        elif data == "p2":
            send_goal_pose(1.0, 0.0)
        elif data == "p3":
            send_goal_pose(2.0, 0.0)
        else:
            send_goal_pose(0.0, 0.0)


def send_initial_pose():
    navigator = BasicNavigator()
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = "map"
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = 0.0
    initial_pose.pose.position.y = 0.0
    initial_pose.pose.position.z = 0.0
    initial_pose.pose.orientation.x = 0.0
    initial_pose.pose.orientation.y = 0.0
    initial_pose.pose.orientation.z = 0.0
    initial_pose.pose.orientation.w = 1.0
    navigator.setInitialPose(initial_pose)

    # rclpy.spin_once(navigator)
    navigator.waitUntilNav2Active()


def send_goal_pose(x, y):
    navigator = BasicNavigator()
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = "map"
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = x
    goal_pose.pose.position.y = y
    goal_pose.pose.position.z = 0.0
    goal_pose.pose.orientation.x = 0.0
    goal_pose.pose.orientation.y = 0.0
    goal_pose.pose.orientation.z = 0.0
    goal_pose.pose.orientation.w = 1.0
    navigator.goToPose(goal_pose)

    # rclpy.spin_once(navigator)
    navigator.waitUntilNav2Active()


def main(args=None):
    rclpy.init(args=args)
    listener = SendActionSub()
    try:
        rclpy.spin(listener)
    except KeyboardInterrupt:
        pass
    finally:
        listener.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
