"""
Advent of Code 2020
Day 18

Refactored to use Python's PEG parser, `pegen` and the AST.

You will need to install pegen; ast is standard library.

This is awesome.
"""
from pegen.testutil import parse_string, make_parser
import ast


def get_data(fname: str) -> list:
    """
    Read the data file into a list.
    """
    with open(fname) as f:
        return [line.strip() for line in f]


def part1(fname: str) -> int:
    """Part 1.

    Define a grammar with { actions }.

    Tests
    >>> part1("./data/day18_test.txt")
    585
    """
    grammar = make_parser("""
    start: expr NEWLINE $ { ast.Expression(expr, lineno=1, col_offset=0) }
    expr: ( expr '+' term { ast.BinOp(expr, ast.Add(), term, lineno=expr.lineno, col_offset=expr.col_offset, end_lineno=term.end_lineno, end_col_offset=term.end_col_offset) }
          | expr '*' term { ast.BinOp(expr, ast.Mult(), term, lineno=expr.lineno, col_offset=expr.col_offset, end_lineno=term.end_lineno, end_col_offset=term.end_col_offset) }
          | term { term }
          )
    term: ( '(' expr ')' { expr }
            | atom { atom }
            )
    atom: ( n=NUMBER { ast.Constant(value=ast.literal_eval(n.string), lineno=n.start[0], col_offset=n.start[1], end_lineno=n.end[0], end_col_offset=n.end[1]) }
          )""")
    return sum(eval(compile(parse_string(expr, grammar), "", "eval")) for expr in get_data(fname))


def part2(fname: str) -> int:
    """Part 2.

    Tests
    >>> part2("./data/day18_test.txt")
    1773
    """
    grammar = make_parser("""
    start: expr NEWLINE $ { ast.Expression(expr, lineno=1, col_offset=0) }
    expr: ( expr '*' term { ast.BinOp(expr, ast.Mult(), term, lineno=expr.lineno, col_offset=expr.col_offset, end_lineno=term.end_lineno, end_col_offset=term.end_col_offset) }
          | term { term }
          )
    term: ( l=term '+' r=other { ast.BinOp(l, ast.Add(), r, lineno=l.lineno, col_offset=l.col_offset, end_lineno=r.end_lineno, end_col_offset=r.end_col_offset) }
          | other { other }
          )
    other: ( '(' expr ')' { expr }
            | atom { atom }
            )
    atom: ( n=NUMBER { ast.Constant(value=ast.literal_eval(n.string), lineno=n.start[0], col_offset=n.start[1], end_lineno=n.end[0], end_col_offset=n.end[1]) }
          )""")
    return sum(eval(compile(parse_string(expr, grammar), "", "eval")) for expr in get_data(fname))


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day18.txt"
    print(f"Part 1 sum: {part1(fname)}")
    print(f"Part 2 sum: {part2(fname)}")
