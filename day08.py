"""
Advent of Code 2020
Day 8
"""


def get_data(fname: str) -> list:
    """
    Read the data file into a list of tuples.
    """
    with open(fname) as f:
        parse = lambda s: (s.split()[0], int(s.split()[1]))
        return [parse(rec) for rec in f.read().split("\n")]

OPS = {'acc': 1, 'nop': 1}

def part1(fname: str) -> int:
    """Part 1.

    Tests
    >>> part1("./data/day08_test.txt")
    5
    """
    instrx = get_data(fname)
    exec = [0 for _ in instrx]
    pointer, accumulator = 0, 0
    while exec[pointer] < 1:
        op, value = instrx[pointer]
        accumulator += value if op == 'acc' else 0
        exec[pointer] += 1
        pointer += OPS.get(op, value)
    return accumulator


def part2(fname: dict):
    """Part 2.

    Just check what happens if flip every location.

    Tests
    >>> part2("./data/day08_test.txt")
    8
    """
    instrx = get_data(fname)
    for p in [i for i, e in enumerate(instrx) if e[0] != 'acc']:
        exec = [0 for _ in instrx]
        pointer, accumulator = 0, 0
        while pointer < len(instrx):
            if max(exec) > 2: break
            op, value = instrx[pointer]
            if pointer == p:
                op = {'nop': 'jmp', 'jmp': 'nop'}.get(op)
            accumulator += value if op == 'acc' else 0
            exec[pointer] += 1
            pointer += OPS.get(op, value)
        else:
            return accumulator


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day08.txt"
    print(f"Part 1 accumulator: {part1(fname)}")
    print(f"Part 2 accumulator: {part2(fname)}")
