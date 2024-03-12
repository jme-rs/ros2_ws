# ROS2 Workshop day 2

## commands

```sh
colcon build --packages-select nav2_test
source ~/ros2_ws/install/local_setup.bash
```

```sh
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
ros2 launch turtlebot3_gazebo robot_state_publisher.launch.py
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
ros2 run turtlebot3_teleop teleop_keyboard
ros2 run nav2_map_server map_saver_cli -f ~/map
```

```sh
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$HOME/map.yaml
```

```sh
ros2 run nav2_test key_input_node
ros2 run nav2_test send_action_node
# ros2 launch nav2_test nav_launch.py
```
