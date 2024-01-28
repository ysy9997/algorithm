# https://www.acmicpc.net/problem/1094
import sys


def iteration(bars: list, size: int):
    bar = bars[-1]
    bars = bars[:-1]
    bars.append(bar // 2)
    if sum(bars) < size:
        bars.append(bar)
        return bars, 1

    return bars, 0


if __name__ == '__main__':
    bars = [64]
    size = int(sys.stdin.readline()[:-1])

    n = 1
    while sum(bars) > size:
        bars, result = iteration(bars, size)
        n = n + result

    print(n)
