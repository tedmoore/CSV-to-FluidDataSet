import csv
import json
import argparse
import numpy as np
import os

def fluidDataSet_path_to_csv_data(json_path):
    print()
    print(json_path)
    with open(json_path) as file_:
        print(file_)
        data = json.load(file_)
        print(data)
        csv_data = []
        for key in data['data']:
            row = []
            row.append(key)
            row.extend(data['data'][key])
            csv_data.append(row)

        return csv_data

def fluidDataSet_path_to_csv_file(path,file_suffix):
    csv_data = fluidDataSet_path_to_csv_data(path)

    new_path = os.path.splitext(path)[0]
    
    if file_suffix != None:
        new_path += '_' + file_suffix

    new_path += '.csv'

    csv_data_to_file(csv_data,new_path)

def csv_data_to_file(csv_data,path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",action='store',dest='input',type=str,required=True,nargs='+')
    parser.add_argument("--file-suffix",action='store',dest='file_suffix',type=str)
    # parser.add_argument("--label-column",action='store_true',dest='label_column')
    args = parser.parse_args()

    for f in args.input:
        print()
        print(f)
        fluidDataSet_path_to_csv_file(f,args.file_suffix)
