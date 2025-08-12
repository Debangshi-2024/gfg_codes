def print_spiral(matrix):
    if not matrix:
        return
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])
    while top < bottom and left < right:
        for i in range(left, right):
            print(matrix[top][i], end=' ')
        top += 1
        for i in range(top, bottom):
            print(matrix[i][right - 1], end=' ')
        right -= 1
        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                print(matrix[bottom - 1][i], end=' ')
            bottom -= 1
        if left < right:
            for i in range(bottom - 1, top - 1, -1):
                print(matrix[i][left], end=' ')
            left += 1

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10,11,12],
    [13,14,15,16]
]

print_spiral(matrix)
