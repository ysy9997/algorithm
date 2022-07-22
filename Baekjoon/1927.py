# https://www.acmicpc.net/problem/1927
import sys
import heapq


n = int(sys.stdin.readline()[:-1])
h = list()


for _ in range(n):
    num = int(sys.stdin.readline()[:-1])
    if num == 0:
        if len(h) != 0:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, num)
