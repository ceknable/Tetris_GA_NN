# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 23:07:12 2024

@author: cekna
"""
import numpy as np
from Rand_CRs import Rand_CRs
from sigmoid import sigmoid

gameboard = np.zeros(200)
DNA = Rand_CRs()

def NN (gameboard, DNA):
    ''' This function takes the raw DNA as the input. Unravels it into
    chromosomes. Then based on Chromosome 0 cuts and arranges Theta weight
    matrices to fit the shape of the new neural network.'''
    
    # Unravel DNA
    for i in range(len(DNA)):
        globals()['CR'+str(i)] = DNA[i]
        
    # Initialize weight matrices
    Theta1 = 0
    Theta2 = 0
    Theta3 = 0
    Theta4 = 0
    
    # Create weight Matrices    
    
    
    # Create Theta1 Matrix
    
    Row1 = int(CR0[1])              # Measure row dimensions based on number of neurons in first layer
    Theta1 = CR1[0:Row1,:]          # Cut CR1 (raw matrix) to fit size
    
    
    # Create Theta2 Matrix if layer 2 or 3 active
    
    if CR0[2] == 1:                 # if layer 2 is active
        Row2 = int(CR0[3])              # number of neurons in layer 2
        Col2 = Row1+1                   # number of neurons in layer 1 + bias
        Theta2 = CR2[0:Row2,0:Col2]     # Cut CR2 (raw matrix) to fit size
    elif CR0[4] == 1:               # if layer 3 is active and layer 2 is not 
        Row2 = int(CR0[5])              # number of neurons in layer 3
        Col2 = Row1+1                   # number of neurons in layer 1 + bias
        Theta2 = CR3[0:Row2,0:Col2]     # Cut CR3 (raw matrix) to fit size
    
    
    # Create Theta3 Matrix if layer 2 and 3 active
    
    if CR0[4] == 1 and CR0[2] == 1: # if layers 2 and 3 are active
        Row3 = int(CR0[5])              # number of neurons in layer 3
        Col3 = Row2+1                   # number of neurons in layer 2 + bias
        Theta3 = CR3[0:Row3,0:Col3]     # Cut CR3 (raw matrix) to fit size
    
    
    # Create Output Matrix (Theta 2 or 3 or 4) from CR4
    
    if type(Theta3) != int and type(Theta2) != int and type(Theta1) != int: # if all 3 layers are active
         Col4 = Row3+1                                                          # number of neurons in layer 3 + bias
         Theta4 = CR4[:,0:Col4]                                                 # Cut CR4 to size
    elif type(Theta2) != int and type(Theta1) != int:                       # if 2 layers are active
         Col4 = Row2+1                                                          # number of neurons in layer 2 or 3 + bias
         Theta3 = CR4[:,0:Col4]                                                 # Cut CR4 to size
    elif type(Theta1) != int:                                               # if only 1 layer active
         Col4 = Row1+1                                                          # number of neurons in layer 1 + bias
         Theta2 = CR4[:,0:Col4]                                                 # Cut CR4 to size
    
    
    # Print CR0 and sizes of weight matrices
    
    print(CR0)
    if type(Theta1) != int:
        print('Theta 1:',Theta1.shape)
    if type(Theta2) != int:    
        print('Theta 2:',Theta2.shape)
    if type(Theta3) != int:
        print('Theta 3:',Theta3.shape)
    if type(Theta4) != int:
        print('Theta 4:',Theta4.shape)
    
    # Return all Thetas. Thetas that are not active are integer zeros.
    return(Theta1,Theta2,Theta3,Theta4)

N = NN(gameboard, DNA)    