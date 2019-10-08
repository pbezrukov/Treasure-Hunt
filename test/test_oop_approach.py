import os
import sys
from unittest.mock import patch

sys.path.append(os.path.abspath(__file__ + "../../.."))
from src.map import Map

INPUT_WITH_TREASURE = ['34 21 32 41 25',
                       '14 42 43 14 31',
                       '54 45 52 42 23',
                       '33 15 51 31 35',
                       '21 52 33 13 23'
                       ]


OUTPUT_TREASURE = [34, 42, 15, 25, 31, 54, 13, 32, 45, 35, 23, 43, 51, 21, 14, 41, 33, 52]


INPUT_WITHOUT_TREASURE = ['34 21 32 41 25',
                          '14 42 43 14 31',
                          '54 45 52 42 23',
                          '33 15 51 31 35',
                          '21 22 33 13 23']


OUTPUT_MESSAGE = 'This map has not treasure\n'


FILE = ['22 33 44 22 44',
        '22 33 44 22 44',
        '22 33 44 22 44',
        '22 33 44 22 44',
        '22 33 44 22 44']


def test_from_file_oop():
    maps = Map()
    maps.from_file(FILE)
    for i in range(5):
        assert len(maps.grid[i]) == 5


def test_from_keyboard_oop():
    maps = Map()
    with patch('builtins.input', side_effect=FILE):
        maps.from_keyboard()
    for i in range(5):
        assert len(maps.grid[i]) == 5


def test_hunt_treasure_oop():
    maps = Map()
    with patch('builtins.input', side_effect=INPUT_WITH_TREASURE):
        maps.from_keyboard()
    maps.hunt_treasure()
    assert maps.hunt_treasure() == OUTPUT_TREASURE


def test_hunt_treasure_oop_negative():
    maps = Map()
    with patch('builtins.input', side_effect=INPUT_WITHOUT_TREASURE):
        maps.from_keyboard()
    maps.hunt_treasure()
    assert maps.message == "This map has not treasure"
