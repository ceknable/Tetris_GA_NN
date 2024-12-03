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
generations = 10
mutation_rate_0 = 0.05
mutation_rate_14 = 0.1

# Run the algorithm
best_brain, best_fitness, genchamps = genetic_algorithm(population_size, generations, mutation_rate_0, mutation_rate_14)
fitness_hist = []
for i in range(len(genchamps)):
    fitness_hist.append(genchamps[i][1])
plt.plot(fitness_hist)
plt.title(name+': Fitness of Best Player')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.savefig(name+'.jpeg', format='jpeg', dpi=300)
plt.show()


# Save Results
class MyClass:
    def __init__(self, value):
        self.value = value

# Create an instance of MyClass
my_object = MyClass(genchamps)

# Save the object to a file
with open(name+'.pkl', 'wb') as f:
    pickle.dump(my_object, f)
    

#print(f"\nBest brain: {best_brain}, Fitness: {best_fitness}")


