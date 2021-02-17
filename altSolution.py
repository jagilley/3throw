import cv2
from matplotlib import pyplot as plt
import numpy as np
import random

left = cv2.VideoCapture(0)
right = cv2.VideoCapture(1)

REMAP_INTERPOLATION = cv2.INTER_LINEAR

calibration = np.load("/home/pi/Code/IE3Throw/calibration.npz", allow_pickle=False)
imageSize = tuple(calibration["imageSize"])
leftMapX = calibration["leftMapX"]
leftMapY = calibration["leftMapY"]
leftROI = tuple(calibration["leftROI"])
rightMapX = calibration["rightMapX"]
rightMapY = calibration["rightMapY"]
rightROI = tuple(calibration["rightROI"])


while True:
    if not (left.grab() and right.grab()):
        print("No more frames")
        break

    _, leftFrame = left.retrieve()
    _, rightFrame = right.retrieve()

    #cv2.imshow('left', leftFrame)
    #cv2.imshow('right', rightFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    fixedLeft = cv2.remap(leftFrame, leftMapX, leftMapY, REMAP_INTERPOLATION)
    fixedRight = cv2.remap(rightFrame, rightMapX, rightMapY, REMAP_INTERPOLATION)

    lfn = cv2.cvtColor(fixedLeft, cv2.COLOR_BGR2GRAY)
    rfn = cv2.cvtColor(fixedRight, cv2.COLOR_BGR2GRAY)
    
    stereo = cv2.StereoBM_create()
    stereo.setMinDisparity(4)
    stereo.setNumDisparities(128)
    stereo.setBlockSize(21)
    stereo.setSpeckleRange(16)
    stereo.setSpeckleWindowSize(45)
    disparity = stereo.compute(lfn,rfn)
    DEPTH_VISUALIZATION_SCALE = 2048
    cv2.imshow('depth', disparity / DEPTH_VISUALIZATION_SCALE)

left.release()
right.release()
cv2.destroyAllWindows()