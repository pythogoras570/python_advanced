n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))

x, y = 0, 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            x, y = i, j
            break

fish_caught = 0

while True:
    command = input()

    if command == 'up':
        x -= 1
        if x < 0:
            x = n - 1
    elif command == 'down':
        x += 1
        if x >= n:
            x = 0
    elif command == 'left':
        y -= 1
        if y < 0:
            y = n - 1
    elif command == 'right':
        y += 1
        if y >= n:
            y = 0

    if matrix[x][y] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{x},{y}]")
        break

    if matrix[x][y].isdigit():
        fish_caught += int(matrix[x][y])
        matrix[x][y] = '-'
        matrix[x][y] = 'S'

    if command == 'collect the nets':
        if fish_caught >= 20:
            print("Success! You managed to reach the quota!")
        else:
            print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_caught} tons of fish more.")

        if fish_caught > 0:
            print(f"Amount of fish caught: {fish_caught} tons.")

        for row in matrix:
            print(''.join(row))
        break