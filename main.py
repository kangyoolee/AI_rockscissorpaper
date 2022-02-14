# -*- coding: utf-8 -*- 

import tensorflow.keras
import numpy as np
import cv2
from playsound import playsound
import time
import keyboard
from PIL import ImageFont, ImageDraw, Image

import emoji

# 머신 러닝 모듈 가져오는 부분이다. 태민아
model_filename ='model/keras_model.h5'
model = tensorflow.keras.models.load_model(model_filename)

# gawi = cv2.imread('컴퓨터는 "가위" 를 골랐습니다!.png')
# bawi = cv2.imread('컴퓨터는 "바위" 를 골랐습니다!.png')
# bo = cv2.imread('컴퓨터는 "보" 를 골랐습니다!.png')
# com = cv2.imread('컴퓨터의 선택은?.png')

# com = cv2.cvtColor(com, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(com, 1, 255, cv2.THRESH_BINARY)
# 그 카메라 팝업카메라 띄우는거 그거임
capture = cv2.VideoCapture(1)

# 카메라 크기 
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)

# 이미지 처리하기
def preprocessing(frame):
    #frame_fliped = cv2.flip(frame, 1)
    # 사이즈 조정 티쳐블 머신에서 사용한 이미지 사이즈로 변경해준다.
    size = (224, 224)
    frame_resized = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
    
    # 이미지 정규화
    # astype : 속성
    frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1

    # 이미지 차원 재조정 - 예측을 위해 reshape 해줍니다.
    # keras 모델에 공급할 올바른 모양의 배열 생성
    frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))
    #print(frame_reshaped)
    return frame_reshaped

# 예측용 함수
def predict(frame):
    prediction = model.predict(frame)
    return prediction



while True:
    if keyboard.is_pressed('q'):
        print(emoji.emojize('컴퓨터의 선택은? 🤔'))
        playsound('가위바위보.mp3')
        ret, frame = capture.read()

        preprocessed = preprocessing(frame)
        prediction = predict(preprocessed)
        a = 0
        gawibawibo_list = []
        gawibawibo_list.append(prediction[0,0])
        gawibawibo_list.append(prediction[0,1])
        gawibawibo_list.append(prediction[0,2])

        if max(gawibawibo_list) == prediction[0,0]:
            a=1
        # cv2.putText(frame, '가위', (0, 50), cv2.FONT_HERSHEY_TRIPLEX , 1, (0, 0, 0))
    
        elif max(gawibawibo_list) == prediction[0,1]:
            # cv2.putText(frame, '보', (0, 50), cv2.FONT_HERSHEY_TRIPLEX , 1, (0, 0, 0))
            a=2

        else:
        # cv2.putText(frame, '바위', (0, 50), cv2.FONT_HERSHEY_TRIPLEX , 1, (0, 0, 0))
            a=3

        if a == 1:
            print(emoji.emojize('컴퓨터는 "가위 💇 " 를 골랐습니다!'))
            print('-------------------------------')
        elif a ==2:
            print(emoji.emojize('컴퓨터는 "보 🖐 " 를 골랐습니다!'))
            print('-------------------------------')
        else:
            print(emoji.emojize('컴퓨터는 "바위 👊 " 를 골랐습니다!'))
            print('-------------------------------')
