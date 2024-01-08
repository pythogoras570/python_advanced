n = int(input())

long_intersection = set()

for _ in range(n):
    range1, range2 = input().split('-')
    start1, end1 = [int(x) for x in range1.split(',')]
    start2, end2 = [int(x) for x in range2.split(',')]

    set1 = set(range(start1, end1 + 1))
    set2 = set(range(start2, end2 + 1))

    intersection = set(set1 & set2)

    if len(intersection) > len(long_intersection):
        long_intersection = intersection

print(f'Longest intersection is {list(long_intersection)} with length {len(long_intersection)}')
