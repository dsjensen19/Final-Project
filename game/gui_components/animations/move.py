import arcade.key
import constants
from game.gui_components.animations.animation import Animation

class Move(Animation):
    def __init__(self, game_object, key):
        self.key = key
        super().__init__(game_object, game_object.get_speed())
        
    def set_initial_values(self):
        speed = constants.GRID_SQUARE_PIXLE_LENGTH / self._time_end
        
        dx = 0
        dy = 0
        if self.key == arcade.key.UP or self.key == arcade.key.W:
            dy = speed
        elif self.key == arcade.key.DOWN or self.key == arcade.key.S:
            dy = -1 * speed
        elif self.key == arcade.key.RIGHT or self.key == arcade.key.D:
            dx = speed
        elif self.key == arcade.key.LEFT or self.key == arcade.key.A:
            dx = -1 * speed
        else:
            self.is_finished = True
            self._game_object.is_in_animation = False
            return

        self._game_object.dx = dx
        self._game_object.dy = dy

    def set_final_values(self):
        super().set_final_values()
        self._game_object.dx = 0
        self._game_object.dy = 0
        if self._game_object.supplies > 0:
            self._game_object.supplies -= 1
        