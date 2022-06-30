# https://www.acmicpc.net/problem/17276
import sys


def rot(mat, angle):
    n = angle // 45
    middle = len(mat) // 2

    clock = True
    if n < 0:
        clock = False
        n = -n

    # 기본 점이 8 방향 중 하나에 있고, 거기서 다른 방향으로 이동시켜주면 됨




n = int(sys.stdin.readline()[:-1])
for i in range(n):
    l, angle = map(int, sys.stdin.readline()[:-1].split(' '))
    matrix = [sys.stdin.readline()[:-1].split(' ') for _ in range(l)]
