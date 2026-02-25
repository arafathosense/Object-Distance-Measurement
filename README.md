# 📏 Object Distance Measurement 

## 📌 Project Overview

This project measures the distance of an object from a webcam in real-time using **OpenCV** and basic computer vision techniques. It detects the largest visible object in the frame using thresholding and contour detection, then estimates its distance using a simple pinhole camera distance formula.

<img width="1365" height="728" alt="Screenshot_1" src="https://github.com/user-attachments/assets/6ff87021-be65-458c-aa49-3e0391367756" />
<img width="1365" height="726" alt="Screenshot_2" src="https://github.com/user-attachments/assets/5b22e32d-a092-4257-984d-cc64ca7e0906" />
<img width="1365" height="726" alt="Screenshot_3" src="https://github.com/user-attachments/assets/1f2bb923-2159-40f9-9909-8958fd054a55" />

## ⚙️ How It Works

1. Captures live video from webcam.
2. Converts frame to grayscale.
3. Applies Gaussian blur to reduce noise.
4. Uses binary thresholding to isolate objects.
5. Detects contours in the frame.
6. Selects the largest contour.
7. Calculates distance using:

[
Distance = \frac{Known_Width \times Focal_Length}{Object_Width_in_Pixels}
]

8. Displays bounding box and estimated distance in centimeters.


## 🧠 Distance Formula Explained

The system uses the pinhole camera model:

```
Distance = (KNOWN_WIDTH × FOCAL_LENGTH) / Object_Width_in_Pixels
```

* **KNOWN_WIDTH** → Real-world width of the object (in cm)
* **FOCAL_LENGTH** → Camera focal length (must be calibrated)
* **Object_Width_in_Pixels** → Width of detected object in image


## 📦 Requirements

Install dependencies:

```bash
pip install opencv-python numpy
```


## ▶️ How to Run

```bash
object_distance.py
```

Press **Q** to exit the application.


## 🎯 Important Notes

* The system detects the **largest object** in view — it is NOT face detection.
* Accuracy depends on:

  * Proper focal length calibration
  * Stable lighting conditions
  * Clear object separation from background
* Works best with solid, high-contrast objects.



## 🔧 How to Calibrate Focal Length

1. Place object at a known distance (e.g., 50 cm).
2. Measure detected object width in pixels (e.g., 120 px).
3. Use formula:

```
FOCAL_LENGTH = (Pixel_Width × Known_Distance) / KNOWN_WIDTH
```

Example:

```
FOCAL_LENGTH = (120 × 50) / 7
```

Use this calculated value in your script.


## 📌 Features

* Real-time distance estimation
* Lightweight and fast
* No external ML models required
* Simple and easy to modify

## ⚠️ Limitations

* Not suitable for complex backgrounds
* Sensitive to lighting changes
* Detects any large object, not specific categories
* Distance estimation is approximate


## 🚀 Future Improvements

* Add face detection support
* Use edge detection + morphology for better accuracy
* Integrate MediaPipe for facial distance measurement
* Add smoothing filter for stable distance output

## 🛠 Technologies Used

* Python
* OpenCV
* NumPy

## 👤 Author

**HOSEN ARAFAT**  

**Software Engineer, China**  

**GitHub:** https://github.com/arafathosense

**Researcher: Artificial Intelligence, Machine Learning, Deep Learning, Computer Vision, Image Processing**
