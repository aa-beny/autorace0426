import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import time
import math

Direct = ""
cnt = 1

class LaserScanSubscriber(Node):

    def __init__(self):
        super().__init__('laser_scan_subscriber')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 100)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',  # 修改为你的激光雷达话题名称
            self.scan_callback,
            10)
        self.subscription  # 防止被Python清理掉

        self.pub_stop = self.create_publisher(Bool, '/GO_STOP', 1)
        self.pub_lane_toggle = self.create_publisher(Bool, 'detect/lane_toggle', 1)

    def scan_callback(self, msg):
        global Direct
        global cnt


        # print(msg.angle_min)
        # print(msg.angle_max)

        # # 角度增量（弧度）
        # print(msg.angle_increment)

        # print( int((math.radians(172) - msg.angle_min) / msg.angle_increment))

        # print(msg.angle_increment)

        # # 距离列表
        print(len(msg.ranges))
        # print(msg.ranges)

        # raise SystemExit

        #self.get_logger().info('a')
        distenceUp, distenceDown, distenceRight, distenceLeft = self.find_distance_forward(msg)
        #print(distenceUp, distenceDown, distenceRight, distenceLeft)
        print(distenceUp)

        for i in distenceUp:
            if i<=0.2:
                Direct = "Up"
                print( str(cnt) + " " + Direct)
                cnt = cnt + 1
                break

        for i in distenceDown:
            if i<=0.2:
                Direct = "Down"
                print( str(cnt) + " " + Direct)
                cnt = cnt + 1
                break

        for i in distenceRight:
            if i<=0.2:
                Direct = "Right"
                print( str(cnt) + " " + Direct)
                cnt = cnt + 1
                break

        for i in distenceLeft:
            if i<=0.2:
                Direct = "Left"
                print( str(cnt) + " " + Direct)
                cnt = cnt + 1
                break

        # stop_msg = Bool()
        # pub_lane_msg = Bool()
        # for i in distenceUp:
        #     self.get_logger().info('Distance at  degrees: %f' % i)
        #     if i<=0.3:
        #         # 將車停下來
        #         self.get_logger().info('STOP')
        #         stop_msg.data = True
        #         self.pub_stop.publish(stop_msg)
        #         self.get_logger().info('GO')
        #         stop_msg.data = False
        #         self.pub_stop.publish(stop_msg)

        #         #停止循線模式
        #         pub_lane_msg.data = False
        #         self.pub_lane_toggle.publish(pub_lane_msg)

        #         # msg_motor=Twist()
        #         # msg_motor.linear.x=50.0
        #         # msg_motor.angular.z=5.2
        #         # self.publisher_.publish(msg_motor)
        #         # time.sleep(3)
        #         # msg_motor.linear.x=50.0
        #         # msg_motor.angular.z=0.0
        #         # self.publisher_.publish(msg_motor)
        #         # time.sleep(3)
        #         # msg_motor.linear.x=50.0
        #         # msg_motor.angular.z=-3.0
        #         # self.publisher_.publish(msg_motor)
        #         # time.sleep(4)
        #         # msg_motor.linear.x=50.0
        #         # msg_motor.angular.z=-8.0
        #         # self.publisher_.publish(msg_motor)
        #         # time.sleep(2)
        #         # msg_motor.linear.x=50.0
        #         # msg_motor.angular.z=0.0
        #         # self.publisher_.publish(msg_motor)
        #         # time.sleep(6)
        #         # msg_motor.linear.x=50.0
        #         # msg_motor.angular.z=5.0
        #         # self.publisher_.publish(msg_motor)
        #         # time.sleep(2.7)
        #         # msg_motor.linear.x=0.0
        #         # msg_motor.angular.z=0.0
        #         # self.publisher_.publish(msg_motor)
        #         # time.sleep(1)

        #         ## 切回循線模式
        #         pub_lane_msg.data = True
        #         self.pub_lane_toggle.publish(pub_lane_msg)
        #         raise SystemExit
        #         # break
        #          # 左轉
        #     else:
        #         pass #不動作    
        # # if distance_at_90_degrees is not None:
        # #     self.get_logger().info('Distance at 90 degrees: %f' % distance_at_90_degrees)
        # # else:
        # #     self.get_logger().warn('No valid distance found at 90 degrees.')


    def find_distance_forward(self, scan_msg):
        # 角度范围（弧度）
        angle_min = scan_msg.angle_min  #start angle of the scan 
        angle_max = scan_msg.angle_max  # angular distance between measurements


        # 角度增量（弧度）0.005806980188935995
        angle_increment = scan_msg.angle_increment

        # 距离列表

        # 園的全弧切分成angle_increment等份
        #（2Pi) / angle_increment(0.005806980188935995) = 1082 等份/園的全弧
        ranges = scan_msg.ranges

        forward_degrees_Down=[]
        forward_degrees_Up=[]
        forward_degrees_Right=[]
        forward_degrees_Left=[]
        idx_forward_degrees_Down=[]
        idx_forward_degrees_Up=[]#用陣列去存切到第幾個
        idx_forward_degrees_Right=[]
        idx_forward_degrees_Left=[]
        distenceDown=[]
        distenceUp=[]
        distenceRight=[]
        distenceLeft=[]
        # 计算90度对应的索引

        angle_min = 0

        #            (Left)
        #             270
        #              |
        # （Down) 0 <--+--> 180 (Up) (Power switch)
        #  (Backward)  |    (Forward)
        #             90
        #            (Right)

        angleW = 2
        idx = 180
        for i in range(idx,idx+angleW):
            forward_degrees_Up.append(math.radians(i))  # 将180度(i地一次跑是180）转换为弧度
                                                        # 弧度/angle_increment =lidar ranges位置0
            idx_forward_degrees_Up.append(int((forward_degrees_Up[i-idx] - angle_min) / angle_increment))

            # 如果索引在范围内，则返回对应的距离；否则返回None
            if idx_forward_degrees_Up[i-idx] >= 0 and idx_forward_degrees_Up[i-idx] < len(ranges):
                # return ranges[idx_90_degrees]
                #idx_forward_degrees_Up[i-idx]是這列第幾個後，
                #ranges陣列裡面的直是距離，單位是公尺
                distenceUp.append(ranges[idx_forward_degrees_Up[i-idx]])
            else:
                return None

        idx = 0
        for i in range(idx,idx+angleW):
            forward_degrees_Down.append(math.radians(i))  # 将90度转换为弧度
            idx_forward_degrees_Down.append(int((forward_degrees_Down[i-idx] - angle_min) / angle_increment))
            # 如果索引在范围内，则返回对应的距离；否则返回None
            if idx_forward_degrees_Down[i-idx] >= 0 and idx_forward_degrees_Down[i-idx] < len(ranges):
                # return ranges[idx_90_degrees]
                distenceDown.append(ranges[idx_forward_degrees_Down[i-idx]])
            else:
                return None

        idx = 90
        for i in range(idx,idx+angleW):
            forward_degrees_Right.append(math.radians(i))  # 将90度转换为弧度
            idx_forward_degrees_Right.append(int((forward_degrees_Right[i-idx] - angle_min) / angle_increment))
            # 如果索引在范围内，则返回对应的距离；否则返回None
            if idx_forward_degrees_Right[i-idx] >= 0 and idx_forward_degrees_Right[i-idx] < len(ranges):
                # return ranges[idx_90_degrees]
                distenceRight.append(ranges[idx_forward_degrees_Right[i-idx]])
            else:
                return None                

        idx = 270
        for i in range(idx,idx+angleW):
            forward_degrees_Left.append(math.radians(i))  # 将90度转换为弧度
            idx_forward_degrees_Left.append(int((forward_degrees_Left[i-idx] - angle_min) / angle_increment))
            # 如果索引在范围内，则返回对应的距离；否则返回None
            if idx_forward_degrees_Left[i-idx] >= 0 and idx_forward_degrees_Left[i-idx] < len(ranges):
                # return ranges[idx_90_degrees]
                distenceLeft.append(ranges[idx_forward_degrees_Left[i-idx]])
            else:
                return None                

        return distenceUp, distenceDown, distenceRight, distenceLeft
    

def main(args=None):
    rclpy.init(args=args)
    laser_scan_subscriber = LaserScanSubscriber()
    try:
        rclpy.spin(laser_scan_subscriber)
    except SystemExit:                 # <--- process the exception 
        rclpy.logging.get_logger("Quitting").info('Done')
    rclpy.shutdown()

if __name__ == '__main__':
    main()