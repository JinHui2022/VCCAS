# VCCAS项目说明
## 开发意图
VCCAS，即Video Capture, Correct and Stitch， 是一件服务于由杨骁轶和黎聪开发的多线虫成像平台的软件支持项目。由于成像平台使用四台产自杰锐微通的工业相机组成的镜头阵列，而该类相机并不支持外来信号控制，因而我们需要编写相关的软件来实现四台相机的同时开启与关闭，并及时对摄取的图像进行畸变的校正，继而缝合成为一个视频文件，用于对线虫进行追踪分析。

## 项目内容
本项目由四部分组成：
### 视频捕捉
该部分由capturevideo.py、getcameraid.exe两个文件组成，config.ini是对应的配置文件。在config.ini中可以设置每个视频的拍摄时间，视频的分辨率与帧率。捕捉得到的视频在储存在同一个根文件夹下的"cami_video"(i=1,2,3,4)中，以供其他用途。

其运行的原理在于将每个相机拍摄图像的执行交由计算机的不同线程完成，实际运行时还需要由协调各个相机拍摄的主进程以及检查设备状态的辅助进程，因而为保证正确运行该项目，请确保你的计算机能够支持六个及以上进程的进行。

### 视频校正
杰瑞微通的工业相机存在一定的畸变，然而为了确保线虫追踪的效果以及视频缝合的正常进行，我们需要对前一步获取的视频进行畸变的校正。该部分由.idea、venv、videocorrect.py三个文件组成。

其运行的原理在于利用我们实现测定的相机的畸变参数，对图像进行调整。

### 视频缝合


## 如何运行

## 运行环境说明

## 致谢
本项目的编写参考了以下三个开源项目：
* [videocapture](https://github.com/LLGJUN/videocapture)
* [undivid](https://github.com/cdw/undivid)
* 