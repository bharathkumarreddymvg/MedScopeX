import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import cv2
import numpy as np
from models.yolo_ent import YOLOENTDetector
from utils.color_analysis import analyze_ear, analyze_nose

st.set_page_config(page_title="MedScopeX – YOLO ENT", layout="centered")
st.title("MedScopeX – Real-Time YOLO ENT Detection")

detector = YOLOENTDetector()

frame = st.camera_input("Scan Ear / Nose Area (Use Torch)")

if frame:
    img_bytes = np.frombuffer(frame.getvalue(), np.uint8)
    image = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)

    st.image(image, channels="BGR", caption="Input Frame")

    detections = detector.detect(image)

    if not detections:
        st.error("No facial region detected. Try better lighting.")
    else:
        for det in detections:
            roi = det["roi"]

            st.subheader("Detected ENT Region")

            st.image(roi, channels="BGR")

            ear_result = analyze_ear(roi)
            nose_result = analyze_nose(roi)

            st.metric("Ear Condition", ear_result["severity"])
            st.metric("Ear Confidence", ear_result["confidence"])
            st.info(ear_result["recommendation"])

            st.metric("Nose Condition", nose_result["severity"])
            st.metric("Nose Confidence", nose_result["confidence"])
            st.info(nose_result["recommendation"])
