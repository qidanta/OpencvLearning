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