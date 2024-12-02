"""
Created on Sat Nov 30 19:59 2024

@author: KingRamenXIV
"""

def initialize_board():
    ''' 
    Function that initializes the tetris board. 

    Returns: 
        gameboard: The initilized board 
        env: The Tetris env to be played in
    
    '''
    
    # Create an instance of Tetris
    env = gym.make("tetris_gymnasium/Tetris", render_mode="human")
    #env.reset(seed=42) # Fixed Seed
    env.reset()
    
    terminated = False
    # Move the first block down one cell
    action = env.unrwappped.actions.move_down
    observation, reward, terminated, truncated, info = env.step(action)

    # Get flattened board to feed to TETRIS
    gameboard, height, holes = featurize(observation)

    return gameboard, env
