# https://www.acmicpc.net/problem/2108
import sys

l = int(sys.stdin.readline()[:-1])

nums = [0 for _ in range(8001)]
_sum = 0
max_v = -9000
min_v = 9000
for i in range(l):
    n = int(sys.stdin.readline()[:-1])
    nums[n + 4000] = nums[n + 4000] + 1
    _sum = _sum + n
    if max_v < n:
        max_v = n
    if min_v > n:
        min_v = n

print(round(_sum / l))

count = 0
second = 0
save = None
fre = max(nums)
varify = [None, None]
for key in range(8001):
    con = nums[key]
    if con != 0:
        count = count + con
        if count > l // 2 and save is None:
            save = key - 4000
        if con == fre:
            if varify[0] is None:
                varify[0] = key - 4000
            elif varify[1] is None:
                varify[1] = key - 4000

        if varify[1] is not None and save is not None:
            break

print(save)
if varify[1] is not None:
    print(varify[1])
else:
    print(varify[0])
print(max_v - min_v)
