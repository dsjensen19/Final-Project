from game.gui_components.objects.game_object import Game_Object
from random import randint
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
import random as random
from game.gui_components.objects.ship import Ship


class Haven(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "Haven_Large"
        self.x = screen_width / 2 + 100
        self.y = screen_height / 2
    def reset(self):
        "stuff"
    def draw(self, centered_object):

        x = self.x  - centered_object.x + screen_width / 2
        y = self.y  - centered_object.y + screen_height / 2

        self.sprite.draw(x, y)

    #def touch_ship(self, centered_object):
        #open GUI

    def buy_treasure(self):
        treasure = self.ship.get_hold
        rate = 3
        self.ship.gold = treasure * rate
        self.ship.treasure = 0