def get_color(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_range = np.array([20, 150, 50], dtype=np.uint8)
    upper_range = np.array([30, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_range, upper_range)
    average = np.average(mask, axis=0)
    average = np.average(average, axis=0)
    if average > 150:
        return 'Y'
    
    lower_range = np.array([100, 100,80], dtype=np.uint8)
    upper_range = np.array([130, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_range, upper_range)
    average = np.average(mask, axis=0)
    average = np.average(average, axis=0)
    if average > 150:
        return 'B'

    lower_range = np.array([60, 100,80], dtype=np.uint8)
    upper_range = np.array([80, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_range, upper_range)
    average = np.average(mask, axis=0)
    average = np.average(average, axis=0)
    if average > 150:
        return 'G'

##    lower_range = np.array([5, 155, 50], dtype=np.uint8)
##    upper_range = np.array([25, 255, 255], dtype=np.uint8)
    
##    lower_range = np.array([3, 100, 100], dtype=np.uint8)
##    upper_range = np.array([10, 255, 255], dtype=np.uint8)
    
##    lower_range = np.array([5, 80, 200], dtype=np.uint8)
##    upper_range = np.array([15, 255, 255], dtype=np.uint8)

    lower_range = np.array([5, 100, 100], dtype=np.uint8)
    upper_range = np.array([25, 255, 255], dtype=np.uint8)
    
##    lower_range = np.array([5, 150, 200], dtype=np.uint8)
##    upper_range = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_range, upper_range)
    average = np.average(mask, axis=0)
    average = np.average(average, axis=0)
    if average > 150:
        return 'O'

##    lower_range = np.array([0, 0, 0], dtype=np.uint8)
##    upper_range = np.array([220,150, 100], dtype=np.uint8)

    lower_range = np.array([0, 0, 0], dtype=np.uint8)
    upper_range = np.array([250,200, 120], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_range, upper_range)
    average = np.average(mask, axis=0)
    average = np.average(average, axis=0)
    if average > 100:
        return 'L'

    return 'R'
    


import numpy as np
import cv2
import pygame
import pygame.camera
from pygame.locals import *
import kociemba

x = 130
y = 130
length = 200
border = 20

edge = int((length-6*border)/3)
x1 = x+border
x2 = x+border+edge
x3 = x+3*border+edge
x4 = x+3*border+2*edge
x5 = x+5*border+2*edge
x6 = x+5*border+3*edge
y1 = y+border
y2 = y+border+edge
y3 = y+3*border+edge
y4 = y+3*border+2*edge
y5 = y+5*border+2*edge
y6 = y+5*border+3*edge
