import numpy as np
import cv2
from imutils.video import FPS, WebcamVideoStream

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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame',gray)
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
        print (frame)
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