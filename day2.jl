using DelimitedFiles
using Test


"""
    count_chars(data)

Count the characters according to part 1's rules.
"""
function count_chars(data)::Int
    total = 0
    for (r, t, s) in eachrow(data)
        a, b = [parse(Int, ri) for ri in split(r, "-")]
        n = length(collect(m.match for m in eachmatch(Regex("$(t[1])"), s)))
        if a <= n <= b
            total += 1
        end
    end
    return total
end

data = readdlm("./day2_test.txt")
@test count_chars(data) == 2

data = readdlm("./day2.txt")
println("Part 1 count: $(count_chars(data))")


"""
    count_chars_again(data)

Count according to the new rules.
"""
function count_chars_again(data)::Int
    total = 0
    for (r, t, s) in eachrow(data)
        a, b = [parse(Int, ri) for ri in split(r, "-")]
        n = (s[a] == t[1]) + (s[b] == t[1])
        if n == 1
            total += 1
        end
    end
    return total
end

data = readdlm("./day2_test.txt")
@test count_chars_again(data) == 1

data = readdlm("./day2.txt")
println("Part 2 count: $(count_chars_again(data))")
