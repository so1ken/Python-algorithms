from collections import deque

def solve():
    # Считываем N и Q
    N, Q = map(int, input().split())
    # Строим список смежности для вершин 0..N
    graph = [[] for _ in range(N + 1)]
    
    # Для каждого факта [l, r] добавляем ребро между (l-1) и r
    for _ in range(Q):
        l, r = map(int, input().split())
        graph[l - 1].append(r)
        graph[r].append(l - 1)
    
    # BFS от 0 до N
    dist = [-1] * (N + 1)
    dist[0] = 0
    queue = deque([0])
    
    while queue:
        u = queue.popleft()
        if u == N:
            break
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    
    # Выводим ответ
    if dist[N] == -1:
        print("No")
    else:
        print("Yes")
        print(dist[N])

if __name__ == "__main__":
    solve()
