# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 01:31:10 2024

@author: matth
"""

from GeneticAlgorithm_V2 import genetic_algorithm
from GeneticAlgorithm_V2 import pickle_jar
import Computer_Input_Tetris_V3 as computer
from NeuralNet import create
from Initialize_Board import initialize_board
import matplotlib.pyplot as plt
import pickle
import numpy as np

name = '1000Gen'
with open(name +'.pkl', 'rb') as f:
    loaded_object = pickle.load(f)

    fitness_history = []
for i in range(len(loaded_object)):
    fitness_history.append(loaded_object[i][1])

index = np.argmax(fitness_history)
best_DNA = loaded_object[index][0]
seed = loaded_object[index][2]

gameboard, env, seed = initialize_board(True, int(seed))
computer.TETRIS_V2(create(best_DNA), gameboard, env, loud = True)

print('fitness')
print(loaded_object[index][1])