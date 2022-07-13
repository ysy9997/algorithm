# https://www.acmicpc.net/problem/1107
import sys
import math


def only_updown(n, p):
    if n < p:
        return p - n
    else:
        return n - p


def num2list(n):
    split = list()
    if n == 0:
        return [0]
    while n != 0:
        split.append(n % 10)
        n = n // 10

    return split[::-1]


def close_n(n, broken):
    if len(broken) == 10:
        return 100
    l = 0

    while True:
        minus = n - l
        if minus > -1:
            split_minus = num2list(minus)

            varify = True
            for i in split_minus:
                if i in broken:
                    varify = False
                    break

            if varify:
                return minus

        plus = n + l
        split_plus = num2list(plus)

        varify = True
        for i in split_plus:
            if i in broken:
                varify = False
                break

        if varify:
            return plus

        l = l + 1


n = int(sys.stdin.readline()[:-1])
m = int(sys.stdin.readline()[:-1])
broken = list(map(int, sys.stdin.readline()[:-1].split(' '))) if m > 0 else list()

temp = close_n(n, broken)
l = int(math.log10(temp)) + 1 if temp != 0 else 1
print(min(only_updown(n, 100), only_updown(n, temp) + l))
