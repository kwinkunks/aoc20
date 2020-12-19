"""
Advent of Code 2020
Day 18

This is... I don't know what this is...
"""
from typing import Callable


def get_data(fname: str) -> list:
    """
    Read the data file into dicts.
    """
    with open(fname) as f:
        return [line.strip() for line in f]


def simple(expr: str) -> int:
    """Evaluate a simple expression with no parens.

    >>> simple("3 + 4 * 5")
    35
    >>> simple("1 + 2 * 3 + 4 * 5 + 6")
    71
    """
    # Split into bits then get out if we're done.
    bits = expr.split()
    if len(bits) == 1:
        return int(expr)

    # Evaluate the first three bits.
    a, op, b = bits[:3]
    if op == '+':
        x = int(a) + int(b)
    else:
        x = int(a) * int(b)
    
    # Make a new expression and recurse.
    new_expr = ' '.join([str(x)] + bits[3:])
    return simple(new_expr)


def chunked(L, n=3):
    """Give length n chunks of L."""
    for i in range(0, len(L), n):
        yield L[i:i + n]


def simplex(expr: str) -> int:
    """Evaluate a simple expression with no parens.

    >>> simplex("3 + 4 * 5")
    35
    >>> simplex("1 + 2 * 3 + 4 * 5 + 6")
    231
    """
    # Split into bits then get out if we're done.
    bits = expr.split()
    if (len(bits) <= 3) or ('+' not in expr):
        return simple(expr)

    # Aargh, wtf.
    bits.extend(['+', '0'])

    # Evaluate the chunks of 3 bits IFF it's an add.
    new_expr, skips, count = "", 0, 0
    for (a, op, b) in zip(bits, bits[1:], bits[2:]):
        if skips:
            skips -= 1
            continue
        elif (op == '+') and (not count):
            count, skips = 1, 2
            a = int(a) + int(b)
        new_expr += f" {a} "

    return simplex(new_expr)


def evaluate(expr: str, func: Callable[[str], int]) -> int:
    """
    >>> evaluate("1 + (2 * 3) + (4 * (5 + 6))", simple)
    51
    """
    # If we're out of parens then we're done.
    if ('(' not in expr):
        return func(expr)

    # Otherwise find the parenthesis depth.
    depths, d, last = [], 0, 0
    for char in expr:
        d += 1 if char=='(' else -1 if char==')' else 0
        if last - d == 1:
            depths.append(d+1)
        else:
            depths.append(d)
        last = d

    # Break up the expression to find the innermost parentheses.
    before, inner, after = "", "", ""
    captured = False
    for d, char in zip(depths, expr):
        if d == max(depths) and not captured:
            inner += char
        elif inner and d <= max(depths):
            captured = True
            after += char
        else:
            before += char

    # Delete the parens and replace the innermost with its result.
    inner = inner.replace('(', '').replace(')', '')
    val = func(inner) if inner else ""
    new_expr = before + str(val) + after

    return evaluate(new_expr, func=func)

def part1(fname: str) -> int:
    """Part 1.

    Tests
    >>> part1("./data/day18_test.txt")
    585
    """
    return sum(evaluate(expr, simple) for expr in get_data(fname))

def part2(fname: str) -> int:
    """Part 2.

    Tests
    >>> part2("./data/day18_test.txt")
    1773
    """
    return sum(evaluate(expr, simplex) for expr in get_data(fname))


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day18.txt"
    print(f"Part 1 sum: {part1(fname)}")
    print(f"Part 2 sum: {part2(fname)}")
