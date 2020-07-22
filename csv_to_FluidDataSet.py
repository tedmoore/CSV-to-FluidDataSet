"""
Ted Moore
ted@tedmooremusic.com
www.tedmooremusic.com
July 19, 2020

Take in a CSV file of data and create a json file that is appropriately formatted for loading into a FluidDataSet (www.flucoma.org)
"""

import csv
import json
import argparse
import numpy as np
import os

def csv_to_FluidDataSet(csv_data,indices,label_column,header_row):

    json_dict = {}

    json_dict['cols'] = len(indices)

    selected_data = []
    
    for i, row in enumerate(csv_data):
        if header_row and i == 0:
            # skip this row
        else:
            frame = []
            for index in indices:
                if label_column:
                    index += 1
                frame.append(row[index])
            selected_data.append(frame)

    json_data = {}

    for i, vector in enumerate(selected_data):
        label = str(i)
        if label_column:
            label = csv_data[i][0]
        json_data[label] = vector

    json_dict["data"] = json_data

    return json_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",action='store',dest='input',type=str,required=True)
    parser.add_argument("--start-index",action='store',dest='start_index',type=int)
    parser.add_argument("--end-index",action='store',dest='end_index',type=int)
    parser.add_argument("--file-suffix",action='store',dest='file_suffix',type=str)
    parser.add_argument("--specify-indices",action='store',dest='specified_indices',nargs='+',type=int)
    parser.add_argument("--label-column",action='store',dest='label_column',type=bool,default=False)
    parser.add_argument("--header-row",action='store',dest='header_row',type=bool,default=False)
    args = parser.parse_args()

    
    csv_data = []

    with open(args.input) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            csv_data.append(np.array(row))

    csv_data = np.array(csv_data)

    if args.specified_indices == None:
        start_index = None
        end_index = None
        
        if args.start_index == None:
            start_index = 0
        else:
            start_index = args.start_index

        if args.end_index == None:
            end_index = len(csv_data[0]) - 1
        else:
            end_index = args.end_index

        indices = range(start_index,end_index+1)
    else:
        indices = args.specified_indices

    json_dict = csv_to_FluidDataSet(csv_data,indices,args.label_column,args.header_row)
    
    file_suffix = ''
    
    if args.file_suffix != None:
        file_suffix = args.file_suffix
    
    new_path = os.path.splitext(args.input)[0] + '_' + file_suffix + '.json'

    with open(new_path,"w") as json_file:
        json.dump(json_dict, json_file)