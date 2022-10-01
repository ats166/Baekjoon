import heapq,sys
input = sys.stdin.readline
V = int(input())
M = int(input())

arr =[[]*V for _ in range(V)]

for i in range(M):
    a,b,c = map(int,input().split())

    arr[a - 1].append((b - 1, c))
start,end = map(int,input().split())

result = [float('INF')] * V
heap = []

def dijkstra(start):
    heapq.heappush(heap,(0,start))
    result[start] = 0

    while heap:
        sk, k = heapq.heappop(heap)
        result[start] = 0

        if result[k] < sk:
            continue

        for i in arr[k]:
            cost = sk + i[1]
            if cost < result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))

dijkstra(start-1)
print(result[end-1])