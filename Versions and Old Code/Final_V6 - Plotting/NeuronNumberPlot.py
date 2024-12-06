# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:54:29 2024

@author: cekna
"""
import pickle
import numpy as np
import matplotlib.pyplot as plt

name = 'ConstStructTest' 
with open(name+'.pkl', 'rb') as f:
    genchamps = pickle.load(f)
layer1 = []
layer2 = []
layer3 = []
for k in range(len(genchamps)):
    layer1.append(genchamps[k][0][0][1])
    layer2.append(genchamps[k][0][0][3])
    layer3.append(genchamps[k][0][0][5])
data1 = layer1#moving_average(layer1,500)
data2 = layer2#moving_average(layer2,500)
data3 = layer3#moving_average(layer3,500)


plt.plot(data1, label = 'Layer1')
plt.plot(data2, label = 'Layer2')
plt.plot(data3, label = 'Layer3')


name = name+': Number of Neurons'
plt.title(name)
plt.legend()
plt.xlabel('Generations (Moving Average)')
plt.ylabel('Number of Neurons')

plt.show()