from game.gui_components.objects.game_object import Game_Object
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)

class Ship(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "Ship"
        self.gold = 0

        self.speed_values = [0.3, 0.2, 0.1, 0.05, 0.025]
        self.vision_values = [1.5, 2.5, 3.5, 4.5, 5.5, 8]
        self.hold_values = [200, 350, 500, 700, 1000]
        self.crew_values = [5, 7, 9, 12, 16]
        self.max_health_values = [100, 200, 300, 400, 500]

        self.speed_upgrades = [100, 250, 625, 1563]
        self.vision_upgrades = [100, 250, 625, 1563, 3906]
        self.hold_upgrades = [100, 250, 625, 1563]
        self.crew_upgrades = [100, 250, 625, 1563]
        self.max_health_upgrades = [100, 250, 625, 1563]

        self.speed_level = 0
        self.vision_level =0
        self.hold_level = 0
        self.crew_level = 0
        self.max_health_level = 0

        self.x = screen_width / 2
        self.y = screen_height / 2
        self.curent_health = 0
        self.supplies = 0
        self.treasure = 0
        self.in_port = False
        self.reset()

    def reset(self):
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.curent_health = self.get_max_health()
        self.treasure = 0
        self.supplies = 100
        self.in_port = False
    def upgrade(self, trait):
        if (trait == "speed") and self.speed_level < len(self.speed_values)-1:
            if self.get_gold() > self.speed_upgrades[self.speed_level]:
                self.gold -= self.speed_upgrades[self.speed_level]
                self.speed_level += 1
                
        elif (trait == "vision") and self.vision_level < len(self.vision_values)-1:
            if self.get_gold() > self.vision_upgrades[self.vision_level]:
                self.gold -= self.vision_upgrades[self.vision_level]
                self.vision_level += 1
                
        elif (trait == "hold") and self.hold_level < len(self.hold_values)-1:
            if self.get_gold() > self.hold_upgrades[self.hold_level]:
                self.gold -= self.hold_upgrades[self.hold_level]
                self.hold_level += 1
                
        elif (trait == "crew") and self.crew_level < len(self.crew_values)-1:
            if self.get_gold() > self.crew_upgrades[self.crew_level]:
                self.gold -= self.crew_upgrades[self.crew_level]
                self.crew_level += 1
                
        elif (trait == "supplies"):
            if self.get_gold() > 50 and self.supplies <= 500:
                self.supplies += 100
                self.gold -= 50
        elif (trait == "health") and self.max_health_level < len(self.max_health_values)-1:
            if self.get_gold() > self.max_health_upgrades[self.max_health_level]:
                self.gold -= self.max_health_upgrades[self.max_health_level]
                self.max_health_level += 1
                self.current_health = self.get_max_health()


    def get_speed(self):
        return self.speed_values[self.speed_level]
    
    def get_max_health(self):
        return self.max_health_values[self.max_health_level]

    def get_vision(self):
        return self.vision_values[self.vision_level]

    def get_hold(self):
        return self.hold_values[self.hold_level]
    
    def get_gold(self):
        return self.gold
        
    def get_treasure(self):
        return self.treasure

    def get_crew(self):
        return self.crew_values[self.crew_level]

    def damage(self, damage_value):
        self.curent_health -= damage_value
        if self.curent_health <= 0:
            self.reset()
    
    def add_treasure(self, treasure_value):
        if self.treasure + treasure_value > self.get_hold():
            self.treasure = self.get_hold()
        else:
            self.treasure += treasure_value


    def draw(self):
        x = screen_width / 2
        y = screen_height / 2
        self.sprite.draw(x, y)
    def update(self):
        super().update(self)

