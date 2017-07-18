from fs.folders import traversal
from fs.folders import traversal_dirs_tree
from fs.md import dirstree_to_content
from util.log import info
import os

dirs = traversal_dirs_tree('/home/eric/Dropbox/Sketch')
print (dirstree_to_content(dirs))