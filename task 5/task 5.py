n, a, b = map(int, input().split())
s = list(input())

open_count = s.count('(')
close_count = 2 * n - open_count
diff = abs(open_count - close_count) // 2
cost = diff * b

if open_count > close_count:
    cnt = diff
    for i in range(len(s)-1, -1, -1):
        if cnt == 0:
            break
        if s[i] == '(':
            s[i] = ')'
            cnt -= 1
else:
    cnt = diff
    for i in range(len(s)):
        if cnt == 0:
            break
        if s[i] == ')':
            s[i] = '('
            cnt -= 1

balance = 0
swap_cost = 0

for i in range(len(s)):
    if s[i] == '(':
        balance += 1
    else:
        balance -= 1

    if balance < 0:
        found = -1
        for j in range(len(s)-1, i, -1):
            if s[j] == '(':
                found = j
                break
        if found != -1:
            s[i], s[found] = s[found], s[i]
            swap_cost += a
            balance += 2

total_cost = cost + swap_cost
print(total_cost)
