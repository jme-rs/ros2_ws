import rclpy
import cv2
from .camera_node import CameraNode


def main():
    try:
        capture = cv2.VideoCapture(-1)

        rclpy.init()
        camera_node = CameraNode(capture)
        rclpy.spin(camera_node)
    except KeyboardInterrupt:
        pass
    finally:
        capture.release()
        camera_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
