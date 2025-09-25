import cv2
import numpy as np

video = cv2.VideoCapture(0)
ok, img = video.read()
cv2.namedWindow('Camera', cv2.WINDOW_AUTOSIZE)
low_redor = np.array([0, 100, 100])
up_redor = np.array([10, 255, 255])
low_redpur = np.array([170, 100, 100])
up_redpur = np.array([180, 255, 255])

while (True):
    ok, img = video.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #COLOR_BGR2RGB, COLOR_BGR2RGB
    redor_maska = cv2.inRange(hsv, low_redor, up_redor)
    redpur_maska = cv2.inRange(hsv, low_redpur, up_redpur)
    red_maska = cv2.bitwise_or(redor_maska, redpur_maska)
    hsv_red_result = cv2.bitwise_and(img, img, mask=red_maska)

    cv2.imshow('Camera', hsv_red_result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()