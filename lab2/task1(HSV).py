import cv2

#Задание 1
video = cv2.VideoCapture(0)
ok, img = video.read()
cv2.namedWindow('Camera', cv2.WINDOW_AUTOSIZE)


while (True):
    ok, img = video.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #COLOR_BGR2RGB, COLOR_BGR2RGB
    cv2.imshow('Camera', hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
