import cv2

frameWidth = 1280
frameHeight = 960
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while cap.isOpened():
    success, img = cap.read()
    if success:
        cv2.imshow("New wind", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
