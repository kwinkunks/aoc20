"""
Advent of Code 2020
Day 11
"""
import copy


def get_data(fname: str) -> list:
    """
    Read the data file into dicts.
    """
    with open(fname) as f:
        text = f.read()
    return [list(line) for line in text.split('\n')]


def get_neighbours(world: list, loc: tuple, max_steps: int) -> int:
    """
    Adapted from AoC 2018, Day 18.
    """
    dirs = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
    ns = ['.' for _ in dirs]
    for i, (xi, yi) in enumerate(dirs):
        (x, y), steps = loc, 0
        while ns[i] == '.' and steps < max_steps:
            x, y = x + xi, y + yi
            if (x < 0) or (y < 0) or (x >= len(world[0])) or (y >= len(world)):
                break
            ns[i], steps = world[y][x], steps + 1
    return ns


def play(world: list, max_rounds: int=500, empties: int=4, max_steps: int=1) -> int:
    """
    Also adapted from AoC 2018, Day 18.
    """
    for rnd in range(max_rounds):
        w = copy.deepcopy(world)
        for y, row in enumerate(world):
            for x, e in enumerate(row):
                ns = get_neighbours(world, (x, y), max_steps=max_steps)
                if e == 'L' and ns.count('#') == 0:
                    w[y][x] = '#'
                elif e == '#' and ns.count('#') >= empties:
                    w[y][x] = 'L'
        if all([a==b for a, b in zip(w, world)]):
            return w  # Get out early.
        world = copy.deepcopy(w)
    return None


def part1(fname: str):
    """Part 1.

    Tests
    >>> part1("./data/day11_test.txt")
    37
    """
    stable = play(get_data(fname))
    return sum(row.count('#') for row in stable)


def part2(fname: str):
    """Part 2.

    Tests
    >>> part2("./data/day11_test.txt")
    26
    >>> get_neighbours(get_data("./data/day11_test2.txt"), (3, 4), 1).count('#')
    2
    >>> get_neighbours(get_data("./data/day11_test2.txt"), (3, 4), 10).count('#')
    8
    >>> get_neighbours(get_data("./data/day11_test3.txt"), (3, 3), 1).count('#')
    0
    >>> get_neighbours(get_data("./data/day11_test3.txt"), (3, 3), 10).count('#')
    0
    """
    stable = play(get_data(fname), empties=5, max_steps=1_000_000)
    return sum(row.count('#') for row in stable)


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day11.txt"
    print(f"Part 1 occupied: {part1(fname)}")
    print(f"Part 2 occupied: {part2(fname)}")
