# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 23:14:49 2024

@author: cekna
"""
import numpy as np
import random 
'''
thirty_z = [0]*30
CR1 = [0]*32
CR1[0] = random.randint(0, 1)
CR1[1] = random.randint(4, 30)
for i in range(len(CR1)-2):
    CR1[i+2] = thirty_z
for i in range(len(CR1)-2):
    for j in range(len(thirty_z)):
        CR1[i][j] = random.uniform(0.01,0.1)
print(CR1[3][4])
'''
#CR1 = [0 or 1, number of neurons, 0 or 1, number of neurons, 0 or 1, number of neurons]
CR1 = np.zeros(6)
CR2 = np.zeros([30,30])
CR3 = CR2
CR4 = CR2
for i in range(len(CR2)):
    for j in range(len(CR2)):
        CR2[i][j] = random.uniform(0.01,0.1)
        CR3[i][j] = random.uniform(0.01,0.1)
        CR4[i][j] = random.uniform(0.01,0.1)
print(CR2)