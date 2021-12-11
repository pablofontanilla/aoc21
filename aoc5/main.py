# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from array import *
from functools import reduce


w, h = 1000, 1000
array_map = [[0 for x in range(w)] for y in range(h)]

def get_coords_from_input_line(tuple):
    x1, x2 = tuple[0].split(',')
    y1, y2 = tuple[1].split(',')
    return int(x1), int(x2), int(y1), int(y2)

def hor_or_vert(coords):#0,9 -> 2,9
    x1,x2,y1,y2 = coords
    return x1==y1 or x2==y2

def get_direction(number):
    if number > 0:
        return 1
    if number == 0:
        return 0
    return -1

def get_points_in_line(line_coords):
    x1,y1,x2,y2 = line_coords
    direction_vector = get_direction(x2-x1), get_direction(y2-y1)
    result = []

    while x1 != x2 or y1 != y2:
        result.append((x1,y1))
        x1+=direction_vector[0]
        y1+=direction_vector[1]

    result.append((x2,y2))
    return result


def add_to_map(coords_line):
    for point in coords_line:
        array_map[point[0]][point[1]]+=1




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    floor =[]

    with open('input.txt') as input_file: #0,9 -> 2,9

        for line in input_file:
            data_tuple = line.replace('\n', '').split(' -> ')
            coords = get_coords_from_input_line(data_tuple)
            #if hor_or_vert(coords):
            #    add_to_map(get_points_in_line(coords))
            add_to_map(get_points_in_line(coords))
        total = 0
        for line in array_map:
            for column in line:
                if column > 1:
                    total +=1

        print(total)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
