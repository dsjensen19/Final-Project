'''
Created on Jun 07, 2021

@author: sethb
'''

from game.gui_components.objects.game_object import Game_Object

class Dot(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
