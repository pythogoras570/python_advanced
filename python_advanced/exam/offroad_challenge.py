fuel = input().split()
fuel = [int(x) for x in fuel]

consumption = input().split()
consumption = [int(x) for x in consumption]

needed = input().split()
needed = [int(x) for x in needed]

reached = []

for i in range(len(needed)):
    current_fuel = fuel.pop()
    current_consumption = consumption.pop(0)

    if current_fuel - current_consumption >= needed[i]:
        print(f"John has reached: Altitude {i + 1}")
        reached.append(i + 1)
        needed.pop(0)
    else:
        print(f"John did not reach: Altitude {i + 1}")
        break

if len(needed) == 0:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    if len(reached) > 0:
        print("John failed to reach the top.")
        print(f"Reached altitudes: Altitude {', '.join([str(x) for x in reached])}")
    else:
        print("John failed to reach the top.")
        print("John didn't reach any altitude.")