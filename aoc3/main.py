# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections
import sys





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = 'input.txt'
    bit_number = 5 if filename == 'test.txt' else 12
    bits = []
    binary_gamma_rate = []
    binary_epsilon_rate = []
    for index in range (0,bit_number):
        bits.append([])
    with open(filename) as input_file:
        for line in input_file:
            for index in range(0, bit_number):
                bits[index].append(line[index])

        for position in bits:
            most_common = collections.Counter(position).most_common((1))[0][0]
            binary_gamma_rate.append(most_common)
            binary_epsilon_rate.append('0' if most_common == '1' else '1')

        binary_gamma_rate = ''.join(str(bit) for bit in binary_gamma_rate)
        binary_epsilon_rate = ''.join(str(bit) for bit in binary_epsilon_rate)
        int_gamma_rate = int(str(binary_gamma_rate),2)
        int_epsilon_rate = int(str(binary_epsilon_rate), 2)


        print(int_gamma_rate*int_epsilon_rate)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
