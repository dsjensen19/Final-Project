from game.gui_components.objects.game_object import Game_Object
from random import randint
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
import random as random

MIN_TRESURE = 5
MAX_TRESURE = 15

class Island(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        image_num = random.randint(1,4)
        self.rotation = 90 * random.randint(0,3)
        self.image = "Island_" + str(image_num)
        self.treasure = randint(MIN_TRESURE, MAX_TRESURE)
    def reset(self):
        image_num = random.randint(1,4)
        self.rotation = 90 * random.randint(0,3)
        self.image = "Island_" + str(image_num)
        self.treasure = randint(MIN_TRESURE, MAX_TRESURE)
    def draw(self, centered_object):

        x = self.x - centered_object.x + screen_width / 2
        y = self.y - centered_object.y + screen_height / 2

        self.sprite.draw(x, y)

    def touch_ship(self, centered_object):
        if centered_object.supplies >= 5:
            if self.treasure > 0:
                if centered_object.tresure < centered_object.get_hold():
                    centered_object.add_treasure(self.treasure)
                    centered_object.supplies -= 5
                    self.treasure = 0
                    self.image = "Island_looted"
