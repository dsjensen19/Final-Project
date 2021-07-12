from game.gui_components.objects.game_object import Game_Object
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)

class Backround(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "Backround"
    def update(self, centerd_object):
        self.is_on_screen = True
    def draw(self, centered_object):
        x = screen_width / 2
        y = screen_height / 2
        self.sprite.draw(x, y)