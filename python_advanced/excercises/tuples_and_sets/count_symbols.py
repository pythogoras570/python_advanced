string = tuple(input())

symbols = sorted((set(string)))

for el in symbols:
    print(f'{el}: {string.count(el)} time/s')
