import sys
import os
import numpy as np
import torch

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT)

from models.depth import DepthModel
from models.risk import RiskModel
from utils.postprocess import interpret_dental
from utils.color_analysis import analyze_ear, analyze_nose

depth_model = DepthModel()
risk_model = RiskModel()

def run(image):
    ear_result = analyze_ear(image)
    nose_result = analyze_nose(image)

    gray = np.mean(image, axis=2) / 255.0
    cavity_percent = round(float(np.mean(gray) * 100), 2)

    depth_logits = depth_model()
    depth_stage = int(torch.argmax(depth_logits).item())

    risk_score = risk_model(cavity_percent, depth_stage)

    dental = interpret_dental(cavity_percent, depth_stage, risk_score)

    return {
        "ear": ear_result,
        "nose": nose_result,
        "dental": dental
    }
