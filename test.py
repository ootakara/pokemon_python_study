import curses

def main(stdscr):
    stdscr.nodelay(1)
    curses.curs_set(0)

    selected_index = 0
    techniques = ['技A', '技B', '技C', '技D']

    while True:
        stdscr.clear()
        stdscr.addstr("技を選択してください:\n")

        for i, technique in enumerate(techniques):
            if i == selected_index:
                stdscr.addstr(f"> {technique}\n")
            else:
                stdscr.addstr(f"  {technique}\n")


        key = None
        while key not in [curses.KEY_UP, curses.KEY_DOWN, ord('\n')]:
            key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_index = (selected_index - 1) % len(techniques)
        elif key == curses.KEY_DOWN:
            selected_index = (selected_index + 1) % len(techniques)
        elif key == ord('\n'):
            selected_technique = techniques[selected_index]
            stdscr.addstr(f"\n選択された技: {selected_technique}")
            stdscr.refresh()

            # break

        stdscr.refresh()

curses.wrapper(main)

