from game.gui_components.objects.fog import Fog
from game.gui_components.point import Point
from constants import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GRID_SQUARE_PIXLE_LENGTH,
    WORLD_DISTANCE,
    RENDER_DISTANCE,
    ISLAND_DENSTIY,
    ROCK_DENSTIY)

class Fog_Map():
    def __init__(self):
        self.reset()
        self.fog_drawer = Fog()

    def reset(self):
        self.fog = [[True for y in range(WORLD_DISTANCE)] for x in range(WORLD_DISTANCE)]

    def update(self, centered_object):
        shipx = int((centered_object.x -SCREEN_WIDTH/2) / GRID_SQUARE_PIXLE_LENGTH + WORLD_DISTANCE/2)
        shipy = int((centered_object.y -SCREEN_HEIGHT/2) / GRID_SQUARE_PIXLE_LENGTH + WORLD_DISTANCE/2)
        
        p = Point(0,0)
        for x in range(shipx - RENDER_DISTANCE, shipx + RENDER_DISTANCE+1):
            p.x = SCREEN_WIDTH/2 + GRID_SQUARE_PIXLE_LENGTH * (x - WORLD_DISTANCE/2)
            for y in range(shipy - RENDER_DISTANCE, shipy + RENDER_DISTANCE+1):
                p.y = SCREEN_HEIGHT/2 + GRID_SQUARE_PIXLE_LENGTH * (y - WORLD_DISTANCE/2)
                if p.distance(centered_object.center) <= 100 *centered_object.get_vision():
                    self.fog[x][y] = False
        
    def draw(self, centered_object):
        shipx = int((centered_object.x -SCREEN_WIDTH/2) / GRID_SQUARE_PIXLE_LENGTH + WORLD_DISTANCE/2)
        shipy = int((centered_object.y -SCREEN_HEIGHT/2) / GRID_SQUARE_PIXLE_LENGTH + WORLD_DISTANCE/2)
        for x in range(shipx - RENDER_DISTANCE, shipx + RENDER_DISTANCE+1):
            for y in range(shipy - RENDER_DISTANCE, shipy + RENDER_DISTANCE+1):
                if self.fog[x][y]:
                    self.fog_drawer.x = SCREEN_WIDTH/2 + GRID_SQUARE_PIXLE_LENGTH * (x - WORLD_DISTANCE/2)
                    self.fog_drawer.y = SCREEN_HEIGHT/2 + GRID_SQUARE_PIXLE_LENGTH * (y - WORLD_DISTANCE/2)
                    self.fog_drawer.draw(centered_object)
