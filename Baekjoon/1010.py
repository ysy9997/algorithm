# https://www.acmicpc.net/problem/1010
import sys

def factorial(n):
    if n == 0:
        return 1

    result = 1
    while n > 1:
        result = result * n
        n = n - 1

    return result


def conbination(n, r):
    up = 1
    for i in range(r):
        up = up * (n - i)

    return round(up / factorial(r))


if __name__ == '__main__':
    n = int(sys.stdin.readline()[:-1])

    a = list()
    b = list()
    for _ in range(n):
        _a, _b = sys.stdin.readline()[:-1].split(' ')
        a.append(int(_a))
        b.append(int(_b))

    results = list()
    for _a, _b in zip(a, b):
        results.append(conbination(_b, _a))

    for result in results:
        print(result)
