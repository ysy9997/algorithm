# https://www.acmicpc.net/problem/1764
import sys


n, m = map(int, sys.stdin.readline()[:-1].split(' '))

names = dict()
for _ in range(n):
    names[sys.stdin.readline()[:-1]] = 0

count = 0
for _ in range(m):
    try:
        name = sys.stdin.readline()[:-1]
        names[name] = names[name] + 1
        count = count + 1
    except KeyError:
        pass

names = sorted(names.items())
print(count)
for name in names:
    if name[1] == 1:
        print(name[0])

