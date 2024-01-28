# https://www.acmicpc.net/problem/1259
import sys

if __name__ == '__main__':
    words = list()
    while True:
        word = sys.stdin.readline()[:-1]
        if word == '0':
            break
        else:
            words.append(word)

    results = list()
    for word in words:
        if word == word[::-1]:
            results.append('yes')
        else:
            results.append('no')

    for result in results:
        print(result)
