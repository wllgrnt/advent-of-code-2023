"""day4.py"""
from ..utils import *


def count_scratchcard_wins(input_str: str) -> int:
    """
    Given newline-separated cards of the form:

        Card <x>: <winning numbers> | <your numbers>

    Find how many matches you have, then your score is 2^(num_matches-1)

    Returns:
        The sum of all wins:
    """
    sum_scores = 0
    for line in input_str.split("\n"):
        if not line:
            continue
        _, numbers = line.split(":")
        winning_numbers, your_numbers = numbers.split("|")
        winning_numbers = set(int(x.strip()) for x in winning_numbers.split())
        your_numbers = set(int(x.strip()) for x in your_numbers.split())
        num_matches = sum(x in winning_numbers for x in your_numbers)
        if num_matches > 0:
            score = 2 ** (num_matches - 1)
        else:
            score = 0
        sum_scores += score
    return sum_scores


def count_scratchcard_copies(input_str: str) -> int:
    """
    Given newline-separated cards of the form:

        Card <x>: <winning numbers> | <your numbers>

    Find how many matches you have. Then you receive a copy of the <num_matches>
    cards below. (i.e if you have 3 matches on card 1 you get a copy of 2,3,4.)
    Returns:
        The total number of scratchcards.
    """
    num_scratchcards = {}
    for line in input_str.split("\n"):
        if not line:
            continue
        card, numbers = line.split(":")
        card_no = int(card.split()[-1])
        num_scratchcards[card_no] = num_scratchcards.get(card_no, 0) + 1
        winning_numbers, your_numbers = numbers.split("|")
        winning_numbers = set(int(x.strip()) for x in winning_numbers.split())
        your_numbers = set(int(x.strip()) for x in your_numbers.split())
        num_matches = sum(x in winning_numbers for x in your_numbers)

        for i in range(num_matches):
            # add copies to the scratchcards below.
            # if we have e.g 5 copies of our current card, then the increment is 5 since the
            # process runs for all copies.
            num_scratchcards[card_no + i + 1] = (
                num_scratchcards.get(card_no + i + 1, 0) + num_scratchcards[card_no]
            )

    return sum(num_scratchcards.values())


test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


assert count_scratchcard_wins(test_input) == 13
assert count_scratchcard_copies(test_input) == 30

if __name__ == "__main__":
    input = read_input()
    print("part 1: ", count_scratchcard_wins(input))
    print("part 2: ", count_scratchcard_copies(input))
