
## Project Overview

* **Lane Following** – camera detects yellow/white lines and follows the center.
* **Obstacle Avoidance** – LiDAR detects obstacles ahead and performs a bypass.
* **Traffic Light Detection** – HSV color segmentation for **RED/GREEN** stop–go.
* **Traffic Sign Detection (YOLOv7)** – left/right/stop/park…
* **Navigation (Nav2 + AMCL)** – optional; localize on a saved map and go to goals.
* **Core Coordinator** – orchestrates all modules (stop/go, lane toggle, turns, parking).

---

## System Requirements

* **ROS2:** Humble (Ubuntu 22.04)
* **Robot:** TurtleBot3 (Burger/Waffle) or compatible differential drive
* **Camera:** USB/CSI available as `/dev/video*`
* **LiDAR:** 2D LiDAR publishing `/scan` (e.g., TB3 LDS-01)
* **Compute:** Jetson or PC (GPU recommended for YOLOv7)
* **Motor Controller:** OpenCR or any driver consuming `/cmd_vel`

---

## 1) Workspace Setup (FIRST)

> The repo provides **Docker**. Build inside the container. No extra `pip install torch/opencv` steps here.

### 1.1 Create workspace & clone

```bash
mkdir -p ~/autorace_ws/src
cd ~/autorace_ws/src
git clone https://github.com/aa-beny/autorace0426.git
```

### 1.2 Build & run Docker (provided in repo)

*device → pc/jetson*

```bash
cd ~/autorace_ws/src/autorace0426/src/autorace_docker_humble_gazebro
./build.sh
./run.sh
```

### 1.3 Build the workspace **inside** the Docker terminal

```bash
# you are now inside the container
cd /workspaces/autorace_ws   # or the path used by run.sh
colcon build
source install/setup.bash
```

### 1.4 Device permissions (host or container, as appropriate)

**Camera**

```bash
ls /dev/video*
sudo chmod 666 /dev/video0
```

**Serial devices (OpenCR/LiDAR if serial)**

```bash
ls /dev/ttyUSB* /dev/ttyACM*
sudo chmod 666 /dev/ttyUSB0 /dev/ttyACM0
```

> If devices aren’t visible in Docker, run with `--privileged` and mount `/dev`, or just use the repo’s `run.sh` which already handles it. Ensure X11/GPU access if you need OpenCV windows and/or CUDA.

---

## 2) Quick Start (cheat sheet)

```bash
# optional env helpers
. setup_turtlebot.sh
export ROS_DOMAIN_ID=25
```

**Bring up TB3 base (motors/LiDAR)**

```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_bringup robot.launch.py
```

**Emergency stop (zero velocity)**

```bash
ros2 topic pub /cmd_vel geometry_msgs/Twist \
  "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

**YOLO sign detection**

```bash
ros2 launch object_detection object_detection_launch.py
```

*No YOLO weights? Fake a sign for testing*

```bash
ros2 run detect_lane key_pub_signs
ros2 topic pub -1 /detect/signs std_msgs/String "{data: cave}"
```

**Lane detection (calibrate first, then follow)**

```bash
# calibration mode (pick HSV; RViz shows helper views)
ros2 launch detect_lane detect_lane_launch.py calibration:=True
# saved to: /home/open/autorace0426/src/detect/detect_lane/config/hsv_parameters_own.yaml

# follow mode
ros2 launch detect_lane detect_lane_launch.py calibration:=False
```

**Choose which line to follow**

```bash
# 0: dual, 1: yellow, 2: white
ros2 topic pub -1 /detect/lane_mode std_msgs/Int64 "{data: 1}"
```

**Monitor detection strength**

```bash
ros2 topic echo /detect/yellow_fraction
ros2 topic echo /detect/white_fraction
```

**Core coordinator (recommended)**

```bash
ros2 run core core
```

**PD lane controller**

```bash
ros2 run control control_lane
```

**Traffic lights (HSV)**

```bash
# calibration
ros2 launch detect_lane detect_traffic_launch.py calibration:=True
# saved to: /home/open/autorace0426/src/detect/detect_lane/config/hsv_parameters_tr_own.yaml

# run
ros2 launch detect_lane detect_traffic_launch.py calibration:=False

# no real light? mock it:
ros2 topic pub -1 /detect/traffic_light std_msgs/String "{data: GREEN}"
```

**Mapping (Cartographer) + keyboard teleop**

```bash
ros2 launch turtlebot3_cartographer cartographer.launch.py
ros2 run teleop_twist_keyboard teleop_twist_keyboard
ros2 run nav2_map_server map_saver_cli -f ~/work/map
```

**Navigation (Nav2) with your map**

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/work/map.yaml
ros2 topic echo /initialpose
ros2 topic echo /amcl_pose
ros2 run rqt_reconfigure rqt_reconfigure
```

---

## 3) Launch Order (beginner friendly)

Open **multiple terminals** (all `source install/setup.bash`):

1. **Base bringup**

```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_bringup robot.launch.py
```

2. **Camera + Lane Detection**

```bash
# calibrate OR run (pick one)
ros2 launch detect_lane detect_lane_launch.py calibration:=True
ros2 launch detect_lane detect_lane_launch.py calibration:=False
```

3. **Lane Controller**

```bash
ros2 run control control_lane
```

4. **YOLOv7 Signs**

```bash
ros2 launch object_detection object_detection_launch.py
ros2 topic echo /detect/signs
```

5. **Traffic Lights**

```bash
ros2 launch detect_lane detect_traffic_launch.py calibration:=False
ros2 topic echo /detect/traffic_light
```

6. **Obstacle Avoidance**

```bash
ros2 run control control_avoidance_v2_test.py
```

7. **Navigation (optional)**

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/work/map.yaml
```

8. **Core (optional, recommended)**

```bash
ros2 run core core
```

---

## 4) Feature Modules

### 4.1 Camera & Visualization

* Topic: `/image/image_raw`
* View: `rviz2` (Image), `rqt_image_view`
* Calibration/YOLO open OpenCV windows (configure X11 if needed)

### 4.2 YOLOv7 – Traffic Signs

* Launch: `ros2 launch object_detection object_detection_launch.py`
* Outputs: `/detect/signs` (String), `/detect/bounding_box` (custom msg)
* Params: `weights` (default `sign.pt`), `conf_thres`, `iou_thres`, `device`, `img_size`

### 4.3 Lane Detection & HSV Calibration

* Launch: `detect_lane_launch.py` (use `calibration:=True` first)
* Topics: `/control/lane`, `/detect/yellow_fraction`, `/detect/white_fraction`,
  `/detect/lane_toggle` (Bool), `/detect/lane_mode` (Int64)
* Params: HSV ranges; perspective ROI (`top_x/top_y/bottom_x/bottom_y`)

### 4.4 Traffic Lights (HSV)

* Launch: `detect_traffic_launch.py`
* Publishes `"RED"`/`"GREEN"` on `/detect/traffic_light`
* Calibrate with `calibration:=True` then run with `False`

### 4.5 Obstacle Avoidance (LiDAR)

* Checks a narrow front sector in `/scan` (<\~0.35 m)
* Pauses lane (`/detect/lane_toggle` False), executes timed maneuver, sends `/avoidance_done` True

### 4.6 Navigation (Nav2 + AMCL)

* Build a map (Cartographer/SLAM), save `map.yaml`
* Launch Nav2, set initial pose in RViz, send goals
* Example: `example_follow_path.py` (Nav2 Simple Commander)

---

## 5) Manual Control & Debugging

**Keyboard teleop**

```bash
ros2 run turtlebot3_teleop teleop_keyboard
```

**Software stop**

```bash
# zero velocity
ros2 topic pub /cmd_vel geometry_msgs/Twist \
  "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
# or stop/resume flag
ros2 topic pub -1 /control/go_stop std_msgs/Bool "data: true"
ros2 topic pub -1 /control/go_stop std_msgs/Bool "data: false"
```

**Useful topics**

```bash
ros2 topic echo /detect/signs
ros2 topic echo /detect/traffic_light
ros2 topic echo /control/lane
ros2 topic echo /detect/yellow_fraction
ros2 topic echo /detect/white_fraction
ros2 topic echo /detect/lane_toggle
ros2 topic echo /amcl_pose
ros2 topic echo /cmd_vel
```

---

## 6) Troubleshooting

* **No camera image:** check `/dev/video*`, permissions, only one camera node running.
* **No YOLO detections:** ensure weights exist (Docker image includes), correct topics, try smaller `img_size`.
* **Lane wobbles/loses line:** recalibrate HSV, adjust perspective ROI, try single-line mode.
* **Traffic light flicker:** tune ROI & HSV; optionally debounce in core.
* **Avoidance fails:** timings are open-loop; adjust durations/speeds; test slowly.
* **Nav2 issues:** set initial pose; verify TF; inspect costmaps/params.

---

## 7) Repository Structure (high level)

* **camera/** – camera node publishing `/image/image_raw`
* **detect\_lane/** – lane & traffic lights

  * `launch/detect_lane_launch.py`, `launch/detect_traffic_launch.py`
  * `config/hsv_parameters_own.yaml`, `config/hsv_parameters_tr_own.yaml`
  * `src/detect_lane.py`, `src/detect_traffic.py`
* **object\_detection/** – YOLOv7 signs

  * `launch/object_detection_launch.py`, `weights/sign.pt`
  * `src/object_detection.py`, `models/`, `utils/`
* **control/** – control & coordination

  * `src/control_lane.py`, `src/control_avoidance_v2_test.py`, `src/core.py`, `src/example_follow_path.py`
* **detect\_interfaces/** – custom messages (e.g., `BoundingBox`)

---

## Credits

This README helps juniors run the whole system without bothering the author.
For questions, use **GitHub Issues** so answers are searchable for future students.

Drive safely & have fun! 🚗💨

---

