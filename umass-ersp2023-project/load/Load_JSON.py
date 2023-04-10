import json
import pandas as pd
from ast import literal_eval
import glob
import csv
import copy

path_to_json = "../data/"
data = []

files = sorted(glob.glob('umass-ersp2023-project/data/*', recursive=False))

f = open(files[0], 'r')
print(f)

for single_file in files:
    with open(single_file, 'r') as f:
        json_file = json.load(f)
        new_string = json.dumps(json_file, indent = 2)
        #print(new_string)
        data.append(json_file)

#Some tutorial########
#list(Obj.keys()): return a list/array of all of Obj's attributes in string type


#This is to sort (if needed) ###############################
# def myFunc(e):
#     return len(e)

# for single_file in data:
#     att =  list(single_file.keys())
#     if (single_file['gameId'] == 'TangramsRace'):
#         temp = single_file['states']
#         b = []
#         for i in temp:
#             b.append(i['stateId'])
#         b.sort(key=myFunc)
#         for i in b:
#             print(i)
##################################################

#This is to check sound/picture/video outputs
# for single_file in data:
#     temp = single_file['states']
#     for i in temp:
#         att = list(i.keys())
#         for key in att:
#             if (key == 'pictureOutputs'):
#                 if (i[key]):
#                     print(single_file['gameId'])
#####################################################

#This is to extract text
c = []
for single_file in data:
    temp = single_file['states']
    d = []
    #print('------------------------------')
    for i in temp:
        att = list(i.keys())
        for key in att:
            if (key == 'displayText'):
                s = ''
                text = list(i[key].keys())
                for j in text:
                    s += i[key][j]
                d.append(s)
    c.append(d)

for i in c[0]:
    print(i)
####################################################

            


