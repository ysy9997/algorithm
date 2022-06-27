# https://www.acmicpc.net/problem/2110
import sys


def varify(home, c, l):
    c = c - 1
    i = 1
    set_home = home[0]
    while c > 0 and i < len(home):
        if home[i] - set_home >= l:
            c = c - 1
            set_home = home[i]
        i = i + 1

    return c == 0


def bi(home, c, start, end):
    if end - start < 2:
        if varify(home, c, end):
            return end
        elif varify(home, c, end - 1):
            return end - 1
        else:
            return start

    mid = (start + end) // 2

    if varify(home, c, mid):
        return bi(home, c, mid, end)
    else:
        return bi(home, c, start, mid)


n, c = map(int, sys.stdin.readline()[:-1].split(' '))

home = list()
for i in range(n):
    home.append(int(sys.stdin.readline()[:-1]))
home = sorted(home)

start = 0
end = home[-1]

print(bi(home, c, start, end))
