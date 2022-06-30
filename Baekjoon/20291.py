# https://www.acmicpc.net/problem/20291
import sys


n = int(sys.stdin.readline()[:-1])
files = [sys.stdin.readline()[:-1].split('.')[-1] for _ in range(n)]

extend = dict()
for file in files:
    if file not in extend.keys():
        extend[file] = 1
    else:
        extend[file] = extend[file] + 1

keys = sorted(extend.keys())
for key in keys:
    print(key, extend[key])
