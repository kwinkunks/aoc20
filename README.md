# aoc20
Advent of Code 2020

Going to start off with Julia, which I haven't used for ages. Tips and corrections welcome!

- Day 1: A bit frustrating at first, eventually got there. Then learned from [trhallam](https://github.com/trhallam) and refactored.
- Day 2: File parsing. Still not doing it very smartly, lots of splitting and indexing. Thankful for list comprehension.
- Day 3: Modulo indexing, and the file reading is super-weird. Tried and failed to use `CartesianIndex`. Later learned about `mod1()` and then `CircularArray` which might come in useful in future. Favourite solution so far: https://julialang.zulipchat.com/#narrow/stream/265470-advent-of-code/topic/Solutions.20day.203/near/218664645 
- Day 4: File parsing was enough to punt me into Python today, where dicts are so nice... Used a dict of boolean test functions.
- Day 5: Back to Julia for a nice and easy Saturday problem, parsing strings to binary numbers. Probably a better way than brute force on part 2, but it's a small problem.
- Day 6: Relatively easy set theory problem... but I reverted to Python again.

