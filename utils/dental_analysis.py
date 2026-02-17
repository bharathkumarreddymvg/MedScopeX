import cv2
import numpy as np

def analyze_dental(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    dark_pixels = np.sum(blur < 80)
    total_pixels = blur.size
    cavity_ratio = dark_pixels / total_pixels

    if cavity_ratio < 0.15:
        return {
            "range": "0–15%",
            "severity": "Healthy / Early Stage",
            "confidence": "0.82",
            "action": "No treatment required. Maintain oral hygiene."
        }
    elif cavity_ratio < 0.35:
        return {
            "range": "15–35%",
            "severity": "Moderate Decay (Filling likely)",
            "confidence": "0.70",
            "action": "Dental filling recommended."
        }
    else:
        return {
            "range": "35–60%",
            "severity": "Severe Decay (RCT risk)",
            "confidence": "0.86",
            "action": "High risk of root canal. Immediate dental consultation required."
        }
