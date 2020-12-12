# aoc20
Advent of Code 2020

Going to start off with Julia, which I haven't used for ages. Predicted stamina: 3.5 days. Tips and corrections welcome!

- **Day 1** — A bit frustrating at first, eventually got there. Then learned from [trhallam](https://github.com/trhallam) and refactored.
- **Day 2** — File parsing. Still not doing it very smartly, lots of splitting and indexing. Thankful for list comprehension.
- **Day 3** — Modulo indexing, and the file reading is super-weird. Tried and failed to use `CartesianIndex`. Later learned about `mod1()` and then `CircularArray` which might come in useful in future. Favourite solution so far: https://julialang.zulipchat.com/#narrow/stream/265470-advent-of-code/topic/Solutions.20day.203/near/218664645 
- **Day 4** — File parsing was enough to punt me into Python today, where dicts are so nice... Used a dict of boolean test functions.
- **Day 5** — Back to Julia for a nice and easy Saturday problem, parsing strings to binary numbers. Probably a better way than brute force on part 2, but it's a small problem.
- **Day 6** — Relatively easy set theory problem... but I reverted to Python again. Maybe the least code I've ever needed for an Advent of Code.
- **Day 7** — Not only using Python, but NetworkX as well. Thought it would make part 2 easy, but no; my eventual solution is "elegant" like a dancing 🦒 giraffe.
- **Day 8** — Here comes the machine code 😬 Not too bad today, but you know where it's going! 
- **Day 9** — Part 2 reminiscent of Day 1, again wanting recursion. But again brute force is fine.
- **Day 10** — Was hard to think through part 2; one of those problems needing more thinking than coding. Most interesting one so far this year.
- **Day 11** — Very similar to 2018, Day 18, so I cheated a bit and used my functions from that day. Almost thought we had to do the polar coordinate checking again too (2019, Day 10), but thank goodness no.
- **Day 12** — Fun vector math problem for a Saturday, my favourite of the easier ones so far.

