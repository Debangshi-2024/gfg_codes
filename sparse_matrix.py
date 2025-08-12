def is_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_elements = rows * cols
    zero_count = sum(row.count(0) for row in matrix)
    return zero_count > total_elements // 2

matrix = [
    [0, 0, 3],
    [0, 0, 0],
    [7, 0, 0]
]

if is_sparse(matrix):
    print("Sparse Matrix")
else:
    print("Not a Sparse Matrix")
