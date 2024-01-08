data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for col in range(cols):
    total_row = 0
    for row in range(rows):
        total_row += matrix[row][col]
    print(total_row)
