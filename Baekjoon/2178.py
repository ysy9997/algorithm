# https://www.acmicpc.net/problem/1278
import sys
import collections


n, m = map(int, sys.stdin.readline()[:-1].split(' '))

graph = [list(map(int, list(sys.stdin.readline()[:-1]))) for _ in range(n)]
visit = [[-1 for _ in range(m)] for _ in range(n)]

visit[0][0] = 1
q = collections.deque()
q.append([0, 0])

while visit[-1][-1] == -1:
    y, x = q.popleft()
    p_visit = visit[y][x]

    # up
    if y > 0 and visit[y - 1][x] == -1 and graph[y - 1][x] != 0:
        visit[y - 1][x] = p_visit + 1
        q.append([y - 1, x])
    # right
    if x < m - 1 and visit[y][x + 1] == -1 and graph[y][x + 1] != 0:
        visit[y][x + 1] = p_visit + 1
        q.append([y, x + 1])
    # down
    if y < n - 1 and visit[y + 1][x] == -1 and graph[y + 1][x] != 0:
        visit[y + 1][x] = p_visit + 1
        q.append([y + 1, x])
    # left
    if x > 0 and visit[y][x - 1] == -1 and graph[y][x - 1] != 0:
        visit[y][x - 1] = p_visit + 1
        q.append([y, x - 1])

print(visit[-1][-1])
