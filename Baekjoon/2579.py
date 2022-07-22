# https://www.acmicpc.net/problem/2579
import sys


scores = [int(sys.stdin.readline()[:-1]) for _ in range(int(sys.stdin.readline()[:-1]))]

if len(scores) == 1:
    print(scores[0])
else:
    total = [0 for _ in range(len(scores))]
    total[0] = scores[0]
    total[1] = scores[0] + scores[1]

    for n in range(2, len(scores)):
        total[n] = max(total[n - 3] + scores[n - 1] + scores[n], total[n - 2] + scores[n])

    print(total[-1])

