# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:53:39 2024

@author: cekna
"""

import sys

import cv2
import gymnasium as gym

from tetris_gymnasium.envs import Tetris

import time

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
        count = 0
        time = 0
        while time == 0 and action == None:
            key = cv2.waitKey(1) # wait 1 ms
             
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
            count = count+1
            if count == 67:
                time = 1
            if (
                cv2.getWindowProperty(env.unwrapped.window_name, cv2.WND_PROP_VISIBLE)
                == 0
            ):
                sys.exit()
        if action == None:
            action = env.unwrapped.actions.move_down
        # Perform the action
        observation, reward, terminated, truncated, info = env.step(action)

    # Game over
    print("Game Over!")