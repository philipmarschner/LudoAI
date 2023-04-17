from agent import Agent, NUM_STATES 
import numpy as np
import ludopy
import time
import multiprocessing as mp

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
            print(tempAgent.get_chromosome())
            self.agents.append(tempAgent)
    


    def playGame(self, agent):
        # Evaluate agents by playing numGames games
        if self.numEnemys not in [1, 3]:
            raise ValueError("Number of enemys must be 1 or 3")
        
        if self.numEnemys == 1:
            g= ludopy.Game([1,3])
        else:
            g = ludopy.Game()

        gamesWon = 0
        for i in range(self.numGames):
            there_is_a_winner = False

            while not there_is_a_winner:
                (dice, move_pieces, player_pieces, enemy_pieces, player_is_a_winner, there_is_a_winner), player_i = g.get_observation()

                if len(move_pieces):
                    if player_i == 0:
                        piece_to_move = agent.get_best_action(dice, move_pieces, player_pieces, enemy_pieces)
                        win = 1
                    else:
                        piece_to_move = move_pieces[np.random.randint(0, len(move_pieces))]
                        win = 0
                else:
                    piece_to_move = -1

                _, _, _, _, _, there_is_a_winner = g.answer_observation(piece_to_move)
            
            gamesWon += win
            g.reset()
        
        return gamesWon/self.numGames

    def evaluate(self):
        # Multithreading is used to speed up the process
        # https://analyticsindiamag.com/run-python-code-in-parallel-using-multiprocessing/

        start = time.perf_counter()

        pool = mp.Pool(processes=self.numAgents)
        evalRes = pool.map(self.playGame, self.agents)
       
        end = time.perf_counter()
        print(f"Eval time taken: {end - start} seconds")
        return evalRes     
    
    def select(self):
        # Select agents for next generation
        pass

    def crossover(self):
        # Crossover agents
        pass

    def mutate(self):
        # Mutate agents
        pass

    def computeFitness(self, evalRes):
        # Compute fitness of agents
        self.fitness.append(evalRes)
        return evalRes

    def train(self):
        # Initialize population
        self.initializePopulation()
        
        for i in range(self.numGenerations):
            # Evaluate agents
            evalRes = self.evaluate()

            # Compute fitness
            fitness = self.computeFitness(evalRes)

            # Select agents for next generation
            self.select()         # TODO NEXT

            # Crossover agents
            self.crossover()

            # Mutate agents
            self.mutate()

        pass