# https://www.acmicpc.net/problem/1074
import sys


def order(x, y):
    if x < 2 and y < 2:
        if x == 0 and y == 0:
            return 0
        elif x == 1 and y == 0:
            return 1
        elif x == 0 and y == 1:
            return 2
        elif x == 1 and y == 1:
            return 3

    max_xy = max(x, y)

    count = -1
    while max_xy > 0:
        max_xy = max_xy >> 1
        count = count + 1

    if x >= 2 ** count and y >= 2 ** count:
        x = x - 2 ** count
        y = y - 2 ** count
        return order(x, y) + 2 ** (count * 2) * 3
    elif y >= 2 ** count:
        y = y - 2 ** count
        return order(x, y) + 2 ** (count * 2) * 2
    else:
        x = x - 2 ** count
        return order(x, y) + 2 ** (count * 2) * 1


_, y, x = map(int, sys.stdin.readline()[:-1].split(' '))
print(order(x, y))
