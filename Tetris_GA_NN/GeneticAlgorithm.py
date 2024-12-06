"""
Created on Mon Nov 30 15:38 2024

@author: KingRamenXIV
Forked from cknable and ChatGPT "Ex_GA_GPT_V0.py" with adjustments.
"""
# Import libraries
import random
import numpy as np
import pickle

# Import Files
import Tetris as T
import NeuralNet as NN

'''
Basic Function descriptions (for more info look at doc strings)
Functions:
    Rand_CRs:                   Makes random chromosomes
    create_intial_population:   creates the initial population
    simulate_brain:             simulates the game of Tetris using the Neural Network
    select_parents:             picks the best of the population
    crossover:                  crosses genetic material of two parents
    mutate14:                   mutates chromosomes 1-4
    mutate0:                    mutates chromosome 0
    mutate:                     mutates DNA
    genetic_algorithm:          runs the GA
'''

# Function to generate a random set of Chromosomes
def Rand_CRs(low_bound = -10, up_bound = 10, low_N = 4, up_N = 30):
    ''' 
    This code generates 4 chromosomes for the initialization of a Neural Network
    Chromosome (CR) format
    CR0 = [0 or 1, number of neurons, 0 or 1, number of neurons, 0 or 1, number of neurons]
    CR1-4 = [ThetaMatrix]
    
    Inputs:
        low_bound: the lower bounds of the value of the weights for the NN
        up_bound: the upper bounds of the value of the weights for the NN
        low_N: the lower bounds of the number of neurons for the NN
        up_N: the upper bounds of the number of neurons for the NN
    Outputs:
        DNA: a list containing all chromosomes CR0-CR4
    '''
    wmax = up_bound # weight max (Default 0.1)
    wmin = low_bound # weight min (Default 0.01)
    
    
    # Initialize Chromosomes (Vectors)
    CR0 = np.zeros(6)
    CR1 = np.zeros([up_N,201])
    CR2 = np.zeros([up_N,up_N+1])
    CR3 = CR2
    CR4 = np.zeros([4,up_N+1])
    
    # Loop through each chromosome and generate random vector of specified length
    for i in range(len(CR1)):
        for j in range(len(CR1[0])):
            CR1[i][j] = random.uniform(wmin,wmax)
    
    for i in range(len(CR2)):
        for j in range(len(CR2)+1):
            CR2[i][j] = random.uniform(wmin,wmax)
            CR3[i][j] = random.uniform(wmin,wmax)
    
    for i in range(len(CR4)):
        for j in range(len(CR4[0])):
            CR4[i][j] = random.uniform(wmin,wmax)
    
    
    # Loop through CR0 to generate random layer properties
    for i in range(len(CR0)):
        if i == 0:
            CR0[i] = 1
        elif i%2:
            CR0[i] = random.randint(low_N,up_N)
        else:
            CR0[i] = random.randint(0, 1)
    
    DNA = [CR0,CR1,CR2,CR3,CR4]
    return(DNA)

# Function to create the initial population of brains
def create_initial_population(population_size, low_bound, up_bound,low_N,up_N):
    """Generate an initial population of random chromosomes.
    
    Inputs:
        population_size: the size of the population
        low_bound: the lower bounds of the value of the weights for the NN
        up_bound: the upper bounds of the value of the weights for the NN
        low_N: the lower bounds of the number of neurons for the NN
        up_N: the upper bounds of the number of neurons for the NN
    Outputs:
        A list of all DNA for a given population size
        """
    return [Rand_CRs(low_bound,up_bound,low_N,up_N) for _ in range(population_size)]


# Function to simulate the game for a single brain and calculate fitness
def simulate_brain(DNA):
    """Simulate Tetris for a given individual and return its fitness.
    Inputs:
        DNA: List of Chromosomes containing NN data
    Outputs:
        fitness: a score of how well the individual did at playing Tetris
        i_seed: the game seed that that individual played on"""
    # Create the weight matrices (brain) from DNA
    brain = NN.create(DNA)
    
    # Initialize the board
    gameboard, env, i_seed = T.initialize_board()
    # Start the game
    gameboard, height_hist, holes_hist, total_score = T.tetris(brain, gameboard, env)

    # Fitness Test
    #avg_height = np.average(height_hist[-1, :])  # Final average column height
    holes = holes_hist  # Final number of holes
    fitness = total_score*5 - holes  # Higher fitness is better
    return fitness, i_seed

# Function to select the best parents from a population
def select_parents(population, fitnesses, k=4):
    """Select two distinct parents using tournament selection.
    
    Inputs:
        population: the list of all individuals in a tested population
        fitnesses: the corresponding list of fitnesses for each individual
        k: how many individals from the population should compete [DISABLED]
    Outputs:
        parent1: the DNA of the higest fitness individual
        parent2: the DNA of the second highest fitness individual
        """
    # Create a zipped population for easy handling, pair chromosomes and their fitness
    pop_with_fitness = list(zip(population, fitnesses))
    
    # Create a tournament with k random individuals from the available population
    #candidates = random.sample(pop_with_fitness, k)
    candidates = pop_with_fitness
    
    # Sort the candidates by fitness in descending order (higher fitness is better)
    candidates.sort(key=lambda x: x[1], reverse=True)
    #print(candidates)
    
    # Select the two best parents
    parent1 = candidates[0][0]  # DNA of the highest fitness
    parent2 = candidates[1][0]  # DNA of the second highest fitness
    
    return parent1, parent2

# Function to perform crossover between two parents
def crossover(parent1, parent2):
    """Takes two parents and crosses each chromosome at a random point, similar
    to the actual crossing of chromosomes in real life.
    Input:
        parent1: the DNA (list of chromosomes) of the first parent
        parent2: the DNA (list of chromosomes) of the second parent
    Output:
        child1: child as the result of a cross that takes first half of DNA
        child2: child as a result of a cross that takes the other half of DNA
        """
    # initialize lists for DNA
    child1 = []
    child2 = []
    
    # loop through genetic code of parents 1 and 2 and cross
    for i in range(len(parent1)):
        n = random.randint(0, len(parent1[i])) # pick random cross point
        child1.append(np.concatenate((parent1[i][0:n], parent2[i][n:])))
        child2.append(np.concatenate((parent2[i][0:n], parent1[i][n:])))
    return(child1, child2)

# Function to mutate chromosomes 1-4
def mutate14(chromosome, mutation_rate, low_bound = -10, up_bound = 10):
    """Apply mutation to chromosomes 1-4.
    Input:
        chromosome: the list of chromosomes 1-4 (CR1-CR4)
        mutation_rate: the rate at which a gene on these chromosomes will be changed
        low_bound: the lower bounds of the value of the weights for the NN
        up_bound: the upper bounds of the value of the weights for the NN
    Outputs:
        chromosomes: the list of mutated chromosomes 1-4 (CR1-CR4)
        """
    # loop through chromosomes
    for i in range(len(chromosome)):
        if random.random() < mutation_rate: # determining if a gene should mutate
            j = random.randint(0,len(chromosome[i])-1) # choose gene within that column
            chromosome[i][j] += random.uniform(-low_bound*0.05, up_bound*0.05) # increment gene by a random amount
            # if statements to keep genes in proper bounds
            if chromosome[i][j] > up_bound:
                chromosome[i][j] = up_bound
            elif chromosome[i][j] < low_bound:
                chromosome[i][j] = low_bound
    return chromosome

# Function to mutate chromosome 0
def mutate0(chromosome, mutation_rate, low_N = 4, up_N= 100):
    """Apply mutation to chromosome 0.
    Input:
        chromosome: chromosome 0 (CR0)
        mutation_rate: the rate at which a gene on these chromosomes will be changed
        low_N: the lower bounds of the number of neurons for the NN
        up_N: the upper bounds of the number of neurons for the NN
    Outputs:
        chromosomes: mutated chromosome 0 (CR0)
        """
    # Loop through length of chromosome
    for i in range(1, len(chromosome)):
        if random.random() < mutation_rate: # check if there should be a mutation
            # mutation for active layers
            if (i%2 == 0): 
                if chromosome[i] ==1:
                    chromosome[i] = 0
                else:
                    chromosome[i] =1
            # mutation for number of neurons in layer
            else:
                chromosome[i] = random.randint(low_N, up_N)
                chromosome[i] = max(min(chromosome[i], up_N), low_N)  # Keep within bounds
    return chromosome

# Function to mutate all chromosomes
def mutate(child, zerorate, onefourrate, low_bound, up_bound, low_N, up_N):
    """Calls mutate0 and mutate14 to mutate the an individuals DNA.
    Input:
        child: the DNA (list of chromosomes) of an individual
        zerorate: the rate of mutation for chromosome 0
        onefourrate: the rate of mutation for chromosomes 1-4
        low_bound: the lower bounds of the value of the weights for the NN
        up_bound: the upper bounds of the value of the weights for the NN
        low_N: the lower bounds of the number of neurons for the NN
        up_N: the upper bounds of the number of neurons for the NN
    Output:
        child: the mutated DNA of the individual 
    """
    child[0] = mutate0(child[0], zerorate, low_N, up_N)
    for i in range(1, 5):
        child[i] = mutate14(child[i], onefourrate, low_bound, up_bound)
    return child

# Genetic Algorithm
def genetic_algorithm(population_size, generations, mutation_rate_0, mutation_rate_14, low_bound, up_bound, low_N, up_N):
    """Run the genetic algorithm.
    Input:
        population_size: the size of the population
        generations: the number of generations 'evolution' will operate on
        mutation_rate_0: the mutation rate of chromosome 0 (CR0)
        mutation_rate_14: the mutation rate of chromosomes 1-4 (CR1-CR4)
        low_bound: the lower bounds of the value of the weights for the NN
        up_bound: the upper bounds of the value of the weights for the NN
        low_N: the lower bounds of the number of neurons for the NN
        up_N: the upper bounds of the number of neurons for the NN
    Output:
        population[best_idx]: the DNA of the best inidividual in the population
        fitnesses[best_idx]: the fitness of the best inidividual in the population
        genchamps: a historical list of the best individual DNA (list), fitness
        of that individual (int), and the game seed that individual played on (int)"""
        
    # Step 1: Create initial population
    population = create_initial_population(population_size, low_bound, up_bound,low_N,up_N)
    genchamps = [] # list which will hold the best brain of each genertion and the corresponding fitness- index using [gen][0 for brain, 1 for fitness]
    
    for generation in range(generations):
        # Step 2: Simulate each brain and calculate fitness
        fit_plus_seeds = [simulate_brain(DNA) for DNA in population]
        # Extract resutls into individual lists
        fitnesses = []
        seeds = []
        for i in range(len(fit_plus_seeds)):
            fitnesses.append(fit_plus_seeds[i][0])
            seeds.append(fit_plus_seeds[i][1])
        
        # Step 3: Select the next generation
        new_population = []
        for _ in range(population_size // 2):  # Half-size as 2 children are generated per pair
            # Select parents
            parent1, parent2 = select_parents(population, fitnesses)
            # Crossover
            child1, child2 = crossover(parent1, parent2)
            # Mutate
            child1 = mutate(child1, mutation_rate_0, mutation_rate_14, low_bound, up_bound, low_N, up_N)
            child2 = mutate(child2, mutation_rate_0, mutation_rate_14, low_bound, up_bound, low_N, up_N)
            # Add children to the new population
            new_population.append(child1)
            new_population.append(child1)
            
        # Step 4: Output the best individual of the generation 
        best_idx = np.argmax(fitnesses) # find the index of the individual with the best fitness      
        if best_idx > len(population): # fail safe for index when an odd number is picked for the population
            best_idx = len(population)-1
        best_individual = population[best_idx]
        best_fitness = fitnesses[best_idx]
        best_seed = seeds[best_idx]
        
        # Step 5: Record in genchamps
        genchamps.append([best_individual, best_fitness, best_seed])
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")
        
        #Step 6: Update population and repeat
        population = new_population
    
    # Return the best individual and its fitness
    best_idx = np.argmax(fitnesses)
    
    return population[best_idx], fitnesses[best_idx], genchamps



