from game_presenter import GamePresenter


class GameView:
    def __init__(self):
        self.presenter = GamePresenter(self)

    def start_game(self, rows: int, cols: int):
        self.presenter.start_game(rows, cols)

    def on_game_started(self, rows, cols):
        raise NotImplementedError("Must be implemented on the concrete GameView class")

    def on_building_placed(self, name, x, y):
        raise NotImplementedError("Must be implemented on the concrete GameView class")

