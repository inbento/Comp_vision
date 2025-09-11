import cv2

#Задание 1 + 2
img1 = cv2.imread(r"first.jpg", 65)
img2 = cv2.imread(r"second.png", 8)
img3 = cv2.imread(r"third.jfif", cv2.IMREAD_GRAYSCALE)


cv2.namedWindow('Display window', cv2.WINDOW_AUTOSIZE)
cv2.moveWindow('Display window', 500, 250)
cv2.imshow('Display window', img1)
cv2.waitKey(0)

cv2.imshow('Display window', img2)
cv2.waitKey(0)

cv2.namedWindow('Display window', cv2.WINDOW_FULLSCREEN)
cv2.imshow('Display window', img3)
cv2.waitKey(0)

cv2.destroyAllWindows()


#Задание 3,4 

vid = cv2.VideoCapture(r'football.gif', 0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
w = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_writer = cv2.VideoWriter("output.mp4", fourcc, 25, (w, h))

while True:
    ret, frame = vid.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #BGR2GRAY

    cv2.imshow('frame', hsv)
    video_writer.write(hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

#Задание 5
img4 = cv2.imread(r"third.jfif")

cv2.imshow('Orig img', img4)

hsv = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV) #BGR2GRAY
cv2.imshow('Orig wind', hsv)

cv2.waitKey(0)

cv2.destroyAllWindows()

