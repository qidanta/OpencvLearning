from fs.folders import traversal
from fs.folders import traversal_dirs_tree
from fs.md import dirstree_to_mdul, md_meau
from fs.fs import str_to_md
from util.log import info
import os

dirs = traversal_dirs_tree('/home/eric/Dropbox/Sketch')
md = md_meau('/home/eric/Dropbox/Sketch', filters = ['.git', '.vscode', 'img', 'resource'], relpath = True, title='test', quote = 'test')
str_to_md(md)