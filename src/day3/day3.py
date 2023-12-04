"""day3.py

Read a set of game ids + draws of blue, red, green balls, and identify which games are possible given some starting conditions.
"""
from ..utils import *


test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def find_part_numbers(input_str :str) -> list:
    """Look for all numbers next to a symbol. Return the sum of these numbers
    
    Next to here includes up, down, or diagonally.
    """


    lines = [line for line in input_str.split() if line]
    # find the indices of the numbers (and the numbers)
    part_numbers = []
    for i, line in enumerate(lines):
        possible_part_number = ""
        indices = []
        for j, char in enumerate(line):
            if char.isnumeric():
                possible_part_number += char
                indices += [(i,j)]
            else:
                if possible_part_number:
                    part_numbers.append((int(possible_part_number), indices))
                indices = []
                possible_part_number = ""
        # handle end-of-line
        if possible_part_number:
            part_numbers.append((int(possible_part_number), indices))

    # for each possible part number, grab the indices. Then look +-1 from them for symbols.

    actual_part_numbers = []
    for part_number, indices in part_numbers:
        i = indices[0][0]
        assert all(x[0] == i for x in indices)
        j_start = indices[0][1]
        j_end = indices[-1][1]

        # look for symbols (i'm sure this could be prettier)
        for j in range(j_start-1, j_end+2):
            if j < 0 or j >= len(lines[0]):
                 continue 
            
            if j == j_start-1 or j == j_end+1:
                if not (i < 0 or i >= len(lines)):
                    char_side = lines[i][j]
                    if not char_side.isnumeric() and char_side != '.':
                        actual_part_numbers.append(part_number)
                        break

            if not (i-1 < 0 or i-1 >= len(lines)):
                char_above = lines[i-1][j]
                if not char_above.isnumeric() and char_above != '.':
                        actual_part_numbers.append(part_number)
                        break
                
            if not (i+1 < 0 or i+1 >= len(lines)):
                char_below = lines[i+1][j]
                if not char_below.isnumeric() and char_below != '.':
                        actual_part_numbers.append(part_number)
                        break

    return actual_part_numbers

def sum_part_numbers(input_str: str) -> int:
    return sum(find_part_numbers(input_str))

def sum_gear_ratios(input_str :str) -> int:
    """Look for all gears (marked by *) next to two part numbers. Sum the product of the two part numbers
    for each gear.

    Repeating lots of code from sum_part_numbers for speed. 
    """
    lines = [line for line in input_str.split() if line]
    # find the indices of the numbers (and the numbers)
    part_numbers = []
    for i, line in enumerate(lines):
        possible_part_number = ""
        indices = []
        for j, char in enumerate(line):
            if char.isnumeric():
                possible_part_number += char
                indices += [(i,j)]
            else:
                if possible_part_number:
                    part_numbers.append((int(possible_part_number), indices))
                indices = []
                possible_part_number = ""
        # handle end-of-line
        if possible_part_number:
            part_numbers.append((int(possible_part_number), indices))

    # generate a list of possible gear locations. Then check the possible part numbers
    # against the list of known part numbers. If there are two, then that's a gear.
    gears = {}
    for part_number, indices in part_numbers:
        i = indices[0][0]
        assert all(x[0] == i for x in indices)
        j_start = indices[0][1]
        j_end = indices[-1][1]

        # look for symbols (i'm sure this could be prettier)
        for j in range(j_start-1, j_end+2):
            if j < 0 or j >= len(lines[0]):
                 continue 
            
            if j == j_start-1 or j == j_end+1:
                if not (i < 0 or i >= len(lines)):
                    char_side = lines[i][j]
                    if char_side == '*':
                        gears[(i, j)] = gears.get((i,j), []) + [part_number]

            if not (i-1 < 0 or i-1 >= len(lines)):
                char_above = lines[i-1][j]
                if char_above == '*':
                    gears[(i-1, j)] = gears.get((i-1,j), []) + [part_number]

                
            if not (i+1 < 0 or i+1 >= len(lines)):
                char_below = lines[i+1][j]
                if char_below == '*':
                    gears[(i+1, j)] = gears.get((i+1,j), []) + [part_number]

    actual_part_numbers = set(find_part_numbers(input_str))
    
    gear_ratio_sum = 0 
    for parts in gears.values():
        actual_parts = [x for x in parts if x in actual_part_numbers]
        if len(actual_parts) == 2:
            gear_ratio_sum += actual_parts[0] * actual_parts[1]

    return gear_ratio_sum

assert sum_part_numbers(test_input) == 4361
assert sum_gear_ratios(test_input) == 467835

if __name__ == '__main__':
    input = read_input()
    print('part 1: ', sum_part_numbers(input))
    print('part 2: ', sum_gear_ratios(input))
