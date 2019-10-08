import sys

from src.cell import Cell
from src.utils import validate


class Map:
    """Class of map which maybe contains treasure"""
    def __init__(self):
        """Initialize class objects"""
        self.grid = [[]]*5
        self.road_to_treasure = []
        self.treasure_value = None
        self.message = None

    def from_file(self, lines):
        """Creating treasure map as list 5 by 5 from file"""
        for i in range(5):
            line = lines[i].split()
            row = list(map(int, line))
            if validate(row):
                self.grid[i] = [Cell(value) for value in row]
            else:
                input("Error: your file has incorrect values. For exit press Enter")

    def from_keyboard(self):
        """Creating treasure map as list 5 by 5 from keyboard"""
        counter = 0
        while counter < 5:
            line = input()
            line = line.strip().split()
            row = list(map(int, line))
            if validate(row):
                self.grid[counter] = [Cell(value) for value in row]
                counter += 1

    def next_cell(self, cell_value):
        """Finding next cell in map"""
        x, y = cell_value.coordinates
        next_cell_value = self.grid[x][y]
        return next_cell_value

    def hunt_treasure(self):
        """Finding treasure"""
        cell_value = self.grid[0][0]
        while True:
            if cell_value.value not in self.road_to_treasure:
                self.road_to_treasure.append(cell_value.value)
                if cell_value.value == self.next_cell(cell_value).value:
                    self.treasure_value = self.next_cell(cell_value).value
                else:
                    cell_value = self.next_cell(cell_value)
            else:
                if self.treasure_value:
                    print(" ".join(map(str, self.road_to_treasure)))
                else:
                    self.message = "This map has not treasure"
                    print("This map has not treasure")
                return self.road_to_treasure
