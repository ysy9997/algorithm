# https://www.acmicpc.net/problem/2343
import sys


def video_list(videos, m, _max):
    total = [0 for _ in range(m)]
    p = 0
    for i in videos:
        if total[p] + i <= _max:
            total[p] = total[p] + i
        else:
            p = p + 1
            if p >= m or i > _max:
                return False
            total[p] = total[p] + i
    return True


def bi(videos, m, start, end):
    if end - start < 2:
        if video_list(videos, m, start):
            return start
        elif video_list(videos, m, start + 1):
            return start + 1
        else:
            return start + 2

    mid = (start + end) // 2
    if video_list(videos, m, mid):
        return bi(videos, m, start, mid)
    else:
        return bi(videos, m, mid, end)


n, m = map(int, sys.stdin.readline()[:-1].split(' '))
videos = list(map(int, sys.stdin.readline()[:-1].split(' ')))

start = 0
end = sum(videos)

print(bi(videos, m, start, end))

