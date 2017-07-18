from fs.folders import traversal
from fs.folders import traversal_dirs_tree
from util.log import info
import os

#info('basename', traversal("/home/eric/Desktop/rect6/Image"))
info('dirs', os.listdir('/home/eric/Desktop/rect6'))
info('tree', traversal_dirs_tree('/home/eric/glog'))