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

### folders.py

* def `traversal` - in `os`

## exe

contain some applications by using modules above!

### Annote

* [ ] - set `self.ax.patches[index]` visible false by `[1-9]`
* [ ] - remove `[index]` coor in `self.rect_coor`
* [x] - save `self.rect_coor` into data by by press `key s or d`
* [ ] - convert json to txt in special formation
* [ ] - add some glog/remove info

## How to use it?

file which has `test` prefix, is **main entry file**!


