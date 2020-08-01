import csv
import json
import argparse
import numpy as np
import os
from sklearn.manifold import TSNE, MDS
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

from csv_to_FluidDataSet import csv_path_to_data
from fluidDataSet_to_csv import csv_data_to_file
from concate_csv_datasets import make_new_path

def append_old_path(old_path,extension,label):
    out_path = os.path.splitext(old_path)[0]

    if label != None:
        out_path += '_' + label

    out_path += '.' + extension

    return out_path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",action='store',dest='input',type=str,required=True,nargs='+')
    parser.add_argument("--label-column",action='store_true',dest='label_column',default=False)
    parser.add_argument("--header-row",action='store_true',dest='header_row',default=False)
    args = parser.parse_args()

    pca_ = PCA(2)
    mds_ = MDS(2,verbose=2)
    tsne_ = TSNE(2,verbose=2)

    scaler_ = MinMaxScaler()

    for path in args.input:
        data = np.array(csv_path_to_data(path))
        header_row = None
        label_column = None
        if args.header_row:
            header_row = data[0]
            data = data[1:]
        if args.label_column:
            label_column = data[:,0]
            data = data[:,1:]

        normed_data = scaler_.fit_transform(data)

        print(len(normed_data),len(normed_data[0]))
        
        pca_output = pca_.fit_transform(normed_data)
        pca_output = scaler_.fit_transform(pca_output)

        mds_output = mds_.fit_transform(normed_data)
        mds_output = scaler_.fit_transform(mds_output)

        tsne_output = tsne_.fit_transform(normed_data)
        tsne_output = scaler_.fit_transform(tsne_output)

        # print(pca_output,mds_output,tsne_output)

        new_data =[]
        for i, row in enumerate(data):
            new_row = list(row) + list(pca_output[i]) + list(mds_output[i]) + list(tsne_output[i])
            if args.label_column != None:
                new_row.insert(0,label_column[i])
            new_data.append(new_row)

        if args.header_row:
            header_row += ['pca_1','pca_2','mds_1','mds_2','tsne_1','tsne_2']
            new_data.insert(0,header_row)
        new_path = append_old_path(path,'csv','with_pca_mds_tsne')
        csv_data_to_file(new_data,new_path)

