from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    prioridades = list(map(int, input().split()))

    q = deque()
    for i in range(n):
        q.append((prioridades[i], i))

    tiempo = 0

    while True:
        p, idx = q.popleft()

        if any(p2 > p for p2, _ in q):
            q.append((p, idx))
        else:
            tiempo += 1
            if idx == m:
                print(tiempo)
                break