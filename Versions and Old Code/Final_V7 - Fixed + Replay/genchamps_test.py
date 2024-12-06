# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:42:59 2024

@author: cekna
"""
import pickle

name = '1000Gen' 
with open(name+'.pkl', 'rb') as f:
    genchamps = pickle.load(f)
seeds = []
fitness = []
for k in range(len(genchamps)):
    seeds.append(genchamps[k][2])    
    fitness.append(genchamps[k][1])
    print(genchamps[k][1],genchamps[k][2])
#print(genchamps[0][2])
#print(seeds)
#print(fitness)