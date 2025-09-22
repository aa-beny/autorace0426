# my_autorace
# autorace0426
Project Overview

This repository implements a ROS2 (Humble) autonomous driving stack for a small differential-drive robot (e.g., TurtleBot3):

Lane Following – camera detects yellow/white lane lines and follows the center.

Obstacle Avoidance – LiDAR detects obstacles ahead and performs a bypass maneuver.

Traffic Light Detection – color segmentation for RED/GREEN; stop/go logic.

Traffic Sign Detection (YOLOv7) – recognizes course signs (left/right/stop/park …).

Navigation (Nav2 + AMCL) – optional; localize on a saved map and navigate to goals.

You can run each module standalone or use the core coordinator to orchestrate the full flow (signals → decisions → control).

System Requirements

ROS2: Humble (Ubuntu 22.04).

Robot Base: TurtleBot3 (Burger/Waffle) or compatible differential-drive robot.

Camera: USB cam or Jetson CSI camera available as /dev/video*.

LiDAR: 2D LiDAR (TB3 Burger’s LDS-01 publishes /scan).

Compute: Jetson or a PC (GPU recommended for YOLOv7).

Motor Controller: TB3 OpenCR (or your driver that consumes /cmd_vel).

1) Workspace Setup (First)

The repo provides Docker; no separate “pip install torch/opencv” steps are needed here.
You’ll build inside the container.

Create workspace & clone

mkdir -p ~/autorace_ws/src
cd ~/autorace_ws/src
git clone https://github.com/aa-beny/autorace0426.git


Build & Run Docker (provided in repo)

# device -> pc/jetson
cd ~/autorace_ws/src/autorace0426/src/autorace_docker_humble_gazebro
./build.sh
./run.sh


Build your workspace inside the Docker terminal

# (you are now inside the container)
cd /workspaces/autorace_ws    # or the path used by the run script
colcon build
source install/setup.bash


Device permissions (host or container as appropriate)

# Camera
ls /dev/video*
sudo chmod 666 /dev/video0

# Serial devices (OpenCR/LiDAR if serial)
ls /dev/ttyUSB* /dev/ttyACM*
sudo chmod 666 /dev/ttyUSB0 /dev/ttyACM0


If you’re not seeing the devices inside Docker, run the container with --privileged and mount /dev, or use the repo’s run.sh which already handles it.
Make sure X11/GPU access is configured if you need OpenCV windows and/or CUDA.

2) Quick Start (cheat sheet)
# (optional) environment helpers
. setup_turtlebot.sh
export ROS_DOMAIN_ID=25


Bring up TB3 base (motors/LiDAR):

export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_bringup robot.launch.py


Emergency stop (zero velocity):

ros2 topic pub /cmd_vel geometry_msgs/Twist \
  "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"


YOLO sign detection:

ros2 launch object_detection object_detection_launch.py


No YOLO? Fake it for testing:

ros2 run detect_lane key_pub_signs
ros2 topic pub -1 /detect/signs std_msgs/String "{data: cave}"


Lane detection (HSV first, then follow):

# Calibrate first
ros2 launch detect_lane detect_lane_launch.py calibration:=True
# Calibration is saved to:
# /home/open/autorace0426/src/detect/detect_lane/config/hsv_parameters_own.yaml

# Then run
ros2 launch detect_lane detect_lane_launch.py calibration:=False


Switch which line to follow (dual/yellow/white):

# 0: dual, 1: yellow, 2: white
ros2 topic pub -1 /detect/lane_mode std_msgs/Int64 "{data: 1}"


Check detection strength:

ros2 topic echo /detect/yellow_fraction
ros2 topic echo /detect/white_fraction


Core coordinator (mode switching, stop/go, avoidance toggling):

ros2 run core core


Control (PD lane controller):

ros2 run control control_lane


Traffic lights (HSV):

# Calibrate
ros2 launch detect_lane detect_traffic_launch.py calibration:=True
# Saved to:
# /home/open/autorace0426/src/detect/detect_lane/config/hsv_parameters_tr_own.yaml

# Run
ros2 launch detect_lane detect_traffic_launch.py calibration:=False

# No real light? Publish a mock state:
ros2 topic pub -1 /detect/traffic_light std_msgs/String "{data: GREEN}"


Mapping (Cartographer) & keyboard teleop:

ros2 launch turtlebot3_cartographer cartographer.launch.py
ros2 run teleop_twist_keyboard teleop_twist_keyboard
# Save map (choose your path)
ros2 run nav2_map_server map_saver_cli -f ~/work/map


Navigation (Nav2) with your map:

ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/work/map.yaml
# Listen
ros2 topic echo /initialpose
ros2 topic echo /amcl_pose
# Dynamic tuning
ros2 run rqt_reconfigure rqt_reconfigure

3) Launch Order (Beginner Friendly)

Open multiple terminals (all source install/setup.bash):

Base bringup (motors/LiDAR)

export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_bringup robot.launch.py


Camera + Lane Detection (calibrate OR run)

# Recommended: calibrate once
ros2 launch detect_lane detect_lane_launch.py calibration:=True
# Then normal
ros2 launch detect_lane detect_lane_launch.py calibration:=False


Lane Controller (PD → /cmd_vel)

ros2 run control control_lane


YOLOv7 Sign Detection

ros2 launch object_detection object_detection_launch.py
ros2 topic echo /detect/signs


Traffic Light Detection (HSV)

ros2 launch detect_lane detect_traffic_launch.py calibration:=False
ros2 topic echo /detect/traffic_light


Obstacle Avoidance (LiDAR)

ros2 run control control_avoidance_v2_test.py
# or the avoidance node provided by the repo


Navigation (optional, with map)

ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/work/map.yaml
# In RViz: 2D Pose Estimate, then send Nav2 goal


Core Coordinator (optional, recommended)

ros2 run core core


The core handles: red/green stop-go, (de)activating lane during avoidance, reacting to signs (intersection/turn/park), and recovering after avoidance.

4) Feature Modules
4.1 Camera & Visualization

Camera topic: /image/image_raw

Visualize: rviz2 (Image display) or rqt_image_view

OpenCV windows appear in calibration and YOLO; set up X11 if running headless.

4.2 YOLOv7 – Traffic Signs

Launch: ros2 launch object_detection object_detection_launch.py

Outputs:

/detect/signs (std_msgs/String) – label like left, right, stop, park, Ts …

/detect/bounding_box – custom msg with image bbox

Params via launch: weights (default sign.pt), conf_thres, iou_thres, device, img_size

No model available? Use key_pub_signs or publish directly to /detect/signs.

4.3 Lane Detection & HSV Calibration

Launch: detect_lane_launch.py

Calibration (calibration:=True): pick HSV in RViz; values saved to hsv_parameters_own.yaml

Key topics:

/control/lane (Float64) – lateral error/control input for controller

/detect/yellow_fraction, /detect/white_fraction

/detect/lane_toggle (Bool) – on/off lane following (avoidance sets False)

/detect/lane_mode (Int64) – 0: dual, 1: yellow, 2: white

Params:

HSV ranges for yellow/white

Bird’s-eye ROI: top_x/top_y/bottom_x/bottom_y

Reliability thresholds for line presence

4.4 Traffic Lights (HSV)

Launch: detect_traffic_launch.py

ROI + HSV masks → publish "RED" / "GREEN" on /detect/traffic_light

Calibration mode shows masked images; tune hsv_parameters_tr_own.yaml

Core bridges to /control/go_stop to pause/resume motion.

4.5 Obstacle Avoidance (LiDAR)

Monitors narrow front sector in /scan (<~0.35 m)

Steps:

Publish False to /detect/lane_toggle (pause lane)

Execute timed maneuver (turn/forward sequence) to bypass

Publish /avoidance_done True; node usually exits after one run

For multiple obstacles, respawn the node or modify to keep running.

4.6 Navigation (Nav2 + AMCL)

Build a map (Cartographer/SLAM Toolbox), save map.yaml

Launch Nav2 with your map; set initial pose in RViz; send goals

Example script: example_follow_path.py (Nav2 Simple Commander)

5) Manual Control & Debugging

Keyboard teleop:

ros2 run turtlebot3_teleop teleop_keyboard


Software stop:

Zero /cmd_vel (see Quick Start)

Or toggle /control/go_stop:

ros2 topic pub -1 /control/go_stop std_msgs/Bool "data: true"   # stop
ros2 topic pub -1 /control/go_stop std_msgs/Bool "data: false"  # resume


Useful topics to watch:

ros2 topic echo /detect/signs
ros2 topic echo /detect/traffic_light
ros2 topic echo /control/lane
ros2 topic echo /detect/yellow_fraction
ros2 topic echo /detect/white_fraction
ros2 topic echo /detect/lane_toggle
ros2 topic echo /amcl_pose
ros2 topic echo /cmd_vel


RViz adds: Image (raw/processed), LaserScan (/scan), TF, Map/Costmap, Path, PoseArray (AMCL).

6) Troubleshooting (fast tips)

No camera image: check /dev/video*, permissions, correct topic; ensure only one camera node is running.

No YOLO detections: ensure weights file is present (repo includes it via Docker), correct topic names; reduce img_size if slow.

Lane wobbles/loses line: recalibrate HSV; adjust perspective ROI; try single-line mode via /detect/lane_mode.

Traffic light flicker: tune ROI & HSV; (optionally) debounce in core.

Avoidance fails: timings are open-loop; adjust durations/speeds; test slowly in open space.

Nav2 issues: set initial pose properly; confirm TF; check costmaps & parameters.

7) Repository Structure (high level)

camera/ – camera node publishing /image/image_raw.

detect_lane/ – lane & traffic-light detection
launch/detect_lane_launch.py, launch/detect_traffic_launch.py,
config/hsv_parameters_own.yaml, config/hsv_parameters_tr_own.yaml,
src/detect_lane.py, src/detect_traffic.py

object_detection/ – YOLOv7 sign detection
launch/object_detection_launch.py, weights/sign.pt,
src/object_detection.py, models/, utils/

control/ – control & coordination
src/control_lane.py (PD lane → /cmd_vel)
src/control_avoidance_v2_test.py (avoidance)
src/core.py (coordinator)
src/example_follow_path.py (Nav2 example)

detect_interfaces/ – custom messages (e.g., BoundingBox)
