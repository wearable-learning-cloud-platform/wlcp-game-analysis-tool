import json
import pandas as pd
from ast import literal_eval
import glob
import csv

path_to_json = "../data/"
data = []

files = glob.glob('umass-ersp2023-project/data/*', recursive=False)
#print(files)

for single_file in files:
    with open(single_file, 'r') as f:
        json_file = json.load(f)
        new_string = json.dumps(json_file, indent = 2)
        print(new_string)
        data.append(json_file)