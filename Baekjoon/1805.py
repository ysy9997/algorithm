# https://www.acmicpc.net/problem/1181
import sys


def cut(ls, h):
    total = 0
    for l in ls:
        if l > h:
            total = total + l - h
    return total


n, m = map(int, sys.stdin.readline()[:-1].split(' '))
trees = list(map(int, sys.stdin.readline()[:-1].split(' ')))

start = 0
end = max(trees)

result = 0
while start <= end:
    mid = (start + end) // 2
    branch = cut(trees, mid)
    if branch < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    # else:
    #     break

print(result)
