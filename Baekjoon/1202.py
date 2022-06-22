# https://www.acmicpc.net/problem/1080
# time over
import sys


n, k = map(int, sys.stdin.readline()[:-1].split(' '))

gems = list()
for i in range(n):
    m, v = map(int, sys.stdin.readline()[:-1].split(' '))
    gems.append([v, m])
gems = sorted(gems, reverse=True)

bags = list()
for i in range(k):
    bags.append(int(sys.stdin.readline()[:-1]))
bags = sorted(bags)

can = list()
for bag in bags:
    v = -1
    save = -1
    for i, gem in enumerate(gems):
        if gem[1] <= bag and v < gem[0]:
            save = i
            v = gem[0]
            break
    if save != -1:
        can.append(gems.pop(save))

print(sum([_[0] for _ in can]))
