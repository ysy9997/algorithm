# https://www.acmicpc.net/problem/7576
import sys
import collections

m, n = map(int, sys.stdin.readline()[:-1].split(' '))

graph = list()
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline()[:-1].split(' '))))

q = collections.deque()
visit = [[-1 if graph[y][x] == 0 else 0 for x in range(m)] for y in range(n)]

for x in range(m):
    for y in range(n):
        if graph[y][x] == 1:
            q.append([x, y])

while q:
    x, y = q.popleft()
    count = visit[y][x] + 1

    if x > 0 and visit[y][x - 1] == -1:
        visit[y][x - 1] = count
        q.append([x - 1, y])

    if x < m - 1 and visit[y][x + 1] == -1:
        visit[y][x + 1] = count
        q.append([x + 1, y])

    if y > 0 and visit[y - 1][x] == -1:
        visit[y - 1][x] = count
        q.append([x, y - 1])

    if y < n - 1 and visit[y + 1][x] == -1:
        visit[y + 1][x] = count
        q.append([x, y + 1])

max_count = 0
var = True
for x in range(m):
    for y in range(n):
        if visit[y][x] == -1:
            var = False
        elif max_count < visit[y][x]:
            max_count = visit[y][x]
    if not var:
        break

print(max_count) if var else print(-1)
