# X4LidarLaunch
ROS2 docker compose files for launching x4 Lidar

## How to run
For a Linux system, to show rviz2 window, xhost needs to be used to enable other processes to access the X11 server (this isn’t exactly secure, but for now it works). On terminal input the following to start the docker container:
```
xhost local:root	# can be ommited if display is not needed
sudo docker compose up	# add -d to run in background
```
To run a bash session on terminal:
```
sudo docker exec -it ros2 /bin/bash
```


## Run ydlidar_ros2_driver
##### Run ydlidar_ros2_driver using launch file

The command format is : 

 `ros2 launch ydlidar_ros2_driver [launch file].py`

1. Connect LiDAR uint(s).
   ```
   ros2 launch ydlidar_ros2_driver ydlidar_launch.py 
   ```
   or 

   ```
   launch $(ros2 pkg prefix ydlidar_ros2_driver)/share/ydlidar_ros2_driver/launch/ydlidar.py 
   ```
2. RVIZ 
   ```
   ros2 launch ydlidar_ros2_driver ydlidar_launch_view.py 
   ```
    ![View](images/view.png  "View")

3. echo scan topic
   ```
   ros2 run ydlidar_ros2_driver ydlidar_ros2_driver_client or ros2 topic echo /scan
   ```
   
For more info on running the lidar see https://github.com/YDLIDAR/ydlidar_ros2_driver 
