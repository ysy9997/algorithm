# # https://www.acmicpc.net/problem/1389
# import sys
# import collections
#
#
# n, m = map(int, sys.stdin.readline()[:-1].split(' '))
#
# graph = [list() for _ in range(n)]
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline()[:-1].split(' '))
#     a = a - 1
#     b = b - 1
#
#     if a not in graph[b]:
#         graph[a].append(b)
#         graph[b].append(a)
#
# min_val = 1e9
# who = -1
# for v in range(n):
#     q = collections.deque()
#     q.append(v)
#     visited = [-1 if _ != v else 0 for _ in range(n)]
#
#     while q:
#         p = q.popleft()
#
#         for i in graph[p]:
#             if visited[i] == -1:
#                 q.append(i)
#                 visited[i] = visited[p] + 1
#                 q.append(i)
#
#     if sum(visited) < min_val:
#         min_val = sum(visited)
#         who = v + 1
#
# print(who)


import sys
from collections import deque


def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()

        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target] + 1
                queue.append(i)


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a = a - 1
    b = b - 1

    if a not in graph[b]:
        graph[a].append(b)
        graph[b].append(a)

min_val = 1e9
who = -1
for i in range(n):
    visited = [0] * n
    bfs(i)
    if min_val > sum(visited):
        min_val = sum(visited)
        who = i + 1

print(who)
