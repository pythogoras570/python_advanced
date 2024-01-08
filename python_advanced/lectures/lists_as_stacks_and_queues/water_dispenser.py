from collections import deque

quantity = int(input())
waterline = deque()

name = input()

while name != 'Start':
    waterline.append(name)
    name = input()

command = input()

while command != 'End':
    data = command.split()
    if len(data) == 1:
        liters_to_give = int(data[0])
        if liters_to_give <= quantity:
            person_name = waterline.popleft()
            print(f'{person_name} got water')
        elif liters_to_give > quantity:
            person_name = waterline.popleft()
            print(f'{person_name} must wait')
        quantity -= liters_to_give

    else:
        liters_to_add = int(data[1])
        quantity += liters_to_add

    command = input()
if quantity < 0:
    quantity = 0

print(f'{quantity} liters left')
