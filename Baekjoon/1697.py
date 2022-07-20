# https://www.acmicpc.net/problem/1697
import sys
import collections


n, k = map(int, sys.stdin.readline()[:-1].split(' '))

if n >= k:
    print(n - k)

else:
    visit = [-1 for _ in range(1000001)]
    q = collections.deque()

    q.append(n)
    visit[n] = 0

    while visit[k] == -1 and q:
        p = q.popleft()
        if p < 1000000 and visit[p + 1] == -1:
            visit[p + 1] = visit[p] + 1
            q.append(p + 1)
        if p > 0 and visit[p - 1] == -1:
            visit[p - 1] = visit[p] + 1
            q.append(p - 1)
        if p * 2 < 1000000 and visit[p * 2] == -1:
            visit[p * 2] = visit[p] + 1
            q.append(p * 2)

    print(visit[k])
