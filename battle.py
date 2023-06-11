import time
import curses
from enemyAI import EnemyAI

class Battle: 
    def battle(self, stdscr, my_pokemon, enemy_pokemon):
        stdscr.nodelay(1)
        curses.curs_set(0)
        stdscr.clear()

        selected_index = 0
        actions = ["たたかう", "ポケモン", "こうさん"]

        stdscr.addstr("　バトルを開始します\n")
        stdscr.refresh()
        time.sleep(2)
        
        stdscr.addstr("　敵が　勝負を　仕掛けてきた！\n")
        stdscr.refresh()
        time.sleep(2)

        stdscr.addstr(f"　敵は　{enemy_pokemon['name']}を　くりだした！\n")
        stdscr.refresh()
        time.sleep(2)

        stdscr.addstr(f"　ゆけっ！　{my_pokemon['name']}！\n")
        stdscr.refresh()
        time.sleep(2)

        while True:
            stdscr.clear()

            stdscr.addstr(f"\n　敵：{enemy_pokemon['name']} Lv:{enemy_pokemon['level']} HP:{enemy_pokemon['for_battle']['buttle_hp']}/{enemy_pokemon['real_status']['hp']}\n\n")
            stdscr.addstr(f"　自分：{my_pokemon['name']} Lv:{enemy_pokemon['level']} HP:{my_pokemon['for_battle']['buttle_hp']}/{my_pokemon['real_status']['hp']}\n\n\n")

            stdscr.addstr(f"　{my_pokemon['name']}は　どうする？\n\n")

            for i, action in enumerate(actions):
                if i == selected_index:
                    stdscr.addstr(f"　> {action}\n")
                else:
                    stdscr.addstr(f"　  {action}\n")

            key = None
            while key not in [curses.KEY_UP, curses.KEY_DOWN, ord('\n')]:
                key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(actions)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(actions)
            elif key == ord('\n'):
                selected_action = actions[selected_index]
                if selected_action == "たたかう":
                    stdscr.clear()
                    selected_index = 0

                    while True:
                        stdscr.clear()

                        stdscr.addstr(f"　敵：{enemy_pokemon['name']} Lv:{enemy_pokemon['level']} HP:{enemy_pokemon['for_battle']['buttle_hp']}/{enemy_pokemon['real_status']['hp']}\n\n")
                        stdscr.addstr(f"　自分：{my_pokemon['name']} Lv:{enemy_pokemon['level']} HP:{my_pokemon['for_battle']['buttle_hp']}/{my_pokemon['real_status']['hp']}\n\n\n")

                        stdscr.addstr(f"　{my_pokemon['name']}は　どうする？\n\n")

                        for i, technique in enumerate(my_pokemon['technique']):
                            if i == selected_index:
                                stdscr.addstr(f"　> {technique['technique_name']}\n")
                            else:
                                stdscr.addstr(f"　  {technique['technique_name']}\n")
                        
                        key = None
                        while key not in [curses.KEY_UP, curses.KEY_DOWN, ord('\n')]:
                            key = stdscr.getch()

                        if key == curses.KEY_UP:
                            selected_index = (selected_index - 1) % len(my_pokemon['technique'])
                        elif key == curses.KEY_DOWN:
                            selected_index = (selected_index + 1) % len(my_pokemon['technique'])
                        elif key == ord('\n'):
                            selected_technique = my_pokemon['technique'][selected_index]['technique_name']
                            if selected_technique == 'もどる':
                                selected_index = 0
                                break



                stdscr.refresh()

            stdscr.refresh()

        return select_level

    # def speedComparison(self, pokemon):
