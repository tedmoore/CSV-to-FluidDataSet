A python script for converting a CSV file of data into a json file that is loadable by FluidDataSet (https://www.flucoma.org/).

When you specify which columns to pull out, the end-index column will end up in the file (e.g., start-index of 2 and end-index of 4 will give you 3 columns [2-4]).

The json file will be put in the same folder as the csv file.

Arguments:

--input		file path of the csv file
--start-index	first column of where you want to start pulling data from
--end-index	last column of where you want to start pulling data from
--file-suffix	string that will be appended to the file name 