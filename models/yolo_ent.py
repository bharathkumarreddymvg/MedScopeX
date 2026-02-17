from ultralytics import YOLO
import cv2

class YOLOENTDetector:
    def __init__(self):
        # lightweight + realtime
        self.model = YOLO("yolov8n.pt")

        # We map COCO classes logically
        self.ent_classes = {
            "person": "face",
        }

    def detect(self, image):
        results = self.model(image, conf=0.35, verbose=False)

        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]

                if label == "person":
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    roi = image[y1:y2, x1:x2]

                    detections.append({
                        "label": "face_region",
                        "roi": roi,
                        "confidence": float(box.conf[0])
                    })

        return detections
