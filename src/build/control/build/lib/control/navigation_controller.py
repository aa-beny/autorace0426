import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from std_srvs.srv import Trigger

class NavigationController(Node):
    def __init__(self):
        super().__init__('navigation_controller')
        self.goal_publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.declare_service = self.create_service(Trigger, 'start_navigation', self.start_navigation)
        self.cached_goal = None

        self.subscription = self.create_subscription(
            PoseStamped,
            '/rviz2_goal_pose',
            self.goal_callback,
            10
        )

        self.get_logger().info("Navigation Controller Initialized. Use the 'start_navigation' service to trigger navigation.")

    def goal_callback(self, msg):
        self.cached_goal = msg
        self.get_logger().info(f"Received new goal: x={msg.pose.position.x}, y={msg.pose.position.y}")

    def start_navigation(self, request, response):
        if self.cached_goal:
            self.goal_publisher.publish(self.cached_goal)
            self.get_logger().info("Navigation goal published, starting movement.")
            response.success = True
            response.message = "Goal sent successfully."
        else:
            self.get_logger().warn("No goal received yet!")
            response.success = False
            response.message = "No goal available to send."

        return response


def main(args=None):
    rclpy.init(args=args)
    node = NavigationController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
