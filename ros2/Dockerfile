FROM osrf/ros:humble-desktop

# install ros package
RUN apt-get update && apt-get install -y \
     ros-$ROS_DISTRO-rosbridge-suite \
     python3-colcon-common-extensions \
     cmake pkg-config && \
    rm -rf /var/lib/apt/lists/*

# display fix for humble rviz2
RUN apt update && apt install -y software-properties-common && add-apt-repository ppa:kisak/kisak-mesa && apt upgrade -y

# build driver dependencies
COPY ./YDLidar-SDK /YDLidar-SDK
WORKDIR /YDLidar-SDK/build
RUN cmake .. && \
	make && \
	make install

WORKDIR /production_ws
COPY ./src ./src

RUN echo 'source /opt/ros/$ROS_DISTRO/setup.bash' >> ~/.bashrc
RUN /bin/bash -c 'source /opt/ros/$ROS_DISTRO/setup.bash &&\
    colcon build --symlink-install'
RUN echo 'source ./install/setup.bash' >> ~/.bashrc

