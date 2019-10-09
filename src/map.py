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

    def next_cell(self, cell):
        """Finding next cell in map"""
        x, y = cell.coordinates
        next_cell = self.grid[x][y]
        return next_cell

    def hunt_treasure(self):
        """Finding treasure"""
        cell = self.grid[0][0]
        while True:
            if cell.value not in self.road_to_treasure:
                self.road_to_treasure.append(cell.value)
                if cell.value == self.next_cell(cell).value:
                    self.treasure_value = self.next_cell(cell).value
                else:
                    cell = self.next_cell(cell)
            else:
                if self.treasure_value:
                    print(" ".join(map(str, self.road_to_treasure)))
                else:
                    self.message = "This map has not treasure"
                    print("This map has not treasure")
                return self.road_to_treasure
