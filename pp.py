from ultralytics import YOLO
import cv2

model = YOLO('./model/yolov8l.pt')

results = model(source="dog.jpeg", show=True)
cv2.waitKey(0)
