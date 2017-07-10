import numpy as np

def array_to_txt(arr, path):
    '''write arr into txt

    - Params:
    @arr: item in arr is string
    @path: somefile.txt's path
    '''
    with open(path, 'wt') as f:
        for line in arr:
            f.write(line + '\n')

def nps_to_npz(dicts, path):
    '''convert dicts to `.npz` file, the dicts should be like
    ... {'one': data, 'two': data}, because some np.array can not saved into `.json`

    - Params:
    @dicts: the dicts should be like {'one': data, 'two': data}
    @path: `.npz` file path, such as `/to/xx.npz`
    '''
    keys_list = list(dict.keys())
    np.save("path", **dict)