# https://www.acmicpc.net/problem/1427
import sys


[print(i, end='') for i in sorted(sys.stdin.readline()[:-1], reverse=True)]
