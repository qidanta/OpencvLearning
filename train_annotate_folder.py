from exe.annotate_folder import Note
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--folderpath', default="/home/eric/Desktop/rect6/Image", help='img folder to annote')
opt = parser.parse_args()
n = Note(opt)
plt.show()
