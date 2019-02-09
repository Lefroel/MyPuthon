from arcade import *
WIDTH = 1600
HEIGHT = 800
CELL = 20
open_window(WIDTH, HEIGHT, "Main Menu")
set_background_color([255, 255, 255])
start_render()


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


def tochkodetector_x(x):
    temp = x*CELL
    return temp


def tochkodetector_y(y):
    temp = y * CELL
    return temp


draw_tetrad()
draw_text("5", 1400, 150, [255, 0, 0], 60)
draw_text("Молодец!", 1250, 100, [255, 0, 0], 40)
draw_text("Домашняя работа.", tochkodetector_x(10), tochkodetector_y(37), [0, 213, 0], 40)
draw_circle_outline(tochkodetector_x(50), tochkodetector_y(25), 123, [0, 213, 0], 10)
finish_render()
run()
