from arcade import *
from random import randrange
import os
WIDTH = 1600
HEIGHT = 1000
TITLE = "gamamam"
CSCALE = 0.03
MONEY = 50


class MyGame(Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.player_list = None
        self.coin_list = None
        self.player_sprite = None
        self.score = 0
        self.pacscale = 0.1
        self.set_mouse_visible(False)
        set_background_color(color.AMAZON)

    def setup(self):
        self.player_list = SpriteList()
        self.coin_list = SpriteList()
        self.score = 0
        self.player_sprite = Sprite("pacman.png", self.pacscale)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        for i in range(MONEY):
            coin = Sprite("Coin.png", CSCALE)
            coin.center_x = randrange(WIDTH)
            coin.center_y = randrange(HEIGHT)
            self.coin_list.append(coin)

    def on_draw(self):
        start_render()
        self.coin_list.draw()
        self.player_list.draw()
        output = f"Score: {self.score}"
        draw_text(output, 100, 200, color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        start_render()
        self.coin_list.update()
        coins_hit_list = check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.kill()
            self.score += 1
            self.pacscale += 0.01


def main():
    window = MyGame()
    window.setup()
    run()


if __name__ == '__main__':
    main()
