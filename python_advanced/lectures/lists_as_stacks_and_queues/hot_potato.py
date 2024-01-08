from collections import deque

circle = deque(input().split())
nth_toss = int(input()) -1

while len(circle) != 1:
    circle.rotate(-nth_toss)
    print(f'Removed {circle.popleft()}')

print(f'Last is {circle[0]}')
