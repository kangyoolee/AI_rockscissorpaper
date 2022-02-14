# importing the libraries
import cv2
import numpy as np

# Setup camera
cap = cv2.VideoCapture(1)

# Read logo and resize
logo = cv2.imread('컴퓨터의 선택은?.png')
size = 100
logo = cv2.resize(logo, (270,30))


while True:
	ret, frame = cap.read()
    a = cap.add(frame, logo)
    cap.imshow('a',a)



