from __future__ import absolute_import
import sys
from PIL import Image
import json
import os
from mouse.mouse import Annotate
from fs.folders import traversal
from util.log import info
from matplotlib.patches import Rectangle
import glog as log

class Note(Annotate):
    def __init__(self, opt):
        bg = Image.open('./img/bg.png').convert('RGB')
        super().__init__(bg)
        self.initlized(opt)
        self.opt = opt
        self.index = 0
        self.note_data = {}

    def initlized(self, opt):
        self.img_files = traversal(opt.folderpath)
        self.labels = self.split_labels(opt.labelpath)
        self.labels = self.merge(self.img_files, self.labels)
        info('label', self.labels)
    
    def on_key_press(self, event):
        filepath = self.img_files[self.index]
        self.img = Image.open(filepath)
        basename = os.path.basename(filepath)
        if event.key.upper() == 'D' or event.key.upper() == 'A':
            if event.key.upper() == 'D':
                self.index += 1

            if  event.key.upper() == 'A':
                self.index -= 1  
            
            self.index = len(self.img_files) - 1 if self.index >= len(self.img_files) else self.index
            self.index = 0 if self.index <0 else self.index
            self.note_data[basename] = self.rect_coor
            info(basename, self.note_data)
            self.set_bg(self.img)
            self.redraw_bg()

        if event.key.upper() == 'W':
            if len(self.ax.patches) > 1:
                del self.rect_coor[len(self.rect_coor) - 1]
                self.ax.patches[len(self.ax.patches) - 1].remove()
                self.ax.patches[0].set_visible(False)
            else:
                self.ax.patches[0].set_visible(False)
            self.ax.figure.canvas.draw()

        if event.key.upper() == 'P':
            for index, rect in enumerate(self.ax.patches):
                if index != 0:
                    info('rect-x', rect.get_x())
                else:
                    rect.set_visible(False)
        
    def set_bg(self, frame):
        self.rect_coor = []
        for index, rect in enumerate(self.ax.patches):
            if index != 0:
                rect.remove()
            else:
                rect.set_visible(False)
    def split_labels(self, label_path):
        labels = []
        if os.path.exists(label_path):
            self.continued = True
            with open(label_path, 'rt') as f:
                for line in f:
                    labels.append(line.split(' ')[0])
        else:
            self.continued = False
            log.info("create file in {}".format(label_path))
            os.mknod(label_path)
        return labels
    def merge(self, imgs, labels):
        imgs = [os.path.basename(filepath) for filepath in imgs]
        imgs_sets, labels_sets = set(imgs), set(labels)
        return list(imgs_sets - labels_sets)