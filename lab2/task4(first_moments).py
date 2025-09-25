import cv2
import numpy as np

video = cv2.VideoCapture(0)
ok, img = video.read()
cv2.namedWindow('Camera', cv2.WINDOW_AUTOSIZE)


low_redor = np.array([0, 100, 100])
up_redor = np.array([10, 255, 255])
low_redpur = np.array([170, 100, 100])
up_redpur = np.array([180, 255, 255])

kernel = np.ones((5, 5), np.uint8)

print("Моменты первого порядка:")

while (True):
    ok, img = video.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #COLOR_BGR2RGB, COLOR_BGR2RGB
    redor_maska = cv2.inRange(hsv, low_redor, up_redor)
    redpur_maska = cv2.inRange(hsv, low_redpur, up_redpur)
    red_maska = cv2.bitwise_or(redor_maska, redpur_maska)
    hsv_red_result = cv2.bitwise_and(img, img, mask=red_maska)

    contours, _ = cv2.findContours(red_maska, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for i, contour in enumerate(contours):

        first_moments = cv2.moments(contour)
        
        square = first_moments['m00']
        summ_x = first_moments['m10']
        summ_y = first_moments['m01']
        
        print("Площадь: ", {square})
        print("Сумма по х: ", {summ_x})
        print("Сумма по y: ", {summ_y})
    
    cv2.imshow('Camera', hsv_red_result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
