"""
Created on Sat Nov 30 19:59 2024

@author: KingRamenXIV
"""

def initialize_board():
    ''' Function that initializes the tetris board
    
    '''
    
    # Create an instance of Tetris
    env = gym.make("tetris_gymnasium/Tetris", render_mode="human")
    env.reset(seed=42) # Can change the seed
    
    terminated = False
    # Move the first block down one cell
    action = env.unrwappped.actions.move_down
    observation, reward, terminated, truncated, info = env.step(action)
