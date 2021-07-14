from game.gui_components.objects.game_object import Game_Object
from random import randint
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
import random as random


class Haven(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "Haven_Large"
    def reset(self):
        "stuff"
    def draw(self, centered_object):

        x = self.x + 900 - centered_object.x + screen_width / 2
        y = self.y + 335 - centered_object.y + screen_height / 2

        self.sprite.draw(x, y)

    def touch_ship(self, centered_object):
        #open GUI
        self.image = "Haven_Small"