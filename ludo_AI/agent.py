import numpy as np
class Agent:
    def __init__(self):
        self.chromosome = []


    def set_chromosome(self, chromosome):
        self.chromosome = chromosome
    
    def get_chromosome(self):
        return self.chromosome
    
    def get_action(self, move_pieces):
        # Temp return ranom numbber between 1 and 4
        return np.random.randint(0, len(move_pieces))
    
    def calc_state(self, obs, player_i):