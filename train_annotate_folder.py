from exe.annotate_folder import Note
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--folderpath', default="/home/eric/Desktop/rect6/Image", help='img folder to annote')
parser.add_argument('--labelpath', default="/home/eric/Desktop/rect6/labels6.txt", help='txt to store annote')
parser.add_argument('--continued', default=True, help='contine annote or not')
opt = parser.parse_args()
n = Note(opt)
plt.show()
