# https://www.acmicpc.net/problem/1504
# wrong
import sys
import heapq


def floydwarshall(graph):
    n = len(graph)

    for k in range(n):
        for x in range(n):
            for y in range(n):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    return graph


def dijkstra(start: int, costs, graph):
    # start 출발점
    # cost: e.g. [1e9 for _ in range(v)]
    # graph: e.g. [1e9 for _ in range(v)]

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

    return costs


n, e = map(int, sys.stdin.readline()[:-1].split(' '))
costs = [int(1e9) for _ in range(n + 1)]
graph = [list() for _ in range(n + 1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline()[:-1].split(' '))
    graph[a - 1].append([b, c])
    graph[b - 1].append([a, c])

ma, mb = map(int, sys.stdin.readline()[:-1].split(' '))

costs = dijkstra(1, costs, graph)
c_0 = costs[ma]

costs = [int(1e9) for _ in range(n)]
costs = dijkstra(ma, costs, graph)
c_1 = costs[mb]
c_2 = costs[-1]

costs = [int(1e9) for _ in range(n)]
costs = dijkstra(mb, costs, graph)
c_3 = costs[ma]
c_4 = costs[-1]

result = min(c_0 + c_1 + c_4, c_0 + c_2 + c_3)
if result >= 1e9:
    print(-1)
else:
    print(result)
