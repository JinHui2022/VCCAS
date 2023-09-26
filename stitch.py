# import cv2
# import numpy as np

# # the name of videos
# caps=[]
# for i in range(4):
#     cap=cv2.VideoCapture(".\\videos\\video"+str(i+1)+".avi")
#     caps.append(cap)

# # get the info of video
# frame_rate = int(caps[0].get(5))  # frame rate
# frame_width = int(caps[0].get(3))  # width
# frame_height = int(caps[0].get(4))  # height
# total_frames = int(caps[0].get(7))  # total frame number

# # creat the output
# output_file = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), frame_rate, (frame_width * 2, frame_height * 2))

# # to stitch
# for i in range(total_frames):
#     ret1, frame1 = caps[0].read()
#     ret2, frame2 = caps[1].read()
#     ret3, frame3 = caps[2].read()
#     ret4, frame4 = caps[3].read()

#     if ret1 and ret2 and ret3 and ret4:
#         # creat a blank canvas
#         output_frame = np.zeros((frame_height * 2, frame_width * 2, 3), dtype=np.uint8)

#         output_frame[:frame_height, :frame_width] = frame1
#         output_frame[frame_height:, :frame_width] = frame2
#         output_frame[:frame_height, frame_width:] = frame3
#         output_frame[frame_height:, frame_width:] = frame4

#         output_file.write(output_frame)

# for i in range(4):
#     caps[i].release()
# output_file.release()

# print("视频拼接完成")

import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor

video_files = [".\\videos\\video"+str(i)+".avi" for i in range(1,5)]
caps = [cv2.VideoCapture(file) for file in video_files]

# get the info of video
frame_rate = int(caps[0].get(5))  # frequency
frame_width = int(caps[0].get(3))  # width
frame_height = int(caps[0].get(4))  # height
total_frames = int(caps[0].get(7))  # total frame number

output_file = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), frame_rate, (frame_width * 2, frame_height * 2))

def process_frame(cap, frame_number):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    if ret:
        return frame,1
    else:
        return frame,0

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = []

    for frame_number in range(total_frames):
        frames = [executor.submit(process_frame, cap, frame_number) for cap in caps]
        frames = [future.result() for future in frames]
        
        flag=False
        for frame in frames:
            if frame[1] == 0:
                flag=True
                break
        
        if flag:
            break

        # creat a blank canvas
        output_frame = np.zeros((frame_height * 2, frame_width * 2, 3), dtype=np.uint8)

        output_frame[:frame_height, :frame_width] = frames[0][0]
        output_frame[frame_height:, :frame_width] = frames[1][0]
        output_frame[:frame_height, frame_width:] = frames[2][0]
        output_frame[frame_height:, frame_width:] = frames[3][0]

        output_file.write(output_frame)

for cap in caps:
    cap.release()
output_file.release()

print("finish successfully!")
