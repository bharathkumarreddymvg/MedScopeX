from ultralytics import YOLO

class YOLODetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, image):
        results = self.model(image, conf=0.4, verbose=False)
        return results[0].boxes.xyxy.cpu().numpy()
