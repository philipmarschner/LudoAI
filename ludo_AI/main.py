import numpy as np
import cv2
from agent import Agent
from population import Population
import time
import cProfile

numGames = 200 
numEnemys = 3 
numAgents = 20 
mutationRate = 0.05 
mutationSize = 0.20 
elitism = 0.1 
numGenerations = 1000

if __name__ == '__main__':
    print("Starting Ludo AI")

    # Create population to train
    p = Population(numGames, numEnemys, numAgents, mutationRate, mutationSize, elitism, numGenerations)
    
    # start timer
    start = time.time()

    # Train population
    p.train()

    # end timer
    end = time.time()

    # print time
    print(f"Finished training agents in: {round(end - start,2)} seconds")

    # plot ftiness over
    p.plotFitness("results.pdf")

    
    print("End of script")
