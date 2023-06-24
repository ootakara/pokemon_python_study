import curses

from opening import Opening
from settingPokemon import SettingPokemon
from battle import Battle

class Main:
    def __init__(self):
        self.opening = Opening()
        self.settingPokemon = SettingPokemon()
        self.battle = Battle()

    def run(self):
        selected_level = curses.wrapper(self.opening.selectLevel)
        selected_pokemon = curses.wrapper(self.opening.selectPokemon)

        my_pokemon = self.settingPokemon.myPokemon(selected_level, selected_pokemon)
        enemy_pokemon = self.settingPokemon.enemyPokemon(selected_level)

        curses.wrapper(self.battle.battle, my_pokemon, enemy_pokemon)

if __name__ == "__main__":
    main = Main()
    main.run()