import curses

from opening import Opening
from pokemon import Pokemon
from battle import Battle

class Main:
    def run(self):
        opening = Opening()
        selected_level = curses.wrapper(opening.selectLevel)
        selected_pokemon = curses.wrapper(opening.selectPokemon)

        pokemon = Pokemon()
        my_pokemon = pokemon.myPokemon(selected_level, selected_pokemon)
        enemy_pokemon = pokemon.enemyPokemon(selected_level)

        print(enemy_pokemon)

        battle = Battle()
        curses.wrapper(battle.battle, my_pokemon, enemy_pokemon)


if __name__ == "__main__":
    main = Main()
    main.run()