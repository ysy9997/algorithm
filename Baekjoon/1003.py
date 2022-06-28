# https://www.acmicpc.net/problem/1003
import sys


db = [[-1, -1] for i in range(41)]


def piv_count(num):
    if db[num] != [-1, -1]:
        return db[num]
    elif num == 0:
        db[0] = [1, 0]
        return [1, 0]
    elif num == 1:
        db[1] = [0, 1]
        return [0, 1]

    else:
        a = piv_count(num - 1)
        b = piv_count(num - 2)

        db[num] = [a[0] + b[0], a[1] + b[1]]
        return db[num]


n = int(sys.stdin.readline()[:-1])

nums = [int(sys.stdin.readline()[:-1]) for _ in range(n)]

for num in nums:
    z, o = piv_count(num)
    print(z, o)
