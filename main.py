from fastapi import FastAPI
import cv2
import mediapipe as mp
import math

app = FastAPI()

# Correct way to access Pose on Windows with mediapipe 0.10.33
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

def calculate_angle(a, b, c):
    # a, b, c are landmarks
    a = (a.x, a.y)
    b = (b.x, b.y)
    c = (c.x, c.y)

    angle = math.degrees(
        math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    )

    if angle < 0:
        angle += 360

    return angle

@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/analyze_form")
def analyze_form():
    cap = cv2.VideoCapture(0)  # Use webcam

    success, frame = cap.read()
    if not success:
        cap.release()
        return {"error": "Camera not working"}

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)
    cap.release()

    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark

        hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
        ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]

        angle = calculate_angle(hip, knee, ankle)

        if angle < 90:
            feedback = "Good squat depth"
        else:
            feedback = "Go lower"

        return {
            "exercise": "squat",
            "knee_angle": round(angle, 2),
            "feedback": feedback
        }

    return {"message": "No pose detected"}