"""
Created on Sat Nov 30 16:06 2024

@author: KingRamenXIV
Forked code from ewood. Adjusted to compile all features into one function
"""
import numpy as np
import gymnasium as gym
from tetris_gymnasium.envs import Tetris
from tetris_gymnasium.wrappers.observation import FeatureVectorObservation

def featurization(observation, env):
  
  ## FLATTEN THE BOARD INTO A LIST OF 1S AND 0S
  # Render active tetromino (because it's not on self.board)
  projection = env.unwrapped.project_tetromino()
  # Crop padding away as we don't want to render it
  projection = env.unwrapped.crop_padding(projection)
  
  #flatten board array into a one dimensional list
  gameboard = projection.flatten()
  #convert blocks with a tetromnio in them into 1
  gameboard[np.flatnonzero(gameboard)] = 1

  ## HEIGHT OF EACH COLUMN AFTER EACH FRAME. Every rows is a frame, every column is a column in the game. Last row is endgame frame.
  #create historian to keep track of the heights
  
        
  #print the height after each frame --> the board doesn't include the piece (the piece is a projection onto the board)
  env1 = FeatureVectorObservation(env) #create an instance of the class
  height_i = env1.calc_height(env.unwrapped.board) #call a function from the class with the board as an input
  height_i = (height_i[4:14])-4 #crop out the padding on either side (the bedrock) and normalize by the 4 layers of bedrock underneath
  

  ## HOLES OF BOARD AFTER EVERY FRAME
  #holes_hist = []
  # If holes doesn't work, try uncommenting the lines below.
  ## Render active tetromino (because it's not on self.board)
  #projection = env.unwrapped.project_tetromino() # Displays the tetromino that is falling onto the board

  ## Crop padding away as we don't want to render it
  #projection = env.unwrapped.crop_padding(projection) # Crops padding of the board walls.

  env1 = FeatureVectorObservation(env) #create an instance of the class
  #Calculate the holes after each frame
  holes_i = env1.calc_holes(env.unwrapped.board) # Returns the number of cells that are empty and have a filled cell above it i.e. only want the holes
  #holes_hist.append(holes_i)
  
  return gameboard, height_i, holes_i




