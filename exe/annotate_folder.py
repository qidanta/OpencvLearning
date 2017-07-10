from __future__ import absolute_import

import json
import os
import sys

from matplotlib.patches import Rectangle
from PIL import Image

import glog as log
from fs.folders import traversal
from mouse.mouse import Annotate
from util.log import info


class Note(Annotate):
    '''Note img by rectangles
    '''
    def __init__(self, opt):
        '''initing nota bg img

        - Params:
        @opt: config for Note class
        @index: bg equals -1, other normal index
        @note_data: store note data
        '''
        bg = Image.open('./img/bg.png').convert('RGB')
        super().__init__(bg)
        self.initlized(opt)
        self.opt = opt
        self.index = -1
        self.note_data = {}

    def initlized(self, opt):
        '''get img_files, and already note data in `txt` file
        ...if already exit note data, get img_files by sets(img_files) - sets(labels)
        '''
        self.img_files = traversal(opt.folderpath)
        self.labels = self.split_labels(opt.labelpath)
        self.img_files = self.merge(self.img_files, self.labels)
    
    def on_key_press(self, event):
        '''key press event, `next img`, `pre img`, `remove rects`, `save note data`. 
        ... and auto save note data: 
        - key 'D': next img
        - key 'A': pre img
        - key 'W': remove last rect
        - key 'X': save note data into `json file`

        - Params:
        @self.filepath: pre img filepath
        @self.basename: pre img file name
        @self.index: pre img index in self.img_files(list)
        @filepath: current img filepath
        @img: current img(the img to change img that showed in current windows)
        '''
        self.filepath = self.img_files[self.index]
        self.basename = os.path.basename(self.filepath)
        if event.key.upper() == 'D' or event.key.upper() == 'A':
            if event.key.upper() == 'D':
                self.index += 1

            if  event.key.upper() == 'A':
                self.index -= 1  
            
            self.index = len(self.img_files) - 1 if self.index >= len(self.img_files) else self.index
            self.index = 0 if self.index <0 else self.index
            if self.index != 0:
                self.note_data[self.basename] = self.rect_coor
            filepath = self.img_files[self.index]
            img = Image.open(filepath)
            self.set_bg(img)
            self.redraw_bg(img)

        if event.key.upper() == 'W':
            if len(self.ax.patches) > 1:
                log.info("removing last rect of {}".format(self.basename))
                del self.rect_coor[len(self.rect_coor) - 1]
                self.ax.patches[len(self.ax.patches) - 1].remove()
                self.ax.patches[0].set_visible(False)
            else:
                info.error("already removing all rects {}".format(self.basename))
                self.ax.patches[0].set_visible(False)
            self.ax.figure.canvas.draw()

        if event.key.upper() == 'X':
            log.info("saving {} data into {}".format(self.basename, self.opt.jsonpath))
            if self.index != 0:
                with open(self.opt.jsonpath, 'w') as f:
                    json.dump(self.note_data, f)

        self.auto_save()


    def split_labels(self, label_path):
        '''get labels from `txt` file, labels are imgs that noted
        ...if `txt` file exits, return labels in file; else return []
        '''
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
        '''get a list of (imgs - labels)
        '''
        dirname = os.path.dirname(imgs[0])
        labels = ['{}{}'.format(dirname, basename) for basename in labels]
        imgs_sets, labels_sets = set(imgs), set(labels)
        return list(imgs_sets - labels_sets)

    def auto_save(self):
        '''auto save self.note_data into jsonpath
        '''
        if self.index > 10 and self.index % 10 == 0:
            log.info("auto saving data into {}".format(self.opt.jsonpath))
            with open(self.opt.jsonpath, 'w') as f:
                    json.dump(self.note_data, f)
