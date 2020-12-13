"""
Advent of Code 2020
Day 13
"""


def get_data(fname: str):
    """
    Read the data file into dicts.
    """
    with open(fname) as f:
        t = int(f.readline())
        text = f.readline().split(',')
    data = [int(e) if e != 'x' else e for e in text]
    return t, data


def argmin(l):
    """
    >>> argmin([9,9,9,1,9])
    3
    """
    mini = 0
    for i, e in enumerate(l):
        mini = i if e < l[mini] else mini
    return mini


def part1(fname: str):
    """Part 1.

    Tests
    >>> part1("./data/day13_test.txt")
    295
    """
    t, buses = get_data(fname)
    buses = list(filter(lambda x: x != 'x', buses))
    nexts = [b - (t % b) for b in buses]
    return min(nexts) * buses[argmin(nexts)]


def extended_euclid(a: int, b: int):
    """
    >>> extended_euclid(10, 6)
    (-1, 2)
    """
    if b == 0:
        return (1, 0)
    x, y = extended_euclid(b, a % b)
    return y, x - (a // b) * y


def crt(r1: int, m1: int, r2: int, m2: int):
    """
    Chinese remainder theorem.

    What is the smallest number such that when we divide
    it by m1 and m2 we get remainders r1 and r2 respectively?

    Tests (checked on Wolfram Alpha)
    >>> crt(102, 221, 16, 19)
    (3417, 4199)
    """
    x, y = extended_euclid(m1, m2)
    m, n = m1 * m2, r2 * x * m1 + r1 * y * m2
    return (n % m + m) % m, m1 * m2


def part2(fname: str):
    """Part 2.

    Tests
    >>> part2("./data/day13_test.txt")
    1068781
    """
    _, buses = get_data(fname)

    schedule = [(bus-i, bus) for i, bus in enumerate(buses) if bus != 'x']

    mod, t = schedule[0]
    for r, bus in schedule[1:]:
        t, mod = crt(t, mod, r, bus)
    return t


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day13.txt"
    print(f"Part 1 product: {part1(fname)}")
    print(f"Part 2 timestamp: {part2(fname)}")
