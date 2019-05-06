import numpy as np
import cv2
import pygame
import pygame.camera
from pygame.locals import *
import cv2
import numpy as np
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
x = 230
y = 110
length = 200

cv2.namedWindow('vid',cv2.WINDOW_NORMAL)
cv2.namedWindow('mask',cv2.WINDOW_NORMAL)
cv2.namedWindow('res',cv2.WINDOW_NORMAL)

while(True):
    frame = cam.get_image()
    pygame.image.save(frame, "test.jpeg")
    img = cv2.imread("test.jpeg")
    img = cv2.flip(img,1)
    
    cv2.rectangle(img,(x,y),(x+length ,y+length),(255,0,0), 5)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([5, 100, 100], dtype=np.uint8)
    upper_range = np.array([25, 255, 255], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_range, upper_range)
    res = cv2.bitwise_and(img,img, mask= mask)
    
    cv2.imshow('res',res)
    cv2.imshow('mask',mask)
    cv2.imshow('vid', img)
    k = cv2.waitKey(1)
    if(k == 27):
      break

cv2.destroyAllWindows()
    
