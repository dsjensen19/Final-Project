from random import randint

from game.gui_components.objects.island import Island
from game.gui_components.objects.rock import Rock
from constants import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GRID_SQUARE_PIXLE_LENGTH,
    WORLD_DISTANCE,
    RENDER_DISTANCE,
    ISLAND_DENSTIY,
    ROCK_DENSTIY)
class Map():
    def __init__(self):
        self.island_refrences = []
        self.islands = []
        self.fog = []
        self.create_island_refrences()
        self.place_islands()

    def create_island_refrences(self):
        num_islands = int(WORLD_DISTANCE**2 * ISLAND_DENSTIY)
        for _ in range(num_islands):
            self.island_refrences.append(Island())
        num_rocks = int(WORLD_DISTANCE**2 * ROCK_DENSTIY)
        for _ in range(num_rocks):
            self.island_refrences.append(Rock())
    def place_islands(self):
        self.islands = [[None for y in range(WORLD_DISTANCE)] for x in range(WORLD_DISTANCE)]

        for island_ref in self.island_refrences:
            island_ref.reset()
            island_placed = False
            while(not island_placed):
                index_x = randint(0, WORLD_DISTANCE-1)
                index_y = randint(0, WORLD_DISTANCE-1)
                if not (index_x >= (WORLD_DISTANCE/2 - 4) and index_x <= (WORLD_DISTANCE/2 + 4) and (index_y >= WORLD_DISTANCE/2 - 4) and (index_y <= WORLD_DISTANCE/2 + 4)):
                    if not self.islands[index_x][index_y]:
                        island_ref.x = SCREEN_WIDTH/2 + GRID_SQUARE_PIXLE_LENGTH * (index_x - WORLD_DISTANCE/2)
                        island_ref.y = SCREEN_HEIGHT/2 + GRID_SQUARE_PIXLE_LENGTH * (index_y - WORLD_DISTANCE/2)

                        self.islands[index_x][index_y] = island_ref
                        island_placed = True
        
    def draw(self, centered_object):
        shipx = int((centered_object.x -SCREEN_WIDTH/2) / GRID_SQUARE_PIXLE_LENGTH + WORLD_DISTANCE/2)
        shipy = int((centered_object.y -SCREEN_HEIGHT/2) / GRID_SQUARE_PIXLE_LENGTH + WORLD_DISTANCE/2)
        for x in range(shipx - RENDER_DISTANCE, shipx + RENDER_DISTANCE+1):
            for y in range(shipy - RENDER_DISTANCE, shipy + RENDER_DISTANCE+1):
                if self.islands[x][y]:
                    self.islands[x][y].draw(centered_object)

    def update(self, centered_object):
        shipx = int((centered_object.x -SCREEN_WIDTH/2) / GRID_SQUARE_PIXLE_LENGTH + WORLD_DISTANCE/2)
        shipy = int((centered_object.y -SCREEN_HEIGHT/2) / GRID_SQUARE_PIXLE_LENGTH + WORLD_DISTANCE/2)
        
        for x in range(shipx - RENDER_DISTANCE, shipx + RENDER_DISTANCE+1):
            for y in range(shipy - RENDER_DISTANCE, shipy + RENDER_DISTANCE+1):
                if self.islands[x][y]:
                    self.islands[x][y].update(centered_object)
