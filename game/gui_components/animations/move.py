import arcade.key
import constants
from game.gui_components.animations.animation import Animation

class Move(Animation):
    def __init__(self, game_object, time, key):
        self.key = key
        super().__init__(game_object, time)
        
    def set_initial_values(self):
        speed = constants.grid_square_pixle_length / self._time_end
        
        dx = 0
        dy = 0
        if self.key == arcade.key.UP:
            dy = speed
        elif self.key == arcade.key.DOWN:
            dy = -1 * speed
        elif self.key == arcade.key.RIGHT:
            dx = speed
        elif self.key == arcade.key.LEFT:
            dx = -1 * speed

        self._game_object.dx = dx
        self._game_object.dy = dy

    def set_final_values(self):
        super().set_final_values()
        self._game_object.dx = 0
        self._game_object.dy = 0
        