from agent import Agent, NUM_STATES 
import numpy as np
import ludopy

rng = np.random.default_rng(12345)

# Inspired by https://github.com/AugustMader/Genetic-algorithm-Ludo-game-in-Python/blob/main/geneticAlgorithm/geneticAlgorithm.py

class Population:
    def __init__(self, numAgents, mutationRate, mutationSize, elitism):
        self.agents = [] # List of agents
        self.numAgents = numAgents  # Number of agents in population
        self.mutationRate = mutationRate # Chance of mutation
        self.mutationSize = mutationSize # Size of mutation, 0.1 = 10% of value
        self.elitism = elitism # Percentage of agents that will be copied to next generation

        self.initializePopulation()
    
    def generateChromosome(self):
        # Generate chromosome
        chromosome = rng.random(NUM_STATES)
        return chromosome

    def initializePopulation(self):
        for i in range(self.numAgents):
            tempAgent = Agent()
            tempAgent.set_chromosome(self.generateChromosome())
            print(tempAgent.get_chromosome())
            self.agents.append(tempAgent)
    
    def evaluate(self, numGames, numEnemys):
        # Evaluate agents by playing numGames games
        pass
    
    def select(self):
        # Select agents for next generation
        pass

    def crossover(self):
        # Crossover agents
        pass

    def mutate(self):
        # Mutate agents
        pass

    def computeFitness(self):
        # Compute fitness of agents
        pass

    def playGame(self):
        # Play a game
        pass

    def train(self, numGames, numEnemys):
        # Train agents
        pass