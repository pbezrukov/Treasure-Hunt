import sys
from typing import List


def validate(r: List[int]):
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


def treasure_map_from_file(file_name):
    """Creating treasure map as list 5 by 5 from file"""
    treasure_map = []
    with open(file_name) as cells:
        for line in cells:
            line = line.strip().split()
            row = list(map(int, line))
            if validate(row):
                treasure_map.append(row)
    return treasure_map


def treasure_map_from_keyboard():
    """Creating treasure map as list 5 by 5 from keyboard"""
    treasure_map = []
    while len(treasure_map) < 5:
        line = sys.stdin.readline()
        line = line.strip().split()
        row = list(map(int, line))
        if validate(row):
            treasure_map.append(row)
    return treasure_map


def find_treasure(table: List[List[int]], x: int = 0, y: int = 0) -> None:
    """Finding cell which contains treasure"""
    cell_value: int = table[x][y]
    coordinates: int = (x+1)*10 + y+1
    if cell_value == coordinates:
        print(cell_value, end=' \n')
    else:
        x: int = cell_value // 10 - 1
        y: int = cell_value % 10 - 1
        print(cell_value, end=' ')
        find_treasure(table, x, y)


if __name__ == '__main__':
    first_step = input("how do you want to give map me? File(1) or Keyboard(2)? ")
    if first_step == "1":
        print("Please provide me the path to the file ")
        file = sys.stdin.readline().strip()
        treasure_road = treasure_map_from_file(file)
    elif first_step == "2":
        print("Please enter 25 numbers (each of them should be between 11 and 55) ")
        treasure_road = treasure_map_from_keyboard()
    find_treasure(treasure_road)
