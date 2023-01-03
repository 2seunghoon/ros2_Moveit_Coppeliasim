import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    demo_with_listener_node=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('dyros_tf2'),
            'launch','start_demo_with_listener_launch.py'
        )])
    )

    return LaunchDescription([
        demo_with_listener_node,
        Node(
            package='dyros_tf2',
            executable='fixed_tf2_broadcaster',
            name="fixed_broadcaster"
        )
    ])