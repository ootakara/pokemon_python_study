import curses

class Opening:
    def selectLevel(self, stdscr):
        stdscr.nodelay(1)
        curses.curs_set(0)

        selected_index = 0
        levels = ["Lv.5", "Lv.50", "Lv.100"]

        while True:
            stdscr.clear()
            stdscr.addstr("ようこそ！！\n")
            stdscr.addstr("どのレベルに挑戦しますか？\n")

            for i, level in enumerate(levels):
                if i == selected_index:
                    stdscr.addstr(f"> {level}\n")
                else:
                    stdscr.addstr(f"  {level}\n")

            key = None
            while key not in [curses.KEY_UP, curses.KEY_DOWN, ord('\n')]:
                key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(levels)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(levels)
            elif key == ord('\n'):
                select_level = levels[selected_index]
                stdscr.refresh()
                break

            stdscr.refresh()

        return select_level

    def selectPokemon(self, stdscr):
        stdscr.nodelay(1)
        curses.curs_set(0)

        selected_index = 0
        pokemons = ['フシギダネ', 'ヒトカゲ', 'ゼニガメ']

        while True:
            stdscr.clear()
            stdscr.addstr("ポケモンを1匹選んでください\n")

            for i, pokemon in enumerate(pokemons):
                if i == selected_index:
                    stdscr.addstr(f"> {pokemon}\n")
                else:
                    stdscr.addstr(f"  {pokemon}\n")

            key = None
            while key not in [curses.KEY_UP, curses.KEY_DOWN, ord('\n')]:
                key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(pokemons)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(pokemons)
            elif key == ord('\n'):
                select_pokemon = pokemons[selected_index]
                stdscr.refresh()
                break

            stdscr.refresh()

        return select_pokemon

# print("選択されたレベル:", selected_level)
# print("選択されたポケモン:", selected_pokemon)
