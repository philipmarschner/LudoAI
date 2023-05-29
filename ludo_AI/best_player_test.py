import numpy as np
import cv2
from agent import Agent
from population import Population
import time
import cProfile

numGames = 5000
numEnemys = 3 
numAgents = 1 
mutationRate = 0
mutationSize = 00
elitism = 0
numGenerations = 1

chromosome = [0.122144301428050,	0.415098963072078,	0.0663425351356662,	0.0590735947951773,	0.303222350642040,	0.0178394449174069,	0.0159276262154338,	0.0776216928169868,	0.190644848040070,	0.0500829975281394,	0.0158689779578756,	0.695992583082125,	0.0849567760309734]

if __name__ == '__main__':
    print("Starting Ludo AI")
    print("---Starting new run---")
    print("Mutation rate: ", mutationRate, " Mutation size: ", mutationSize)
    p = Population(numGames, numEnemys, numAgents, mutationRate, mutationSize, elitism, numGenerations)
    p.setChromosome(0, chromosome)
    games_won, score = p.play(p.agents[0])
    print("Games won: ", games_won)
    #save score list to csv file
    np.savetxt("score.csv", score, delimiter=",")

    # Create population to train
    #p = Population(numGames, numEnemys, numAgents, mutationRate, mutationSize, elitism, numGenerations)
    #p.train()


    # plot ftiness over    
    print("End of script")
