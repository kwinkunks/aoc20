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
- **Day 13** — Very satisfying number theory problem about simultaneous linear congruences; solved with the Chinese remainder theorem. More thinking than coding (mostly trying to reinvent the CRT without knowing what it was called... [Google eventually led me there](https://github.com/TheAlgorithms/Python/blob/master/blockchain/chinese_remainder_theorem.py)). Fun problem. Learned about `pow()` with modulus, and `divmod()`.
- **Day 14** — Binary number shuffling, not my favourite. Learned about `str.zfill()`. Tempting to make the entire memory bank, but a `dict` suffices.
- **Day 15** — One of those fiddly loops where you need info from the previous
  iteration. Main insight: storing only 'last time seen' in a `dict`.
- **Day 16** — My least favourite kind of puzzle: convoluted instructions, but ultimately fairly clear what to do, then not much elegance to be had, just a lot of loops and fiddly data management.
- **Day 17** — Another 'count things in a kernel' but thuis time 3 and 4 dimensions. In hindsight should perhaps have tried n-d convolution but it didn't seem too bad to do it with tuples for Part 1... My solution is suuuuper slow, even after trying to use set operations to speed it up.
