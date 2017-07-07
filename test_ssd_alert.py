from mouse.mouse import Annotate
from Video.camera import local_camera
from util.prefix import prefix_polygon, prefix_coor_double
from fs.fs import array_to_txt
import matplotlib.pyplot as plt
import cv2


# cap = cv2.VideoCapture('rtsp://admin:1jiao426@192.168.1.3/h264/main/ch1/av_stream')
# while(True):
#         # Capture frame-by-frame
#         ret, frame = cap.read()
#         # Our operations on the frame come here
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # Display the resulting frame
#         if ret:
#             a = Annotate(frame)
#             break
#     # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
# if not plt.show():
#     polygons  = prefix_coor_double(a.rect_coor)
#     print (polygons)
#     #array_to_txt(polygons, 'rect_data/compile-jpg.txt'.format(caffe_root))
#     array_to_txt(polygons, 'polygons.txt')

#===== another =====#
img1 = cv2.imread("/home/eric/Desktop/Project-PY/pro-py27/04OpencvLearning/img/0.png")
img2 = cv2.imread("/home/eric/Desktop/Project-PY/pro-py27/04OpencvLearning/img/11.jpg")
a = Annotate(img1)
plt.show()
    


