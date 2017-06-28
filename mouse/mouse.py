import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import cv2
import numpy

def listEvent():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print events

# opencv
def draw_rect(event, x, y, flags, params):
    '''draw a rectangle by opencv-mouse

    - Params:
    @event: maybe from cv2.setMouseCallback
    @x,y: from cv2, when mouse click
    @params: from user, (img, (ltx, lty, rbx, rby)), (ltx, lty, rbx, rby) default is (0, 0, 0, 0). And change by mouse event

    - Returns:
    no returns, but will change params[1]
    '''
    global sx, sy, ex, ey
    
    drawing = False
    if event == cv2.EVENT_LBUTTONDOWN:
        sx, sy = x, y
    #elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(params[0], (sx, sy), (x ,y), (0, 255, 0), 1)
        ex, ey = x, y
        params[1] = sx, sy, ex, ey

# matplotlib - mouse
class Annotate(object):
    def __init__(self, frame):
        self.ax = plt.gca()
        self.img = frame
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
        self.x0 = event.xdata if event.xdata else 0
        self.y0 = event.ydata if event.ydata else 0
        self.press = True

    def on_release(self, event):
        self.x1 = event.xdata if event.xdata else 0
        self.y1 = event.ydata if event.ydata else 0
        self.press = False
        # self.rect.set_width(self.x1 - self.x0)
        # self.rect.set_height(self.y1 - self.y0)
        # self.rect.set_xy((self.x0, self.y0))
        self.rect_coor.append((self.x0, self.y0, self.x1, self.y1))
        self.draw_rect(self.rect_coor)
        print(self.rect_coor)
    
    def on_motion(self, event):
        if self.press == True:
            x0, y0, x1, y1 = self.x0, self.y0, self.x1, self.y1
            x_now = event.xdata if event.xdata else 0
            y_now = event.ydata if event.ydata else 0
            dx = x_now - x0
            dy = y_now - y0
            self.rect.set_width(dx)
            self.rect.set_height(dy)
            self.rect.set_xy((self.x0, self.y0))
            self.ax.figure.canvas.draw()

    def draw_rect(self, coor_arrs):
            '''draw rect, and rect's arr from coor_arrs
            '''
            for coor in coor_arrs:
                rect = Rectangle((0,0), 1, 1, edgecolor='red', fill=False)
                self.ax.add_patch(rect)
                rect.set_width(coor[2] - coor[0])
                rect.set_height(coor[3] - coor[1])
                rect.set_xy((coor[0], coor[1]))
                self.ax.figure.canvas.draw()