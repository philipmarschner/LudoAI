import sys
sys.path.insert(0,"../") #for importing ludopy in subfolder
from agent import Agent, NUM_STATES 
import numpy as np
import ludopy
import time
import multiprocessing as mp
import matplotlib.pyplot as plt

rng = np.random.default_rng(12345)

# Inspired by https://github.com/AugustMader/Genetic-algorithm-Ludo-game-in-Python/blob/main/geneticAlgorithm/geneticAlgorithm.py

class Population:
    def __init__(self, numGames, numEnemys, numAgents, mutationRate, mutationSize, elitism, numGenerations):
        self.agents = [] # List of agents
        self.numGames = numGames # Number of games played to evaluate agent
        self.numEnemys = numEnemys # Number of enemys, 1 or 3
        self.numAgents = numAgents  # Number of agents in population
        self.mutationRate = mutationRate # Chance of mutation
        self.mutationSize = mutationSize # Size of mutation, 0.1 = 10% of value
        self.elitism = elitism # Percentage of agents that will be copied to next generation
        self.numGenerations = numGenerations # Number of generations to run
        self.fitness = [] # Fitness of each agent
    
    def generateChromosome(self):
        # Generate chromosome
        chromosome = rng.random(NUM_STATES)
        return chromosome

    def initializePopulation(self):
        for i in range(self.numAgents):
            tempAgent = Agent()
            tempAgent.set_chromosome(self.generateChromosome())
            self.agents.append(tempAgent)

    def playGame(self, agent):
        # Evaluate agents by playing numGames games
        if self.numEnemys not in [1, 3]:
            raise ValueError("Number of enemys must be 1 or 3")
        
        if self.numEnemys == 1:
            g= ludopy.Game([1,3])
        else:
            g = ludopy.Game()

        agent.gamesWon = 0
        for i in range(self.numGames):
            there_is_a_winner = False

            while not there_is_a_winner:
                (dice, move_pieces, player_pieces, enemy_pieces, player_is_a_winner, there_is_a_winner), player_i = g.get_observation()

                if len(move_pieces):
                    if player_i == 0:
                        piece_to_move = move_pieces[agent.get_best_action(dice, move_pieces, player_pieces, enemy_pieces)]
                        win = 1
                    else:
                        piece_to_move = move_pieces[np.random.randint(0, len(move_pieces))]
                        win = 0
                else:
                    piece_to_move = -1

                there_is_a_winner = g.answer_observation(piece_to_move)
            
            agent.gamesWon += win

            g.reset()

        return agent.gamesWon

    def evaluate(self):
        # Multithreading is used to speed up the process
        # https://analyticsindiamag.com/run-python-code-in-parallel-using-multiprocessing/

        start = time.perf_counter()

        pool = mp.Pool(processes=self.numAgents)
        wins = pool.map(self.playGame, self.agents)
        pool.close()
        pool.join()
        end = time.perf_counter()
        print(f"    Finished evaluating agents in: {round(end - start,2)} seconds")


        for i in range(len(self.agents)):
            self.agents[i].gamesWon = wins[i] 

        

        
        
        
    
    def computeFitness(self):
        # Compute fitness of agents
        fitness = []
        for agent in self.agents:
            agent.fitness = agent.gamesWon/self.numGames
            fitness.append(agent.fitness)

        print("    Fitness: ", fitness)
        self.fitness.append(fitness)

    def select(self):
        # sort agents by fitness
        agentsSorted = self.agents.copy()
        agentsSorted.sort(key=lambda x: x.fitness)
        
        rankedAgents = []
        # Select agents for next generation by ranked selection
        # Worst agent has rank 1, best agent has rank numAgents

        for i in range(self.numAgents):
            for j in range (i+1):
                rankedAgents.append(agentsSorted[i])
        
        # Select agents for next generation by elitism
        numElites = int(self.numAgents*self.elitism)

        # Select parents for next generation
        parents = []
        for i in range(self.numAgents):
            if i <= numElites:
                parents.append([agentsSorted[i], agentsSorted[i]])
            else:
                parent1 = rankedAgents[rng.integers(0, len(rankedAgents))]
                parent2 = rankedAgents[rng.integers(0, len(rankedAgents))]
                parents.append([parent1, parent2])
        
        return parents

    def crossover(self, parents):
        # Crossover agents by uniform crossover
        
        childrens = []
        
        # Generate bit mask
        mask = rng.integers(0, 2, NUM_STATES)

        for i in range(self.numAgents):
            # Generate new agent
            child = Agent()

            # Generate new chromosome
            newChromosome = np.array(parents[i][0].get_chromosome())*np.array(mask) + np.array(parents[i][1].get_chromosome())*(1-np.array(mask))

            child.set_chromosome(newChromosome)

            childrens.append(child)
        
        return childrens

    def mutate(self, nextGen):
        # Mutate agents
        mutatedAgents = []

        # Select agents for next generation by elitism
        numElites = int(self.numAgents*self.elitism)

        for agent in nextGen:
            # Copy elite agents to next generation
            if numElites > 0:
                mutatedAgents.append(agent)
                numElites -= 1
                continue

            # Mutate bit in chromosome if random number is less than mutation rate
            for i in range(NUM_STATES):
                if rng.random() < self.mutationRate:
                    currentValue = agent.chromosome[i]
                    newValue = currentValue + rng.uniform(-currentValue*self.mutationSize, currentValue*self.mutationSize)
                    
                    # Make sure new value is between 0 and 1
                    if newValue < 0:
                        newValue = 0
                    elif newValue > 1:
                        newValue = 1
                    agent.chromosome[i] = newValue
            
            # Add agent to list of mutated agents
            mutatedAgents.append(agent)
        return mutatedAgents


    def train(self):
        # Initialize population
        self.initializePopulation()
        
        for i in range(self.numGenerations):
            print("Generation: ", i+1, "/", self.numGenerations)
            # Evaluate agents
            self.evaluate()

            # Compute fitness
            self.computeFitness()

            # Select agents for next generation
            parents = self.select()

            # Crossover agents
            nextGen = self.crossover(parents)

            # Mutate agents
            self.agents = self.mutate(nextGen)
    
    def plotFitness(self, imgPath):
        # Plot max and average fitness of each generation
        maxFitness = []
        avgFitness = []

        for i in range(self.numGenerations):
            maxFitness.append(max(self.fitness[i]))
            avgFitness.append(sum(self.fitness[i])/len(self.fitness[i]))
        
        plt.plot(maxFitness, label="Max fitness")
        plt.plot(avgFitness, label="Average fitness")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.legend()
        plt.savefig(imgPath)
        plt.show()
        
