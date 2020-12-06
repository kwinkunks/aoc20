"""
Advent of Code 2020
Day 4
"""


def get_data(fname: str) -> dict:
    """
    Read the data file into dicts.
    """
    with open(fname) as f:
        data = f.read()

    records = []
    for pair in [rec.split() for rec in data.split("\n\n")]:
        rec = {}
        for p in pair:
            k, v = p.split(":")
            rec.update({k:v})
        records.append(rec)
    return records


def part1(fname: str) -> int:
    """Part 1.

    Tests
    >>> part1("./data/day04_test.txt")
    2
    """
    data = get_data(fname)
    reqs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    opts = ["cid"]
    return sum(sum(req in rec for req in reqs)==len(reqs) for rec in data)


def check_range(s: str, mi: int, ma: int, L: int=4) -> bool:
    if L is None:
        length_check = True
    else:
        length_check = len(s) == L
    return length_check and s.isdigit() and (mi <= int(s) <= ma)

def check_byr(s: str) -> bool:
    """
    >>> check_byr("1920")
    True
    >>> check_byr("2003")
    False
    """
    return check_range(s, 1920, 2002)

def check_iyr(s: str) -> bool:
    return check_range(s, 2010, 2020)

def check_eyr(s: str) -> bool:
    return check_range(s, 2020, 2030)

def check_hgt(s: str) -> bool:
    """
    >>> check_hgt("160cm")
    True
    >>> check_hgt("58in")
    False
    >>> check_hgt("6ft")
    False
    """
    if not s.endswith(('cm', 'in')):
        return False
    if s[-2:] == 'cm':
        return check_range(s[:-2], 150, 193, L=None)
    else:
        return check_range(s[:-2], 59, 76, L=None) 

def check_hcl(s: str) -> bool:
    """
    >>> check_hcl("#333333")
    True
    >>> check_hcl("#eeeee")
    False
    >>> check_hcl("3eeeee")
    False
    """
    allowed = set('0123456789abcdef')
    return s.startswith('#') and len(s)==7 and set(s[1:]).issubset(allowed)

def check_ecl(s: str) -> bool:
    """
    >>> check_ecl("blu")
    True
    >>> check_ecl("blk")
    False
    """
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_pid(s: str) -> bool:
    return len(s)==9 and s.isdigit()

TESTS = {"byr": check_byr,
         "iyr": check_iyr,
         "eyr": check_eyr,
         "hgt": check_hgt,
         "hcl": check_hcl,
         "ecl": check_ecl,
         "pid": check_pid,
        }

def part2(fname: str) -> int:
    """Part 2.

    Tests
    >>> part2("./data/day04_test2.txt")
    4
    """
    data = get_data(fname)
    return sum(sum(TESTS[k](v) for k, v in d.items() if k != "cid")==7 for d in data)


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day04.txt"
    print(f"Part 1 valids: {part1(fname)}")
    print(f"Part 2 valids: {part2(fname)}")
