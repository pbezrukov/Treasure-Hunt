import sys
from typing import List


class Map:
    def __init__(self):
        self.grid = [[]]*5
        self.road_to_treasure = []
        self.treasure_value = None

    def from_file(self, file_name):
        """Creating treasure map as list 5 by 5 from file"""
        with open(file_name) as file:
            lines = file.readlines()
            for i in range(5):
                line = lines[i].strip().split()
                row = map(int, line)
                if self.validate(list(row)):
                    self.grid[i] = [Cell(value) for value in row]

    def from_keyboard(self):
        """Creating treasure map as list 5 by 5 from keyboard"""
        counter = 0
        while counter < 5:
            line = sys.stdin.readline()
            line = line.strip().split()
            row = map(int, line)
            if self.validate(list(row)):
                self.grid[counter] = [Cell(value) for value in row]
                counter += 1

    def validate(self, r: List[int]):
        """Check input data"""
        try:
            if len(r) == 5:
                for number in r:
                    if number not in range(11, 56):
                        raise ValueError
            else:
                raise ValueError

        except ValueError:
            print("Please, format should be five rows of five numbers between 11 and 55")
        else:
            return True

    def next_cell(self, cell_value):
        x = Cell(cell_value).coordinates[0]
        y = Cell(cell_value).coordinates[1]
        next_cell_value = self.grid[x][y]
        # coordinates_sum = (x+1)*10 + y + 1
        if next_cell_value == cell_value:
            self.treasure_value = next_cell_value
        return next_cell_value

    def hunt_treasure(self):
        cell_value = self.grid[0][0]
        while True:
            if cell_value not in self.road_to_treasure:
                self.road_to_treasure.append(cell_value)
                cell_value = self.next_cell(cell_value)
            else:
                if self.treasure_value:
                    print("Treasure has found")
                else:
                    print("This map has not treasure")
                return self.road_to_treasure


class Cell:
    def __init__(self, value):
        self.value = value
        self.__x = value // 10 - 1
        self.__y = value % 10 - 1

    @property
    def coordinates(self):
        return self.__x, self.__y


if __name__ == "__main__":
    a = input("enter")
    n = Map()
    file = input("File")
    n.from_file(file)
    n.hunt_treasure()
