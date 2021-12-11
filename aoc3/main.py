# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from array import *
from functools import reduce
from typing import Tuple


def parse_line(raw_line) -> tuple[str, int]:
    parsed_line = raw_line.split(' ')
    return parsed_line[0], int(parsed_line[1])

if __name__ == '__main__':

    with open('input.txt') as input_file: #0,9 -> 2,9

        horizontal_position = 0
        depth = 0

        for line in input_file:
            direction, distance = parse_line(line)
            match direction:
                case 'forward':
                    horizontal_position+=distance
                case 'down':
                    depth+=distance
                case 'up':
                    depth-=distance


        print(horizontal_position*depth)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
