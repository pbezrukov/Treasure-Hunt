import sys
from typing import List


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
        line = sys.stdin.readline().strip().split()
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
        print("Give me the path to the file ")
        file = sys.stdin.readline().strip()
        treasure_road = treasure_map_from_file(file)
        find_treasure(treasure_road)
        input("do you want continue the game?")
    elif first_step == "2":
        print("Enter 25 number (each of them should be between 11 and 55) ")
        treasure_road = treasure_map_from_keyboard()
        find_treasure(treasure_road)
