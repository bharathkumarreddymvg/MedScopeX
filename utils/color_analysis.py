import cv2
import numpy as np

def inflammation_score(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    saturation = np.mean(hsv[:, :, 1])
    redness = np.mean(image[:, :, 2] - image[:, :, 1])
    return saturation, redness

def analyze_ear(image):
    sat, red = inflammation_score(image)

    if red < 10:
        return {
            "severity": "Normal",
            "confidence": "0.80",
            "recommendation": "Healthy ear canal appearance."
        }
    elif red < 30:
        return {
            "severity": "Mild Inflammation",
            "confidence": "0.65",
            "recommendation": "Possible irritation or wax buildup."
        }
    else:
        return {
            "severity": "Severe Inflammation",
            "confidence": "0.88",
            "recommendation": "High risk of infection. ENT consult advised."
        }

def analyze_nose(image):
    sat, red = inflammation_score(image)

    if red < 12:
        return {
            "severity": "Normal",
            "confidence": "0.78",
            "recommendation": "No visible nasal inflammation."
        }
    elif red < 35:
        return {
            "severity": "Congestion",
            "confidence": "0.70",
            "recommendation": "Possible allergy or cold."
        }
    else:
        return {
            "severity": "Severe Infection Risk",
            "confidence": "0.90",
            "recommendation": "Strong inflammation detected."
        }
