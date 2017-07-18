import os

def traversal(path):
    '''walk path, and return a list contain all files in this folders

    - Params:
    @path: walk path

    - Return:
    return a list contain all files(abspath) in this folders
    '''
    file_list = list(os.walk(path))[0][2]
    file_list = [path + '/' + filename for filename in file_list]
    return file_list

def traversal_dirs_tree(path):
    '''get all dirs under one folders

    - Params:
    @path: get dirs under the `path`

    - Return:
    a dict of dirs
    '''
    root, dirs, files = list(os.walk(path))[0]
    result = {}
    if dirs:
        for dir in dirs:
            path = '{}/{}'.format(root, dir)
            result[path] = traversal_dirs_tree(path)
    return result if result else None