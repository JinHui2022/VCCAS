import cv2
import numpy as np

'''
Library:
N3C31
[1064, 1334] [601, 363] [-0.6, -0.023, -0.1, -0.029, -0.0046]
'''

FILENAME_IN = cv2.imread("N3C31.png")
FILENAME_IN = cv2.resize(FILENAME_IN,(640,480))
FC,CC,KC=[1064, 1334],[601, 363],[-0.6, -0.023, -0.1, -0.029, -0.0046]

def create_matrix_profile(fc, cc, kc):
    fx, fy = fc
    cx, cy = cc
    cam_matrix = np.array([[fx,  0, cx],
                           [ 0, fy, cy],
                           [ 0,  0,  1]], dtype='float32')
    distortion_profile = np.array(kc, dtype='float32')
    return cam_matrix, distortion_profile

def videocorrect(origin):
    video=cv2.VideoCapture(origin)

    ## get the info of original video
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    ## create a writer
    output=origin.split('.')[0]+'_corrected.avi'
    writer = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'MJPG'), fps, (width, height))
    
    ## correct the distortion and store to new video file
    cam_matrix, profile = create_matrix_profile(FC, CC, KC)
    while True:
        ret, frame=video.read()
        if ret:
            new_frame =  cv2.undistort(frame, cam_matrix, profile)
            writer.write(new_frame)
        else:
            break
    video.release()
    writer.release()