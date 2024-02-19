from ultralytics import YOLO
import cv2
import math
from poker import find_poker_hand

cap = cv2.VideoCapture(0)
# add your trained model path/location trained over dataset
model = YOLO("./model/yolov8l-trained.pt")
cap.set(3, 1280)
cap.set(4, 480)


poker_classes = ['10C', '10D', '10H', '10S', '2C',
                 '2D', '2H', '2S', '3C', '3D', '3H',
                 '3S', '4C', '4D', '4H', '4S', '5C',
                 '5D', '5H', '5S', '6C', '6D', '6H',
                 '6S', '7C', '7D', '7H', '7S', '8C',
                 '8D', '8H', '8S', '9C', '9D', '9H',
                 '9S', 'AC', 'AD', 'AH', 'AS', 'JC',
                 'JD', 'JH', 'JS', 'KC', 'KD', 'KH',
                 'KS', 'QC', 'QD', 'QH', 'QS']

while True:
    sucess, img = cap.read()
    results = model(img, stream=True)
    hand = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            conf = (math.ceil(box.conf[0] * 100) / 100)
            cls = box.cls[0]
            cls = int(cls)
            cls = poker_classes[cls]
            # cv2.putText(img, f'{cls}: {conf}', (max(0, x1), max(0, y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
            #             (255, 0, 255), 2, cv2.LINE_AA)
            if conf >= 0.5:
                hand.append(cls)
    hand=list(set(hand))
    if len(hand) == 5:
        results = find_poker_hand(hand)
    cv2.putText(img, f'Poker Hand={results}', (max(0, x1), max(0, y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                (255, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("image", img)
    cv2.waitKey(1)
