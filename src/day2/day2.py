"""day2.py

Read a set of game ids + draws of blue, red, green balls, and identify which games are possible given some starting conditions.
"""

from dataclasses import dataclass

@dataclass
class DrawCount:
    """The number of balls drawn during one game. """
    color_count: dict[str, int]

    def __init__(self, draw:str) -> 'DrawCount':
        color_count = {'blue': 0, 'red': 0, 'green': 0}
        for individual_draw in draw.split(','):
            count, color = individual_draw.strip().split(' ')
            color_count[color] += int(count)
        self.color_count = color_count

@dataclass
class Game:
    id: int 
    draws: list[DrawCount]

    def max_balls_drawn(self):
        """Return the maximum of each ball kind."""
        return{color: max(x.color_count[color] for x in self.draws) for color in ['blue', 'red', 'green']}



def parse_input(input: str) -> list[Game]:
    """Read the input of the form Game <X>: <semi-colon separated list of draws>."""
    games = []
    for line in input.split('\n'):
        if not line:
            continue

        game, draws = line.split(':')
        assert game.startswith('Game ')
        game_id = int(game[5:])
        games.append(Game(id=game_id, draws=[DrawCount(draw) for draw in draws.split(';')]))
            
    return games


def get_possible_games(input_str: str, known_maxes: dict[str, int]) -> int:
    """For each game, check against the known cubes we have, and return sum of all possible
        game ids"""
    games = parse_input(input_str)
    valid_ids = []
    for game in games:
        max_balls_drawn = game.max_balls_drawn()
        if all(known_maxes[color] >= max_balls_drawn[color] for color in ['blue', 'red', 'green']):
            valid_ids.append(game.id)
    return sum(valid_ids)

def get_minimum_possible_cubes(input_str: str) -> int:
    """For each game, find the minimum possible number of cubes. Return the sum of the multiple
    of those numbers for each game.s
    """
    games = parse_input(input_str)
    cube_sum = 0
    for game in games:
        max_balls_drawn = game.max_balls_drawn()
        cube_sum += max_balls_drawn['red'] * max_balls_drawn['green'] * max_balls_drawn['blue']
        
    return cube_sum


test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

test_known_maxes = {'red': 12, 'blue': 14, 'green': 13}

assert get_possible_games(test_input, test_known_maxes) == 8
assert get_minimum_possible_cubes(test_input) == 2286


if __name__ == '__main__':

    with open("input.txt") as flines:
        input = flines.read()
    print('part 1: ', get_possible_games(input, test_known_maxes))
    print('part 2: ', get_minimum_possible_cubes(input))