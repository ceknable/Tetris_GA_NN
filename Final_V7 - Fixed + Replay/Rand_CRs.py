# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 23:14:49 2024

@author: cekna
"""
import numpy as np
import random 
def Rand_CRs(low_bound = -10, up_bound = 10, low_N = 4, up_N = 30):
    ''' 
    This code generates 4 chromosomes for the initialization of a Neural Network
    Chromosome (CR) format
    CR0 = [0 or 1, number of neurons, 0 or 1, number of neurons, 0 or 1, number of neurons]
    CR1-4 = [ThetaMatrix]
    '''
    wmax = up_bound # weight max (Default 0.1)
    wmin = low_bound # weight min (Default 0.01)
    
    
    # Initialize Vectors
    CR0 = np.zeros(6)
    CR1 = np.zeros([up_N,201])
    CR2 = np.zeros([up_N,up_N+1])
    CR3 = CR2
    CR4 = np.zeros([4,up_N+1])
    
    # Loop through each chromosome and generate random vector of specified length
    for i in range(len(CR1)):
        for j in range(len(CR1[0])):
            CR1[i][j] = random.uniform(wmin,wmax)
    
    for i in range(len(CR2)):
        for j in range(len(CR2)+1):
            CR2[i][j] = random.uniform(wmin,wmax)
            CR3[i][j] = random.uniform(wmin,wmax)
    
    for i in range(len(CR4)):
        for j in range(len(CR4[0])):
            CR4[i][j] = random.uniform(wmin,wmax)
    
    
    # Loop through CR1 to get layer properties
    for i in range(len(CR0)):
        if i == 0:
            CR0[i] = 1
        elif i%2:
            CR0[i] = random.randint(low_N,up_N)
        else:
            CR0[i] = random.randint(0, 1)
    #CR0 = [1,20,1,15,1,15]
    DNA = [CR0,CR1,CR2,CR3,CR4]
    return(DNA)


