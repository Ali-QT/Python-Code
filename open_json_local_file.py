
import json

fname = "file-path and name"
def open_file(fname):
   with open(fname) as json_file:
        data = json.load(json_file)
        return data
