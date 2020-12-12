"""
Advent of Code 2020
Day 10
"""


def get_data(fname: str) -> list:
    """
    Read the data file into dicts.
    """
    with open(fname) as f:
        return [int(line) for line in f]


def part1(fname: str) -> int:
    """Part 1.

    Tests
    >>> part1("./data/day10_test.txt")
    35
    >>> part1("./data/day10_test2.txt")
    220
    """
    data = get_data(fname)
    adapters = [0] + sorted(data) + [max(data) + 3]
    diffs = [b-a for a, b in zip(adapters, adapters[1:])]
    count = {}  # Roll own collections.counter.
    for d in diffs:
        count[d] = count.get(d, 0) + 1
    return count[1] * count[3]


def part2(fname: str) -> int:
    """Part 2.

    Tests
    >>> part2("./data/day10_test.txt")
    8
    >>> part2("./data/day10_test2.txt")
    19208
    """
    data = get_data(fname)
    adapters = [0] + sorted(data) + [max(data) + 3]
    choices = []
    for a, b, c, d in zip(adapters, adapters[1:], adapters[2:], adapters[3:]):
        choices.append(len([x-a for x in [b, c, d] if x-a <= 3]))
    count, pointer = 1, 0
    while pointer < len(choices):
        if choices[pointer] == 3:  # Now it depends...
            if choices[pointer+1] == 3:  
                mult, incr = 7, 3
            else:
                mult, incr = 4, 2
        elif choices[pointer] == 2:  # Double.
            mult, incr = 2, 1
        else:
            mult, incr = 1, 1
        count *= mult
        pointer += incr
    return count


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day10.txt"
    print(f"Part 1 count product: {part1(fname)}")
    print(f"Part 2 total arrangements: {part2(fname)}")
