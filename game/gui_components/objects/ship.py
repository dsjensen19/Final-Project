from game.gui_components.objects.game_object import Game_Object
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)

class Ship(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #####
        self.gold = 0
        self.health = 100

        self.image = "Ship"
        self.x = screen_width / 2
        self.y = screen_height / 2

        self.speed_values = [1, 0.8, 0.4, 0.2, 0.1]
        self.vision_values = [3, 4, 5, 6, 7]
        self.hold_values = [200, 350, 500, 700, 1000]
        self.crew_values = [5, 7, 9, 12, 16]
        self.health_values = [100, 200, 300, 400, 500]

        self.speed_level = 0
        self.vision_level = 0
        self.hold_level = 0
        self.crew_level = 0
        self.health_level = 0


    def upgrade(self, trait):
        if (trait == "speed") and self.speed_level < len(self.speed_values)-1:
          self.speed_level += 1
        elif (trait == "vision") and self.vision_level < len(self.vision_values)-1:
          self.vision_level += 1
        elif (trait == "hold") and self.hold_level < len(self.hold_values)-1:
          self.hold_level += 1
        elif (trait == "crew") and self.crew_level < len(self.crew_values)-1:
          self.crew_level += 1
        elif (trait == "Health") and self.health_level < len(self.health_values)-1:
          self.health_level += 1


    def get_speed(self):
        return self.speed_values[self.speed_level]
    
    def get_health(self):
        return self.health_values[self.health_level]

    def get_vision(self):
        return self.vision_values[self.vision_level]

    def get_hold(self):
        return self.hold_values[self.hold_level]

    def get_crew(self):
        return self.crew_values[self.crew_level]

    def draw(self, centered_object):
        print(f"treasure: {self.gold}, Health: {self.health}")
        x = screen_width / 2
        y = screen_height / 2
        self.sprite.draw(x, y)
        self.damage = 0
