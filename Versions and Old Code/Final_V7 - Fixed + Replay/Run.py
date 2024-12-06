# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:44:16 2024

@author: cekna
"""
from GeneticAlgorithm_V2 import genetic_algorithm
from GeneticAlgorithm_V2 import pickle_jar
import matplotlib.pyplot as plt
import pickle

name = input('Input descriptive file name: ')

# Parameters
population_size = 16
generations = 50
mutation_rate_0 = 0.14
mutation_rate_14 = 0.01
low_bound = -10#0.06
up_bound = 10#0.06
low_N = 4
up_N = 100

# Run the algorithm
best_brain, best_fitness, genchamps = genetic_algorithm(population_size, generations, mutation_rate_0, mutation_rate_14, low_bound, up_bound, low_N, up_N)
fitness_hist = []
for i in range(len(genchamps)):
    fitness_hist.append(genchamps[i][1])
plt.plot(fitness_hist)
plt.title(name+': Fitness of Best Player')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.savefig(name+'.jpeg', format='jpeg', dpi=300)
plt.show()

# Save file
with open(name+'.pkl', 'wb') as f:
    pickle.dump(genchamps, f)

#print(f"\nBest brain: {best_brain}, Fitness: {best_fitness}")


