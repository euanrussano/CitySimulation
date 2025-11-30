class Tile:
    def __init__(self, x: int, y: int, is_land: bool):
        self.x = x
        self.y = y
        self.is_land = is_land


class World:
    def __init__(self, rows: int, cols: int):
        self.tiles = []
        self.buildings = []
        self.initialize(rows, cols)

    @property
    def height(self):
        return len(self.tiles)

    @property
    def width(self):
        if not self.tiles:
            return 0
        return len(self.tiles[0])

    def initialize(self, rows: int, cols: int):
        self.tiles = []
        width = cols
        height = rows
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Tile(x, y, True))
            self.tiles.append(row)

    def __str__(self):
        output_str = f"World {self.width} x {self.height}\n"
        output_str += " " # leading char for numbers row
        for x in range(self.width):
            output_str += str(x)
        output_str += "\n"
        for y in range(self.height):
            z=ord('A') + y
            output_str += chr(z)
            buildings = list(filter(lambda building: building.y == y, self.buildings))
            for x in range(self.width):
                building = list(filter(lambda building: building.x == x, buildings))
                tile = self.tiles[y][x]
                char_tile = "." if tile.is_land else "~"
                if building:
                    char_tile = building[0].symbol
                output_str += char_tile
            output_str += '\n'
        return output_str

