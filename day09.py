"""
Advent of Code 2020
Day 9
"""


def get_data(fname: str) -> list:
    """
    Read the data file into a list.
    """
    with open(fname) as f:
        return [int(line) for line in f]


def part1(fname: str, n: int) -> int:
    """Part 1.

    Tests
    >>> part1("./data/day09_test.txt", n=5)
    127
    """
    data = get_data(fname)
    for i, x in enumerate(data[n:]):
        precursor = data[i:i+n]
        for y in precursor:
            if x - y in precursor:
                break
        else:
            return x


def part2(fname: str, n: int, target: int) -> int:
    """Part 2.

    Again this wants recursion, but again I'm resorting
    to brute force. Check every range, even tiny ones
    that have no chance of adding to the target.

    Tests
    >>> fname = "./data/day09_test.txt"
    >>> part2(fname, n=5, target=part1(fname, n=5))
    62
    """
    data = get_data(fname)
    for i, x in enumerate(data[n:]):
        precursor = data[i:i+n]
        for j in range(2, len(precursor)):
            test = precursor[:j]
            if sum(test) == target:
                return min(test) + max(test)


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day09.txt"
    print(f"Part 1 count any: {part1(fname, n=25)}")
    print(f"Part 2 count all: {part2(fname, n=25, target=part1(fname, n=25))}")
