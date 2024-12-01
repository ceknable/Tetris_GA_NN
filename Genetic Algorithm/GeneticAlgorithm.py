"""
Created on Mon Nov 30 15:38 2024

@author: KingRamenXIV. 
Forked from cknable and ChatGPT "Ex_GA_GPT_V0.py" with adjustments
"""
# Import packages
from Featurization import featurization
from Interface import Computer_Input_Tetris_V3 as computer
from Neural Network

import random

def GA(): 
  '''
  The GA code that creates a brain, simulates the Tetris game, gathers gameboard features, assesses brain fitness, breeds 
  the best brains and then continues until opimized. 

  Inputs: 


  Returns: 


  Other: 
  '''

## 1. Simulating the game
# Generate random chromosomes to make the brains
rand_DNA = Rand_CRs


# Function to maximize
def fitness_function(score):
    return score**2

# Generate an initial population
def generate_population(size, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(size)]

# Select parents based on fitness (roulette wheel selection)
def select_parents(population, fitnesses):
    total_fitness = sum(fitnesses)
    selection_probs = [f / total_fitness for f in fitnesses]
    return random.choices(population, weights=selection_probs, k=2)

# Crossover (single-point)
def crossover(parent1, parent2):
    alpha = random.uniform(0, 1)
    return alpha * parent1 + (1 - alpha) * parent2

# Mutation (small random change)
def mutate(individual, mutation_rate, lower_bound, upper_bound):
    if random.random() < mutation_rate:
        individual += random.uniform(-1, 1)
        # Ensure mutation stays within bounds
        individual = max(min(individual, upper_bound), lower_bound)
    return individual

# Genetic Algorithm
def genetic_algorithm(fitness_function, lower_bound, upper_bound, population_size, generations, mutation_rate):
    # Initialize population
    population = generate_population(population_size, lower_bound, upper_bound)

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
