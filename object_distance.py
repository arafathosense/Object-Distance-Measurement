import cv2
import numpy as np

KNOWN_WIDTH = 7
FOCAL_LENGTH = 500

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)

    # Threshold instead of edges (more reliable)
    _, thresh = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        cnt = max(contours, key=cv2.contourArea)

        if cv2.contourArea(cnt) > 3000:
            x, y, w, h = cv2.boundingRect(cnt)

            distance = (KNOWN_WIDTH * FOCAL_LENGTH) / w

            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

            cv2.putText(
                frame,
                f"Distance: {int(distance)} cm",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,0,255),
                2
            )

    cv2.imshow("Object Distance Measurement", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()