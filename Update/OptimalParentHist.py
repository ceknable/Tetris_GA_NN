# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:18:33 2024

@author: cekna
"""

import os
import pickle
import numpy as np
import GeneticAlgorithm as GA

# Get a list of all files in the current directory
files_in_directory = os.listdir('Creating_Master_Pickle')
n = 0
champchamp = []
# Loop through the files and process only the .pkl files
for filename in files_in_directory:
    genchamps = []
    if filename.endswith(".pkl"):  # Check if the file ends with .pkl
        file_path = os.path.join('Creating_Master_Pickle', filename)
        # Check if the file exists and has data
        file_size = os.path.getsize(file_path)
        if file_size > 0:
            with open(file_path, 'rb') as f:
                genchamps = pickle.load(f)
                print(f"Loaded data from {filename}")
            fitness = []
            for k in range(len(genchamps)):
                fitness.append(genchamps[k][1])
            # Find individual with best fitness
            index = np.argmax(fitness)#random.randint(0,len(fitness))
            DNA = genchamps[index][0]
            champchamp.append(genchamps[index]) #don't include 
            fit_plus_seeds = GA.simulate_brain(DNA)
            # Extract resutls into individual lists
            champchamp[n][1] = fit_plus_seeds[0]
            champchamp[n][2] = fit_plus_seeds[1]
            n = n+1
        else:
            print("The file is empty.")
            
# Save genchamps as pickle file
with open('MASTER.pkl', 'wb') as f:
    pickle.dump(champchamp, f)