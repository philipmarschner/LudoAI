import ludopy
import numpy as np
import cv2
from agent import Agent
from population import Population

if __name__ == '__main__':
    print("Starting Ludo AI")

    p = Population(10, 0.05, 0.5, 0.1)
    g = ludopy.Game()
    a = Agent()
    there_is_a_winner = False

    while not there_is_a_winner:
        (dice, move_pieces, player_pieces, enemy_pieces, player_is_a_winner, there_is_a_winner), player_i = g.get_observation()
        

        if len(move_pieces):
            a.calc_state(dice, move_pieces, player_pieces, enemy_pieces)
            piece_to_move = move_pieces[np.random.randint(0, len(move_pieces))]
        else:
            piece_to_move = -1

        _, _, _, _, _, there_is_a_winner = g.answer_observation(piece_to_move)


    print("End of script")
