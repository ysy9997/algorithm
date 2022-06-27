# https://www.acmicpc.net/problem/1654
import sys


def varify(cables, n, value):
    total = 0
    for cable in cables:
        total = total + (cable // value)

    return total >= n


def bi(cables, n, start, end):
    if end - start < 2:
        if varify(cables, n, end):
            return end
        elif varify(cables, n, end - 1):
            return end - 1
        else:
            return end - 2

    mid = (start + end) // 2

    if varify(cables, n, mid):
        return bi(cables, n, mid, end)
    else:
        return bi(cables, n, start, mid)


k, n = map(int, sys.stdin.readline()[:-1].split(' '))

cables = list()
for i in range(k):
    cables.append(int(sys.stdin.readline()[:-1]))

start = 1
end = max(cables)

print(bi(cables, n, start, end))
