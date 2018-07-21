__author__ = 'zhangwh'

import json
import sys

if len(sys.argv) < 3 :
    raise Exception('args must more than 2!')

path_list = sys.argv[1:]

target_notebook = {}
cells_lst = []

for path in path_list :
    with open(path) as notebook:
        notebook_str = notebook.read()
        notebook_json = json.loads(notebook_str)
        cells = notebook_json['cells']
        cells_lst += cells

#复用最后一个文件的格式内容
notebook_json['cells'] = cells_lst
target_str = json.dumps(notebook_json)

target = open('data/target_notebook.ipynb', 'w')
target.write(target_str)


