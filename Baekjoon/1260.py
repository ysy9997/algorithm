# https://www.acmicpc.net/problem/1107
import sys
import collections


n, m, v = map(int, sys.stdin.readline()[:-1].split(' '))
v = v - 1

graph = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline()[:-1].split(' '))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

graph = [sorted(_) for _ in graph]

visited = [False if _ != v else True for _ in range(n)]
stack = list()
stack.append(v)
print(v + 1, end=' ')

while stack:
    visit = False
    p = stack[-1]

    for i in graph[p]:
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            stack.append(i)
            visit = True
            print(i + 1, end=' ')
            break

    if not visit:
        stack = stack[:-1]

print()

q = collections.deque()
q.append(v)
visited = [False if _ != v else True for _ in range(n)]
print(v + 1, end=' ')

while q:
    p = q.popleft()

    for i in graph[p]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
            q.append(i)
            print(i + 1, end=' ')
