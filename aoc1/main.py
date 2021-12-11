# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


def num_increments(lines):
    increments = 0
    line = 0
    previous_line = sys.maxsize

    for line in lines:
        if int(line) > previous_line:
            increments += 1
        previous_line = int(line)

    return increments


def compact(lines):
    added_lines = []
    for index, line in enumerate(lines):
        if index + 2 < len(lines):
            added_lines.append(sum(lines[index:(index + 3)]))
        else:
            break
    return added_lines


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    original_list = []
    with open("input.txt") as input_file:
        for line in input_file:
            original_list.append(int(line))
        compacted_lines = compact(original_list)

        print(num_increments(original_list)) #Problem 1
        print(num_increments(compacted_lines)) #Problem 2

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
