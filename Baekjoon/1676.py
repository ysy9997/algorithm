# https://www.acmicpc.net/problem/1676
import sys


def count5(n):
    count = 0
    while n % 5 == 0:
        n = n // 5
        count = count + 1

    return count

n = int(sys.stdin.readline()[:-1])

count = 0
for i in range(1, n + 1):
    count = count + count5(i)

print(count)
