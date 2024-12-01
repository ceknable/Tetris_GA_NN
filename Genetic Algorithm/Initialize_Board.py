"""
Created on Sat Nov 30 19:59 2024

@author: KingRamenXIV
"""

def initialize
# Create an instance of Tetris
env = gym.make("tetris_gymnasium/Tetris", render_mode="human")
env.reset(seed=42)

# Main game loop
terminated = False
while not terminated:
    # Render the current state of the game as text
    env.render()
