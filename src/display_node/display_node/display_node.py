from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class DisplayNode(Node):
    def __init__(self, topic_name: str = 'camera'):
        super().__init__('display_node')
        self.subscription = self.create_subscription(
            Image,
            topic_name,
            self._listener_callback,
            10)
        self._cv_bridge = CvBridge()

    def _listener_callback(self, image: Image):
        self.get_logger().info('Image received')
        cv_image = self._cv_bridge.imgmsg_to_cv2(image)
        cv2.imshow('DisplayNode', cv_image)
