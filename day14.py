"""
Advent of Code 2020
Day 14
"""


def get_data(fname: str):
    """
    Read the data file into a list.
    """
    with open(fname) as f:
        data = []
        for line in f:
            m, v = line.split(' = ')
            if m == 'mask':
                mask = v.strip()
                continue
            l = int(m[m.find('[')+1:m.find(']')])
            loc = bin(int(l))[2:].zfill(36)
            val = bin(int(v))[2:].zfill(36)
            data.append((mask, loc, val))
        return data

def part1(fname: str):
    """Part 1.

    Tests
    >>> part1("./data/day14_test.txt")
    165
    """
    instrx = get_data(fname)
    memory = {}
    for mask, loc, val in instrx:
        new_val = ''.join(m if m!='X' else l for m, l in zip(mask, val))
        memory[loc] = int(new_val, 2)
    return sum(memory.values())


def part2(fname: str):
    """Part 2.

    Tests
    >>> part2("./data/day14_test2.txt")
    208
    """
    instrx = get_data(fname)
    new_instrx = []
    for mask, loc, val in instrx:
        loc_ = list(loc)
        for i, (m, l) in enumerate(zip(mask, loc)):
            if m == '0':
                loc_[i] = l
            elif m == '1':
                loc_[i] = '1'
            else:
                loc_[i] = 'X'
        new_instrx.append((loc_, val))

    memory = {}
    for loc, val in new_instrx:
        m = loc.count('X')
        repls = [list(bin(x)[2:].zfill(m)) for x in range(2**m)]
        for repl in repls:
            loc_ = ''.join(repl.pop() if l=='X' else l for l in loc)
            memory[int(loc_, 2)] = int(val, 2)

    return sum(memory.values())


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day14.txt"
    print(f"Part 1 v1 sum: {part1(fname)}")
    print(f"Part 2 v2 sum: {part2(fname)}")
