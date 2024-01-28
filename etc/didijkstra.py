from heapq import heappush, heappop


def dijkstra(start, end, graph):
    """

    :param start:
    :param end:
    :param graph: graph[현재 위치] = [[이어진 위치, cost], ...]
    :return:
    """
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
