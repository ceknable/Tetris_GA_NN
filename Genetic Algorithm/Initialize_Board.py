"""
Created on Sat Nov 30 19:59 2024

@author: KingRamenXIV
"""
import gymnasium as gym
from Featurization/featurization import featurization
import random

def initialize_board():
    ''' 
    Function that initializes the tetris board. 

    Returns: 
        gameboard: The initilized board 
        env: The Tetris env to be played in
    
    '''
    
    # Create an instance of Tetris
    env = gym.make("tetris_gymnasium/Tetris", render_mode="human")

    #Create random integer to reset the seed and return
    rand_seed = random.randint(0,100)
    env.reset(rand_seed=42) 
    
    terminated = False
    # Move the first block down one cell
    action = env.unwrapped.actions.move_down
    observation, reward, terminated, truncated, info = env.step(action)

    # Get flattened board to feed to TETRIS
    gameboard, height, holes = featurize(observation)

    return gameboard, env, rand_seed
