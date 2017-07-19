from fs.folders import traversal_dirs_tree
from util.compare import each
import os
import glob

def md_meau(path, filters, relpath, title, quote):
    '''walk `path`, then get all dirs under this `path`, and 
    convert to a ul content in markdown file.

    - Params:
    @path: which path to os.walk
    @filters: a list of dirname, os.walk will skip these dirs
    @relpath: convert abspath to relpath or not
    @title: markdown file, h1 title
    @quote: markdown file quote under h1 title

    - Returns:
    a str contain h1, quote, dirtree content
    '''
    h1 = h1_head(title)
    quote = md_quote(quote)
    dirs = traversal_dirs_tree(path)
    mdul = dirstree_to_mdul(dirs, filters=filters)
    basename = os.path.basename(path)
    if relpath:
        mdul = a_relpath(mdul, '(', basename)
    return h1 + quote + mdul

def dirstree_to_mdul(dirs, lv=0, filters=['.git', '.vscode', 'img', 'resource']):
    '''convert dirs into md file content
    and `.md` under dirs will be converted into `<li><a>/a><</li>`
    and others will be converted into normal `<li></li>`

    - Params:
    @dirs: a dict type, will convert it into md file content.
    @lv: dir tree deepth
    @filters: these dirs in filters, will be skiped when converting

    - Returns:
    a str of dirtree content 
    '''
    heads = dirs.keys()
    content = ''
    indent = '    '*lv if lv >= 1 else ''
    for index in sorted(heads):
        if each(filters, os.path.basename(index)):
            md_files = glob.glob('{}/*.md'.format(index))
            if md_files:
                content += ul_head(os.path.basename(index), indent)
                content += al_head(md_files, indent + '    ')
            else:
                content += ul_head(os.path.basename(index), indent)
            if isinstance(dirs[index], dict):
                content += dirstree_to_mdul(dirs[index], lv=lv+1, filters=filters)
    return content

def ul_head(str, indent):
    '''get a `<li></li>` of markdown type

    - Params:
    @str: content in `<li></li>`
    @indent: nums * 4 space, the li item indent

    - Returns
    a str just like `* xxx`
    '''
    return '{}* {}\n'.format(indent, str)

def al_head(strs, indent):
    '''get a list of `<li><a></a></li>` of markdown type

    - Params:
    @strs: a list of filepath, and will be `<a></a>`'s href
    @indent:  nums * 4 space, the li item indent

    - Returns:
    a str just like `* [xxx](path)\n` + ... + `* [xxx](path)\n`
    '''
    content = ''
    for str in strs:
        filename = os.path.basename(str).split('.')[0]
        fix = '[{}]({})'.format(filename, str)
        content += ul_head(fix, indent)
    return content

def h1_head(str):
    '''convert str into h1

    - Params:
    @str: h1 element's content

    - Returns:
    a str just like '# xxx'
    '''
    return '# {}\n'.format(str)

def md_quote(str):
    '''convert str into quote in markdown file

    - Params:
    @str: quote's content

    - Returns:
    a str just like `> xxx`
    '''
    return '> {}\n'.format(str)

def a_relpath(str, start_flag, end_flag):
    '''convert abspath into relpath
    and str should contain `...(filepath)`, the replace start_flag and end_flag in str into `(./`

    - Params:
    @str: convert abspath in this str, and convert it into relpath
    @start_flag: replace str start flag
    @end_flag: replace str end flag

    - Returns:
    a str just contain relpath
    '''
    arrs = str.split('\n')
    new_arrs = []
    for element in arrs:
        length = len(element)
        if element.find(start_flag) > -1:
            start = element.index(start_flag)
            end = element.index(end_flag)
            new_str = element[0:start] + '(./' + element[end:length]
            new_arrs.append(new_str)
        else:
            new_arrs.append(element)
    return '\n'.join(new_arrs)
