import cv2
import numpy as np

video = cv2.VideoCapture(0)
ok, path = video.read()

low_redor = np.array([0, 133, 133])
up_redor = np.array([7, 255, 255])
low_redpur = np.array([176, 133, 133])
up_redpur = np.array([180, 255, 255])

lastx = 0
lasty = 0
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
        if square < 259:
            continue

        summ_x = first_moments['m10']
        summ_y = first_moments['m01']
        
        print("Площадь: ", {square})
        print("Сумма по х: ", {summ_x})
        print("Сумма по y: ", {summ_y})

        if square > 0:
            center_x = int(summ_x / square)
            center_y = int(summ_y / square)
        else:
            center_x, center_y = 0, 0

        x, y, w, h = cv2.boundingRect(contour)
        
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 3)
        
        cv2.circle(img, (center_x, center_y), 5, (123, 0, 255), -1)
    cv2.line(path, (lastx, lasty), (center_x, center_y), (90,0,0), 5)

    lastx = center_x
    lasty = center_y

    img = cv2.add(img, path)
    cv2.imshow('Camera1', img)
    cv2.imshow('Camera2', hsv_red_result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
