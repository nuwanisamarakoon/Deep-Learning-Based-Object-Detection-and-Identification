from ultralytics import YOLO
import cv2

model = YOLO("D:/Projects/Deep Learning-Based Object Detection and Identification/models/yolov8n.pt")
video_path = "D:/Projects/Deep Learning-Based Object Detection and Identification/data/input_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ERROR: Could not open video. Check the path!")
    exit()
else:
    print("Video opened successfully!")
    
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, persist=True)
    annotated = results[0].plot()

    annotated_small = cv2.resize(annotated, (800, 500))
    cv2.imshow("Object Detection + Tracking", annotated_small)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
