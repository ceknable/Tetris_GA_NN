# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:34:27 2024

@author: cekna
"""

import numpy as np
import random
import NeuralNet as NN
from Rand_CRs import Rand_CRs

# Create random gameboard
gameboard = np.zeros(200)
for i in range(len(gameboard)):
    gameboard[i] = random.randint(0, 1)
#print(gameboard)



# Create brain using DNA
DNA = Rand_CRs()
brain = NN.create(DNA, loud = False)

# Generate Output based on the random brain and gameboard
NN.player(gameboard, brain, loud = False)
    
    