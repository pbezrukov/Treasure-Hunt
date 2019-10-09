import os
import sys
from unittest.mock import patch

import pytest

sys.path.append(os.path.abspath(__file__ + "../../.."))

from src.functional_approach import treasure_map_from_file, treasure_map_from_keyboard, find_treasure
from src.utils import validate

INPUT_WITH_TREASURE = [[34, 21, 32, 41, 25],
                       [14, 42, 43, 14, 31],
                       [54, 45, 52, 42, 23],
                       [33, 15, 51, 31, 35],
                       [21, 52, 33, 13, 23]
                       ]

INPUT_WITHOUT_TREASURE = [[34, 21, 32, 41, 25],
                          [14, 42, 43, 14, 31],
                          [54, 45, 52, 42, 23],
                          [33, 15, 51, 31, 35],
                          [21, 22, 33, 13, 23]
                          ]

OUTPUT_TREASURE = '34 42 15 25 31 54 13 32 45 35 23 43 51 21 14 41 33 52\n'

OUTPUT_MESSAGE = 'This map has not treasure\n'

ERROR_MESSAGE = 'Please, format should be five rows of five numbers between 11 and 55\n'

FILE = ['22 33 44 22 44',
        '22 33 44 22 44',
        '22 33 44 22 44',
        '22 33 44 22 44',
        '22 33 44 22 44']

EXAMPLE_TREASURE_MAP = [[22, 33, 44, 22, 44],
                        [22, 33, 44, 22, 44],
                        [22, 33, 44, 22, 44],
                        [22, 33, 44, 22, 44],
                        [22, 33, 44, 22, 44]]


def test_from_file():
    assert treasure_map_from_file(FILE) == EXAMPLE_TREASURE_MAP


def test_from_keyboard():
    with patch('builtins.input', side_effect=FILE):
        a = treasure_map_from_keyboard()
    assert a == EXAMPLE_TREASURE_MAP


@pytest.mark.parametrize("test_input,expected",
                         [(INPUT_WITH_TREASURE, OUTPUT_TREASURE), (INPUT_WITHOUT_TREASURE, OUTPUT_MESSAGE)])
def test_find_treasure(capsys, test_input, expected):
    find_treasure(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("test_input,expected", [([11, 33, 15, 54, 22], True), ([11, 55, 22, 11, 43], True)])
def test_validate(test_input, expected):
    assert validate(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [([22, 11], ERROR_MESSAGE), ([22, 11, 44, 22, 89], ERROR_MESSAGE)])
def test_validate_negative(capsys, test_input, expected):
    validate(test_input)
    captured = capsys.readouterr()
    assert captured.out == ERROR_MESSAGE
