import cv2
import numpy as np
from imutils.video import FPS, WebcamVideoStream

import glog as log


def local_camera(index):
    '''use laptop camera(in processing)
    
    - Params:
    @index: which camera we select
    '''
    cap = cv2.VideoCapture(index)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Display the resulting frame
            cv2.imshow('frame',gray)
            log.info('Success read img from cap!')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def web_camera(src):
    stream = WebcamVideoStream(src=src).start()
    while True:
        # grab next frame
        frame = stream.read()
        key = cv2.waitKey(1) & 0xFF

        # keybindings for display
        if key == ord('p'):  # pause
            while True:
                key2 = cv2.waitKey(1) or 0xff
                cv2.imshow('frame', frame)
                if key2 == ord('p'):  # resume
                    break
        cv2.imshow('frame', frame)
        if key == 27:  # exit
            break


if __name__ == '__main__':
    #local_camera(0)
    web_camera(src='rstp://admin:1jiao426@192.168.1.3/h264/main/ch1/av_stream')

1. 读取视频不做任何处理（输入到caffe之前），本身就有延迟（8s）
2. caffe调用和第一步读取之间有没有延迟没有测试
3. caffe调用摄像头，以及caffe处理图片然后输出，差值0.8s，一张图片处理时间为0.8s