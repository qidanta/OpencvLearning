from fs.folders import traversal_dirs_tree
import os
import glob

def dirstree_to_content(dirs, lv=0):
    heads = dirs.keys()
    content = ''
    indent = '    '*lv if lv >= 1 else ''
    for index in heads:
        md_files = glob.glob('{}/*.md'.format(index))
        if md_files:
            content += al_head(md_files, indent)
        if isinstance(dirs[index], dict):
            content += dirstree_to_content(dirs[index], lv=lv+1)
    return content

def ul_head(str, indent):
    return '{}* {}\n'.format(indent, str)

def al_head(strs, indent):
    content = ''
    for str in strs:
        fix = '[{}]({})'.format(os.path.basename(str), str)
        content += ul_head(fix, indent)
    return content