def prefix_polygon(coors):
    '''convert coor into `POLYGON((0 0, 0 300, 300 300,300 0, 0 0))` type

    - Params:
    @coors: coor list, like [(ltx, lty, rbx, rby)]

    - Return:
    a list contain ['POLYGON((0 0, 0 300, 300 300,300 0, 0 0))']
    '''
    polygons = []
    for coor in coors:
        print (round(coor[0]))
        lt = '{} {}'.format(round(coor[0]), round(coor[1]))
        lb = '{} {}'.format(round(coor[0]), round(coor[3]))
        rb = '{} {}'.format(round(coor[2]), round(coor[3]))
        rt = '{} {}'.format(round(coor[2]), round(coor[1]))
        polygon = 'POLYGON(({}, {}, {}, {}, {}))'.format(lt, lb, rb, rt, lt)
        polygons.append(polygon)
    
    return polygons

def prefix_coor_double(coors):
    '''convert [(lrx, lty, btx, bty)] to ltx lty,btx bty as string

    - Params:
    @coors: [(ltx, lty, btx, bty)]

    - Returns:
    a list contain 'ltx lty,btx bty'
    '''
    polygons = []
    for coor in coors:
        lt = '{} {}'.format(round(coor[0]), round(coor[1]))
        rb = '{} {}'.format(round(coor[2]), round(coor[3]))
        polygon = '{},{}'.format(lt, rb)
        polygons.append(polygon)
    return polygons

def create_rect_grah(n, distance):
    '''create nxn array, the distance between coor and coor is distance

    - Params:
    @n: the grah'size is nxn
    @distance: the distance of two Adjacent nodes is distance

    - Return:
    ```python
    G = {1:{1:0,    2:6,    4:6},
     2:{1:6,    2:0,    3:6, 5:6},
     3:{2:6, 3:0, 6:6},
     4:{1:6,    4:0, 5:6,   7:6},
     5:{2:6, 4:6, 5:0, 6:6, 8:6},
     6:{3:6, 5:6, 6:0, 9:6},
     7:{4:6, 7:0, 8:6},
     8:{5:6, 7:6, 8:0, 9:6},
     9:{6:6, 8:6, 9:0}}
    ```
    just like that!
    and each node in nxn matrix will be labeled by index from (1, nxn), so nxn will labeled from (1, 9)
    '''
    grah = {}
    for row in range(n):
        for col in range(n):
            line = {}
            nodes = [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]
            for node in nodes:
                if n> node[0] >= 0 and n > node[1] >= 0:
                    index = node[0] * n + node[1] + 1
                    line[index] = distance
            index = row * n + col + 1
            line[index] = 0
            grah[index] = line
    return grah