AI Bird Detection System (YOLOv8)

A real-time bird detection system built using YOLOv8 and OpenCV.
This project detects birds from a webcam feed and displays bounding boxes with confidence scores.

⚠️ Current Status:
This repository currently contains only the AI detection module.
Hardware integration (Arduino + deterrent system) is planned for future development.

Project Overview

This project uses a custom-trained YOLOv8 model to detect birds in real time from a webcam feed.

When a bird is detected:

A bounding box is drawn around the object
Confidence score is displayed
A “BIRD DETECTED” alert appears on screen
The system includes filtering mechanisms to reduce false positives.

Features

Real-time webcam detection,
Custom-trained YOLOv8 model,
Confidence threshold filtering,
Minimum bounding box size filtering,
Clean OpenCV-based visualization,
Lightweight and fast inference

Requirements

Software:
Python 3.9+
Ultralytics YOLOv8
OpenCV (non-headless version)

Hardware (Current Version):
Laptop / PC
Webcam

Installation

1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/bird-detection.git
cd bird-detection
```

2️⃣ Create a Virtual Environment
```bash
python3 -m venv bird-env
source bird-env/bin/activate
```

On Windows:
```powershell
python -m venv bird-env
bird-env\Scripts\Activate.ps1
```
3️⃣ Install Dependencies
```bash
pip install --upgrade pip
pip install ultralytics opencv-python
```
Important: Do NOT install opencv-python-headless, otherwise the display window will not open.

 Model Training (Optional)

If you want to train your own bird detection model:
```bash
yolo detect train \
  model=yolov8n.pt \
  data=data.yaml \
  epochs=100 \
  imgsz=640
```
After training, your model will be saved at:
runs/detect/train/weights/best.pt
Update the model path in bird.py if necessary.

Running the Detection System
```bash
python bird.py
```
Press Q to exit the detection window.

Detection Filtering Logic

To reduce false positives, two filtering mechanisms are used:

Confidence Threshold:
Only detections above this confidence level are considered valid:
CONF_THRESHOLD = 0.65

Minimum Bounding Box Area:
Small detections (likely noise) are ignored
MIN_BOX_AREA = 3000
These values can be adjusted inside bird.py to balance sensitivity and accuracy.

Troubleshooting

If too many false positives

Increase:

CONF_THRESHOLD = 0.7

MIN_BOX_AREA = 5000

No detections
Verify the model path is correct,
Ensure the webcam is accessible,
Lower the confidence threshold slightly

Future Work

Arduino integration,
Pan-tilt servo tracking,
Visual deterrent activation,
Edge device deployment (Jetson / Raspberry Pi),
Field testing in agricultural environments
