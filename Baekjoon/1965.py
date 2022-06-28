# https://www.acmicpc.net/problem/1965
import sys


n = int(sys.stdin.readline()[:-1])
nums = list(map(int, sys.stdin.readline()[:-1].split(' ')))

count = [1 for _ in range(n)]

for p in range(1, n):
    temp = 1
    for i in range(p):
        if nums[p - i - 1] < nums[p] and count[p] + count[p - i - 1] > temp:
            temp = count[p] + count[p - i - 1]
    count[p] = temp

print(max(count))
