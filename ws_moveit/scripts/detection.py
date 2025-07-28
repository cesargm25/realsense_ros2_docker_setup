import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
import cv2
import matplotlib.pyplot as plt


class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber_node')
        self.subs_depth = self.create_subscription(
            Image,
            '/camera/camera/depth/image_rect_raw',
            self.depth_callback,
            10
        )

        self.sub_color = self.create_subscription(
            Image,
            '/camera/camera/color/image_raw',
            self.image_callback,
            10
        )

        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            cv2.imshow("Color Image", cv_image)
          
            
            # Rango HSV blue
            lower_blue = np.array([100, 150, 50]) # range values taken from internet 
            upper_blue = np.array([140, 255, 255]) # same that above 
            hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
            mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
            result_blue = cv2.bitwise_and(cv_image, cv_image, mask=mask_blue)
            cv2.imshow("Azul Detectado", result_blue)

            kernel2 = np.array([[-1, -1,  -1],
                   [-1, 9, -1],
                   [-1, -1,  -1]])


            sharpened_image2 = cv2.filter2D(cv_image, -1, kernel2)
            cv2.imshow("Color", sharpened_image2)

            cv2.waitKey(1)

            #plt.imshow(cv_image)
            #plt.show()
        except Exception as e:
            self.get_logger().error(f"Error al convertir imagen: {e}")

    def depth_callback(self,msg):
        
            depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
           #depth_value = depth_image[y, x]
            print(depth_image.dtype)
            print(depth_image)





def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
