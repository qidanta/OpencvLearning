from __future__ import absolute_import
import sys
from PIL import Image
import json
import os
from mouse.mouse import Annotate
from fs.folders import traversal
from util.log import info

class Note(Annotate):
    def __init__(self, opt):
        bg = Image.open('./img/bg.png').convert('RGB')
        super().__init__(bg)
        self.initlized(opt)
        self.opt = opt
        self.index = 0
        self.note_data = {}
        info('init_img', self.img_files)

    def initlized(self, opt):
        self.img_files = traversal(opt.folderpath)
    
    def on_key_press(self, event):
        filepath = self.img_files[self.index]
        self.img = Image.open(filepath)
        basename = os.path.basename(filepath)
        if event.key.upper() == 'D':
            self.index += 1

        if  event.key.upper() == 'A':
            self.index -= 1  

        if  event.key.upper() == 'S':
            self.index += 1
        
        self.index = len(self.img_files) - 1 if self.index >= len(self.img_files) else self.index
        self.index = 0 if self.index <0 else self.index
        self.note_data[basename] = self.rect_coor
        info(basename, self.note_data)
        self.set_bg(self.img)
        self.redraw_bg()
            
        
