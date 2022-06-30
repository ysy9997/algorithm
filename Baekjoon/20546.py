# https://www.acmicpc.net/problem/20546
import sys


cash = int(sys.stdin.readline()[:-1])
prices = list(map(int, sys.stdin.readline()[:-1].split(' ')))

increase = 0
decrease = 0
previous_price = None

bnp_cash = cash
timing_cash = cash
bnp_stock = 0
timing_stock = 0

for price in prices:
    buy = (bnp_cash // price)
    bnp_cash = bnp_cash - buy * price
    bnp_stock = bnp_stock + buy

    if previous_price is not None:
        if previous_price < price:
            increase = increase + 1
            decrease = 0
        elif previous_price > price:
            decrease = decrease + 1
            increase = 0
        else:
            increase = 0
            decrease = 0

        if increase >= 3:
            timing_cash = timing_cash + timing_stock * price
            timing_stock = 0
        elif decrease >= 3:
            buy = (timing_cash // price)
            timing_cash = timing_cash - buy * price
            timing_stock = timing_stock + buy

    previous_price = price

if bnp_cash + bnp_stock * prices[-1] > timing_cash + timing_stock * prices[-1]:
    print('BNP')
elif bnp_cash + bnp_stock * prices[-1] < timing_cash + timing_stock * prices[-1]:
    print('TIMING')
else:
    print('SAMESAME')
