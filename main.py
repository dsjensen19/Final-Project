
import arcade
from game.game_engine import Game_Engine
from game.gui_components.objects.ship import Ship

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    REFRESH_RATE
)
def main(): 
    ship = Ship()
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pirate")
    game_view = Game_Engine(ship)
    window.show_view(game_view)
    window.set_update_rate(REFRESH_RATE)
    arcade.run()

if __name__ == "__main__":
    main()
