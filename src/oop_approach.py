import sys


class Map:
    """Class of map which maybe contains treasure"""
    def __init__(self):
        """Initialize class objects"""
        self.grid = [[]]*5
        self.road_to_treasure = []
        self.treasure_value = None

    def from_file(self, file_name):
        """Creating treasure map as list 5 by 5 from file"""
        with open(file_name) as file:
            lines = file.readlines()
            for i in range(5):
                line = lines[i].strip().split()
                row = list(map(int, line))
                if self.validate(row):
                    self.grid[i] = [Cell(value) for value in row]
                else:
                    print("Error: your file has incorrect values")
                    return False

    def from_keyboard(self):
        """Creating treasure map as list 5 by 5 from keyboard"""
        counter = 0
        while counter < 5:
            line = sys.stdin.readline()
            line = line.strip().split()
            row = list(map(int, line))
            if self.validate(row):
                self.grid[counter] = [Cell(value) for value in row]
                counter += 1

    @staticmethod
    def validate(r):
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
                    print("This map has not treasure")
                return self.road_to_treasure


class Cell:
    """Class of cells values"""
    def __init__(self, value):
        """Initialize value of cell"""
        self.value = value
        self.__x = value // 10 - 1
        self.__y = value % 10 - 1

    @property
    def coordinates(self):
        """Coordinates of next cell"""
        return self.__x, self.__y


if __name__ == "__main__":
    first_step = input("how do you want to give map me? File(1) or Keyboard(2)? ")
    treasure = Map()
    if first_step == "1":
        print("Please provide me the path to the file ")
        fl_name = sys.stdin.readline().strip()
        if not treasure.from_file(fl_name):
            input("Please for exit press Enter")
        else:
            treasure.from_file(fl_name)
            treasure.hunt_treasure()
    elif first_step == "2":
        print("Please enter 25 numbers (each of them should be between 11 and 55) \n")
        treasure.from_keyboard()
        treasure.hunt_treasure()
