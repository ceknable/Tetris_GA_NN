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
    Row1 = int(CR0[1]) # Measure row dimensions based on number of neurons in first layer
    Theta1 = CR1[0:Row1,:] # Cut CR1 (raw matrix) to fit size
    
    # Create Theta2 Matrix if layer 2 or 3 active
    if CR0[2] == 1:
        Row2 = int(CR0[3])
        Col2 = Row1+1
        Theta2 = CR2[0:Row2,0:Col2]
    elif CR0[4] == 1:
        Row2 = int(CR0[5])
        Col2 = Row1+1
        Theta2 = CR3[0:Row2,0:Col2]
    
    # Create Theta3 Matrix if layer 2 and 3 active
    if CR0[4] == 1 and CR0[2] == 1:
        Row3 = int(CR0[5])
        Col3 = Row2+1
        Theta3 = CR3[0:Row3,0:Col3]
    
    # Create Output Matrix (Theta 2 or 3 or 4) from CR4
    if type(Theta3) != int and type(Theta2) != int and type(Theta1) != int:
         Col4 = Row3+1
         Theta4 = CR4[:,0:Col4]
    elif type(Theta2) != int and type(Theta1) != int:
         Col4 = Row2+1
         Theta3 = CR4[:,0:Col4]
    elif type(Theta1) != int:
         Col4 = Row1+1
         Theta2 = CR4[:,0:Col4]
    
    
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
    
    return(Theta1,Theta2,Theta3,Theta4)

N = NN(gameboard, DNA)    