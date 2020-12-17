"""
Advent of Code 2020
Day 17
"""
from typing import List, Tuple, Set

def get_data(fname: str, dims: int) -> set:
    """
    Read the data file into dicts.
    """
    with open(fname) as f:
        coords = set()
        for y, line in enumerate(f):
            for x, char in enumerate(line):
                if char == '#':
                    coord = (x, y, 0)
                    if dims == 4:
                        coord = coord + (0,)
                    coords.add(coord)
    return coords


def get_offsets(dims: int) -> Set[tuple]:
    """
    Generate the neighbour offsets. This is pretty gross but
    we only do it once.

    >>> len(get_offsets(3)) == 26
    True
    """
    offs = [-1, 0, 1]
    neighbours_3d, neighbours_4d = set(), set()
    for x in offs:
        for y in offs:
            for z in offs:
                if (x, y, z) != (0, 0, 0):
                    neighbours_3d.add((x, y, z))
                for omega in offs:
                    if (x, y, z, omega) != (0, 0, 0, 0):
                        neighbours_4d.add((x, y, z, omega))
    if dims == 3: return neighbours_3d
    if dims == 4: return neighbours_4d


def get_neighbours(p: Tuple[int], offsets: List[tuple]) -> Set[tuple]:
    """
    Get all of the neighbours of a point.
    """
    ns = set()
    for offset in offsets:
        n = []
        for dim in range(len(p)):
            n.append((p[dim]+offset[dim]))
        ns.add(tuple(n))
    return ns


def cycling(active: Set[tuple], offsets: List[tuple]) -> Set[tuple]:
    """
    Do the cycles. Checking the inactive points is
    a challenge... would be much easier with a
    sparse matrix.
    """
    for cycle in range(6):

        # Figure out what to activate.
        activate, superset = set(), set()
        for p in active:
            a = 0
            for n in get_neighbours(p, offsets):
                a += 1 if n in active else 0
                superset = superset.union(get_neighbours(n, offsets))
            if a in [2, 3]:
                activate.add(p)
        
        # Visit all inactive points as well, pfff.
        inactive = superset - active
        for q in inactive:
            a = 0
            for n in get_neighbours(q, offsets):
                a += 1 if n in active else 0
            if a == 3:
                activate.add(q)

        active = activate

    return active


def part1(fname: str) -> int:
    """Part 1.

    Tests
    >>> part1("./data/day17_test.txt")
    112
    """
    active = get_data(fname, dims=3)
    return len(cycling(active, get_offsets(dims=3)))


def part2(fname: str) -> int:
    """Part 2.

    Tests
    >>> part2("./data/day17_test.txt")
    848
    """
    active = get_data(fname, dims=4)
    return len(cycling(active, get_offsets(dims=4)))


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day17.txt"
    print(f"Part 1 3D active: {part1(fname)}")
    print(f"Part 2 4D active: {part2(fname)}")
