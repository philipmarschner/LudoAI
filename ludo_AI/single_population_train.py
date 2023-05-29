import numpy as np
import cv2
from agent import Agent
from population import Population
import time
import cProfile

numGames = 200 
numEnemys = 3 
numAgents = 50 
mutationRate = 0.1
mutationSize = 0.5
elitism = 0.1 
numGenerations = 250

if __name__ == '__main__':
    print("Starting Ludo AI")
    print("---Starting new run---")
    print("Mutation rate: ", mutationRate, " Mutation size: ", mutationSize)
    p = Population(numGames, numEnemys, numAgents, mutationRate, mutationSize, elitism, numGenerations)
    p.train()
            

    # Create population to train
    #p = Population(numGames, numEnemys, numAgents, mutationRate, mutationSize, elitism, numGenerations)
    #p.train()


    # plot ftiness over    
    print("End of script")
