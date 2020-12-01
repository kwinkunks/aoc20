using DelimitedFiles
using Test

#=
Refactor after seeing Tony Hallam's solution and wanting to tidy up with
functions and tests. Might try using doctests tomorrow.

I'm sure this can be solved in a really elegant recursive way but I need
to think about it some more. (Recursion is a state of mind, it seems.)
=#

"""
    part_1(data, target)

Recursive search for the number making up to 2020.
"""
function part_1(data::Array, target::Integer=2020)::Integer
    for d in data
        if (target - d) in data
            return convert(Integer, d * (target - d))
        end
    end
end

test1 = readdlm("./day1_test.txt")
@test part_1(test1) == 514579

data = readdlm("./day1.txt")
println("Part 1: $(part_1(data))")


"""
    part_2(data, target)

I'm sure this could be recursive but I can't quite get it...
"""
function part_2(data::Array, target::Integer=2020)::Integer
    for d in data
        for e in [i for i in data if ((d + i) < target)]
            if (target - d - e) in data
                return convert(Integer, d * e * (target - d - e))
            end
        end
    end
end

test2 = readdlm("./day1_test.txt")
@test part_2(test2) == 241861950

println("Part 2: $(part_2(data))")
