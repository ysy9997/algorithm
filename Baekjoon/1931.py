import sys


n = int(sys.stdin.readline()[:-1])

conf = list()
for i in range(n):
    start, end = map(int, sys.stdin.readline()[:-1].split(' '))
    conf.append([end, start])
conf = sorted(conf)

double = False
p = 0
opened = 0
for end, start in conf:
    if p <= start:
        p = int(end)
        opened = opened + 1

print(opened)
