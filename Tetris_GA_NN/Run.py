# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:44:16 2024

@author: cekna
"""
import GeneticAlgorithm as GA
import matplotlib.pyplot as plt
import pickle

'''This script runs the GA for given input parameters'''

# Create name for file containing genchamps (list of best individuals)
name = input('Input descriptive file name: ')

# Parameters
population_size = 4 # size of population (should be even)
generations = 5 # number of generations
mutation_rate_0 = 0.14 # mutation rate for chromosome 0
mutation_rate_14 = 0.2 #mutation rate for chromosomes 1-4
low_bound = -10 # lower bound of the weights in the NN
up_bound = 10 # upper bound of the weights in the NN
low_N = 4 # lower bound of the number of neurons in each layer of the NN
up_N = 100 # upper bound of the number of neurons in each layer of the NN

# Run the algorithm
best_brain, best_fitness, genchamps = GA.genetic_algorithm(population_size, generations, mutation_rate_0, mutation_rate_14, low_bound, up_bound, low_N, up_N)

# Plot Results
# Create fitness history from genchamps
fitness_hist = []
for i in range(len(genchamps)):
    fitness_hist.append(genchamps[i][1])
plt.plot(fitness_hist)
plt.title(name+': Fitness of Best Player')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.savefig(name+'.jpeg', format='jpeg', dpi=300)
plt.show()

# Save genchamps as pickle file
with open(name+'.pkl', 'wb') as f:
    pickle.dump(genchamps, f)

#print(f"\nBest brain: {best_brain}, Fitness: {best_fitness}")


