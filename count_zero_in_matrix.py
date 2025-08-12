def count_zeros(matrix):
    return sum(row.count(0) for row in matrix)

matrix = [
    [0, 1, 2],
    [3, 0, 0],
    [4, 5, 0]
]

print(count_zeros(matrix))
