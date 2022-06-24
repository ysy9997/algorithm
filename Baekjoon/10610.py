# https://www.acmicpc.net/problem/10610
import sys


s = sys.stdin.readline()[:-1]
nums = sorted([int(_) for _ in s], reverse=True)

if nums[-1] != 0:
    print(-1)
    exit()

if sum(nums) % 3 != 0:
    print(-1)
    exit()

for i in nums:
    print(i, end='')
