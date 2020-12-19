"""
Advent of Code 2020
Day 18

Refactored to use Python's PEG parser and the AST. Install pegen with pip.

After a lot of reading and experimenting with the various 'stories' and tests
in https://github.com/we-like-parsers/pegen, this seems to work...
"""
from pegen.testutil import parse_string, make_parser
import ast


def get_data(fname: str) -> list:
    """
    Read the data file into a list.
    """
    with open(fname) as f:
        return f.readlines()


def part1(fname: str) -> int:
    """Part 1.

    BAsically we'll just treat + and * the same. It will evaluate left-to-right.

    >>> part1("./data/day18_test.txt")
    585
    """
    grammar = make_parser("""
    start: expr NEWLINE $ { ast.Expression(expr, lineno=1, col_offset=0) }
    expr: ( e=expr '+' t=term { ast.BinOp(e, ast.Add(), t, lineno=e.lineno, col_offset=e.col_offset, end_lineno=t.end_lineno, end_col_offset=t.end_col_offset) }
          | e=expr '*' t=term { ast.BinOp(e, ast.Mult(), t, lineno=e.lineno, col_offset=e.col_offset, end_lineno=t.end_lineno, end_col_offset=t.end_col_offset) }
          | term { term }
          )
    term: '(' expr ')' { expr } | atom { atom }
    atom: n=NUMBER { ast.Constant(value=ast.literal_eval(n.string), lineno=n.start[0], col_offset=n.start[1], end_lineno=n.end[0], end_col_offset=n.end[1]) }"""
    )
    return sum(eval(compile(parse_string(expr, grammar), "", "eval")) for expr in get_data(fname))


def part2(fname: str) -> int:
    """Part 2.

    Reverse the usual precedence by saying that + operates on the 'inner' terms.

    >>> part2("./data/day18_test.txt")
    1773
    """
    grammar = make_parser("""
    start: expr NEWLINE $ { ast.Expression(expr, lineno=1, col_offset=0) }
    expr: ( e=expr '*' t=term { ast.BinOp(e, ast.Mult(), t, lineno=e.lineno, col_offset=e.col_offset, end_lineno=t.end_lineno, end_col_offset=t.end_col_offset) }
          | term { term }
          )
    term: ( t=term '+' o=other { ast.BinOp(t, ast.Add(), o, lineno=t.lineno, col_offset=t.col_offset, end_lineno=o.end_lineno, end_col_offset=o.end_col_offset) }
          | other { other }
          )
    other: '(' expr ')' { expr } | atom { atom }
    atom: n=NUMBER { ast.Constant(value=ast.literal_eval(n.string), lineno=n.start[0], col_offset=n.start[1], end_lineno=n.end[0], end_col_offset=n.end[1]) }"""
    )
    return sum(eval(compile(parse_string(expr, grammar), "", "eval")) for expr in get_data(fname))


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day18.txt"
    print(f"Part 1 sum: {part1(fname)}")
    print(f"Part 2 sum: {part2(fname)}")
