from game.gui_components.objects.game_object import Game_Object
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)

class Ship(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.x = screen_width/2
        self.y = screen_height/2

    def draw(self, centered_object):
        x = screen_width / 2
        y = screen_height / 2
        self.sprite.draw(x, y)
