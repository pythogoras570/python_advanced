n = int(input())

u_elements = set()
for _ in range(n):
    elements = (input().split())
    for el in elements:
        u_elements.add(el)

print(*u_elements, sep='\n')
