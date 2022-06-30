# https://www.acmicpc.net/problem/17276
import sys


def rot(mat, angle):
    n = angle // 45
    middle = len(mat) // 2

    clock = True
    if n < 0:
        clock = False
        n = -n




n = int(sys.stdin.readline()[:-1])
for i in range(n):
    l, angle = map(int, sys.stdin.readline()[:-1].split(' '))
    matrix = [sys.stdin.readline()[:-1].split(' ') for _ in range(l)]
