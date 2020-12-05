using DelimitedFiles
using Test


"""
    get_seat_ids(data)

Get all seat ids. Map to binary strings, parse as Int-base2, add.
"""
function get_seat_ids(data)
    rowbin = Dict('F' => '0', 'B' => '1')
    colbin = Dict('L' => '0', 'R' => '1')
    rows = [parse(Int, join(rowbin[c] for c in row[1:7]), base=2) for row in data]
    cols = [parse(Int, join(colbin[c] for c in row[8:10]), base=2) for row in data]
    return [8*row + col for (row, col) in zip(rows, cols)]
    end

test = readdlm("./data/day05_test.txt")
@test all(get_seat_ids(test) .== [567, 119, 820])

data = readdlm("./data/day05.txt")
seats = get_seat_ids(data)
println("Part 1 max id: $(maximum(seats))")


"""
    get_my-seat(data)

Find missing id for which id-1 and id+1 are present.
Just going to brute force this, there aren't that many.
"""
function get_my_seat(seats)
    for s in 1:maximum(seats)
        if s ∉ seats && s-1 ∈ seats && s+1 ∈ seats
            return s
            end
        end
    end

println("Part 2 my seat: $(get_my_seat(seats))")
