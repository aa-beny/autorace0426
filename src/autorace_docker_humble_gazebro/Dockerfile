# FROM nvcr.io/nvidia/l4t-ml:r36.2.0-py3
# FROM dustynv/ros:humble-desktop-l4t-r35.3.1
# FROM dustynv/ros:humble-desktop-pytorch-l4t-r35.4.1
# FROM dustynv/ros:humble-pytorch-l4t-r35.3.1
#FROM dustynv/l4t-pytorch:r36.4.0
FROM dustynv/l4t-pytorch:r36.3.0-cu124

############################## SYSTEM PARAMETERS ##############################
# * Arguments
ARG USER=initial
ARG GROUP=initial
ARG UID=1000
ARG GID="${UID}"
ARG SHELL=/bin/bash
ARG HARDWARE=arm64
ARG ENTRYPOINT_FILE=entrypint.sh

# * Env vars for the nvidia-container-runtime.
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES all
# ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility,compute
ENV ROS_DOMAIN_ID=25
# * Setup users and groups
RUN groupadd --gid "${GID}" "${GROUP}" \
    && useradd --gid "${GID}" --uid "${UID}" -ms "${SHELL}" "${USER}" \
    && mkdir -p /etc/sudoers.d \
    && echo "${USER}:x:${UID}:${UID}:${USER},,,:/home/${USER}:${SHELL}" >> /etc/passwd \
    && echo "${USER}:x:${UID}:" >> /etc/group \
    && echo "${USER} ALL=(ALL) NOPASSWD: ALL" > "/etc/sudoers.d/${USER}" \
    && chmod 0440 "/etc/sudoers.d/${USER}"

# * Replace apt urls
# ? Change to tku
# RUN sed -i 's@archive.ubuntu.com@ftp.tku.edu.tw@g' /etc/apt/sources.list
# ? Change to Taiwan
RUN sed -i 's@archive.ubuntu.com@tw.archive.ubuntu.com@g' /etc/apt/sources.list

# * Time zone
# RUN apt update && apt install -y tzdata
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/"${TZ}" /etc/localtime && echo "${TZ}" > /etc/timezone
# RUN DEBIAN_FRONTEND=noninteractive TZ=Asia/Taipei apt-get -y install tzdata
# RUN apt install tzdata -y

# * Copy custom configuration
# ? Requires docker version >= 17.09
COPY --chmod=0775 ./${ENTRYPOINT_FILE} /entrypoint.sh
COPY --chown="${USER}":"${GROUP}" --chmod=0775 config config
# ? docker version < 17.09
# COPY ./${ENTRYPOINT_FILE} /entrypoint.sh
# COPY config config
# RUN sudo chmod 0775 /entrypoint.sh && \
    # sudo chown -R "${USER}":"${GROUP}" config \
    # && sudo chmod -R 0775 config

# * Install packages
RUN apt update \
    && apt install -y --no-install-recommends \
        sudo \
        git \
        htop \
        wget \
        curl \
        psmisc \
        # * Shell
        tmux \
        udev \
        terminator \
        # * base tools
        python3-pip \
        python3-dev \
        python3-setuptools \
        software-properties-common \
        lsb-release \
        # * Work tools
        xvfb \
        ffmpeg \ 
        freeglut3-dev \
        # camera 
        qv4l2 \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# RUN apt-get purge '*opencv*' -y    
ENV DEBIAN_FRONTEND=noninteractive

RUN add-apt-repository universe \
    && apt update \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null \
    && apt update \
    && apt install -y ros-humble-desktop \
    && apt install -y ros-humble-rmw-cyclonedds-cpp \
    && apt install -y python3-colcon-common-extensions
# RUN add-apt-repository universe \
#     && apt update \
#     && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg \
#     && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null \
#     && apt update \
#     && DEBIAN_FRONTEND=noninteractive apt install -y ros-humble-desktop python3-argcomplete \
#     && apt install -y ros-humble-rmw-cyclonedds-cpp \
#     && apt install -y python3-colcon-common-extensions

#############
# 安裝 C++ 版本的 Dynamixel SDK
# 克隆 Dynamixel SDK
RUN git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git /home/${USER}/DynamixelSDK

# 安裝 C++ 版本的 Dynamixel SDK
#WORKDIR /home/${USER}/turtlebot3/turtlebot3


# 設置 CMake 尋找 SDK 的路徑
ENV CMAKE_PREFIX_PATH="/home/${USER}/DynamixelSDK/c++/install:$CMAKE_PREFIX_PATH"

# 安裝 CMake 和編譯工具
RUN apt update && apt install -y \
    cmake \
    g++ \
    make \
    libboost-all-dev \
    libpython3-dev
##############

# RUN ./config/pip/pip_setup.sh
RUN pip3 install dynamixel_sdk \
                 pynput \
                 setuptools \
                 opencv-python \
                 tqdm \
                 pandas \
                 requests \
                 seaborn \
                 scipy 

RUN apt update
# RUN apt-get purge '*opencv*' -y
# Install Gazebo Cartographer Navigation2
# RUN curl -sSL http://get.gazebosim.org | sh
# RUN apt install -y ros-humble-gazebo-* \
#      ros-humble-cartographer \
#      ros-humble-cartographer-ros \
#      ros-humble-navigation2 \
#      ros-humble-nav2-bringup
RUN apt update && apt install -y \
    ros-humble-cartographer-ros \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y \
    ros-humble-navigation2 \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y \
    ros-humble-nav2-bringup \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y \
    ros-humble-ros-gz \
    && rm -rf /var/lib/apt/lists/*
# RUN apt-get update && apt-get install -y wget gnupg2 && \
#     wget https://packages.osrfoundation.org/gazebo.key -O - | apt-key add - && \
#     echo "deb http://packages.osrfoundation.org/gz-harmonic/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/gz-harmonic.list
# RUN apt-get update && apt-get install -y \
#     ros-humble-ros-gzharmonic \
#     && rm -rf /var/lib/apt/lists/*
# RUN apt-get update && apt-get install -y \
#     ros-humble-ros-gzgarden \
#     && rm -rf /var/lib/apt/lists/*
# Install vcstool
# RUN apt install python3-vcstool 

############################## USER CONFIG ####################################
# * Switch user to ${USER}
USER ${USER}

RUN ./config/shell/bash_setup.sh "${USER}" "${GROUP}" \
    && ./config/shell/terminator/terminator_setup.sh "${USER}" "${GROUP}" \
    && ./config/shell/tmux/tmux_setup.sh "${USER}" "${GROUP}" \
    && sudo rm -rf /config
RUN export CXX=g++
RUN export MAKEFLAGS="-j nproc"
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
RUN echo "set-option -g mouse on" >  ~/.tmux.conf

RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
RUN echo "export LDS_MODEL=rplidar_a1" >> ~/.bashrc

# RUN sudo apt install -y python3-rosdep
# RUN sudo rosdep init
RUN export PATH=/usr/local/cuda/bin:$PATH
RUN export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

# * Switch workspace to ~/work
RUN sudo mkdir -p /home/"${USER}"/work
WORKDIR /home/"${USER}"/work

# RUN useradd -G video,docker,docker2 -g 50 -m -s /bin/bash  -u 501 "$USER"

# * Make SSH available
EXPOSE 22

ENTRYPOINT [ "/entrypoint.sh", "terminator" ]
# ENTRYPOINT [ "/entrypoint.sh", "tmux" ]
# ENTRYPOINT [ "/entrypoint.sh", "bash" ]
# ENTRYPOINT [ "/entrypoint.sh" ]

# CMD ["terminator"]
