"""
Created on Mon Nov 30 15:38 2024

@author: KingRamenXIV
Forked from cknable and ChatGPT "Ex_GA_GPT_V0.py" with adjustments.
"""
# Import packages
import random
import numpy as np
from Featurization import featurization
from Interface import Computer_Input_Tetris_V3 as computer
from Neural_Network import NeuralNet
from Neural_Network import Rand_CRs
from Initialize_Board import initialize_board


# Function to create the initial population of brains
def create_initial_population(population_size):
    """Generate an initial population of random chromosomes."""
    return [Rand_CRs() for _ in range(population_size)]


# Function to simulate the game for a single brain and calculate fitness
def simulate_brain(chromosome):
    """Simulate Tetris for a given chromosome and return its fitness."""
    brain = NeuralNet.create(chromosome)
    gameboard, env = initialize_board()
    gameboard, height_hist, holes_hist, total_score = computer.TETRIS_V2(brain, gameboard, env)

    # Fitness Test
    #avg_height = np.average(height_hist[-1, :])  # Final average column height
    holes = holes_hist[-1]  # Final number of holes
    fitness = total_score - holes  # Higher fitness is better
    return fitness


def select_parents(population, fitnesses, k=4):
    """Select two distinct parents using tournament selection."""
    # Create a zipped population for easy handling, pair chromosomes and their fitness
    pop_with_fitness = list(zip(population, fitnesses))
    
    # Create a tournament with k random individuals from the available population
    candidates = random.sample(pop_with_fitness, k)
    
    # Sort the candidates by fitness in descending order (higher fitness is better)
    candidates.sort(key=lambda x: x[1], reverse=True)
    print(candidates)
    
    # Select the two best parents
    parent1 = candidates[0][0]  # Chromosome of the highest fitness
    parent2 = candidates[1][0]  # Chromosome of the second highest fitness
    
    return parent1, parent2

# Function to perform crossover between two parents
import numpy as np
def crossover(parent1, parent2):
    child1 = []
    child2 = []
    for i in range(len(parent1)):
        n = random.randint(0, len(parent1[i]))
        print(n,i)
        child1.append(np.concatenate((parent1[i][0:n], parent2[i][n:])))
        child2.append(np.concatenate((parent2[i][0:n], parent1[i][n:])))
    return(child1, child2)

# Function to mutate chromosomes 1-4
def mutate14(chromosome, mutation_rate, lower_bound = .01, upper_bound = .1):
    """Apply mutation to a chromosome."""
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] += random.uniform(-.02, .02)
            chromosome[i] = max(min(chromosome[i], upper_bound), lower_bound)  # Keep within bounds
    return chromosome

# Function to mutate chromosome 0
def mutate0(chromosome, mutation_rate, lower_bound = 4, upper_bound= 30):
    """Apply mutation to a chromosome. Lower bound should be 4 and upper bound should be 30"""
    for i in range(1, len(chromosome)):
        if random.random() < mutation_rate:
            if (i%2 == 0):
                if chromosome[i] ==1:
                    chromosome[i] = 0
                else:
                    chromosome[i] =1
            else:
                chromosome[i] += random.randint(1, 10)
                chromosome[i] = max(min(chromosome[i], upper_bound), lower_bound)  # Keep within bounds
    return chromosome

def mutate(child, zerorate, onefourrate):
    child[0] = mutate0(child[0], zerorate)
    for i in range(1, 5):
        child[i] = mutate14(child[i], onefourrate)
    return chromosome

# Genetic Algorithm
def genetic_algorithm(population_size, generations, mutation_rate_0, mutation_rate_14):
    """Run the genetic algorithm."""
    # Step 1: Create initial population
    population = create_initial_population(population_size)
    genchamps = [] # list which will hold the best brain of each genertion and the corresponding fitness- index using [gen][0 for brain, 1 for fitness]
    
    for generation in range(generations):
        # Step 2: Simulate each brain and calculate fitness
        fitnesses = [simulate_brain(chromosome) for chromosome in population]

        # Step 3: Select the next generation
        new_population = []
        for _ in range(population_size // 2):  # Half-size as 2 children are generated per pair
            # Select parents
            parent1, parent2 = select_parents(population, fitnesses)
            # Crossover
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            # Mutate
            child1 = mutate(child1, mutation_rate_0, mutation_rate_14)
            child2 = mutate(child2, mutation_rate_0, mutation_rate_14)
            # Add children to the new population
            new_population.extend([child1, child2])

        # Update population
        population = new_population

        # Step 4: Output the best individual of the generation
        best_idx = np.argmin(fitnesses)
        best_individual = population[best_idx]
        best_fitness = fitnesses[best_idx]
        genchamps.append([bestindivudal, best_fitness])
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

    # Return the best individual and its fitness
    best_idx = np.argmin(fitnesses)
    return population[best_idx], fitnesses[best_idx], genchamps


# Parameters
population_size = 10
generations = 30
mutation_rate_0 = 0.05
mutation_rate_14 = 0.1

# Run the algorithm
best_brain, best_fitness, genchamps = genetic_algorithm(population_size, generations, mutation_rate_0, mutation_rate_14)
print(f"\nBest brain: {best_brain}, Fitness: {best_fitness}")
