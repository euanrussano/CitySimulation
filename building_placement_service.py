import utils
from building_factory import BuildingFactory
from world import World

class BuildingPlacementError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class BuildingPlacementService:
    def __init__(self, world: World):
        self.world = world

    def place_building(self, building_factory:BuildingFactory, x: int, y: int):
        # check if position x,y is free to place building, otherwise error
        tile = self.world.tiles[y][x]
        if not tile.is_land: raise BuildingPlacementError(f"Tile at ({x},{y}) is not land")

        # check if there is not a building already occupying x, y
        for building in self.world.buildings:
            x1 = building.x
            y1 = building.y
            size = building.size
            if x == x1 and y == y1: raise BuildingPlacementError(f"Another building already occupies ({x},{y})")
            bottom_left_x = x1 - size/2
            bottom_left_y = y1 - size/2
            top_right_x = x1 + size/2
            top_right_y = y1 + size / 2
            if utils.is_point_in_rectangle(x, y, bottom_left_x, bottom_left_y, top_right_x, top_right_y):raise BuildingPlacementError(f"Another building already occupies ({x},{y})")


        # create the building and "place" on the position
        building_instance = building_factory.create(x, y)
        self.world.buildings.append(building_instance)

        # TODO FUTURE: building with cost (check money), etc

