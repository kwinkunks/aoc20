"""
Advent of Code 2020
Day 7
"""
import networkx as nx
import re


def flatten(l: list) -> list:
    f = []
    for row in l:
        for i in row:
            f.append(i)
    return f


def get_data(fname: str) -> dict:
    """
    Read the data file into a dict.
    """
    pattern = re.compile(r'(\d) (\w+ \w+) bag')
    data = {}
    with open(fname) as f:
        for line in f:
            bag = ' '.join(line.split()[:2])
            contains = pattern.findall(line)
            contains = [int(n) * [c] for n, c in contains]  # Gross but it works :) 
            data[bag] = flatten(contains)
    return data


def build_graph(data: dict) -> nx.DiGraph:
    """Build a DAG from the Frankendata."""
    G = nx.DiGraph()
    for src, tgts in data.items():
        for tgt in set(tgts):
            G.add_edge(src, tgt)
    return G


def part1(fname: str) -> int:
    """Part 1.

    Tests
    >>> part1("./data/day07_test.txt")
    4
    """
    G = build_graph(get_data(fname))
    return len(nx.algorithms.ancestors(G, 'shiny gold'))


def part2(fname: str) -> int:
    """Part 2.

    Mutate the iterable during iteration, LOLZ.

    Tests
    >>> part2("./data/day07_test.txt")
    32
    >>> part2("./data/day07_test2.txt")
    126
    """
    data = get_data(fname)
    bags = data['shiny gold']
    for bag in bags:
        bags.extend(data.get(bag, []))
    return len(bags)


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day07.txt"
    print(f"Part 1: {part1(fname)}")
    print(f"Part 2: {part2(fname)}")
