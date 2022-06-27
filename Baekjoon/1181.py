# https://www.acmicpc.net/problem/1181
import sys


n = int(sys.stdin.readline()[:-1])

strings = list()
for i in range(n):
    strings.append(sys.stdin.readline()[:-1])

strings = sorted(set(strings))
strings = sorted(strings, key=len)

for s in strings:
    print(s)
