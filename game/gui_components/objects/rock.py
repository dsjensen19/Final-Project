from game.gui_components.objects.game_object import Game_Object
from random import randint
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)

class Rock(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "Rock"
        self.damage = 10

    def reset(self):
        pass
    def draw(self, centered_object):
        x = self.x - centered_object.x + screen_width / 2
        y = self.y - centered_object.y + screen_height / 2
        self.sprite.draw(x, y)
    def update(self, centerd_object):
        super().update(centerd_object)
        if self.damage == 0:
            if self.distance(centerd_object) > 0:
                self.damage = 10

    def touch_ship(self, centered_object):
        centered_object.damage(self.damage)
        if self.damage > 0:
            if centered_object.tresure > 10:
                centered_object.tresure -= 10
            else:
                centered_object.tresure = 0
                
            if centered_object.supplies > 10:
                centered_object.supplies -= 10
            else:
                centered_object.supplies = 0

        self.damage = 0








