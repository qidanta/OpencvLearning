#%%
from exe.annotate_folder import Note
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--folderpath', default="/home/eric/Desktop/Project-PY/pro-py27/03camera2distance/distance-to-camera/distance-to-camera/calibrate/715/remap", help='img folder to annote')
parser.add_argument('--labelpath', default="/home/eric/Desktop/Project-PY/pro-py27/03camera2distance/distance-to-camera/distance-to-camera/calibrate/715/labels6.txt", help='txt to store annote')
parser.add_argument('--jsonpath', default="/home/eric/Desktop/Project-PY/pro-py27/03camera2distance/distance-to-camera/distance-to-camera/calibrate/715/labels6.json", help='json to store annote')
parser.add_argument('--mode', default="preview", help='what kind of mode')

opt = parser.parse_args()
n = Note(opt)
plt.show()
