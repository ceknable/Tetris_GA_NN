# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:44:16 2024

@author: cekna
"""
from GeneticAlgorithm_V2 import genetic_algorithm
import matplotlib.pyplot as plt

# Parameters
population_size = 2
generations = 5
mutation_rate_0 = 0.05
mutation_rate_14 = 0.1

# Run the algorithm
best_brain, best_fitness, genchamps = genetic_algorithm(population_size, generations, mutation_rate_0, mutation_rate_14)
fitness_hist = []
for i in range(len(genchamps)):
    fitness_hist.append(genchamps[i][1])
plt.plot(fitness_hist)
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()
#print(f"\nBest brain: {best_brain}, Fitness: {best_fitness}")
#print(genchamps)