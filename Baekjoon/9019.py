# https://www.acmicpc.net/problem/9019
import sys
import collections


def move(visited, p_n, p_s):
    # D
    temp_n = p_n * 2
    if temp_n > 9999:
        temp_n = temp_n % 10000
    if not visited[temp_n]:
        q.append([temp_n, f'{p_s}D'])
        visited[temp_n] = True

    # S
    temp_n = p_n - 1
    if temp_n < 0:
        temp_n = 9999
    if not visited[temp_n]:
        q.append([temp_n, f'{p_s}S'])
        visited[temp_n] = True

    # L
    temp_n = (10 * p_n + (p_n // 1000)) % 10000
    if not visited[temp_n]:
        q.append([temp_n, f'{p_s}L'])
        visited[temp_n] = True

    # R
    temp_n = (p_n // 10 + (p_n % 10) * 1000) % 10000
    if not visited[temp_n]:
        q.append([temp_n, f'{p_s}R'])
        visited[temp_n] = True


T = int(sys.stdin.readline()[:-1])

_as = list()
_bs = list()
for i in range(T):
    a, b = map(int, sys.stdin.readline()[:-1].split(' '))
    _as.append(a)
    _bs.append(b)

while len(_as) != 0:
    a, b = _as.pop(0), _bs.pop(0)

    q = collections.deque()
    visit = [False for _ in range(10000)]
    q.append([a, ''])
    visit[a] = True
    while True:
        p_n, p_s = q.popleft()
        if p_n == b:
            break
        move(visit, p_n, p_s)
    print(p_s)
