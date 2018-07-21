__author__ = 'uc'

import sys
import json

class Notebook:
    def __init__(self, path):
        self.path = path;
        with open(path) as note_file:
            self.notebook_str = note_file.read()
            self.notebook_json = json.loads(self.notebook_str)

    def __add__(self, another):
        self.notebook_json['cells'] = self.notebook_json['cells'] + another.notebook_json['cells']
        return self;

    def __getitem__(self, index):
        return self.notebook_json['cells'][index]


    def save(self):
        notebook_str = json.dumps(self.notebook_json)
        target_file = open(self.path, 'w')
        target_file.write(notebook_str)

if __name__ == "__main__":
    notebook1 = Notebook("data/1.ipynb")
    notebook2 = Notebook("data/2.ipynb")
    notebook1 += notebook2
    print(notebook1[1])
    notebook1.save()

