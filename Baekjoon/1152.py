# https://www.acmicpc.net/problem/1152
import sys

if __name__ == '__main__':
    string = sys.stdin.readline()[:-1]

    space = True
    num = 0
    for c in string:
        if c != ' ' and space:
            num = num + 1
            space = False
        elif c == ' ':
            space = True

    print(num)
