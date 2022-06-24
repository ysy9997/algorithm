# https://www.acmicpc.net/problem/11650
import sys


n = int(sys.stdin.readline()[:-1])

xy = list()
for i in range(n):
    x, y = map(int, sys.stdin.readline()[:-1].split(' '))
    xy.append([x, y])

xy = sorted(xy)
[print(*_) for _ in xy]
