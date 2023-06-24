import curses

class Opening:
    def __init__(self):
        self.levels = []
        self.pokemons = []

    def selectLevel(self, stdscr):
        stdscr.nodelay(1)
        curses.curs_set(0)

        selected_index = 0
        self.setLevel()

        while True:
            stdscr.clear()
            stdscr.addstr("\n　ようこそ！！\n\n")
            stdscr.addstr("　どのレベルに挑戦しますか？\n\n")

            for i, level in enumerate(self.levels):
                if i == selected_index:
                    stdscr.addstr(f"　>　Lv.{level}\n")
                else:
                    stdscr.addstr(f"　 　Lv.{level}\n")

            key = None
            while key not in [curses.KEY_UP, curses.KEY_DOWN, ord('\n')]:
                key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(self.levels)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(self.levels)
            elif key == ord('\n'):
                select_level = self.levels[selected_index]
                stdscr.refresh()
                break

            stdscr.refresh()

        return select_level

    def selectPokemon(self, stdscr):
        stdscr.nodelay(1)
        curses.curs_set(0)

        selected_index = 0
        self.setPokemon()

        while True:
            stdscr.clear()
            stdscr.addstr("\n　ポケモンを1匹選んでください\n\n")

            for i, pokemon in enumerate(self.pokemons):
                if i == selected_index:
                    stdscr.addstr(f"　>　{pokemon}\n")
                else:
                    stdscr.addstr(f"　 　{pokemon}\n")

            key = None
            while key not in [curses.KEY_UP, curses.KEY_DOWN, ord('\n')]:
                key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(self.pokemons)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(self.pokemons)
            elif key == ord('\n'):
                select_pokemon = self.pokemons[selected_index]
                stdscr.refresh()
                break

            stdscr.refresh()

        return select_pokemon
    
    def setLevel(self):
        self.levels = [5, 50, 100]

    def setPokemon(self):
        self.pokemons = ['フシギダネ', 'ゼニガメ', 'ヒトカゲ']

    
