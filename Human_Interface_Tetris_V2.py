# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:25:53 2024

@author: cekna
"""

import sys
import time
import cv2
import gymnasium as gym

from tetris_gymnasium.envs import Tetris

if __name__ == "__main__":
    # Create an instance of Tetris
    env = gym.make("tetris_gymnasium/Tetris", render_mode="human")
    env.reset(seed=42)
    
    last_update_time = time.time()  # Get the current time
    # Main game loop
    terminated = False
    while not terminated:
        # Render the current state of the game as text
        env.render()

        # Pick an action from user input mapped to the keyboard
        action = None
        time.sleep(0.5)
        action = env.unwrapped.actions.move_down
        
        key = cv2.waitKey(1)
        
        if key == ord("a"):
            action = env.unwrapped.actions.move_left
        elif key == ord("d"):
            action = env.unwrapped.actions.move_right
        elif key == ord("s"):
            action = env.unwrapped.actions.move_down
        elif key == ord("w"):
            action = env.unwrapped.actions.rotate_counterclockwise
        elif key == ord("e"):
            action = env.unwrapped.actions.rotate_clockwise
        elif key == ord(" "):
            action = env.unwrapped.actions.hard_drop
        elif key == ord("q"):
            action = env.unwrapped.actions.swap
        elif key == ord("r"):
            env.reset(seed=42)
            break
            
        if (
            cv2.getWindowProperty(env.unwrapped.window_name, cv2.WND_PROP_VISIBLE)
            == 0
        ):
            sys.exit()

        # Perform the action
        observation, reward, terminated, truncated, info = env.step(action)
        
        #current_time = time.time()  # Get the current time
        #if current_time - last_update_time >= 1:  # Check if 1 second has passed
            #last_update_time = current_time  # Update the last update time
            #action = env.unwrapped.actions.move_down
            #observation, reward, terminated, truncated, info = env.step(action)
            
    # Game over
    print("Game Over!")