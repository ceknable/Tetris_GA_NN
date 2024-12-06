"""
Created on Tue Dec 03 15:15 2024

@author: KingRamenXIV
"""
import numpy as np
import random 
def Rand_CRs(low_bound = -10, up_bound = 10):
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
    CR1 = np.zeros([100,201])
    CR2 = np.zeros([100,101])
    CR3 = CR2
    CR4 = np.zeros([6,101])
    
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
            CR0[i] = random.randint(20,100) # 20 - 100 neurons
            #CR0[i] = random.randint(4,30) 4 - 30 nuerons
        else:
            CR0[i] = random.randint(0, 1)
    DNA = [CR0,CR1,CR2,CR3,CR4]
    return(DNA)


