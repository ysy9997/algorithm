# https://www.acmicpc.net/problem/11399
import sys

n = int(sys.stdin.readline()[:-1])
t = list(map(int, sys.stdin.readline()[:-1].split(' ')))
t = sorted(t)

s = 0
for i in range(len(t)):
    s = s + sum(t[:len(t) - i])

print(s)
