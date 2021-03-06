# UPDATE
> LIST BY FOLDER NAME

<!-- TOC -->

- [UPDATE](#update)
  - [SETTING](#setting)
  - [June](#june)
    - [6-24](#6-24)
    - [6-27](#6-27)
    - [6-28](#6-28)
    - [6-30](#6-30)
  - [July](#july)
    - [7-06](#7-06)
    - [7-10](#7-10)
    - [7-18/1-19](#7-181-19)
    - [7-20](#7-20)

<!-- /TOC -->

## SETTING

* **created**: create files from 0-1
* **add**: add new to origin
* **changed**: change somethings
* **move**: move files/funcs from path1 to path2
* **fixed**: fix bugs

## June

### 6-24

* in `mouse.py` - **created** this folder, and create `mouse.py` file
* in `mouse.py` - **add** class `Annotate` and def `draw_rect`

### 6-27

* in `Video` - **created** this folder, and **created** `camera.py`, and **add** video demo in it!

### 6-28

And default set webcamera src is `src=rstp://admin:1jiao426@192.168.1.3/h264/main/ch1/av_stream` for test!

* in `Video/camera.py` - **add** webcam(under test)

### 6-30

* in `util/log.py` - **created** this file, format print out's format
* in `fs/fs.py` - **created** this file and folder, and **add** `array_to_txt`

## July

* in `util/log.py` - **add** def `info`
* in `util/prefix.py` - **add** def `prefix_polygon`and `prefix_coor_double`

### 7-06

* in `fs/folders.py` - **created** this file, and **traversal**
* in `mouse` - **changed** class `Annotate`

### 7-10

* in `fs/fs.py` - **add** func `nps_to_npz`, convert dict(contain np.array) in `.npz` file

### 7-18/1-19

* in `fs/md.py` - **created** this file, and **add** some defs about markdown files
* in `fs/folders.py` - **add** def `traversal_dirs_tree`
* in `fs/fs.py`- **add** def `str_to_md`
* in `util/compare.py` - **add** def `some` and `each`, do some jobs like `any` and `all` 
* in `ml/road.py` - **create** this folder and file, **add** def `Dijkstra`
* in `util/prefix.py` - **add** def `create_rect_grah` 

### 7-20

* packages `glog` - rewrite `glog.py`, now we can log info into `*.log`. and the rewrited file stored in `README/glog.py`