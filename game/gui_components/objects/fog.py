from game.gui_components.objects.game_object import Game_Object
from constants import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)
class Fog(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "None"

    def draw(self, centered_object):

        x = self.x - centered_object.x + SCREEN_WIDTH/ 2
        y = self.y - centered_object.y + SCREEN_HEIGHT/ 2

        self.sprite.draw(x, y)