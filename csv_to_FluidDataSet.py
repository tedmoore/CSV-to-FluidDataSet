import csv
import json
import argparse
import numpy as np
import os

def csv_to_FluidDataSet(input_path,start_index,end_index):

    csv_data = []

    with open(args.input) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            csv_data.append(np.array([float(val) for val in row]))

    csv_data = np.array(csv_data)

    if args.start_index == None:
        start_index = 0
    else:
        start_index = args.start_index

    if args.end_index == None:
        end_index = len(csv_data[0]) - 1
    else:
        end_index = args.end_index
    
    json_dict = {}

    json_dict['cols'] = (end_index - start_index) + 1

    selected_data = csv_data[:,start_index:end_index+1]

    selected_data = selected_data.tolist()

    json_data = {}

    for i, vector in enumerate(selected_data):
        json_data[str(i)] = vector

    json_dict["data"] = json_data

    return json_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",action='store',dest='input',type=str,required=True)
    parser.add_argument("--start-index",action='store',dest='start_index',type=int)
    parser.add_argument("--end-index",action='store',dest='end_index',type=int)
    parser.add_argument("--file-suffix",action='store',dest='file_suffix',type=str)
    args = parser.parse_args()

    file_suffix = ''
    if args.file_suffix != None:
        file_suffix = args.file_suffix
    
    json_dict = csv_to_FluidDataSet(args.input,args.start_index,args.end_index)

    new_path = os.path.splitext(args.input)[0] + '_' + file_suffix + '.json'

    with open(new_path,"w") as json_file:
        json.dump(json_dict, json_file)