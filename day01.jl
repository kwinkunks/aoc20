using DelimitedFiles

data = readdlm("./data/day01.txt")

# Part 1.
for d in data
    if (2020 - d) in data
        result = convert(Integer, d * (2020 - d))
        println("Two numbers: $result")
        break
    end
end

# Part 2.
found = false
for d in data
    for e in [i for i in data if ((d + i) < 2020)]
        if (2020 - d - e) in data
            result = convert(Integer, d * e * (2020 - d - e))
            println("Three numbers: $result")
            global found = true  # This sucks.
            break
        end
        if found
            break
        end
    end
end

println("Done.")