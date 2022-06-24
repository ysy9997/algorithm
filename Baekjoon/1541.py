# https://www.acmicpc.net/problem/1541
import sys


def div(equ: str):
    nums = list()
    pm = list()

    p = 0
    for n, c in enumerate(equ):
        if c == '+':
            nums.append(int(equ[p:n]))
            pm.append(c)
            p = n + 1
        if c == '-':
            nums.append(int(equ[p:n]))
            pm.append(c)
            p = n + 1

    nums.append(int(equ[p:]))

    return nums, pm


equ = sys.stdin.readline()[:-1]

num, pm = div(equ)

new_num = list()
p = 0
for n, i in enumerate(pm):
    if i == '-':
        new_num.append(sum(num[p:n + 1]))
        p = n + 1

new_num.append(sum(num[p:]))

print(new_num[0] - sum(new_num[1:]))
