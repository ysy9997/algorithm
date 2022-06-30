# https://www.acmicpc.net/problem/12933
import sys


sound = sys.stdin.readline()[:-1]

order = {'q': 0, 'u': 0, 'a': 0, 'c': 0}
max_v = 0

for s in sound:
    if s != 'k':
        order[s] = order[s] + 1
    else:
        for key in order.keys():
            order[key] = order[key] - 1
            if order[key] < 0:
                print(-1)
                exit()

    if order['q'] >= order['u'] >= order['a'] >= order['c']:
        if max_v < order['q']:
            max_v = order['q']
    else:
        print(-1)
        exit()

for key in order.keys():
    if order[key] != 0:
        print(-1)
        exit()
print(max_v)
