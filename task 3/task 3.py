n = int(input())
array = set(map(int, input().split()))
unique = set()
for num in set(array):
    unique.add(num)
    while num > 0:
        num = num // 2
        if (num in unique):
            break
        unique.add(num)

print(min(len(unique), n))
d
