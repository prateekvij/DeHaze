#!/usr/bin/env python
"""
The code represents the course scale network for Multi-Scale Convolutional 
Neural Networks used for haze removal. The code is based on keras library
with theano backend

Link to the paper
https://arxiv.org/pdf/1601.07661.pdf

keras format: 'channel_last'
input format must be (batch, height, width, channels)

"""
import numpy as np
import pickle
import keras
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model

__author__ = "Prateek Vij"
__copyright__ = "Copyright 2017, Indian Institute of Technology Guwahati"
__credits__ = ["Prateek Vij"]
__license__ = "GPL"
__version__ = "1.0.1"

height = 480
width = 640

x_train = pickle.load(open("../../metadata/hazy_data_1_500.pkl"))
print "Training data x loaded"

y_train = pickle.load(open("../../metadata/t_maps_1_500.pkl"))
print "Training label images loaded"

image_input = Input(shape=(height, width, 3,))

conv_1_out = Conv2D(5, 11, activation='relu', name='conv_1', 
					padding='same')(image_input)
pool_1_out = MaxPooling2D(name='pool_1')(conv_1_out)
upsample_1_out = UpSampling2D(name='upsample_1')(pool_1_out)

conv_2_out = Conv2D(5, 9, activation='relu', name='conv_2',
					padding='same')(upsample_1_out)
pool_2_out = MaxPooling2D(name='pool_2')(conv_2_out)
upsample_2_out = UpSampling2D(name='upsample_2')(pool_2_out)

conv_3_out = Conv2D(10, 7, activation='relu', name='conv_3',
					padding='same')(upsample_2_out)
pool_3_out = MaxPooling2D(name='pool_3')(conv_3_out)
upsample_3_out = UpSampling2D(name='upsample_3')(pool_3_out)

linear_out = Conv2D(1, 1, activation='sigmoid', name='linear', 
					padding='same')(upsample_3_out)

model = Model(image_input, linear_out)
model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()