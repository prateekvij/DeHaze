#!/usr/bin/env python
"""
The file contain code for creating training data and storing it as a pickle 
file. The data consist of 1449 hazy images of size (480, 640, 3) 
from the NYU dataset.

Run the file as "python createTrainingData.py" from the pre-processing directory

The image format is (480, 640, 3) and image count is 1449. The value of pixel
is in range [0, 1] rather than integer values from 0 to 255. 

Check the path to the images given in variable 'data_dir'. 
Change the output_dir and output_path to change the path of the pickle file 
to be stored

The code create multiple pickle files for storing the result. The interval is 
mentioned in the var 'interval'. Adjust the intervals as per your need.

"""
import numpy as np 
from PIL import Image
from os import system
from os import listdir
from os.path import isfile, join
import pickle

__author__ = "Prateek Vij"
__copyright__ = "Copyright 2017, Indian Institute of Technology Guwahati"
__credits__ = ["Prateek Vij"]
__license__ = "GPL"
__version__ = "1.0.1"
__status__ = "Production"


intervals = [(1, 500), (501, 1000), (1001, 1449)]
data_dir = "../../data/NYU_Hazy/"
output_dir = "../../metadata/"

for k in intervals:
	start_index = k[0]
	end_index = k[1]
	output_path = ( output_dir + "hazy_data_" + str(start_index) + "_" +
					str(end_index) + ".pkl" )
	hazy_data = []
	for i in range(start_index, end_index+1):
		fpath = join(data_dir,str(i)+"_Hazy.bmp")
		hazy = Image.open(fpath)
		hazy = np.array(hazy)
		hazy = np.asarray(hazy, dtype=np.float32)
		normalised_hazzy = np.divide(hazy, 255.0)
		hazy_data.append(normalised_hazzy)
		print i

	hazy_data = np.asarray(hazy_data, dtype=np.float32)

	with open(output_path, "wb") as out_file:
		pickle.dump(hazy_data, out_file, pickle.HIGHEST_PROTOCOL)
