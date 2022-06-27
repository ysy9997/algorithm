# https://www.acmicpc.net/problem/1026
import sys


n = int(sys.stdin.readline()[:-1])
A = list(map(int, sys.stdin.readline()[:-1].split(' ')))
B = list(map(int, sys.stdin.readline()[:-1].split(' ')))

start = 0
for n, i in enumerate(A):
    if B[0] == i:
        start = n
        break

puzzle = True
for i in range(len(A)):
    if B[i] != A[(i + start) % len(A)]:
        puzzle = False
        break

if puzzle:
    print('good puzzle')
    exit()

A.reverse()
start = 0
for n, i in enumerate(A):
    if B[0] == i:
        start = n
        break

puzzle = True
for i in range(len(A)):
    if B[i] != A[(i + start) % len(A)]:
        puzzle = False
        break

if puzzle:
    print('good puzzle')
    exit()

print('bad puzzle')
