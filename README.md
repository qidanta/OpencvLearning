# OpencvLearning
> Store some tips&funcs&tips about

## What contain?

* mouse-event
    * opencv-mouse
    * matplotlib-mouse
* file I/O
* print
* str

## tips

* `from __future__ import absolute_import` - solve `attempted relative import beyond top-level package`
* `**kwag` - `kwag` is a dict, in function parameters

## Mouse

### mouse.py

* **def** `draw_rect` - by `opencv`
* **class** `Annotate` - by `matplotlib`

## Video

### camera.py

* def `local_camera` - by `cv2`
* def `web_camera`- by `imutils`

### commad

* cut a video - `ffmpeg -i ./car.mp4 -ss 00:00:03 -to 00:00:17 ./result.mp4` is better than any software!!

## util

### prefix.py
* def `prefix_` - in `python3`

### log.py

* def `info` - by  `termcolor`

## fs

### fs.py

* def `array_to_txt` - in `python3`
* def `nps_to_npz` - in `numpy`

### folders.py

* def `traversal` - in `os`

## exe

contain some applications by using modules above!

### Annote

#### TODO

* [ ] - set `self.ax.patches[index]` visible false by `[1-9]`
* [ ] - remove `[index]` coor in `self.rect_coor`
* [x] - save `self.rect_coor` into data by by press `key s or d`
* [ ] - convert json to txt in special formation
* [ ] - add some glog/remove info

#### How to use it?

It works undert `python3`, and `just python train_annotate_folder.py`! And, you nend type your imgs-folder-path in `parser --folderpath`

## How to use it?

* file which has `test` prefix, is **main debug entry file**!
* file which has `train` prefix, is **main entry file which has complete funcs**