"""
Advent of Code 2020
Day 12
"""
import math


def get_data(fname: str) -> list:
    """
    Read the data file into a list.
    """
    with open(fname) as f:
        return [(line[0], int(line[1:])) for line in f]


OPS = {  # Unit vectors.
    'N':  0 - 1j,
    'S':  0 + 1j,
    'E':  1 + 0j,
    'W': -1 + 0j,
}


def rotate(v, deg):
    """Rotate a vector v clockwise by angle deg.
    I guess I could hve used cmath for this (add phase).
    """
    x = v.real * math.cos(math.radians(deg)) - v.imag * math.sin(math.radians(deg))
    y = v.real * math.sin(math.radians(deg)) + v.imag * math.cos(math.radians(deg))
    return complex(round(x, 4), round(y, 4))  # Should deal with non-orthogonal.


def part1(fname: str):
    """Part 1.

    Tests
    >>> part1("./data/day12_test.txt")
    25
    """
    instrx = get_data(fname)    
    pos, face = 0 + 0j, 1
    for op, val in instrx:
        if op == 'F':
            pos += val * face
        elif op == 'R':
            face = rotate(face, val)
        elif op == 'L':
            face = rotate(face, 360 - val)
        else:
            pos += val * OPS[op]
    return int(abs(pos.real) + abs(pos.imag))


def part2(fname: str):
    """Part 2.

    Tests
    >>> part2("./data/day12_test.txt")
    286
    """
    instrx = get_data(fname)
    ship, waypoint = 0+0j, 10-1j
    for op, val in instrx:
        if op == 'F':
            ship += val * waypoint
        elif op == 'R':
            waypoint = rotate(waypoint, val)
        elif op == 'L':
            waypoint = rotate(waypoint, 360 - val)
        else:
            waypoint += val * OPS[op]
    return int(abs(ship.real) + abs(ship.imag))


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day12.txt"
    print(f"Part 1 taxicab distance: {part1(fname)}")
    print(f"Part 2 taxicab distance: {part2(fname)}")
