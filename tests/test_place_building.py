from building_factory import BuildingFactory
from game_presenter import GamePresenter

houseBuildingFactory = BuildingFactory(2, "🏠")

presenter = GamePresenter()
presenter.start_game(5,5)

# should work
presenter.place_building(houseBuildingFactory, 2, 2)

# should work
presenter.place_building(houseBuildingFactory, 4, 4)

# it should not work: place outside the world -> error
try:
    presenter.place_building(houseBuildingFactory, 6, 6)
except Exception as e:
    print(e)

# it should not work: place overlapping existing building -> error
try:
    presenter.place_building(houseBuildingFactory, 2, 2)
except Exception as e:
    print(e)

# it should not work: place overlapping existing building -> error
try:
    presenter.place_building(houseBuildingFactory, 3, 3)
except Exception as e:
    print(e)


print(presenter.world)