from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="mytest", executable="pub_audio", output="screen"),
            Node(package="mytest", executable="sub_robot", output="screen"),
        ]
    )
