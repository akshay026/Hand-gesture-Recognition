import streamlit as st
import subprocess
import signal
import os
import cv2

def main():
    st.title("Hand Gesture Recognition using OpenCV, TensorFlow, and MediaPipe")

    # Add a selector for the app mode on the sidebar
    app_mode = st.sidebar.selectbox("Choose the app mode",["","About the project", "Run the project"])
    if app_mode == "About the project":
        st.write("""
        This project is about recognizing hand gestures using OpenCV, TensorFlow, and MediaPipe.
        The system captures video input, processes each frame to detect hand landmarks,
        and then uses a trained model to predict the gesture being made.
        """)
    elif app_mode == "Run the project":
        if st.button("Start"):
            global p 
            p = subprocess.Popen(["python", "Code.py"])
            st.text("Running Hand Gesture Recognition script...")
if __name__ == "__main__":
    main()
