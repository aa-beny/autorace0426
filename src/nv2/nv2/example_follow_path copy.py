#! /usr/bin/env python3
# Copyright 2021 Samsung Research America
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration

"""
Basic navigation demo to go to poses.
"""


def main():
    rclpy.init()

    navigator = BasicNavigator()
    # Set our demo's initial pose
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = -0.008755388600450447
    initial_pose.pose.position.y = -0.04571622571244375
    initial_pose.pose.orientation.z = 0.02985593111598092
    initial_pose.pose.orientation.w = 0.9995542123252734

    navigator.setInitialPose(initial_pose)

    # Activate navigation, if not autostarted. This should be called after setInitialPose()
    # or this will initialize at the origin of the map and update the costmap with bogus readings.
    # If autostart, you should `waitUntilNav2Active()` instead.
    # navigator.lifecycleStartup()

    # Wait for navigation to fully activate, since autostarting nav2
    navigator.waitUntilNav2Active()

    # If desired, you can change or load the map as well
    # navigator.changeMap('/path/to/map.yaml')

    # You may use the navigator to clear or obtain costmaps
    # navigator.clearAllCostmaps()  # also have clearLocalCostmap() and clearGlobalCostmap()
    # global_costmap = navigator.getGlobalCostmap()
    # local_costmap = navigator.getLocalCostmap()

    # set our demo's goal poses
    goal_poses = []

    # goal_pose1
    goal_pose1 = PoseStamped()
    goal_pose1.header.frame_id = 'map'
    goal_pose1.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose1.pose.position.x = 0.2483252469955661
    goal_pose1.pose.position.y = -0.023350539394781235
    goal_pose1.pose.orientation.z = 0.11815610916939469
    goal_pose1.pose.orientation.w = 0.9929950321456549
    goal_poses.append(goal_pose1)

    # goal_pose2
    goal_pose2 = PoseStamped()
    goal_pose2.header.frame_id = 'map'
    goal_pose2.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose2.pose.position.x = 0.45215008253154965
    goal_pose2.pose.position.y = 0.04319357386325123
    goal_pose2.pose.orientation.z = 0.22103633776241202
    goal_pose2.pose.orientation.w = 0.9752655727485621
    goal_poses.append(goal_pose2)

    # goal_pose3
    goal_pose3 = PoseStamped()
    goal_pose3.header.frame_id = 'map'
    goal_pose3.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose3.pose.position.x = 0.6617469550211063
    goal_pose3.pose.position.y = 0.1791635953912873
    goal_pose3.pose.orientation.z = 0.29291118394057086
    goal_pose3.pose.orientation.w = 0.9561396541941627
    goal_poses.append(goal_pose3)

    # goal_pose4
    goal_pose4 = PoseStamped()
    goal_pose4.header.frame_id = 'map'
    goal_pose4.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose4.pose.position.x = 0.8778726500521002
    goal_pose4.pose.position.y = 0.36030445279235923
    goal_pose4.pose.orientation.z = 0.4010480384786237
    goal_pose4.pose.orientation.w = 0.9160570237886113
    goal_poses.append(goal_pose4)

    # goal_pose5
    goal_pose5 = PoseStamped()
    goal_pose5.header.frame_id = 'map'
    goal_pose5.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose5.pose.position.x = 1.0660142077750083
    goal_pose5.pose.position.y = 0.5911921657644755
    goal_pose5.pose.orientation.z = 0.484235614316722
    goal_pose5.pose.orientation.w = 0.8749376376789987
    goal_poses.append(goal_pose5)

    # goal_pose6
    goal_pose6 = PoseStamped()
    goal_pose6.header.frame_id = 'map'
    goal_pose6.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose6.pose.position.x = 1.2431806994757406
    goal_pose6.pose.position.y = 0.8493170285631956
    goal_pose6.pose.orientation.z = 0.4366957383322743
    goal_pose6.pose.orientation.w = 0.8996092663609184
    goal_poses.append(goal_pose6)

    # goal_pose7
    goal_pose7 = PoseStamped()
    goal_pose7.header.frame_id = 'map'
    goal_pose7.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose7.pose.position.x = 1.416792004908876
    goal_pose7.pose.position.y = 1.0554454368514283
    goal_pose7.pose.orientation.z = 0.38276228294296455
    goal_pose7.pose.orientation.w = 0.9238468675902354
    goal_poses.append(goal_pose7)

    # goal_pose8
    goal_pose8 = PoseStamped()
    goal_pose8.header.frame_id = 'map'
    goal_pose8.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose8.pose.position.x = 1.5881703507551466
    goal_pose8.pose.position.y = 1.2571537642095576
    goal_pose8.pose.orientation.z = 0.4302682014406602
    goal_pose8.pose.orientation.w = 0.9027010993839653
    goal_poses.append(goal_pose8)

    # goal_pose9
    goal_pose9 = PoseStamped()
    goal_pose9.header.frame_id = 'map'
    goal_pose9.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose9.pose.position.x = 1.7038666280741648
    goal_pose9.pose.position.y = 1.4351763243975486
    goal_pose9.pose.orientation.z = 0.5263695802514705
    goal_pose9.pose.orientation.w = 0.8502558820648586
    goal_poses.append(goal_pose9)

    # goal_pose10
    goal_pose10 = PoseStamped()
    goal_pose10.header.frame_id = 'map'
    goal_pose10.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose10.pose.position.x = 1.7288826799689576
    goal_pose10.pose.position.y = 1.51305318681493
    goal_pose10.pose.orientation.z = 0.6171938963972685
    goal_pose10.pose.orientation.w = 0.7868110918447692
    goal_poses.append(goal_pose10)

    # sanity check a valid path exists
    # path = navigator.getPathThroughPoses(initial_pose, goal_poses)

    navigator.goThroughPoses(goal_poses)

    i = 0
    while not navigator.isTaskComplete():
        ################################################
        #
        # Implement some code here for your application!
        #
        ################################################

        # Do something with the feedback
        i = i + 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
            print(
                'Estimated time of arrival: '
                + '{0:.0f}'.format(
                    Duration.from_msg(feedback.estimated_time_remaining).nanoseconds
                    / 1e9
                )
                + ' seconds.'
            )

            # Some navigation timeout to demo cancellation
            if Duration.from_msg(feedback.navigation_time) > Duration(seconds=120.0):
                #navigator.lifecycleShutdown()
                exit(0)
            # if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
            #     navigator.cancelTask()

            # # Some navigation request change to demo preemption
            # if Duration.from_msg(feedback.navigation_time) > Duration(seconds=35.0):
            #     goal_pose4 = PoseStamped()
            #     goal_pose4.header.frame_id = 'map'
            #     goal_pose4.header.stamp = navigator.get_clock().now().to_msg()
            #     goal_pose4.pose.position.x = 0.0
            #     goal_pose4.pose.position.y = 0.0
            #     goal_pose4.pose.orientation.w = 1.0
            #     goal_pose4.pose.orientation.z = 0.0
            #     navigator.goThroughPoses([goal_pose4])

    # Do something depending on the return code
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')

    navigator.lifecycleShutdown()

    exit(0)


if __name__ == '__main__':
    main()
