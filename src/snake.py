import random
import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()

    screen = curses.initscr()
    curses.curs_set(0)
    scrh, scrw  = screen.getmaxyx()
    window = curses.newwin(scrh, scrw, 0, 0)
    window.keypad(1)
    window.timeout(100)

    snake_x = scrw/4
    snake_y = scrh/2
    snake  = [
        [snake_y, snake_x],
        [snake_y, snake_x-1],
        [snake_y, snake_x-2]
    ]

    food = [int(scrh/2), int(scrw/2)]
    window.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, scrh] or snake[0][1] in [0, scrw] or snake[0] in snake[1:]:
            curses.endwin()
            display_score(snake)
            quit()

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1,  scrh-1),
                    random.randint(1, scrw-1)
                ]
                food  = nf if nf not in snake else None
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            window.addch(int(tail[0]), int(tail[1]), ' ')

        try:
            window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
        except:
            pass

def display_score(snake):
    print("Score: " + str(len(snake)))

wrapper(main)