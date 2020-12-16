"""
Advent of Code 2020
Day 16
"""


def get_data(fname: str) -> tuple:
    """
    Read the data file into dicts.
    """
    with open(fname) as f:
        texts = f.read().split('\n\n')

    # Get the fields and all their valid values. Not space efficient,
    # but there aren't that many of them.
    fields = {}
    for field in texts[0].split('\n'):
        name, data = field.split(': ')
        for pair in data.split(' or '):
            mi, ma = pair.split('-')
            ranges = fields.get(name, [])
            ranges.extend(i for i in range(int(mi), int(ma)+1))
            fields[name] = ranges

    # Get my ticket.
    _, data = texts[1].split('\n')
    my_ticket = [int(d) for d in data.split(',')]

    # Get the other tickets.
    tickets = []
    for ticket in texts[2].split('\n')[1:]:
        tickets.append([int(t) for t in ticket.split(',')])

    return fields, tickets, my_ticket


def sort_tickets(fields, tickets) -> tuple:
    """
    Get the valid and invalid tickets.
    """
    valid_numbers = set()
    for f in fields.values():
        valid_numbers.update(f)

    valids, invalids = [], []
    for ticket in tickets:
        invalid = []
        for n in ticket:
            if n in valid_numbers: continue
            invalid.append(n)
        if invalid:
            invalids.extend(invalid)
        else:
            valids.append(ticket)

    return valids, invalids


def part1(fname: str) -> int:
    """Part 1.

    Tests
    >>> part1("./data/day16_test.txt")
    71
    """
    _, invalids = sort_tickets(*get_data(fname)[:2])
    return sum(invalids)


def part2(fname: str) -> int:
    """Part 2.

    This sucks. No test for now.
    """
    fields, tickets, my_ticket = get_data(fname)
    valids, invalids = sort_tickets(fields, tickets)
    
    # If a field is valid, add it to a set of hypotheses
    # *iff* it hasn't bene discarded before.
    # If invalid, remove it from the hypotheses *forever*
    # by adding it to the set of discards.
    hypotheses = {k: set() for k in fields}
    discards = {k: set() for k in fields}
    for valid in valids:
        for i, value in enumerate(valid):
            for field, values in fields.items():
                if value in values:
                    if i not in discards[field]:
                        hypotheses[field].add(i)
                else:
                    hypotheses[field].discard(i)
                    discards[field].add(i)

    # Sort the hypotheses into order, based on how many
    # possibilities are in each field. Hopefully mono-
    # tonically increasing.
    hypotheses = {k:v for k, v in sorted(hypotheses.items(), key=lambda x: len(x[1]))}

    # Now assign the certain fields in order. Each time
    # we make an assignment, add the field to a list
    # so we know what to ignore for future fields.
    certain = {}
    assigned = []
    for field, hypos in hypotheses.items():
        for assign in assigned:
            hypos.discard(assign)
        assert len(hypos) == 1
        position, = hypos  # Singleton set.
        certain[field] = position
        assigned.append(position)

    # Now make the product for our ticket.
    product = 1
    for field, position in certain.items():
        if field.startswith('departure'):
            product *= my_ticket[position]

    return product


if __name__ == "__main__":
    import doctest
    import sys
    doctest.testmod(verbose=True)

    fname = "./data/day16.txt"
    print(f"Part 1 count: {part1(fname)}")
    print(f"Part 2 product: {part2(fname)}")
