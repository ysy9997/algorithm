# https://www.acmicpc.net/problem/1920
import sys


def bi(db, q, start, end):
    if end - start < 2:
        return int(q in db[start:end])
    else:
        mid = (start + end) // 2
        if q < db[mid]:
            end = mid
        else:
            start = mid

        return bi(db, q, start, end)


n = int(sys.stdin.readline()[:-1])
db = sorted(list(map(int, sys.stdin.readline()[:-1].split(' '))))

_ = sys.stdin.readline()
query = list(map(int, sys.stdin.readline()[:-1].split(' ')))

for q in query:
    a = bi(db, q, 0, len(db))
    print(a)
