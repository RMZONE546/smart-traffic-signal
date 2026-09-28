import os
import cv2
from ultralytics import YOLO

class TrafficDetector:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        custom_path = os.path.join(base_dir, "best.pt")

        # 1. Base YOLOv8 model for standard traffic density (cars, buses, trucks, motorcycles)
        print("[YOLO] Loading base vehicle detector (yolov8n.pt)...")
        self.base_model = YOLO("yolov8n.pt")

        # 2. Custom trained YOLOv8 model for ambulance detection
        if os.path.exists(custom_path):
            print(f"[YOLO] Loading custom emergency model from: {custom_path}")
            self.emergency_model = YOLO(custom_path)
        else:
            print("[YOLO Warning] 'best.pt' not found! Using base model fallback.")
            self.emergency_model = None

    def detect(self, frame):
        lane_counts = {"lane_1": 0, "lane_2": 0, "lane_3": 0, "lane_4": 0}
        emergency_detected = False
        frame_width = frame.shape[1]

        # --- STEP A: Run Base Model for Lane Traffic Counts ---
        base_results = self.base_model(frame, conf=0.30, verbose=False)
        
        if base_results and len(base_results) > 0:
            boxes = base_results[0].boxes
            for box in boxes:
                cls_id = int(box.cls[0].item())
                
                # COCO classes: 2 = car, 3 = motorcycle, 5 = bus, 7 = truck
                if cls_id in [2, 3, 5, 7]:
                    x_center = (box.xyxy[0][0].item() + box.xyxy[0][2].item()) / 2.0

                    # Assign vehicle to lane based on x position
                    if x_center < frame_width * 0.25:
                        lane_counts["lane_1"] += 1
                    elif x_center < frame_width * 0.50:
                        lane_counts["lane_2"] += 1
                    elif x_center < frame_width * 0.75:
                        lane_counts["lane_3"] += 1
                    else:
                        lane_counts["lane_4"] += 1

            annotated_frame = base_results[0].plot()
        else:
            annotated_frame = frame

        # --- STEP B: Run Custom Emergency Model ONLY for Emergency Detection ---
        if self.emergency_model:
            # Set confidence threshold to 0.35 to filter out random noise
            custom_results = self.emergency_model(frame, conf=0.35, verbose=False)
            if custom_results and len(custom_results) > 0:
                custom_boxes = custom_results[0].boxes
                for box in custom_boxes:
                    cls_id = int(box.cls[0].item())
                    class_name = self.emergency_model.names[cls_id].lower()
                    
                    # Flag emergency ONLY if custom model detects an object
                    emergency_detected = True
                    print(f"[ALERT] Emergency vehicle detected: {class_name}")

                annotated_frame = custom_results[0].plot(img=annotated_frame)

        return lane_counts, emergency_detected, annotated_frame