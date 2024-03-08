from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="nav2_test", executable="key_input_node", output="screen"),
            Node(package="nav2_test", executable="send_action_node", output="screen"),
        ]
    )
