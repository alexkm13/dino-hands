import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto
import time

detector=HandDetector(detectionCon=0.8, maxHands=1)

time.sleep(2.0)

current_key_pressed = set()

video=cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    hands, img = detector.findHands(frame)
    cv2.rectangle(img, (0, 480), (300, 425),(50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425),(50, 50, 255), -2)
    
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        if fingerUp == [0,0,0,0,0]:
            cv2.putText(frame, 'Finger Count: 0', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Jumping', (440,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            auto.press('up')

        if fingerUp == [0,1,0,0,0]:
            cv2.putText(frame, 'Finger Count: 1', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            
        if fingerUp == [0,1,1,0,0]:
            cv2.putText(frame, 'Finger Count: 2', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp == [0,1,1,1,0]:
            cv2.putText(frame, 'Finger Count: 3', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp == [0,1,1,1,1]:
            cv2.putText(frame, 'Finger Count: 4', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp == [1,1,1,1,1]:
            cv2.putText(frame, 'Finger Count: 5', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
    cv2.imshow("Frame",frame)
    x = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
