# https://www.acmicpc.net/problem/25285
import sys


def grading(hw):
    h, w = hw

    if h < 140.1:
        return 6
    elif h < 146:
        return 5
    elif h < 159:
        return 4
    elif h < 161:
        h100 = h / 100
        bmi = w / (h100 * h100)
        if bmi < 16 or bmi >= 35:
            return 4
        else:
            return 3
    elif h < 204:
        h100 = h / 100
        bmi = w / (h100 * h100)
        if bmi < 16 or bmi >= 35:
            return 4
        elif bmi < 18.5 or bmi >= 30:
            return 3
        elif bmi < 20 or bmi >= 25:
            return 2
        else:
            return 1
    else:
        return 4


n = int(sys.stdin.readline()[:-1])

hw = list()
for i in range(n):
    h, w = sys.stdin.readline()[:-1].split(' ')
    hw.append([int(h), int(w)])

for i in hw:
    print(grading(i))