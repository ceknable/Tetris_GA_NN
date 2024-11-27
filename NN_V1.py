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
        globals()['Theta'+str(i)] = 0
    
    print(CR0)
    
    # Create Theta1 Matrix
    
    #print(len(CR1),len(CR1[0]))
    Row1 = int(CR0[1])
    Theta1 = CR1[0:Row1,:]
    #print(len(Theta1),len(Theta1[0]))
    
    
    # Create Theta2 Matrix
    
    if CR0[2] == 1:
        Row2 = int(CR0[3])
        Col2 = Row1
        Theta2 = CR2[0:Row,0:Col2]
    elif CR0[4] == 1:
        Row2 = int(CR0[5])
        Col2 = Row1
        Theta2 = CR3[0:Row2,0:Col2]
    
    # Create Theta3 Matrix
    
    if CR[4] == 1 and CR[2] == 1:
        Row3 = int(CR0[5])
        Col3 = Row2
        Theta3 = CR3[0:Row3,0:Col3]
    
    # Create Theta4 Matrix
    
     if Theta3 != 0:
         Col4 = Row3
         Theta4 = [:,0:Col4]
     elif Theta2 != 0:
         Col4 = Row2
         Theta4 = [:,0:Col4]
    
    return(Theta1,Theta2)#CR0,Theta2,Theta1)

print('FINAL:',NN(gameboard, DNA)[0])
print('FINAL 2:', NN(gameboard, DNA)[1])    