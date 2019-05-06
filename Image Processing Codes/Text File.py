import serial
import cv2
ser = serial.Serial('/dev/rfcomm2ss',9600)


ser.write(b'RL5Rl35042124ok')
cv2.waitKey(2000)
ser.write(b'1')
cv2.waitKey(2000)
ser.write(b'RL5Rl35042124ok')
cv2.waitKey(2000)
ser.write(b'1')
cv2.waitKey(2000)

while True:
    x=raw_input("enter ")
    ser.write(x)
