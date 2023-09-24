import random
from game import main
from gui import GameGUI
from importlib import util
from collections import defaultdict
from timeit import default_timer as timer

# Modify the variables below to change various properties of the game.

NUM_GAMES = 100
MAP_SIZE = 15
GUI = True
CHECK_TIMING = True
PLAYER_MODULES = ['random_player', 'ai_player', 'random_player']
FPS = 2
MAX_TURNS = 200
MAX_OBJ_PROPORTION = 0.15
VERSION = "1.5"

# Do not touch any lines below this point.

def run(num_games, map_size, show_gui, fps, check_timing, player_modules, max_turns, obj_proportion):
    player_modules = list(enumerate(player_modules))
    wins = defaultdict(int)
    times = defaultdict(int)
    
    if show_gui:
        gui = GameGUI(fps, (map_size, map_size))
        gui.start(len(player_modules))
    else:
        gui = None
    
    for i in range(num_games):
        players = []
        random.shuffle(player_modules)
        for j, (k, player_module) in enumerate(player_modules):
            spec = util.spec_from_file_location("module.name", player_module + ".py")
            foo = util.module_from_spec(spec)
            spec.loader.exec_module(foo)
            players.append(foo.Player())
            players[-1].name = f"Player {k}: {players[-1].name} ({j})"
            players[-1].image_name = f'{k+1}'
            players[-1].i = k
    
        winners, timings, final_turn = main(players, map_size, max_turns, obj_proportion, check_timing, gui)
        print(f"Game {i+1}: {winners}")
        if len(winners) <= 1:
            for w in winners:
                wins[w.split(" (")[0]] += 1
        else:
            wins['Tie'] += 1
        for t in timings:
            times[t.split(" (")[0]] += timings[t] / final_turn
        
        if show_gui:
            gui.update_standings(wins)
    
    if show_gui:
        gui.stop()
    
    game_feedback = f"The results of the {num_games} games were as follows:\n"
    game_feedback += '\n'.join([f"{w}: {wins[w]}" for w in wins])
    print(game_feedback)
    
    timing_feedback = ''
    if check_timing:
        timing_feedback = f"It took the following average number of seconds for each player's step method to be executed:\n"
        timing_feedback += '\n'.join([f"{t}: {times[t]}" for t in times])
        print(timing_feedback)
    
    return game_feedback, timing_feedback, wins, times

if __name__ == '__main__':
    start = timer()
    run(NUM_GAMES, MAP_SIZE, GUI, FPS, CHECK_TIMING, PLAYER_MODULES, MAX_TURNS, MAX_OBJ_PROPORTION)
    end = timer()
    diff = end - start
    print(diff)