# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections


def calculate_binary_oxygen_criteria(column,bit_position):

    frequency = collections.Counter(column).most_common(2)
    if frequency[0][1] == frequency[1][1]:
        most_common = '1'
    else:
        most_common = frequency[0][0]
    return most_common


def calculate_binary_co2_criteria(candidates,bit_position):

    criteria = '0' if calculate_binary_oxygen_criteria(candidates,bit_position) == '1' else '1'
    return criteria


def get_column(full_input,position):
    result = [item[position] for item in full_input]
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = 'input.txt'
    bit_number = 5 if filename == 'test.txt' else 12
    bits = []
    binary_oxygen_criteria = []
    binary_co2_criteria = []
    oxygen_rate_candidates = []
    co2_rate_candidates = []
    oxygen_rate = '0'
    co2_rate = '0'
    for index in range (0,bit_number):
        bits.append([])
    with open(filename) as input_file:
        #Fill initial candidates
        for line in input_file:
            clean_line = line.strip('\n')
            oxygen_rate_candidates.append(clean_line)
            co2_rate_candidates.append(clean_line)


        #calculate oxygen rate
        next_oxygen_rate_candidates = []

        for index in range (0,bit_number):
            candidates = get_column(oxygen_rate_candidates,index)
            oxygen_criteria_bit = calculate_binary_oxygen_criteria(candidates,index)
            for candidate in oxygen_rate_candidates:
                candidate_bit = candidate[index]
                if candidate_bit == oxygen_criteria_bit:
                    next_oxygen_rate_candidates.append(candidate)
            oxygen_rate_candidates = next_oxygen_rate_candidates
            next_oxygen_rate_candidates = []
            if len(oxygen_rate_candidates) == 1:
                oxygen_rate = oxygen_rate_candidates[0]
                break

        # co2 index
        next_co2_rate_candidates = []
        for index in range(0, bit_number):
            candidates = get_column(co2_rate_candidates, index)
            co2_criteria_bit = calculate_binary_co2_criteria(candidates, index)
            for candidate in co2_rate_candidates:
                candidate_bit = candidate[index]
                if candidate_bit == co2_criteria_bit:
                    next_co2_rate_candidates.append(candidate)
            co2_rate_candidates = next_co2_rate_candidates
            next_co2_rate_candidates = []
            if len(co2_rate_candidates) == 1:
                co2_rate = co2_rate_candidates[0]
                break
        print(int(str(co2_rate),2)*int(str(oxygen_rate),2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
