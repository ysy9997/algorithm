# https://www.acmicpc.net/problem/2529
import sys


def count_in(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '<':
            count = count + 1
        else:
            break
    return count


def count_de(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '>':
            count = count + 1
        else:
            break
    return count


def sort_max(l, comp):
    new = list()

    i = 0
    while i < len(comp):
        if comp[i] == '>':
            new.append(l.pop(0))
            i = i + 1
        else:
            count = count_in(comp[i:])
            i = i + count + 1
            for x in [_ for _ in range(count + 1)][::-1]:
                new.append(l.pop(x))

    if len(l) == 1: new.append(l[0])
    return new


def sort_min(l, comp):
    new = list()

    i = 0
    while i < len(comp):
        if comp[i] == '<':
            new.append(l.pop(0))
            i = i + 1
        else:
            count = count_de(comp[i:])
            i = i + count + 1
            for x in [_ for _ in range(count + 1)][::-1]:
                new.append(l.pop(x))

    if len(l) == 1: new.append(l[0])
    return new


n = int(sys.stdin.readline()[:-1])
comp = sys.stdin.readline()[:-1].split(' ')

max_list = [_ for _ in range(9 - n, 10)][::-1]
min_list = [_ for _ in range(n + 1)]

max_list = sort_max(max_list, comp)
min_list = sort_min(min_list, comp)

for i in max_list:
    print(i, end='')
print()
for i in min_list:
    print(i, end='')
