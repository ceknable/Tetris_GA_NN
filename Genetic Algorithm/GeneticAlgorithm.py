"""
Created on Mon Nov 30 15:38 2024

@author: KingRamenXIV. 
Forked from cknable and ChatGPT "Ex_GA_GPT_V0.py" with adjustments
"""
# Import packages
from Featurization import featurization
from Interface import Computer_Input_Tetris_V3 as computer
from Neural_Network import NeuralNet as 
from Neural_Newtork import Rand_CRs
from Initialize_Board import initialize_board

import random
import numpy as np

def GA(): 
  '''
  The GA code that creates a brain, simulates the Tetris game, gathers gameboard features, assesses brain fitness, breeds 
  the best brains and then continues until opimized. 

  Inputs: 


  Returns: 


  Other: 
  '''

# Function to simulate the game for a single brain and calculate fitness
def simulate_brain(chromosome):
    # Create the brain from the chromosome
    brain = NeuralNet.create(chromosome)
    
    # Initialize the game
    gameboard, env = initialize_board()
    
    # Play the game
    gameboard, height_hist, holes_hist = computer.TETRIS_V2(brain, gameboard)
    
    # Fitness Test
    avg_height = np.average(height_hist[-1, :])  # Final average column height
    holes = holes_hist[-1]  # Final number of holes
    
    # Fitness criterion: lower is better
    fitness = avg_height + holes
    
    return fitness

## 3. Compare Brains
# Sort brains by fitness (ascending order: lowest fitness first)
brains.sort(key=lambda x: x[1])

# Select the two parent brains with the lowest fitness criteria
best_brains = brains[:2]
# Extract the DNAs of the two brains
best_dnas = [dna for dna, fitness in best_brains]

# Print or use the best brains as needed
if LOUD = True
  print("Two best brains:")
  for idx, (dna, fitness) in enumerate(best_brains, start=1):
      print(f"Brain {idx}: Fitness = {fitness}")

# Crossover the DNAs (single-point)
def crossover(parent1, parent2):
    alpha = random.uniform(0, 1)
    return alpha * parent1 + (1 - alpha) * parent2


# Mutation in DNA (small random change) 
def mutate(individual, mutation_rate, lower_bound, upper_bound):
    if random.random() < mutation_rate:
        individual += random.uniform(-1, 1)
        # Ensure mutation stays within bounds
        individual = max(min(individual, upper_bound), lower_bound)
    return individual

# Genetic Algorithm
def genetic_algorithm(fitness_function, lower_bound, upper_bound, population_size, generations, mutation_rate):
    ## 1. Decision making criteria
    # No decision making criteria in this case. The brain does not "think" about it's action it just acts. 
  
    ## 2. Simulating the game
    # Generate an initial population of brains
    num_brains = population_size
    brains = []  # List to store chromosomes and fitness criteria

    for _ in range(num_brains):
      rand_DNA = Rand_CRs()  # Generate random chromosomes
      fitness = simulate_brain(rand_DNA)  # Simulate the game and calculate fitness
      brains.append((rand_DNA, fitness))  # Store chromosome and fitness as a tuple
  
    for generation in range(generations):
        # Evaluate fitness
        fitnesses = [fitness_function(ind) for ind in population]

        # Create the next generation
        new_population = []
        for _ in range(population_size // 2):  # Half-size as we generate 2 children per pair
            # Select parents
            parent1, parent2 = select_parents(population, fitnesses)
            # Crossover
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            # Mutate
            child1 = mutate(child1, mutation_rate, lower_bound, upper_bound)
            child2 = mutate(child2, mutation_rate, lower_bound, upper_bound)
            # Add to the new population
            new_population.extend([child1, child2])

        population = new_population

        # Output the best individual of the generation
        best_individual = max(population, key=fitness_function)
        print(f"Generation {generation+1}: Best Individual = {best_individual}, Fitness = {fitness_function(best_individual)}")

    # Return the best solution
    return max(population, key=fitness_function)

# Parameters
lower_bound = -10
upper_bound = 10
population_size = 20
generations = 30
mutation_rate = 0.1

# Run the algorithm
best_solution = genetic_algorithm(fitness_function, lower_bound, upper_bound, population_size, generations, mutation_rate)
print(f"\nBest solution: {best_solution}, Fitness: {fitness_function(best_solution)}")
