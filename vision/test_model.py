import os
import cv2
from ultralytics import YOLO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best.pt")
VIDEO_PATH = os.path.join(BASE_DIR, "lane1.mp4")

model = YOLO(MODEL_PATH)
cap = cv2.VideoCapture(VIDEO_PATH)

print("Scanning lane1.mp4 for class 1 (ambulance) detections...")

frame_idx = 0
found = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_idx += 1
    # Run inference with a lower confidence threshold to catch weak predictions
    results = model(frame, conf=0.05, verbose=False)[0]
    
    if results.boxes is not None and len(results.boxes) > 0:
        for b in results.boxes:
            cls_id = int(b.cls[0])
            conf = float(b.conf[0])
            if cls_id == 1:
                print(f"Frame {frame_idx}: Ambulance detected with confidence {conf:.4f}")
                found = True

if not found:
    print("No class 1 (ambulance) detections found even at conf=0.05.")

cap.release()