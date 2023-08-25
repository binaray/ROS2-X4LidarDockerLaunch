from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('rosbridge_server'),
                    'launch',
                    'rosbridge_websocket_launch.xml'
                ]),
            ]),
            launch_arguments={
                'port': '9090',
                'address': '',
                'ssl': 'false',
                'certfile': '',
                'keyfile': '',
                'retry_startup_delay': '5.0',
                'fragment_timeout': '600',
                'delay_between_messages': '0',    
                'max_message_size': '10000000',
                'unregister_timeout': '10.0',
                'use_compression': 'false',
                'topics_glob': '',
                'services_glob': '',
                'params_glob': '',
                'bson_only_mode': 'false',
                'binary_encoder': 'default'                     
            }.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('ydlidar_ros2_driver'),
                    'launch',
                    'ydlidar_launch_view.py'
                ])
            ])
        )
    ])
