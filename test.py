import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import cv2

class Annotate(object):
    def __init__(self):
        self.ax = plt.gca()
        self.img = cv2.imread('./img/0.png')
        self.rect = Rectangle((0,0), 1, 1, edgecolor='red')
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.range = self.img.shape[0:2]
        self.rect_coor = []
        self.press = False
        self.ax.add_patch(self.rect)
        self.ax.imshow(self.img)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.ax.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.ax.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        print 'press'
        self.x0 = event.xdata
        self.y0 = event.ydata
        if self.x0 < 1:
            self.x0 = 1
        self.press = True
        print self.range

    def on_release(self, event):
        print 'release'
        self.x1 = event.xdata
        self.y1 = event.ydata
        self.press = False
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
        self.rect_coor.append((self.x0, self.y0, self.x1, self.y1))
        self.ax.figure.canvas.draw()
    
    def on_motion(self, event):
        print 'motion'
        if self.press == True:
            x0, y0, x1, y1 = self.x0, self.y0, self.x1, self.y1
            dx = event.xdata - x0
            dy = event.ydata - y0
            self.rect.set_width(dx)
            self.rect.set_height(dy)
            self.rect.set_xy((self.x0, self.y0))
            self.ax.figure.canvas.draw()

    def range_detect(self, coor):
        if not coor[0]:
            print 'ok'
            coor[0] = 0
            print coor[0]
        if not coor[1]:
            coor[1] = 0

a = Annotate()
plt.show()