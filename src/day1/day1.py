import re


def sum_numbers(document: str) -> int:
    """Return the sum of the numbers hidden in the lines of text in <document>

    Read lines of text, and for each line, pull the two digits to make a two-digit number.
    Return the sum of these numbers.
    """
    running_sum = 0
    for line in document.split("\n"):
        if not line:
            continue
        numbers = re.findall(r"\d", line)
        if not numbers:
            raise ValueError(f"no numbers found in line {line}")
        number = int(numbers[0]) * 10 + int(numbers[-1])
        running_sum += number
    return running_sum


def sum_numbers_and_words(document):
    """Return the sum of the numbers hidden in the lines of text in <document>, including
        spelled-out numbers e.g. 'one', 'two', ... 'nine'.

    Read lines of text, and for each line, pull the two digits to make a two-digit number.
    Return the sum of these numbers.
    """
    digit_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    digits = list(digit_map.keys()) + [r"\d"]
    running_sum = 0
    for line in document.split("\n"):
        if not line:
            continue
        # need to use the lookahead to catch overlapping matches
        # e.g "twone" should return two and one
        reg_pattern = "|".join(digits)
        numbers = re.findall(rf"(?=({reg_pattern}))", line)
        if not numbers:
            raise ValueError(f"no numbers found in line {line}")
        first_number = int(numbers[0]) if numbers[0].isnumeric() else digit_map[numbers[0]]
        second_number = int(numbers[-1]) if numbers[-1].isnumeric() else digit_map[numbers[-1]]
        number = first_number * 10 + second_number
        running_sum += number
    return running_sum


test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


part_two_test_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

assert sum_numbers(test_input) == 142
assert sum_numbers_and_words(part_two_test_input) == 281


if __name__ == "__main__":
    with open("input.txt") as flines:
        input = flines.read()

    print("part one:", sum_numbers(input))
    print("part two:", sum_numbers_and_words(input))
