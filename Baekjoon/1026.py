# https://www.acmicpc.net/problem/1026
import sys


n = int(sys.stdin.readline()[:-1])
A = sorted(list(map(int, sys.stdin.readline()[:-1].split(' '))))
B = sorted(list(map(int, sys.stdin.readline()[:-1].split(' '))), reverse=True)

total = 0
for a, b in zip(A, B):
    total = total + a * b

print(total)
