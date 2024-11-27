# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:06:27 2024

@author: cekna
"""
import cv2
import gymnasium as gym
import time
from tetris_gymnasium.envs import Tetris

TInput = [Left,Right,Down,Rotate,SDown,Swap]

def TETRIS(TInput):
    
    if __name__ == "__main__":
        # Create an instance of Tetris
        env = gym.make("tetris_gymnasium/Tetris", render_mode="human")
        env.reset(seed=42)
    
        # Main game loop
        terminated = False
        while not terminated:
            # Render the current state of the game as text
            env.render()
            
            # Pick an action from user input mapped to the keyboard
            action = None
            time = 0
            while time == 0:
                key = cv2.waitKey(1)
                
                time.sleep(1)  # 200 ms is 0.2 seconds
                
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
                elif key == ord("r"):
                    env.reset(seed=42)
                    break
                
                time = 1
                
                if (
                    cv2.getWindowProperty(env.unwrapped.window_name, cv2.WND_PROP_VISIBLE)
                    == 0
                ):
                    sys.exit()
    
            # Perform the action
            observation, reward, terminated, truncated, info = env.step(action)
    
        # Game over
        print("Game Over!")