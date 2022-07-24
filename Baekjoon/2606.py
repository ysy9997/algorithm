# https://www.acmicpc.net/problem/2606
import sys
import collections


graph = [list() for _ in range(int(sys.stdin.readline()[:-1]))]

for _ in range(int(sys.stdin.readline()[:-1])):
    s, e = map(int, sys.stdin.readline()[:-1].split(' '))
    graph[s - 1].append(e - 1)
    graph[e - 1].append(s - 1)

q = collections.deque()
q.append(0)
visit = [False for _ in range(len(graph))]
visit[0] = True
count = 0

while q:
    p = q.popleft()

    for line in graph[p]:
        if not visit[line]:
            visit[line] = True
            count = count + 1
            q.append(line)

print(count)
