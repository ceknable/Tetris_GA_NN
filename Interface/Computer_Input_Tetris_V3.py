"""
Created on Mon Nov 30 15:38 2024

@author: KingRamenXIV
"""
import cv2
import gymnasium as gym
import time
from tetris_gymnasium.envs import Tetris

def TETRIS_V2(brain, gameboard):
  '''
  Inputs: 
    brain: The NN that takes in the current board state and outputs an action.
    gameboard: Initial game board with the first block moved down. Flattened array of 1 and 0. 

  Other: 
    TIInput: A 1x6 array where all but one entries are 0. The non-zero position defines the action to take. 
             TInput = [Left,Right,Down,Rotate,SDown,Swap]

  Return: 
    gameboard: The final gameboard at game over
    height_hist: The history of the column heights over every step of the game
    holes_hist: The history of the number of holes in each column over every step of the game. 
    
    A "game over" message is printed 
    
  '''
    
    if __name__ == "__main__":
        ## The following lines were moved to the Initialize_Tetris function START
        # # Create an instance of Tetris
        # env = gym.make("tetris_gymnasium/Tetris", render_mode="human")
        # env.reset(seed=42)
        
        # # Main game loop
        # terminated = False
        ## END
        while not terminated:
            # Render the current state of the game as text
            env.render()
            
            # Reset parameters 
            action = None

          
            while time == 0 and action == None:

                # Get action input from brain
                action_prob = player_V2(gameboard, brain) # Output from sigmoid function
                TInput = max_action(action_prob) # 1x6 array. Only one element will be 1. Everything else is 0. 
              
                if TInput[0]:
                    action = env.unwrapped.actions.move_left
                elif TInput[1]:
                    action = env.unwrapped.actions.move_right
                elif TInput[2]:
                    action = env.unwrapped.actions.move_down
                elif TInput[3]:
                    action = env.unwrapped.actions.rotate_clockwise
                elif TInput[4]:
                    action = env.unwrapped.actions.hard_drop
                elif TInput[5]:
                    action = env.unwrapped.actions.swap
                elif key == ord("r"): # Pressing "r" still resets the game. 
                    env.reset(seed=42)
                    break

                
                if (
                    cv2.getWindowProperty(env.unwrapped.window_name, cv2.WND_PROP_VISIBLE)
                    == 0
                ):
                    sys.exit()
            
            if action == None:
                action = env.unwrapped.actions.move_down
            
            # Perform the action
            observation, reward, terminated, truncated, info = env.step(action)
            # Get the flattened board for this step, height and holes histroy for the game. 
            gameboard, height_hist, holes_hist = featurization(observation, env)
    
        # Game over
        print("Game Over!")

return gameboard, height_hist, holes_hist
