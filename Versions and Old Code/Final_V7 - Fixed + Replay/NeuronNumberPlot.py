# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:54:29 2024

@author: cekna
"""
import pickle
import numpy as np
import matplotlib.pyplot as plt

def moving_average(data, window_size):
    """
    Calculate the moving average of a given list of numbers.
    
    Parameters:
    - data: list or numpy array of numbers
    - window_size: the size of the moving window
    
    Returns:
    - A list of moving averages.
    """
    if window_size <= 0:
        raise ValueError("Window size must be greater than 0")
    if window_size > len(data):
        raise ValueError("Window size must be smaller or equal to the length of data")
    
    # Using numpy to compute the moving average
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

name = 'test9' 
with open(name+'.pkl', 'rb') as f:
    genchamps = pickle.load(f)
layer1 = []
layer2 = []
layer3 = []
data = []
for k in range(len(genchamps)):
    layer1.append(genchamps[k][0][0][1])
    layer2.append(genchamps[k][0][0][3])
    layer3.append(genchamps[k][0][0][5])
    data.append(genchamps[k][1])
data1 = layer1#moving_average(layer1,500)
data2 = layer2#moving_average(layer2,500)
data3 = layer3#moving_average(layer3,500)
#datadata = moving_average(data,2500)

plt.plot(data1, label = 'Layer1')
plt.plot(data2, label = 'Layer2')
plt.plot(data3, label = 'Layer3')
#plt.plot(datadata)

name = name+': Fitness'
plt.title(name)
plt.legend()
plt.xlabel('Generations (Moving Average)')
plt.ylabel('Fitness')

plt.show()