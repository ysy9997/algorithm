# https://www.acmicpc.net/problem/10610
import sys
import collections


def move(visited, q):
    x, y = q.popleft()
    n = len(visited)
    if x - 2 >= 0 and y - 1 >= 0 and visited[y - 1][x - 2] == -1:
        q.append([x - 2, y - 1])
        visited[y - 1][x - 2] = visited[y][x] + 1
    if x - 2 >= 0 and y + 1 < n and visited[y + 1][x - 2] == -1:
        q.append([x - 2, y + 1])
        visited[y + 1][x - 2] = visited[y][x] + 1
    if y - 2 >= 0 and visited[y - 2][x] == -1:
        q.append([x, y - 2])
        visited[y - 2][x] = visited[y][x] + 1
    if y + 2 < n and visited[y + 2][x] == -1:
        q.append([x, y + 2])
        visited[y + 2][x] = visited[y][x] + 1
    if x + 2 < n and y - 1 >= 0 and visited[y - 1][x + 2] == -1:
        q.append([x + 2, y - 1])
        visited[y - 1][x + 2] = visited[y][x] + 1
    if x + 2 < n and y + 1 < n and visited[y + 1][x + 2] == -1:
        q.append([x + 2, y + 1])
        visited[y + 1][x + 2] = visited[y][x] + 1


n = int(sys.stdin.readline()[:-1])
visited = [[-1 for _ in range(n)] for _ in range(n)]

p_x, p_y, t_x, t_y = map(int, sys.stdin.readline()[:-1].split(' '))

q = collections.deque()
q.append([p_x, p_y])
visited[p_y][p_x] = 0
while len(q) != 0:
    move(visited, q)

if not visited[t_y][t_x]:
    print(-1)
else:
    print(visited[t_y][t_x])
