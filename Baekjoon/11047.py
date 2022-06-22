import sys


n, k = map(int, sys.stdin.readline()[:-1].split(' '))

coin = list()
for i in range(n):
    coin.append(int(sys.stdin.readline()[:-1]))

count = 0
while k != 0:
    p_coin = coin.pop(-1)
    share = k // p_coin
    k = k % p_coin
    count = count + share

print(count)
