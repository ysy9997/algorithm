# https://www.acmicpc.net/problem/1620
import sys


n, m = map(int, sys.stdin.readline()[:-1].split(' '))

poket = dict()
for i in range(n):
    poket[sys.stdin.readline()[:-1]] = i + 1
key = list(poket.keys())

for _ in range(m):
    nors = sys.stdin.readline()[:-1]

    try:
        num = int(nors)
        print(key[num - 1])
    except ValueError:
        print(poket[nors])
