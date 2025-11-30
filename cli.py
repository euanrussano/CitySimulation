from building_factory import BuildingFactory
from game_view import GameView

building_factories = {
    "house": BuildingFactory("House", 1, "🏠"),
    "well": BuildingFactory("Well", 1, "⛲")
}

class CommandLineGameView(GameView):
    def __init__(self):
        super().__init__()

    def run(self, commands: list[str]):
        for command in commands:
            args = command.split(" ")
            if args[0] == "start":
                rows = int(args[1])
                cols = int(args[2])
                self.start_game(rows, cols)
            elif args[0] == "place":
                building_name = args[1]
                x = int(args[2])
                y = int(args[3])
                building_factory = building_factories[building_name]
                try:
                    self.presenter.place_building(building_factory, x, y)
                except Exception as e:
                    print(e)
            elif args[0] == "show":
                self.show()


    def show(self):
        print(self.presenter.world)

    def on_game_started(self, rows, cols):
        print(f"Game started with grid {rows} x {cols}. All tiles empty.")

    def on_building_placed(self, name, x, y):
        print(f"Placed {name} at ({x},{y})")

