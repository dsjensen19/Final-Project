from game.gui_components.objects.game_object import Game_Object
from game.gui_components.point import Point
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
import random as random

class Island(Game_Object):
    def __init__(self,centered_object, **kwargs):
        super().__init__(**kwargs)
        image = random.randint(1,4)
        if image == 1:
            self.image = "Island_1"
        elif image == 2:
            self.image = "Island_2"
        elif image == 3:
            self.image = "Island_3"
        elif image == 4:
            self.image = "Island_4"
        self.centered_object = centered_object.center

    def draw(self):

        x = self.x - self.centered_object.x + screen_width / 2
        y = self.y - self.centered_object.y + screen_height / 2

        self.sprite.draw(x, y)
