from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # control_avoidance_node = Node(
    #     package='control',
    #     executable='control_avoidance_v2_test',
    # )

    # control_avoidance_node = Node(
    #     package='control',
    #     executable='control_avoidance_2',
    # )

    control_navigation_node = Node(
        package='nv2',
        executable='example_follow_path',
    )
    # Create the launch description
    ld = LaunchDescription()

    # Add the launch arguments and nodes to the launch description
    ld.add_action(control_navigation_node)

    return ld


