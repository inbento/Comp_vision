import cv2

#Задание 6
video = cv2.VideoCapture(0)
ok, img = video.read()
cv2.namedWindow('Camera', cv2.WINDOW_AUTOSIZE)

w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter("camera_video.mp4", fourcc, 25, (w, h))

while (True):
    ok, img = video.read()
    
    center_x, center_y = w // 2, h // 2
    center_color = (img[center_y, center_x])
    print(center_color)
    max_color = int(max(center_color))
    print(max_color)
    for i in range(0,3):
        if center_color[i] < max_color:
            center_color[i] = 0
        elif center_color[i] == max_color:
            center_color[i] = 255   
    b = int(center_color[0])
    g = int(center_color[1])
    r = int(center_color[2])    

    cross_size = 50
    line_width = 12
    cv2.rectangle(img, (center_x - 15 // 2, center_y - 50), (center_x + 15 // 2, center_y + 50), (b, g, r), 3)
    cv2.rectangle(img, (center_x - 50, center_y - 15 // 2), (center_x + 50, center_y + 15 // 2), (b, g, r), 3)

    cv2.imshow('Camera', img)
    video_writer.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
