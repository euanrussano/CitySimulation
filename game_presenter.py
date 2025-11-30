from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game_view import GameView

from building_factory import BuildingFactory
from world import World
from building_placement_service import BuildingPlacementService

class GamePresenter:
    def __init__(self, view: "GameView"):
        self.world = None
        self.building_placement_service = None
        self.view = view

    def start_game(self, rows: int, cols: int):
        self.world = World(rows, cols)
        self.building_placement_service = BuildingPlacementService(self.world)
        self.view.on_game_started(rows, cols)


    def place_building(self, building_factory: BuildingFactory, x: int, y: int):
        self.building_placement_service.place_building(building_factory, x, y)
        self.view.on_building_placed(building_factory.name, x, y)
