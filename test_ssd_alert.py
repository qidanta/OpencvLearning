from mouse.mouse import Annotate
from Video.camera import local_camera
from util.prefix import prefix_polygon
from fs.fs import array_to_txt
import matplotlib.pyplot as plt
import cv2


cap = cv2.VideoCapture(0)
while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        if ret:
            a = Annotate(frame)
            break
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
if not plt.show():
    polygons  = prefix_polygon(a.rect_coor)
    print (polygons)
    #array_to_txt(polygons, 'rect_data/compile-jpg.txt'.format(caffe_root))
    array_to_txt(polygons, 'polygons.txt')
    


