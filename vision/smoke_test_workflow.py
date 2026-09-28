import os
import cv2
import base64
from inference_sdk import InferenceHTTPClient, InferenceConfiguration

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")
WORKSPACE_NAME = "ram-mundhada"
WORKFLOW_ID = "emeergency12-vemeergency12-fjrnz-1-rfdetr-nas-pecoret-t1-6cb5f8-logic"

if not ROBOFLOW_API_KEY:
    raise ValueError("Please set the ROBOFLOW_API_KEY environment variable.")

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=ROBOFLOW_API_KEY
)
client.configure(InferenceConfiguration(api_key_transport="header"))

# Resolve video path relative to current script directory
video_path = os.path.join(BASE_DIR, "lane1.mp4")

if not os.path.exists(video_path):
    raise FileNotFoundError(f"Video file not found at: {video_path}")

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
cap.release()

if not ret or frame is None:
    raise ValueError(f"Could not read frame from {video_path}")

_, buffer = cv2.imencode('.jpg', frame)
base64_image = base64.b64encode(buffer).decode('utf-8')

print("🔍 Sending request to Roboflow Workflow...")
results = client.run_workflow(
    workspace_name=WORKSPACE_NAME,
    workflow_id=WORKFLOW_ID,
    images={"image": base64_image}
)

print("✅ Workflow execution successful!")
print("Output keys returned:", list(results[0].keys()) if results else "Empty response")