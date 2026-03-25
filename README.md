# 🏋️ Fitness Form Analyzer API

This project is a simple AI-powered backend system that analyzes human posture (e.g., squat form) using computer vision.

## 🚀 Features
- Pose detection using MediaPipe
- Joint angle calculation
- Basic squat feedback
- FastAPI-based REST API

## 🧠 How It Works
1. Capture image/video input
2. Extract body keypoints
3. Calculate joint angles
4. Generate feedback
5. Return structured JSON response

## 🔧 Tech Stack
- Python
- FastAPI
- MediaPipe
- OpenCV

## 📡 API Endpoint

### POST /analyze_form

**Response:**
```json
{
  "exercise": "squat",
  "knee_angle": 87.5,
  "feedback": "Good squat depth"
}