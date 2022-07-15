# https://www.acmicpc.net/problem/1463
import sys


n = int(sys.stdin.readline()[:-1])

dp = [-1 for i in range(n + 1)]
dp[0] = 0
dp[1] = 0

for i in range(2, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        dp[i] = dp[i - 1] + 1
    elif i % 2 == 0 and i % 3 != 0:
        res = min(dp[i // 2], dp[i - 1]) + 1
        dp[i] = res
    elif i % 2 != 0 and i % 3 == 0:
        res = min(dp[i // 3], dp[i - 1]) + 1
        dp[i] = res
    else:
        res = min(dp[i // 2], dp[i // 3], dp[i - 1]) + 1
        dp[i] = res

print(dp[n])
