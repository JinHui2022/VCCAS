import cv2

def rotate(video):
    cap = cv2.VideoCapture(video)

    new_video=video.split('.')[0]+"_rot.avi"
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 定义编解码器并创建 VideoWriter 对象
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(new_video, fourcc, fps, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    # 循环遍历视频的每一帧并顺时针旋转90度
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        out.write(rotated_frame)

    # 释放资源
    cap.release()
    out.release()
    cv2.destroyAllWindows()

video1="USB Camera1_2023-09-21 20-10-48.avi"
video2="USB Camera2_2023-09-21 20-10-48.avi"
video3="USB Camera3_2023-09-21 20-10-48.avi"
video4="USB Camera4_2023-09-21 20-10-48.avi"
rotate(video1)
rotate(video2)
rotate(video3)
rotate(video4)
