# https://www.acmicpc.net/problem/9095
import sys

dp = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274]

for i in range(int(sys.stdin.readline()[:-1])):
    print(dp[int(sys.stdin.readline()[:-1]) - 1])
