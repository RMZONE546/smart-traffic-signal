# 🚦 Smart Traffic System using Computer Vision & AI

An intelligent, real-time AI-powered traffic management system designed to dynamically optimize signal timing based on vehicle density and detect emergency vehicles (ambulances) to grant immediate green wave clearance.

---

## ✨ Features

- **🚨 Real-Time Emergency Clearance:** Uses custom-trained YOLO object detection (`best.pt`) to identify ambulances and prioritize emergency lanes dynamically.
- **📊 Adaptive Traffic Timing:** Calculates traffic density using general vehicle detection (`yolov8n.pt`) and assigns optimal green signal duration (15s / 30s / 45s).
- **🕹️ Manual Override:** Allows control operators to manually force green signals for specific lanes in emergency situations via web API.
- **💻 Live Dashboard:** Real-time web visualization for traffic monitoring and telemetry updates.
- **⚡ Fast & Local Inference:** Powered locally by Ultralytics YOLOv8 for sub-10ms frame processing latency.

---

## 🛠️ Project Architecture & Tech Stack

- **Backend & Vision:** Python, OpenCV, Flask, Flask-CORS, Ultralytics YOLOv8
- **Frontend:** HTML5, CSS3, JavaScript / React / Next.js
- **Model Weights:**
  - `best.pt`: Custom trained model for Emergency Vehicle / Ambulance detection.
  - `yolov8n.pt`: COCO pre-trained model for standard vehicle detection (Cars, Motorcycles, Buses, Trucks).

---

## 📁 Directory Structure

```text
Smart_Traffic_System/
│
├── vision/
│   ├── main.py              # Core Flask backend & YOLO video processing loop
│   ├── best.pt              # Trained weights for ambulance detection
│   ├── yolov8n.pt           # COCO pre-trained weights for general vehicles
│   ├── lane1.mp4            # Input video feed - Lane 1
│   ├── lane2.mp4            # Input video feed - Lane 2
│   ├── lane3.mp4            # Input video feed - Lane 3
│   ├── lane4.mp4            # Input video feed - Lane 4
│   └── requirements.txt     # Python dependencies
│
├── frontend/                # Live monitoring web application
└── README.md
