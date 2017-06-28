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
        