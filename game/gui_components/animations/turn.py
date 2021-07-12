from game.gui_components.animations.animation import Animation

import arcade.key

class Turn(Animation):
    def __init__(self, game_object, key):
        self.key = key
        rotation = 0
        if key == arcade.key.UP or key == arcade.key.W:
            rotation = 90
        elif key == arcade.key.DOWN or key == arcade.key.S:
            rotation = 270
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            rotation = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            rotation = 180
        else:
            self.is_finished = True
            return
        if game_object.rotation == rotation:
            self.is_finished = True
            return
        else:
            self.end_rotation = rotation
            super().__init__(game_object, 3/4 * game_object.get_speed())
            
        
    def set_initial_values(self):
        r1 = self._game_object.rotation
        r2 = self.end_rotation

        sign = 1
        t = 1
        if r1 == 0:
            if r2 == 180:
                t = 2
            elif r2 == 270:
                sign = -1
        elif r1 == 90:
            if r2 == 0:
                sign = -1
            elif r2 == 270:
                t = 2
        elif r1 == 180:
            if r2 == 0:
                t = 2
            elif r2 == 90:
                sign = -1
        elif r1 == 270:
            if r2 == 90:
                t = 2
            elif r2 == 180:
                sign = -1

        d_rotation = sign * 90 / self._time_end
        self._time_end *= t
        self._game_object.dRotation = d_rotation
        pass

    def set_final_values(self):
        super().set_final_values()
        self._game_object.rotation = self.end_rotation
        self._game_object.dRotation = 0
       