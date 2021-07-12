from game.gui_components.objects.game_object import Game_Object
from random import randint
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)

class Island(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "None"

    def draw(self, centered_object):
        x = self.x - centered_object.x + screen_width / 2
        y = self.y - centered_object.y + screen_height / 2
        self.sprite.draw(x, y)

    def touch_ship(self, centered_object):
        centered_object.damage += 100
        self.image = "None"