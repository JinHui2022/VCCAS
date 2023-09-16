from capturevideo import *
from videocorrect import *
import os

if __name__=="__main__":
    ## capture the video
    videocapture()

    ## correct the video and store in the same folder
    for i in range(1,5):
        folder_path=".//cam"+str(i)+"_video"
        for filename in os.endswith(".avi") and not filename.endswith("_corrected.avi"):
            file_path=os.path.join(folder_path,filename)
            videocorrect(file_path)
    
    ## stitch the video
    