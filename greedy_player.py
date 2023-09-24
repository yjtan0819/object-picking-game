from consts import *
import random
from play import MAP_SIZE

class Player(GamePlayer):
    def __init__(self):
        self.name = "Greedy"
        self.group = 'n/a'
    
    def step(self, game_map, turn, cur_pos):
        return self.greedy(game_map, turn, cur_pos)
    
    def greedy(self, game_map, turn, cur_pos):
        


    
