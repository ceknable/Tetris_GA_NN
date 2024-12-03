# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:44:16 2024

@author: cekna
"""
from GeneticAlgorithm_V2 import genetic_algorithm
from GeneticAlgorithm_V2 import pickle_jar
import matplotlib.pyplot as plt
import pickle
import numpy as np

varnames = ['Population', 'mutation_rate_0','mutation_rate_14','bounds_mag', 'bounds_sign']
varrange = [[5,120],[0,0.25],[0,0.4],[-2,2],[-2,2]]

for i in range(len(varnames)):
    
    if i == 3 or i == 4:
        span = np.logspace(varrange[i][0],varrange[i][1], 10)
    else:
        span = np.linspace(varrange[i][0],varrange[i][1], 10)
    
    name = varnames[i]
    
    for j in range(len(span)):

        # Parameters
        population_size = 16
        if i == 0:
            generations = 500
        else:
            generations = 1000
        mutation_rate_0 = 0.05
        mutation_rate_14 = 0.1
        low_bound = -10
        up_bound = 10
        
        if i == 0:
            population_size = int(span[j])
        elif i == 1:
            mutation_rate_0 = span[j]
        elif i == 2:
            mutation_rate14 = span[j]
        elif i == 3:
            low_bound = -span[j]
            up_bound = span[j]
        elif i == 4:
            low_bound = 0.01
            up_bound = span[j]
        
        # Run the algorithm
        best_brain, best_fitness, genchamps = genetic_algorithm(population_size, generations, mutation_rate_0, mutation_rate_14, low_bound, up_bound)
        fitness_hist = []
        for i in range(len(genchamps)):
            fitness_hist.append(genchamps[i][1])
        numj = np.round(span[j],2)
        labelj = 'Var = '+str(numj)
        plt.plot(fitness_hist, label = labelj )
        plt.title(name+': Fitness of Best Player')
        plt.legend()
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        
        # Save file
        with open('!'+name+str(j)+'.pkl', 'wb') as f:
            pickle.dump(genchamps, f)
    plt.show()
    plt.savefig(name+'.jpeg', format='jpeg', dpi=300)
#print(f"\nBest brain: {best_brain}, Fitness: {best_fitness}")


