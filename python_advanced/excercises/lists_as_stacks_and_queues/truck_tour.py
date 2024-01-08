from collections import deque

n = int(input())

pumps = deque()
start_position = 0
stops_counter = 0

for _ in range(n):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

while stops_counter < n:
    fuel = 0
    for i in range(n):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops_counter = 0
            break
        fuel -= destination
        stops_counter += 1

print(start_position)