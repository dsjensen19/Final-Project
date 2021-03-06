import arcade
from game.gui_components.objects.game_object import Game_Object
from random import randint
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
import random as random



class Haven(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = "Haven_Large"
        self.x = screen_width / 2 + 100
        self.y = screen_height / 2

        self.sound_coins = arcade.load_sound("sounds\Coins.mp3")

    def reset(self):
        "stuff"
    def draw(self, centered_object):

        x = self.x  - centered_object.x + screen_width / 2
        y = self.y  - centered_object.y + screen_height / 2

        self.sprite.draw(x, y)

    #def touch_ship(self, centered_object):
        #open GUI

    def touch_ship(self, centered_object):
        self.buy_treasure(centered_object)   
        centered_object.in_port = True       
    
    def buy_treasure(self, ship):
        treasure = ship.get_treasure()
        if treasure > 0: 
            rate = 6
            ship.gold += treasure * rate
            ship.treasure = 0
            arcade.play_sound(self.sound_coins, 0.25)