import time
import curses
from enemyAI import EnemyAI
from Calculation.calculation import Calculation
from Management.battleProgression import BattleProgression

class Battle: 
    def __init__(self):
        self.enemyAI = EnemyAI()
        self.calculation = Calculation()
        self.battleProgression = BattleProgression()

    def battle(self, stdscr, my_pokemon, enemy_pokemon):

        self.battleProgression.startBattle(stdscr, my_pokemon, enemy_pokemon)

        self.battleProgression.theActionChoice(stdscr, my_pokemon, enemy_pokemon)
