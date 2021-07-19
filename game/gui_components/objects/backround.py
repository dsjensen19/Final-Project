from game.gui_components.objects.game_object import Game_Object
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)

class Backround(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "Backround_smol"
        self.x = screen_width / 2
        self.y = screen_height / 2
    def update(self):
        pass
    def draw(self, centered_object):
        if not centered_object.is_in_animation:
            self.x = centered_object.x
            self.y = centered_object.y
        x = self.x - centered_object.x + screen_width / 2
        y = self.y - centered_object.y + screen_height / 2
        self.sprite.draw(x, y)
