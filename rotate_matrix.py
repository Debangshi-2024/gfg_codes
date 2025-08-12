def rotate_90(matrix):
    rotated = list(zip(*matrix[::-1]))
    return [list(row) for row in rotated]

matrix = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90,100,110,120],
    [130,140,150,160]
]

rotated = rotate_90(matrix)

for row in rotated:
    print(*row)
