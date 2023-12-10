import cv2
import numpy as np
def onTrack1(val):
    global hueLow
    hueLow=val
def onTrack2(val):
    global hueHigh
    hueHigh=val
def onTrack3(val):
    global satLow
    satLow=val
def onTrack4(val):
    global satHigh
    satHigh=val
def onTrack5(val):
    global valLow
    valLow=val
def onTrack6(val):
    global valHigh
    valHigh=val

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar',400,300)

hueHigh=0
hueLow=0
satLow=0
satHigh=0
valLow=0
valHigh=0

cv2.createTrackbar('Hue Low','Trackbar',110,179,onTrack1)
cv2.createTrackbar('Hue High','Trackbar',150,179,onTrack2)
cv2.createTrackbar('Sat Low','Trackbar',80,255,onTrack3)
cv2.createTrackbar('Sat High','Trackbar',255,255,onTrack4)
cv2.createTrackbar('Val Low','Trackbar',134,255,onTrack5)
cv2.createTrackbar('Val High','Trackbar',255,255,onTrack6)
image=cv2.imread('ball.png')
while True:
    frameHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueLow,satLow,valLow])#lower and upper boundary
    upperBound = np.array([hueHigh,satHigh,valHigh])
    mask = cv2.inRange(frameHSV, lowerBound, upperBound)
    masked = cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('mask', mask)
    cv2.imshow('Ball', image)
    cv2.imshow('masked',masked)
    print("lowerBound: ", lowerBound)
    print("upperBound: ", upperBound)
    if cv2.waitKey(1) & 0xff == ord('q'): # to quit the camera press 'q'
        break
cv2.destroyAllWindows()