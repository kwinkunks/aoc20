test = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

def count(data, move=(1, 3)):
    return sum(c=='#' for l,line in enumerate(data.split('\n')) for c in line[move[1]*l%len(line)] if l%move[0]==0)
    
# Test
assert count(test) == 7
