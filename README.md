#  Fitness Form Analyzer API

This project is a simple AI-powered backend system that analyzes human posture (e.g., squat form) using computer vision.

##  Features
- Pose detection using MediaPipe
- Joint angle calculation
- Basic squat feedback
- FastAPI-based REST API

##  How It Works
1. Capture image/video input
2. Extract body keypoints
3. Calculate joint angles
4. Generate feedback
5. Return structured JSON response

##  Tech Stack
- Python
- FastAPI
- MediaPipe
- OpenCV

##  Hardware & Edge Integration Blueprint (Future Scope)
While this API currently runs as a cloud service processing video streams, the underlying math and data processing logic are designed to bridge directly into wearable health technology. 

### 1. Shifting to Sensor-Based Kinematics
Instead of relying on camera feeds, the joint-angle calculation algorithms can be driven by a network of body-worn **Inertial Measurement Units (IMUs)**, such as the **MPU6050** or **LSM6DSOX**.
* **Data Ingestion:** Microcontrollers sample raw accelerometer and gyroscope data via **I2C or SPI** protocols.
* **On-Chip Processing:** An **STM32** or **ESP32** utilizing a complementary filter or Kalman filter resolves spatial orientation in real-time.

### 2. Edge AI & Constrained Environments
* **Porting to Embedded C:** The mathematical framework used to evaluate joint constraints is being adapted into lightweight, fixed-point C logic to bypass the overhead of Python.
* **Haptic Feedback Control:** Integrating actuator control logic (using **PWM** to drive precise micro-vibration motors) to instantly alert a user when their form deviates from safe thresholds.


##  API Endpoint

### POST /analyze_form

**Response:**
```json
{
  "exercise": "squat",
  "knee_angle": 87.5,
  "feedback": "Good squat depth"
}
