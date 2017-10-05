#!/usr/bin/env python
"""
The file contain code for creating transmission maps from actual and 
hazy images and store them as pickle files for easy loading.

Run the file as "python buildTransMap.py" from the pre-processing directory

Check the path to the images given in variable HAZY_img_dir 
and ORIGINAL_img_dir. Change the output_path to change the path of the pickle 
file to be stored

The code create multiple pickle files for storing the result. The interval is 
mentioned in the var 'interval'. Adjust the intervals as per your need.

"""
import numpy as np 
from PIL import Image
import pickle

__author__ = "Prateek Vij"
__copyright__ = "Copyright 2017, Indian Institute of Technology Guwahati"
__credits__ = ["Prateek Vij"]
__license__ = "GPL"
__version__ = "1.0.1"


intervals = [(1, 500), (501, 1000), (1001, 1449)]
A = np.ones((480,640,3), dtype = np.float32)
HAZY_img_dir = "../../data/NYU_Hazy/"
ORIGINAL_img_dir = "../../data/NYU_GT/"
output_dir = "../../metadata/"

for k in intervals:
	start_index = k[0]
	end_index = k[1]

	output_path = (output_dir + "t_maps_" + str(start_index) +
					"_" + str(end_index) + ".pkl")

	transmission_maps = []

	for i in range(start_index, end_index+1):
		I_path = HAZY_img_dir+str(i)+"_Hazy.bmp"
		J_path = ORIGINAL_img_dir+str(i)+"_Image_.bmp"
		
		I = np.asarray(Image.open(I_path), dtype=np.float32)
		I = np.divide(I, 255.001)

		J = np.asarray(Image.open(J_path), dtype=np.float32)
		J = np.divide(J, 255.001)

		t_num = np.subtract(A, I)
		t_den = np.subtract(A, J)
		t = np.divide(t_num, t_den)
		transmission_maps.append(t)
		print i

		# Uncomment the lines below if you want to save the 
		# the transmission map as image in the current folder

		# t_image = np.multiply(t, 255.001)
		# t_image = np.asarray(t_image, dtype=np.uint8)
		# print np.amax(t_image)
		# img = Image.fromarray(t_image)
		# img.save(str(i)+'original.png')

	with open(output_path, "wb") as out_file:
		pickle.dump(t, out_file, protocol=pickle.HIGHEST_PROTOCOL)