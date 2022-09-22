from heapq import heappush, heappop


def dijkstra(start, end, graph):
    n = len(graph)
    dis = [0xffffff] * (n + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heappop(q)
        if k > dis[u]: continue
        for v, w in graph[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heappush(q, [dis[v], v])

    return dis[end]


def solution(n, s, a, b, fares):
    g = [list() for _ in range(n + 1)]

    for fare in fares:
        g[fare[0]].append([fare[1], fare[2]])
        g[fare[1]].append([fare[0], fare[2]])

    min_val = dijkstra(s, a, g) + dijkstra(s, b, g)

    for t in range(1, n + 1):
        new = dijkstra(s, t, g) + dijkstra(t, a, g) + dijkstra(t, b, g)
        if min_val > new:
            min_val = new

    return min_val
