from game.gui_components.objects.game_object import Game_Object
from random import randint
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
import random as random

class Island(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        image_num = random.randint(1,4)
        self.rotation = 90 * random.randint(0,3)
        self.image = "Island_" + str(image_num)
        self.gold = randint(50, 1000)

    def draw(self, centered_object):

        x = self.x - centered_object.x + screen_width / 2
        y = self.y - centered_object.y + screen_height / 2

        self.sprite.draw(x, y)

    def touch_ship(self, centered_object):
        centered_object.gold += self.gold
        self.gold = 0
        self.image = "None"