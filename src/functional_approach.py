import sys
from typing import List

TREASURE_MAP = []


def create_treasure_map_from_file():
    file_name = input("Give me the path to the file ")
    with open(file_name) as cells:
        for line in cells:
            line = line.strip().split()
            TREASURE_MAP.append(list(map(int, line)))
    return TREASURE_MAP


def create_treasure_map_from_keyboard():
    print("Enter 25 number (each of them should be between 11 and 55) ")
    while len(TREASURE_MAP) < 5:
        row = list(map(int, sys.stdin.readline().strip().split()))
        try:
            if len(row) == 5:
                for number in row:
                    if number < 11 or number > 55:
                        raise ValueError


            else:
                raise ValueError
            # print('Each row should contain five numbers')
        except ValueError:
            print("Enter correct number")
        else:
            TREASURE_MAP.append(row)

    return TREASURE_MAP


def treasure(table: List[List[int]], x: int = 0, y: int = 0) -> None:
    value_of_cell: int = table[x][y]
    coordinates: int = (x+1)*10 + y+1

    if value_of_cell == coordinates:
        print(value_of_cell, end=' \n')

    else:
        x: int = value_of_cell // 10 - 1
        y: int = value_of_cell % 10 - 1
        print(value_of_cell, end=' ')
        treasure(table, x, y)


#
#
if __name__ == '__main__':
    first = input("how do you want to give map me? File or Keyboard? ")
    if first == "File":
        create_treasure_map_from_file()
        treasure(TREASURE_MAP)
    elif first == "Keyboard":
        create_treasure_map_from_keyboard()
        treasure(TREASURE_MAP)
