# https://www.acmicpc.net/problem/1965
import sys
import heapq


def dijkstra(start: int, costs):
    # start 출발점
    # cost: e.g. [1e9 for _ in range(v)]

    q = list()
    heapq.heappush(q, [0, start])
    costs[start] = 0

    while q:
        dist, p = heapq.heappop(q)
        if costs[p] < dist:
            continue

        for i in graph[p]:
            distance = dist + i[1]
            if distance < costs[i[0]]:
                costs[i[0]] = distance
                heapq.heappush(q, [distance, i[0]])


v, e = map(int, sys.stdin.readline()[:-1].split(' '))
start = int(sys.stdin.readline()[:-1]) - 1
costs = [1e9 for _ in range(v)]
graph = [list() for _ in range(v)]

for i in range(e):
    u, v, w = map(int, sys.stdin.readline()[:-1].split(' '))
    graph[u - 1].append([v - 1, w])

dijkstra(start, costs)

for cost in costs:
    if cost == 1e9:
        print('INF')
    else:
        print(cost)
