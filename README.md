<h1 align="center">Object Picking Game</h1>

## Description
This is a multiplayer turn-based game that takes place on a grid. In this game, players must strategically move on the grid to collect various objects, including bananas, coins, and cauldrons. The game continues until all objects have been collected, or a turn limit is reached. The player with the most collected objects in each category is declared the winner.

## Gameplay

* The game is played on a grid where players move simultaneously in each turn.
* Objects (bananas, coins, and cauldrons) are randomly placed on the grid.
* Players automatically collect an object when moving onto a square containing it.
* If multiple players move onto the same object simultaneously, one is randomly selected to collect it.

## Winning Conditions
* The game ends when all objects are collected or the turn limit is reached.
* The player with the most collected objects in each category (banana, coin, cauldron) wins that category.
* If a player has the most objects in two or more categories, they are declared the overall winner.
* In case of a tie in any category, or if two players tie for the top spot in one category, there is no winner for that category.

## How to Play

1. Installation
    * Before running the game for the first time, you must install the pygame library

        ```bash
        pip install pygame
        ```
2. Running the Game
    * To run the game, run the `play.py` file
    
3. Configuration
    * In the play.py file, you can modify various game parameters at the top:
        * NUM_GAMES: Set the number of games to run (integer).
        * MAP_SIZE: Define the length of the grid (integer).
        * GUI: Toggle the graphical user interface on/off (boolean).
        * CHECK_TIMING: Enable/disable timing statistics on your step method (boolean).
        * PLAYER_MODULES: A list containing the names of files corresponding to the players that will participate in the game. Initially, only two random players are playing. If you want your player to participate, you can:
            * Replace one of the two strings with 'ai_player'.
            * Add 'ai_player' as an element to the list. This will result in three players: two random and your player. You can have any number of players in a game.