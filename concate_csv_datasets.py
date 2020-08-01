import csv
import argparse
import numpy as np
import os
import time

from csv_to_FluidDataSet import csv_path_to_data
from fluidDataSet_to_csv import csv_data_to_file

def make_new_path(old_path,extension,label,append_old_filename=False):
    out_path_tmp = os.path.splitext(old_path)[0].split('/')
    if append_old_filename:
        out_path_tmp = out_path_tmp[:-1]

    out_path = ''
    for token in out_path_tmp:
        out_path += token + '/'

    out_path += time.strftime('%y%m%d_%H%M%S')

    if label != None:
        out_path += '_' + label

    out_path += '.' + extension

    return out_path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",action='store',dest='input',type=str,required=True,nargs='+')
    parser.add_argument("--file-name",action='store',dest='file_name',type=str)
    parser.add_argument("--vertical",action='store_true',dest='vertical')
    parser.add_argument("--horizontal",action='store_true',dest='horizontal')
    args = parser.parse_args()

    if args.horizontal and args.vertical:
        print('Cannot specify both horizontal and vertical')
        exit()

    if not args.horizontal and not args.vertical:
        print('Must specify either horizontal or vertical')
        exit()

    if args.vertical:
        final_data = []
        length = None
        for i, path in enumerate(args.input):
            data = csv_path_to_data(path)
            if i == 0:
                length = len(data[0])
            else:
                if length != len(data[0]):
                    print('ERROR: dataset vectors not same length!')
                    exit()
            final_data += data
        new_path = make_new_path(path,'csv',args.file_name,True)
        csv_data_to_file(final_data,new_path)

    if args.horizontal:
        print("horizontal not implemented yet")
        exit()