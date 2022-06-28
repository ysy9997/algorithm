# https://www.acmicpc.net/problem/1965
import sys


n = int(sys.stdin.readline()[:-1])

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a = 1
    b = 2
    for i in range(n - 2):
        new = (a + b) % 15746
        a = b
        b = new
    print(b)
