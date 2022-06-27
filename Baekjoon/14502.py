# https://www.acmicpc.net/problem/14502
import sys
import collections
import itertools
import copy


def move(q, visit):
    p_x, p_y = q.popleft()
    n, m = len(visit), len(visit[0])

    if p_x > 0 and not visit[p_y][p_x - 1]:
        q.append([p_x - 1, p_y])
        visit[p_y][p_x - 1] = True
    if p_x + 1 < m and not visit[p_y][p_x + 1]:
        q.append([p_x + 1, p_y])
        visit[p_y][p_x + 1] = True
    if p_y > 0 and not visit[p_y - 1][p_x]:
        q.append([p_x, p_y - 1])
        visit[p_y - 1][p_x] = True
    if p_y + 1 < n and not visit[p_y + 1][p_x]:
        q.append([p_x, p_y + 1])
        visit[p_y + 1][p_x] = True


n, m = map(int, sys.stdin.readline()[:-1].split(' '))

graph = [list(map(int, sys.stdin.readline()[:-1].split(' '))) for _ in range(n)]
combs = list(itertools.combinations([_ for _ in range(m * n)], 3))
total = 0

t = None

for comb in combs:
    if graph[comb[0] // m][comb[0] % m] == 0 and graph[comb[1] // m][comb[1] % m] == 0 and graph[comb[2] // m][comb[2] % m] == 0:
        t_graph = copy.deepcopy(graph)
        t_graph[comb[0] // m][comb[0] % m] = 1
        t_graph[comb[1] // m][comb[1] % m] = 1
        t_graph[comb[2] // m][comb[2] % m] = 1

        visit = [[True if t_graph[y][x] == 1 else False for x in range(m)] for y in range(n)]

        q = collections.deque()
        for y in range(n):
            for x in range(m):
                if t_graph[y][x] == 2:
                    p_x = x
                    p_y = y
                    q.append([p_x, p_y])
                    visit[p_y][p_x] = True

        while len(q) > 0:
            move(q, visit)

        _sum = m * n
        for y in range(n):
            for x in range(m):
                if visit[y][x]:
                    _sum = _sum - 1
        if total < _sum:
            total = _sum
            t = t_graph

print(total)
