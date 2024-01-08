data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []
sums = 0

for i in range(rows):
    elements = [int(el) for el in input().split(',')]
    sums += sum(elements)
    matrix.append(elements)

print(sums)
print(matrix)
