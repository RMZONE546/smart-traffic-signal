import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Updated to include the nested 'vision/sample_videos' folder path
VIDEO_SOURCE = os.path.join(BASE_DIR, "vision", "sample_videos", "ambulance_scene.mp4")

# Option B: If your folder is named 'sample_videos'
# VIDEO_SOURCE = os.path.join(BASE_DIR, "sample_videos", "ambulance_scene.mp4")
CONFIDENCE_THRESHOLD = 0.3

# MQTT Broker Settings
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "traffic/intersection_1"

# Class mappings based on COCO dataset (YOLOv8)
VEHICLE_CLASSES = [2, 3, 5, 7]  # Car, motorcycle, bus, truck
EMERGENCY_CLASSES = ["ambulance", "fire truck"]  # Custom or matched via label names