import math

n = int(input())
times_arr = set(tuple(map(int, input().split())) for _ in range(n))
for _ in range(int(input())):
    line, time = map(int, input().split())
    a, b = times_arr[line - 1]
    if time <= a:
        print(a)
    else:
        print(a + b * math.ceil((time - a) / b))
