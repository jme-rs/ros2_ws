from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv2 import VideoCapture


class CameraNode(Node):
    def __init__(self,
                 capture: VideoCapture,
                 topic_name: str = 'camera',
                 timer_period: float = 0.5):

        super().__init__('camera_node')
        self.__capture  = capture
        self.publisher_ = self.create_publisher(Image, topic_name, 10)
        self.timer      = self.create_timer(timer_period, self.__timer_callback)

    def __timer_callback(self):
        # Check if the camera is opened
        if not self.__capture.isOpened():
            self.get_logger().error('Camera not opened')
            return

        has_frame, frame = self.__capture.read()

        # Check if the frame is valid
        if not has_frame:
            self.get_logger().error('No frame')
            return

        # Convert the frame and publish it
        image = CvBridge().cv2_to_imgmsg(frame)
        self.publisher_.publish(image)
        self.get_logger().info('Image published')
