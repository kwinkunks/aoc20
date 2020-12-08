"""
Advent of Code 2020
Day 6
"""


def get_data(fname: str) -> dict:
    """
    Read the data file into dicts.
    """
    with open(fname) as f:
        return [rec.split() for rec in f.read().split("\n\n")]


def part1(fname: str) -> int:
    """Part 1.

    Tests
    >>> part1("./data/day06_test.txt")
    11
    """
    return sum(len(set(''.join(group))) for group in get_data(fname))


def part2(fname: dict):
    """Part 2.

    Tests
    >>> part2("./data/day06_test.txt")
    6
    """
    return sum(len(set.intersection(*[set(pax) for pax in group])) for group in get_data(fname))


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day06.txt"
    print(f"Part 1 count any: {part1(fname)}")
    print(f"Part 2 count all: {part2(fname)}")
