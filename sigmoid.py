# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:48:48 2024

@author: cekna
"""
import numpy as np

def sigmoid(z):
    '''Function that takes an input z and returns the sigmoid transformation.
    If z is a vector or a matrix, it should perform the sigmoid transformation on every element.
    Input:
    z [=] scalar or array
    Return:
    g [=] scalar or array
    '''

    # Calculate sigmoid transform of z
    g = 1/(1+np.exp(-z))

    return g
