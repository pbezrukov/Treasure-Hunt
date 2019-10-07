import sys
from typing import List

class Map:
    def __init__(self):
        self.grid = [[]]*5

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
        lines = sys.stdin.readlines()
        for i in range(5):
            line = lines[i].strip().split()
            row = map(int, line)
            if self.validate(list(row)):
                self.grid[i] = [Cell(value) for value in row]

    def validate(self, r: List[int]):
        """Check input data"""
        try:
            if len(r) == 5:
                for number in r:
                    if number not in range(11, 56):
                        raise ValueError

        except ValueError:
            print("Please, format should be five rows of five numbers between 11 and 55")
        else:
            return True


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
    print(n)
