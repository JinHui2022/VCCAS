import cv2

video1="USB Camera1_2023-09-21 20-10-48.avi"
video2="USB Camera2_2023-09-21 20-10-48.avi"
video3="USB Camera3_2023-09-21 20-10-48.avi"
video4="USB Camera4_2023-09-21 20-10-48.avi"

def get_image(video, img_name):
    cap=cv2.VideoCapture(video)
    cap.read()
    ret,frame=cap.read()
    if ret:
        cv2.imwrite(img_name,frame)

get_image(video1, "img1.jpg")
get_image(video2, "img2.jpg")
get_image(video3, "img3.jpg")
get_image(video4, "img4.jpg")