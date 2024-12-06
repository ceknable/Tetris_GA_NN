# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:27:37 2024

@author: cekna
"""
#Libraries
import gymnasium as gym
from tetris_gymnasium.envs.tetris import Tetris
from tetris_gymnasium.envs.tetris import TetrisState
from tetris_gymnasium.wrappers.observation import FeatureVectorObservation

import sys
import cv2
import time
import numpy as np

import os

#import neat
import random
import pickle

def TETRIS_V2(brain,i_seed):
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
        # Create an instance of Tetris
        env = gym.make("tetris_gymnasium/Tetris", render_mode="human")
        env.reset(seed = i_seed)

        start_clip =0
        
        # Main game loop
        #Initialize total score
        total_score = 0

        # # Main game loop
        terminated = False

        while not terminated:
            # Render the current state of the game as text
            env.render()

            # Render active tetromino (because it's not on self.board)
            projection = env.unwrapped.project_tetromino()

            # Crop padding away as we don't want to render it
            projection = env.unwrapped.crop_padding(projection)
            gameboard = projection.flatten()
              #convert blocks with a tetromnio in them into 1
            gameboard[np.flatnonzero(gameboard)] = 1
             # Pick an action from user input mapped to the keyboard
            action = None
            while action is None:
                key = cv2.waitKey(1)

                if start_clip==0:
                    if key == ord("a"):
                        action = env.unwrapped.actions.move_left
                        start_clip=1
                else:
                    # Get action input from brain
                    action_prob = player(gameboard, brain) # Output from NEURAL NETWORK
                    TInput = np.zeros(6)
                    TInput[np.argmax(action_prob)] = 1 # 1x6 array. Only one element will be 1. Everything else is 0. 

                    if TInput[0]:
                        action = env.unwrapped.actions.move_left
                    elif TInput[1]:
                        action = env.unwrapped.actions.move_right
                    elif TInput[2]:
                        action = env.unwrapped.actions.hard_drop
                    elif TInput[3]:
                        action = env.unwrapped.actions.rotate_clockwise
                    elif TInput[4]:
                        action = env.unwrapped.actions.move_down
                    elif TInput[5]:
                        action = env.unwrapped.actions.swap
                
                if (
                    cv2.getWindowProperty(env.unwrapped.window_name, cv2.WND_PROP_VISIBLE)
                    == 0
                ):
                    sys.exit()
            time.sleep(.1) 
            # Perform the action
            observation, reward, terminated, truncated, info = env.step(action)

            #Update the score:
            total_score += reward
            env1 = FeatureVectorObservation(env) #create an instance of the class
            #Calculate the holes after each frame
            holes_hist = env1.calc_holes(env.unwrapped.board) 
    
    return holes_hist, total_score

def player(gameboard,brain, loud = False):
    ''' This function takes the gameboard and uses the brain to make decisions
    about how to move in Tetris
    Input: 
        gameboard: the gameboard vector
        brain: the brain outputted from "create", a list of weight matrices
        loud: boolean for optional print output
    Output:
        output: a vector of probabilities for each possible move
    '''
    
    # Determine the size of the brain for number of operations
    int_count = sum(isinstance(x, int) for x in brain)
    brain_size = 4 - int_count
    # Add bias to gameboard
    gameboard = np.insert(gameboard, 0, 1)

    # Compute Layer 1 operations
    layer1 = gameboard@brain[0].T # MatMult of gameboard and weights
    layer1 = sigmoid(layer1) # take sigmoid of output
    layer1 = np.insert(layer1, 0, 1) # insert bias for next computation
   
    layer2 = layer1@brain[1].T # MatMult of layer1 and weights
    layer2 = sigmoid(layer2) # take sigmoid of output
    output = layer2 # define final output
    
    # print brain size
    if loud:
        print('size =', brain_size)
    
    # if brain is big enough, continue operations
    if brain_size >= 3:
        layer2 = np.insert(layer2, 0, 1) # insert bias for next computation
        layer3 = layer2@brain[2].T # MatMult of layer2 and weights
        layer3 = sigmoid(layer3) # take sigmoid of output
        output = layer3 # define final output
        
    if brain_size == 4:
        layer3 = np.insert(layer3, 0, 1) # insert bias for next computation
        layer4 = layer3@brain[3].T # MatMult of layer3 and weights
        layer4 = sigmoid(layer4) # take sigmoid of output
        output = layer4 # define final output
        
    #output = np.round(output/np.sum(output)*100,0) # normalize output    
    return(output)
def create(DNA, loud = False):
    ''' This function takes the raw DNA as the input. Unravels it into
    chromosomes. Then based on Chromosome 0 cuts and arranges Theta weight
    matrices to fit the shape of the new neural network.
    Input:
        DNA: the list of chromosomes taken from a GA or Rand_CRs
        loud: boolean for optional print output
    Output:
        brain: a list of weight matrices for the NN'''
    
    # Unravel DNA
    for i in range(len(DNA)):
        globals()['CR'+str(i)] = DNA[i]
        
    # Initialize weight matrices
    Theta1 = 0
    Theta2 = 0
    Theta3 = 0
    Theta4 = 0
    
    # Create weight Matrices    
    
    # Create Theta1 Matrix
    
    Row1 = int(CR0[1])              # Measure row dimensions based on number of neurons in first layer
    Theta1 = CR1[0:Row1,:]          # Cut CR1 (raw matrix) to fit size
    
    
    # Create Theta2 Matrix if layer 2 or 3 active
    
    if CR0[2] == 1:                 # if layer 2 is active
        Row2 = int(CR0[3])              # number of neurons in layer 2
        Col2 = Row1+1                   # number of neurons in layer 1 + bias
        Theta2 = CR2[0:Row2,0:Col2]     # Cut CR2 (raw matrix) to fit size
    elif CR0[4] == 1:               # if layer 3 is active and layer 2 is not 
        Row2 = int(CR0[5])              # number of neurons in layer 3
        Col2 = Row1+1                   # number of neurons in layer 1 + bias
        Theta2 = CR3[0:Row2,0:Col2]     # Cut CR3 (raw matrix) to fit size
    
    
    # Create Theta3 Matrix if layer 2 and 3 active
    
    if CR0[4] == 1 and CR0[2] == 1: # if layers 2 and 3 are active
        Row3 = int(CR0[5])              # number of neurons in layer 3
        Col3 = Row2+1                   # number of neurons in layer 2 + bias
        Theta3 = CR3[0:Row3,0:Col3]     # Cut CR3 (raw matrix) to fit size
    
    
    # Create Output Matrix (Theta 2 or 3 or 4) from CR4
    
    if type(Theta3) != int and type(Theta2) != int and type(Theta1) != int: # if all 3 layers are active
         Col4 = Row3+1                                                          # number of neurons in layer 3 + bias
         Theta4 = CR4[:,0:Col4]                                                 # Cut CR4 to size
    elif type(Theta2) != int and type(Theta1) != int:                       # if 2 layers are active
         Col4 = Row2+1                                                          # number of neurons in layer 2 or 3 + bias
         Theta3 = CR4[:,0:Col4]                                                 # Cut CR4 to size
    elif type(Theta1) != int:                                               # if only 1 layer active
         Col4 = Row1+1                                                          # number of neurons in layer 1 + bias
         Theta2 = CR4[:,0:Col4]                                                 # Cut CR4 to size
    
    
    # Print CR0 and sizes of weight matrices
    if loud:
        print(CR0)
        if type(Theta1) != int:
            print('Theta 1:',Theta1.shape)
        if type(Theta2) != int:    
            print('Theta 2:',Theta2.shape)
        if type(Theta3) != int:
            print('Theta 3:',Theta3.shape)
        if type(Theta4) != int:
            print('Theta 4:',Theta4.shape)
    
    # Return all Thetas. Thetas that are not active are integer zeros.
    brain = (Theta1,Theta2,Theta3,Theta4)
    return(brain)
def sigmoid(z):
    '''Function that takes an input z and returns the sigmoid transformation.
    If z is a vector or a matrix, it should perform the sigmoid transformation on every element.
    Input:
    z [=] scalar or array
    Return:
    g [=] scalar or array
    '''

    # Calculate sigmoid transform of z
    g = 1/(1+np.exp(-z))

    return g

name = 'test14'
with open(name+'.pkl', 'rb') as f:
    genchamps = pickle.load(f)
    #DNA, fitness, seed

fitness = []
for k in range(len(genchamps)):
    fitness.append(genchamps[k][1])
index = np.argmax(fitness)
i_seed = genchamps[index][2] #don't include 
#print(loaded_object[45][1])

#Create the brain from the dna
brain = create(genchamps[index][0])

#### ENTER THE SEED IN MANUALLY SINCE IT HAS TO BE OF TYPE INTEGER
hol_i , sco_i = TETRIS_V2(brain, int(genchamps[index][2]))
fitness = (sco_i*2) - hol_i
print(fitness)