# https://www.acmicpc.net/problem/10989
import sys

n = int(sys.stdin.readline()[:-1])

nums = [0 for _ in range(10000)]
for i in range(n):
    n = int(sys.stdin.readline()[:-1])
    nums[n - 1] = nums[n - 1] + 1

for i in range(len(nums)):
    for _ in range(nums[i]):
        print(i + 1)
