import cv2

capture = cv2.VideoCapture(1)

# 카메라 크기 
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    ret, frame = capture.read()
    cv2.imshow("adsf", frame)