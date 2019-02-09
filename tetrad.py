from arcade import *
WIDTH = 1600
HEIGHT = 800
CELL = 20


def draw_tetrad():
    for i in range(1, WIDTH // CELL):
        if i == WIDTH // CELL - 4:
            tmp_color = [255, 0, 0]
            draw_line(CELL*i, 0, CELL*i, WIDTH, tmp_color, 7)
        else:
            tmp_color = [21, 18, 237]
            draw_line(CELL*i, 0, CELL*i, WIDTH, tmp_color, 2)
    for i in range(1, HEIGHT // CELL):
        draw_line(0, CELL * i, WIDTH, CELL * i, [21, 18, 237], 2)


open_window(WIDTH, HEIGHT, "Main Menu")
set_background_color([255, 255, 255])
start_render()
draw_tetrad()
finish_render()
run()
