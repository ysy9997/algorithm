# https://www.acmicpc.net/problem/17413
import sys


def reverse(s):
    return s[::-1]


string = sys.stdin.readline()[:-1]
n = len(string)

left = 0
new = list()
for n, s in enumerate(string):
    if s == '<':
        [new.append(_) for _ in list(map(reverse, string[left:n].split(' ')))]
        left = n
    elif s == '>':
        new.append(string[left:n + 1])
        left = n + 1

[new.append(reverse(_)) for _ in string[left:].split(' ')]

pre_string = None
for s in new:
    if pre_string is not None and '<' not in pre_string and '<' not in s:
        print(' ', end='')
    print(s, end='')
    pre_string = s
