using DelimitedFiles
using Test


"""
    count_trees(data, move=(1, 3))

Move and count trees according to part 1's rules.
"""
function count_trees(data, move=(1, 3))::Int
    arr = permutedims(hcat(collect.(data)...))  # wtf syntax
    rows, cols = size(arr)
    dr, dc = move
    total = 0
    col = 1
    for row in 1:dr:rows
        if arr[row, col] == '#'
            total += 1
            end
        col = (col + dc - 1) % cols + 1  # Stupid 1-index, next time: mod1(a, b)
        end
    return total
    end

test = readdlm("./data/day03_test.txt")
@test count_trees(test) == 7

data = readdlm("./data/day03.txt")
println("Part 1 trees: $(count_trees(data))")


"""
    count_all(data, moves)

Part 2 function
"""
function count_all(data, moves)
    product = 1
    for move in moves
        product *= count_trees(data, move)
        end
    return product
    end

moves = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

@test count_all(test, moves) == 336

println("Part 2 product: $(count_all(data, moves))")
