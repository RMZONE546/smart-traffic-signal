import cv2
import time
import json
import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, VIDEO_SOURCE
from detector import TrafficDetector

class TrafficPublisher:
    def __init__(self):
        self.detector = TrafficDetector()
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        try:
            self.client.connect(MQTT_BROKER, MQTT_PORT, 60)
            print(f"[MQTT] Connected to broker at {MQTT_BROKER}:{MQTT_PORT}")
        except Exception as e:
            print(f"[MQTT Warning] Could not connect to broker: {e}")

    def start_streaming(self):
        print(f"[INFO] Opening video source: {VIDEO_SOURCE}")
        cap = cv2.VideoCapture(VIDEO_SOURCE)

        if not cap.isOpened():
            print(f"[ERROR] Could not open video file at {VIDEO_SOURCE}. Check the path!")
            return

        # Create a named window explicitly
        cv2.namedWindow("YOLOv8 Real-time Detection Feed", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("YOLOv8 Real-time Detection Feed", 800, 600)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                # Loop video back to beginning
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            # Run detection pipeline
            lane_counts, emergency_detected, annotated_frame = self.detector.detect(frame)

            print(f"[DEBUG] Counts: {lane_counts} | Emergency: {emergency_detected}")

            # Force window rendering
            cv2.imshow("YOLOv8 Real-time Detection Feed", annotated_frame)

            # Essential for OpenCV windows on Windows OS
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

            # Publish payload to MQTT
            payload = {
                "intersection_id": "INT_01",
                "lane_counts": lane_counts,
                "emergency_override": emergency_detected
            }
            try:
                self.client.publish(MQTT_TOPIC, json.dumps(payload))
            except Exception:
                pass

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    publisher = TrafficPublisher()
    publisher.start_streaming()