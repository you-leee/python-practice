# Find all integers, where a^3 + b^3 == c^3 + d^3 between 1 and 1000

# a + b = c + d
sum_pairs = {}
result = set()

for i in range(1, 1000):
    for j in range(i + 1, 1001):
        c1 = i**3
        c2 = j**3
        sum = c1 + c2
        if sum in sum_pairs:
            result.add(i)
            result.add(j)
            pair = sum_pairs[sum]
            result.add(pair[0])
            result.add(pair[1])

            print(i, j, pair[0], pair[1])
        else:
            sum_pairs[sum] = (i, j)


print(result)
