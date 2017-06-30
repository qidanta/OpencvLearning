def array_to_txt(arr, path):
    '''write arr into txt

    - Params:
    @arr: item in arr is string
    @path: somefile.txt's path
    '''
    with open(path, 'wt') as f:
        for line in arr:
            f.write(line + '\n')