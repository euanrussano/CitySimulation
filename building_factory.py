class BuildingInstance:
    def __init__(self, name: str, x: int, y: int, size:int, symbol: str):
        self.name = name
        self.x = x
        self.y = y
        self.size = size
        self.symbol = symbol


class BuildingFactory:
    def __init__(self, name: str, size: int, symbol: str):
        self.name = name
        self.size = size
        self.symbol = symbol

    def create(self, x: int, y: int) -> BuildingInstance:
        return BuildingInstance(self.name, x, y, self.size, self.symbol)