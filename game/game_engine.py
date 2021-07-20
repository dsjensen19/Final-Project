import arcade
from arcade.color import BLACK, BLUE_GRAY as backround_color
import constants
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height,
    WORLD_DISTANCE
)
from game.gui_components.objects.backround import Backround
from game.map import Map
from game.fog_map import Fog_Map
from game.gui_components.animations.move import Move
from game.gui_components.animations.turn import Turn
from game.status import Status_Indecator
from game.shop_screen import Shop_Screen

class Game_Engine(arcade.View):
    def __init__(self, ship):
        super().__init__()
        self.keys_held = []
        arcade.set_background_color(backround_color)
        
        
        

        """ your code here"""
        self.sound_song = arcade.load_sound("sounds\OceanAndSeagulls.mp3")
        self.animations = []
        self.ship = ship
        self.backround = Backround()
        self.map = Map()
        self.fog_map = Fog_Map()
        self.status = Status_Indecator()
        self.pause_view = None

    def on_show(self):
        arcade.set_background_color(backround_color)
        arcade.play_sound(self.sound_song, .25 ,0, True)
        self.map.place_islands()
        self.fog_map.reset()
        self.window.set_mouse_visible(False)
    def update(self, delta_time):
        self.while_key_held()
        """ your code here"""
        for ani in self.animations:
            if ani.is_finished:
                self.animations.remove(ani)
            else:
                ani.update()
        self.ship.update()
        self.map.update(self.ship)
        self.fog_map.update(self.ship)      
        if self.ship.in_port:
            shop = Shop_Screen(self.ship, self)
            self.window.show_view(shop)  

    def on_draw(self):
        arcade.start_render()
        """ your code here"""
        self.backround.draw(self.ship)
        self.map.draw(self.ship)
        self.ship.draw()
        self.fog_map.draw(self.ship)
        self.status.draw(self.ship)
        
    def on_key_press(self, key, key_modifiers):
        if not key in self.keys_held:
            self.keys_held.append(key)
        """ your code here"""   
        if key == arcade.key.KEY_1:
            self.ship.upgrade("speed")
        if key == arcade.key.KEY_2:
            self.ship.upgrade("vision")
        if key == arcade.key.KEY_3:
            self.ship.upgrade("hold")
        if key == arcade.key.KEY_4:
            self.ship.upgrade("crew")
        if key == arcade.key.KEY_5:
            self.ship.upgrade("health")

    def while_key_held(self):
        for key in self.keys_held:
            """ your code here"""
            if not self.ship.is_in_animation:
                self.animations.append(Turn(self.ship, key))
                self.animations.append(Move(self.ship, key))
        
    def on_key_release(self, key, key_modifiers):
        if key in self.keys_held:
            self.keys_held.remove(key)
        """ your code here"""