# https://www.acmicpc.net/problem/17276
import sys


def new_point(x, y, new):
    l = max(abs(x), abs(y))

    if new == 0:
        return -l, -l
    elif new == 1:
        return 0, -l
    elif new == 2:
        return l, -l
    elif new == 3:
        return l, 0
    elif new == 4:
        return l, l
    elif new == 5:
        return 0, l
    elif new == 6:
        return -l, l
    elif new == 7:
        return -l, 0


def rot(mat, angle):
    n = angle // 45
    middle = len(mat) // 2
    l = len(mat)
    new_mat = [[None for _ in range(l)] for _ in range(l)]

    for y in range(l):
        y = y - middle
        for x in range(l):
            x = x - middle
            if x == y and x <= 0 and y <= 0:
                p = 0
                new = (p + n) % 8
                new_x, new_y = new_point(x, y, new)
                new_mat[new_y + middle][new_x + middle] = mat[y + middle][x + middle]
            elif x == 0 and y < 0:
                p = 1
                new = (p + n) % 8
                new_x, new_y = new_point(x, y, new)
                new_mat[new_y + middle][new_x + middle] = mat[y + middle][x + middle]
            elif x == -y and x > 0 and y < 0:
                p = 2
                new = (p + n) % 8
                new_x, new_y = new_point(x, y, new)
                new_mat[new_y + middle][new_x + middle] = mat[y + middle][x + middle]
            elif x > 0 and y == 0:
                p = 3
                new = (p + n) % 8
                new_x, new_y = new_point(x, y, new)
                new_mat[new_y + middle][new_x + middle] = mat[y + middle][x + middle]
            elif x == y and x > 0 and y > 0:
                p = 4
                new = (p + n) % 8
                new_x, new_y = new_point(x, y, new)
                new_mat[new_y + middle][new_x + middle] = mat[y + middle][x + middle]
            elif x == 0 and y > 0:
                p = 5
                new = (p + n) % 8
                new_x, new_y = new_point(x, y, new)
                new_mat[new_y + middle][new_x + middle] = mat[y + middle][x + middle]
            elif x == -y and x < 0 and y > 0:
                p = 6
                new = (p + n) % 8
                new_x, new_y = new_point(x, y, new)
                new_mat[new_y + middle][new_x + middle] = mat[y + middle][x + middle]
            elif y == 0 and x < 0:
                p = 7
                new = (p + n) % 8
                new_x, new_y = new_point(x, y, new)
                new_mat[new_y + middle][new_x + middle] = mat[y + middle][x + middle]
            else:
                new_mat[y + middle][x + middle] = mat[y + middle][x + middle]

    return new_mat


n = int(sys.stdin.readline()[:-1])
for i in range(n):
    l, angle = map(int, sys.stdin.readline()[:-1].split(' '))
    matrix = [sys.stdin.readline()[:-1].split(' ') for _ in range(l)]

    new_mat = rot(matrix, angle)
    for y in range(l):
        for x in range(l):
            print(new_mat[y][x], end=' ')
        print()
