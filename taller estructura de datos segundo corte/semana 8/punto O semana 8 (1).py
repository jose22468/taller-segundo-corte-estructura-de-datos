import heapq

n = int(input())
a = list(map(int, input().split()))

health = 0
heap = []

for x in a:
    health += x
    heapq.heappush(heap, x)

    if health < 0:
        health -= heapq.heappop(heap)

print(len(heap))