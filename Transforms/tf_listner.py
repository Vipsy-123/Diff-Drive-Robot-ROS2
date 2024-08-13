import rclpy
from rclpy.node import Node
from tf2_ros.buffer import Buffer
from tf2_ros import TransformException
from tf2_ros.transform_listener import TransformListener

class FrameListener(Node):
    def __init__(self):
        super().__init__('sample_tf2_frame_listener')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(1.0, self.on_timer)
        
    def on_timer(self):
        from_frame_rel = 'obj_1'
        to_frame_rel = 'base_link'
        try:
            t = self.tf_buffer.lookup_transform( to_frame_rel, from_frame_rel)
            self.get_logger().info(f'Successfully received data!')
        except TransformException as e:
            self.get_logger().info(f'Could not transform {to_frame_rel} to {from_frame_rel}')
            return
        # Logging transform data...
        self.get_logger().info(f'Translation X: {t.transform.translation}')
        self.get_logger().info(f'Translation Y: {t.transform.translation}')
        self.get_logger().info(f'Translation Z: {t.transform.translation}')
        self.get_logger().info(f'Rotation X: {t.transform.rotation.x}')
        self.get_logger().info(f'Rotation Y: {t.transform.rotation.y}')
        self.get_logger().info(f'Rotation Z: {t.transform.rotation.z}')
        self.get_logger().info(f'Rotation W: {t.transform.rotation.w}')
        
def main():
    rclpy.init()
    node = FrameListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()