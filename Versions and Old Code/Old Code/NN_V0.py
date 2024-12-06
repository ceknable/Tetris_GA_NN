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
        #globals()['Theta'+str(i)] = 0
    
    Theta1 = 0
    Theta2 = 0
    Theta3 = 0
    Theta4 = 0
    
    print(CR0)
    
    # Create Theta1 Matrix
    print(len(CR1),len(CR1[0]))
    Col1 = int(CR0[1])
    #print(CR1)
    Theta1 = CR1[:][0:31]
    #print('break')
    #print(Theta1)
    # Create Theta2 Matrix
    if CR0[2] == 1:
        Row2 = int(CR0[3])
        Col2 = Row1
        Theta2 = CR2[0:Row2][0:Col2]
    elif CR0[4] == 1:
        Row2 = int(CR0[5])
        Col2 = Row1
        Theta2 = CR3[0:Row2][0:Col2]
    #print('break:',Theta1)
    
    return(Theta1,Theta2)#CR0,Theta2,Theta1)

print('FINAL:',NN(gameboard, DNA)[0])
#print('FINAL 2:', NN(gameboard, DNA)[1])    