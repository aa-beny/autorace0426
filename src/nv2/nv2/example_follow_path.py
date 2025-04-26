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
    initial_pose.pose.position.x = 0.0638553818788543
    initial_pose.pose.position.y = 0.03418011885167457
    initial_pose.pose.position.z = 0.0
    initial_pose.pose.orientation.x = 0.0
    initial_pose.pose.orientation.y = 0.0
    initial_pose.pose.orientation.z = -0.017536317467315484
    initial_pose.pose.orientation.w = 0.9998462269617692

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
    goal_pose1.pose.position.x = 0.20929201700611055
    goal_pose1.pose.position.y = 0.03841473653502412
    goal_pose1.pose.position.z = 0.0
    goal_pose1.pose.orientation.x = 0.0
    goal_pose1.pose.orientation.y = 0.0
    goal_pose1.pose.orientation.z = 0.09119001108226422
    goal_pose1.pose.orientation.w = 0.995833511124634
    goal_poses.append(goal_pose1)

    # goal_pose2
    goal_pose2 = PoseStamped()
    goal_pose2.header.frame_id = 'map'
    goal_pose2.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose2.pose.position.x = 0.39809473237791926
    goal_pose2.pose.position.y = 0.08971307194005947
    goal_pose2.pose.position.z = 0.0
    goal_pose2.pose.orientation.x = 0.0
    goal_pose2.pose.orientation.y = 0.0
    goal_pose2.pose.orientation.z = 0.19276334163875575
    goal_pose2.pose.orientation.w = 0.9812452772473661
    goal_poses.append(goal_pose2)

    # goal_pose3
    goal_pose3 = PoseStamped()
    goal_pose3.header.frame_id = 'map'
    goal_pose3.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose3.pose.position.x = 0.61599327499747
    goal_pose3.pose.position.y = 0.19993619888445993
    goal_pose3.pose.position.z = 0.0
    goal_pose3.pose.orientation.x = 0.0
    goal_pose3.pose.orientation.y = 0.0
    goal_pose3.pose.orientation.z = 0.26026199412987794
    goal_pose3.pose.orientation.w = 0.9655380336431804
    goal_poses.append(goal_pose3)

    # goal_pose4
    goal_pose4 = PoseStamped()
    goal_pose4.header.frame_id = 'map'
    goal_pose4.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose4.pose.position.x = 0.8272747434660263
    goal_pose4.pose.position.y = 0.31582538404203897
    goal_pose4.pose.position.z = 0.0
    goal_pose4.pose.orientation.x = 0.0
    goal_pose4.pose.orientation.y = 0.0
    goal_pose4.pose.orientation.z = 0.29818806916805873
    goal_pose4.pose.orientation.w = 0.9545071374305302
    goal_poses.append(goal_pose4)

    # goal_pose5
    goal_pose5 = PoseStamped()
    goal_pose5.header.frame_id = 'map'
    goal_pose5.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose5.pose.position.x = 1.0088542801718865
    goal_pose5.pose.position.y = 0.48225436412108147
    goal_pose5.pose.position.z = 0.0
    goal_pose5.pose.orientation.x = 0.0
    goal_pose5.pose.orientation.y = 0.0
    goal_pose5.pose.orientation.z = 0.37450767898731113
    goal_pose5.pose.orientation.w = 0.9272238124528172
    goal_poses.append(goal_pose5)

    # goal_pose6
    goal_pose6 = PoseStamped()
    goal_pose6.header.frame_id = 'map'
    goal_pose6.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose6.pose.position.x = 1.1952124335469083
    goal_pose6.pose.position.y = 0.6309276046619843
    goal_pose6.pose.position.z = 0.0
    goal_pose6.pose.orientation.x = 0.0
    goal_pose6.pose.orientation.y = 0.0
    goal_pose6.pose.orientation.z = 0.34636390015738394
    goal_pose6.pose.orientation.w = 0.9381002338064764
    goal_poses.append(goal_pose6)

    # goal_pose7
    goal_pose7 = PoseStamped()
    goal_pose7.header.frame_id = 'map'
    goal_pose7.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose7.pose.position.x = 1.3708184104448151
    goal_pose7.pose.position.y = 0.7917121104693104
    goal_pose7.pose.position.z = 0.0
    goal_pose7.pose.orientation.x = 0.0
    goal_pose7.pose.orientation.y = 0.0
    goal_pose7.pose.orientation.z = 0.34992967008554504
    goal_pose7.pose.orientation.w = 0.9367759742829774
    goal_poses.append(goal_pose7)

    # goal_pose8
    goal_pose8 = PoseStamped()
    goal_pose8.header.frame_id = 'map'
    goal_pose8.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose8.pose.position.x = 1.5438731285369074
    goal_pose8.pose.position.y = 0.9451479040624252
    goal_pose8.pose.position.z = 0.0
    goal_pose8.pose.orientation.x = 0.0
    goal_pose8.pose.orientation.y = 0.0
    goal_pose8.pose.orientation.z = 0.39813907658271486
    goal_pose8.pose.orientation.w = 0.9173250654472835
    goal_poses.append(goal_pose8)

    # # goal_pose9
    # goal_pose9 = PoseStamped()
    # goal_pose9.header.frame_id = 'map'
    # goal_pose9.header.stamp = navigator.get_clock().now().to_msg()
    # goal_pose9.pose.position.x = 1.712639779994931
    # goal_pose9.pose.position.y = 1.13416616024452
    # goal_pose9.pose.position.z = 0.0
    # goal_pose9.pose.orientation.x = 0.0
    # goal_pose9.pose.orientation.y = 0.0
    # goal_pose9.pose.orientation.z = 0.4339693640335123
    # goal_pose9.pose.orientation.w = 0.9009276281035835
    # goal_poses.append(goal_pose9)

    # # goal_pose10
    # goal_pose10 = PoseStamped()
    # goal_pose10.header.frame_id = 'map'
    # goal_pose10.header.stamp = navigator.get_clock().now().to_msg()
    # goal_pose10.pose.position.x = 1.889539367442386
    # goal_pose10.pose.position.y = 1.3505246003918334
    # goal_pose10.pose.position.z = 0.0
    # goal_pose10.pose.orientation.x = 0.0
    # goal_pose10.pose.orientation.y = 0.0
    # goal_pose10.pose.orientation.z = 0.5167162696587929
    # goal_pose10.pose.orientation.w = 0.8561567010015758
    # goal_poses.append(goal_pose10)

    # goal_pose11 - 使用amcl.txt的最後一個點位
    goal_pose11 = PoseStamped()
    goal_pose11.header.frame_id = 'map'
    goal_pose11.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose11.pose.position.x = 1.9672345824904196
    goal_pose11.pose.position.y = 1.4500631211937838
    goal_pose11.pose.position.z = 0.0
    goal_pose11.pose.orientation.x = 0.0
    goal_pose11.pose.orientation.y = 0.0
    goal_pose11.pose.orientation.z = 0.5924126581838589
    goal_pose11.pose.orientation.w = 0.8056346829820166
    goal_poses.append(goal_pose11)

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
