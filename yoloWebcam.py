from ultralytics import YOLO
import cv2
import math

cap = cv2.VideoCapture(0)
model = YOLO("./model/yolov8l.pt")
cap.set(3, 1280)
cap.set(4, 480)

coco_classes = [
    "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light",
    "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
    "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
    "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
    "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
    "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
    "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
    "hair drier", "toothbrush"
]

while True:
    sucess, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            conf = (math.ceil(box.conf[0] * 100) / 100)
            # cv2.putText(img, f'{conf}', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2, cv2.LINE_AA)
            # print(conf)
            cls = box.cls[0]
            cls = int(cls)
            cls = coco_classes[cls]
            cv2.putText(img, f'{cls}: {conf}', (max(0, x1), max(0, y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (255, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("image", img)
    cv2.waitKey(1)
