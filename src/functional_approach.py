import os
import sys
from typing import List

sys.path.append(os.path.abspath(__file__ + "../../.."))

from src.utils import open_file, next_game, validate


def treasure_map_from_file(lines):
    """Creating treasure map as list 5 by 5 from file"""
    treasure_map = []
    for line in lines:
        line = line.split()
        row = list(map(int, line))
        if validate(row):
            treasure_map.append(row)
        else:
            return False
    return treasure_map


def treasure_map_from_keyboard():
    """Creating treasure map as list 5 by 5 from keyboard"""
    treasure_map = []
    while len(treasure_map) < 5:
        line = input()
        line = line.strip().split()
        row = list(map(int, line))
        if validate(row):
            treasure_map.append(row)
    return treasure_map


road_to_treasure = []


def find_treasure(table: List[List[int]], x: int = 0, y: int = 0):
    """Finding cell which contains treasure"""
    cell_value: int = table[x][y]
    coordinates: int = (x + 1) * 10 + y + 1
    if cell_value == coordinates:
        print(" ".join(map(str, road_to_treasure)))
        del road_to_treasure[:]
    elif len(road_to_treasure) > 25:
        print("This map has not treasure")
        del road_to_treasure[:]
    else:
        x: int = cell_value // 10 - 1
        y: int = cell_value % 10 - 1
        road_to_treasure.append(cell_value)
        find_treasure(table, x, y)


if __name__ == '__main__':
    while True:
        first_step = input("how do you want to give map me? File(1) or Keyboard(2)? ")
        if first_step == "1":
            print("Please provide me the path to the file ")
            fl_name = sys.stdin.readline().strip()
            rows = open_file(fl_name)
            treasure_road = treasure_map_from_file(rows)
            if not treasure_road:
                input("Error: your file has incorrect values")
            else:
                find_treasure(treasure_road)

        elif first_step == "2":
            print("Please enter 25 numbers (each of them should be between 11 and 55) ")
            treasure_road = treasure_map_from_keyboard()
            find_treasure(treasure_road)
        if not next_game():
            break
