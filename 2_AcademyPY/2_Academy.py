def count_abc(s):
    a, ab, result = 0, 0, 0
    for ch in s:
        if ch == 'a':
            a += 1
        elif ch == 'b':
            ab += a
        elif ch == 'c':
            result += ab
    return result
s = input().strip()
print(count_abc(s))
