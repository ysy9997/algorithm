# https://www.acmicpc.net/problem/1018
import sys


Y, X = map(int, sys.stdin.readline()[:-1].split(' '))
board = list()
for y in range(Y):
    board.append(sys.stdin.readline()[:-1])

wb = ['W', 'B']

min_count = 1e9
for cy in range(Y - 8 + 1):
    for cx in range(X - 8 + 1):
        count_wb = 0
        for y in range(cy, cy + 8):
            for x in range(cx, cx + 8):
                if board[y][x] != wb[(y + x) % 2]:
                    count_wb = count_wb + 1
        _min = min(count_wb, 64 - count_wb)
        if min_count > _min:
            min_count = _min
        if min_count == 0:
            print(0)
            exit()

print(min_count)
