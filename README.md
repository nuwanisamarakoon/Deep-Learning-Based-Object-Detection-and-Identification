# Deep Learning-Based Object Detection and Identification

## Project Description

This project implements a deep learning–based system for detecting and identifying multiple objects in video using the YOLOv8 model. The system can detect different object classes, draw bounding boxes, and assign unique IDs to track the same objects across frames.

The project is designed as a simple and practical implementation suitable for academic projects, mini-projects, and learning purposes.

---

## Features

- Real-time object detection using YOLOv8  
- Multiple object identification with tracking IDs  
- Supports video input  
- Displays bounding boxes and class labels  
- Easy to run and extend  

---

## Requirements

- Python 3.10 or higher  
- OpenCV  
- Ultralytics YOLOv8  

Install dependencies:
- pip install -r requirements.txt

---

## Setup
1. Create and activate a virtual environment (optional but recommended).
2. Download the YOLOv8 pretrained model (yolov8n.pt) and place it in the models/ folder.
3. Add your test video to the data/ folder and name it input_video.mp4 (or update the path in the code).

---

## Running the Project
- Object Detection Only
     python src/detect.py

This will show detected objects with bounding boxes and labels.

- Object Detection with Tracking
      python src/track.py

This will show detected objects along with unique IDs for multiple object identification.

Press q to close the output window.

---

## Output
 - Bounding boxes around detected objects
 - Class names such as person, cup, laptop, etc.
 - Tracking IDs when running track.py

---

## Notes
- Performance depends on your hardware.
- You can change the output window size in the code if the display is too large.
- The project can be extended with features like object counting or saving output video.

---

## References
- Ultralytics YOLOv8 Documentation
- OpenCV Documentation

---

