import csv
import json
import argparse
import numpy as np
import os

def fluidDataSet_to_csv(json_path):
    data = None
    with open(json_path) as f:
        data = json.load(f)
    csv_data = []
    for key in data['data']:
        row = []
        row.append(key)
        row.extend(data['data'][key])
        csv_data.append(row)

    return csv_data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",action='store',dest='input',type=str,required=True)
    parser.add_argument("--file-suffix",action='store',dest='file_suffix',type=str)
    # parser.add_argument("--label-column",action='store_true',dest='label_column')
    args = parser.parse_args()

    csv_data = fluidDataSet_to_csv(args.input)

    new_path = os.path.splitext(args.input)[0]
    
    if args.file_suffix != None:
        new_path += '_' + args.file_suffix

    new_path += '.csv'

    with open(new_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
