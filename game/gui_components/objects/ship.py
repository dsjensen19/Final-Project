from game.gui_components.objects.game_object import Game_Object
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)

class Ship(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #####
        self.gold = 0
        self.damage = 0

        self.image = "Ship"
        self.x = screen_width / 2
        self.y = screen_height / 2

        self.speed_values = [1, 2, 3, 4, 5]
        self.vision_values = [3, 4, 5, 6, 7]
        self.hold_values = [200, 350, 500, 700, 1000]
        self.crew_values = [5, 7, 9, 12, 16]

        self.speed_level = 0
        self.vision_level = 0
        self.hold_level = 0
        self.crew_level = 0


    def upgrade(self, trait):
        if (trait == "speed"):
          self.speed_level += 1
        elif (trait == "vision"):
          self.vision_level += 1
        elif (trait == "hold"):
          self.hold_level += 1
        elif (trait == "crew"):
          self.crew_level += 1


    def get_speed(self):
        return self.speed_values[self.speed_level]

    def get_vision(self):
        return self.vision_values[self.vision_level]

    def get_hold(self):
        return self.hold_values[self.hold_level]

    def get_crew(self):
        return self.crew_values[self.crew_level]

    def draw(self, centered_object):
        x = screen_width / 2
        y = screen_height / 2
        self.sprite.draw(x, y)
