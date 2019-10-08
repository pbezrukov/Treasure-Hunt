import os
import sys

sys.path.append(os.path.abspath(__file__ + "../../.."))


from src.utils import next_game, open_file
from src.map import Map


if __name__ == "__main__":
    while True:
        first_step = input("How do you want to give map me? File(1) or Keyboard(2)? ")
        treasure = Map()
        if first_step == "1":
            print("Please provide me the path to the file ")
            fl_name = sys.stdin.readline().strip()
            rows = open_file(fl_name)
            treasure.from_file(rows)
            treasure.hunt_treasure()
        elif first_step == "2":
            print("Please enter 25 numbers (each of them should be between 11 and 55) ")
            treasure.from_keyboard()
            treasure.hunt_treasure()
        if not next_game():
            break
