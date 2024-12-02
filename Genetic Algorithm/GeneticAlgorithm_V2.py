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


# Function to select parents using tournament selection
def select_parents(population, fitnesses, k=4):
    """Select two distinct parents using tournament selection."""
    def tournament_selection(available_population):
        # Create a tournament with k random individuals from the available population
        candidates = random.sample(available_population, k)
        # Sort the candidates by fitness in ascending order
        candidates = candidates.sort(key = lambda x: x[1])
        
        return min(candidates, key=lambda x: x[1])[0]  # Return only the chromosome

    # Create a zipped population for easy handling
    pop_with_fitness = list(zip(population, fitnesses))

    # Select the first parent
    parent1 = tournament_selection(pop_with_fitness)
    # Remove parent1 from the population
    pop_with_fitness = [pair for pair in pop_with_fitness if pair[0] != parent1]

    # Select the second parent from the remaining individuals
    parent2 = tournament_selection(pop_with_fitness)

    return parent1, parent2


# Function to perform crossover between two parents
import numpy as np

def crossover(parent1, parent2):
    """
    Perform crossover between two parents using NumPy for efficient matrix operations,
    ensuring the child maintains the specified format.
    
    Inputs:
    - parent1: 3D matrix with 5 elements as described.
    - parent2: 3D matrix with 5 elements as described.

    Output:
    - child: 3D matrix with the same structure and valid values as the parents.
    """
    child = []

    # CR0: A list with specific value ranges and binary elements
    CR0 = []
    for i in range(len(parent1[0])):
        if i in {2, 4}:  # Binary values (0 or 1)
            CR0.append(random.choice([parent1[0][i], parent2[0][i]]))  # Randomly pick from parents
        else:  # Values in a range (e.g., 4-30)
            alpha = random.uniform(0, 1)
            CR0.append(alpha * parent1[0][i] + (1 - alpha) * parent2[0][i])  # Weighted average
    child.append(CR0)

    # CR1, CR2, CR3, and CR4: Use matrix operations for efficient crossover
    for i, (p1, p2) in enumerate([parent1[1], parent1[2], parent[3], parent1[4]]):
        alpha = np.random.uniform(0, 1, len(p1))  # Vector of random alpha values
        child_segment = alpha * np.array(p1) + (1 - alpha) * np.array(p2)
        child_segment = np.clip(child_segment, 0.01, 0.1)  # Ensure values stay within bounds
        child.append(child_segment.tolist())

    return child



# Function to mutate chromosomes 1-4
def mutate14(chromosome, mutation_rate, lower_bound, upper_bound):
    """Apply mutation to a chromosome."""
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] += random.uniform(-.02, .02)
            chromosome[i] = max(min(chromosome[i], upper_bound), lower_bound)  # Keep within bounds
    return chromosome

# Function to mutate chromosome 0
def mutate0(chromosome, mutation_rate, lower_bound, upper_bound):
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

# Genetic Algorithm
def genetic_algorithm(population_size, generations, mutation_rate, lower_bound, upper_bound):
    """Run the genetic algorithm."""
    # Step 1: Create initial population
    population = create_initial_population(population_size)

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
            child1 = mutate(child1, mutation_rate, lower_bound, upper_bound)
            child2 = mutate(child2, mutation_rate, lower_bound, upper_bound)
            # Add children to the new population
            new_population.extend([child1, child2])

        # Update population
        population = new_population

        # Step 4: Output the best individual of the generation
        best_idx = np.argmin(fitnesses)
        best_individual = population[best_idx]
        best_fitness = fitnesses[best_idx]
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

    # Return the best individual and its fitness
    best_idx = np.argmin(fitnesses)
    return population[best_idx], fitnesses[best_idx]


# Parameters
lower_bound = -10
upper_bound = 10
population_size = 20
generations = 30
mutation_rate = 0.1

# Run the algorithm
best_brain, best_fitness = genetic_algorithm(population_size, generations, mutation_rate, lower_bound, upper_bound)
print(f"\nBest brain: {best_brain}, Fitness: {best_fitness}")
