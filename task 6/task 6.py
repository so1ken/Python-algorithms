import heapq

n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(0)
    exit()

prev = list(range(-1, n - 1))
next = list(range(1, n + 1))
active = [True] * n

heap = []
for i in range(n - 1):
    diff = abs(a[i + 1] - a[i])
    heapq.heappush(heap, (-diff, i, i + 1))

total = 0

while heap:
    neg_diff, left, right = heapq.heappop(heap)
    if not active[left] or not active[right] or next[left] != right:
        continue
    total += -neg_diff

    active[left] = active[right] = False

    p = prev[left]
    s = next[right]

    if p != -1:
        next[p] = s
    if s < n:
        prev[s] = p

    if p != -1 and s < n:
        new_diff = abs(a[s] - a[p])
        heapq.heappush(heap, (-new_diff, p, s))

print(total)
