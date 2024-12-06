# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 23:14:49 2024

@author: cekna
"""
import numpy as np
import random 
def Rand_CRs():
    ''' 
    This code generates 4 chromosomes for the initialization of a Neural Network
    Chromosome (CR) format
    CR1 = [0 or 1, number of neurons, 0 or 1, number of neurons, 0 or 1, number of neurons]
    CR2-4 = [ThetaMatrix]
    '''
    # Initialize Vectors
    CR1 = np.zeros(6)
    CR2 = np.zeros([30,30])
    CR3 = CR2
    CR4 = CR2
    
    # Loop through each chromosome and generate random vector of specified length
    for i in range(len(CR2)):
        for j in range(len(CR2)):
            CR2[i][j] = random.uniform(0.01,0.1)
            CR3[i][j] = random.uniform(0.01,0.1)
            CR4[i][j] = random.uniform(0.01,0.1)
    
    # Loop through CR1 to get layer properties
    for i in range(len(CR1)):
        if i == 0:
            CR1[i] = 1
        elif i%2:
            CR1[i] = random.randint(4,30)
        else:
            CR1[i] = random.randint(0, 1)
    
    return(CR2,CR3,CR4,CR1)