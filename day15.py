"""
Advent of Code 2020
Day 15
"""

def play(data: list, turns: int):
    """
    Play the game.
    """
    # Start the game.
    previous = {}  # No comp so speak exists.
    for turn, speak in enumerate(data, 1):
        previous[speak] = turn

    # Take 4th turn. A bit annoying.
    spoke = 0
    turn += 1

    # Carry on...
    for turn in range(turn, turns):
        speak = (turn - previous[spoke]) if spoke in previous else 0
        previous[spoke] = turn
        spoke = speak

    return speak


def part1(data: list) -> int:
    """Part 1.

    Tests
    >>> part1([0,3,6])
    436
    >>> part1([1,3,2])
    1
    """
    return play(data, turns=2020)


def part2(data: str) -> int:
    """Part 2.

    Tests
    >>> part2([0,3,6])
    175594
    """
    return play(data, turns=30_000_000)


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    START = [12,20,0,6,1,17,7]

    print(f"Part 1: {part1(START)}")
    print(f"Part 2 count all: {part2(START)}")
