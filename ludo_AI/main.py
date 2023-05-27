import numpy as np
import cv2
from agent import Agent
from population import Population
import time
import cProfile

numGames = 200 
numEnemys = 3 
numAgents = 10 
#mutationRate = 0.05
mutationRates = [0.01, 0.05, 0.1, 0.2]
#mutationSize = 0.20
mutationSizes = [0.05, 0.1, 0.2, 0.5]
elitism = 0.1 
numGenerations = 500

if __name__ == '__main__':
    print("Starting Ludo AI")

    for i in range(len(mutationRates)):
        for j in range(len(mutationSizes)):
            mutationRate = mutationRates[i]
            mutationSize = mutationSizes[j]
            print("---Starting new run---")
            print("Mutation rate: ", mutationRate, " Mutation size: ", mutationSize)
            p = Population(numGames, numEnemys, numAgents, mutationRate, mutationSize, elitism, numGenerations)
            p.train()

    # Create population to train
    #p = Population(numGames, numEnemys, numAgents, mutationRate, mutationSize, elitism, numGenerations)
    #p.train()


    # plot ftiness over    
    print("End of script")
