# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:25:40 2024

@author: cekna
"""
import pickle
# Load the object from the file
with open('test.pkl', 'rb') as f:
    genchamps = pickle.load(f)
print(genchamps)
