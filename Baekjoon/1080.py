# https://www.acmicpc.net/problem/1080
import sys


def reverse(mat, x, y):
    mat[y][x] = int(not mat[y][x])
    mat[y + 1][x] = int(not mat[y + 1][x])
    mat[y + 2][x] = int(not mat[y + 2][x])
    mat[y][x + 1] = int(not mat[y][x + 1])
    mat[y + 1][x + 1] = int(not mat[y + 1][x + 1])
    mat[y + 2][x + 1] = int(not mat[y + 2][x + 1])
    mat[y][x + 2] = int(not mat[y][x + 2])
    mat[y + 1][x + 2] = int(not mat[y + 1][x + 2])
    mat[y + 2][x + 2] = int(not mat[y + 2][x + 2])

    return mat


n, m = map(int, sys.stdin.readline()[:-1].split(' '))

A = list()
for i in range(n):
    A.append([int(_) for _ in sys.stdin.readline()[:-1]])

B = list()
for i in range(n):
    B.append([int(_) for _ in sys.stdin.readline()[:-1]])

cnt = 0
for y in range(n - 2):
    for x in range(m - 2):
        if A[y][x] != B[y][x]:
            A = reverse(A, x, y)
            cnt = cnt + 1

if A == B:
    print(cnt)
else:
    print(-1)
