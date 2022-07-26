# https://www.acmicpc.net/problem/7576
import sys
import heapq


for _ in range(int(sys.stdin.readline()[:-1])):
    visited = [False for _ in range(1_000_001)]

    h_max = list()
    h_min = list()
    for i in range(int(sys.stdin.readline()[:-1])):
        command, num = sys.stdin.readline()[:-1].split(' ')
        if command == 'I':
            num = int(num)
            heapq.heappush(h_max, [-num, i])
            heapq.heappush(h_min, [num, i])
            visited[i] = True
        elif num == '-1':
            while h_min and not visited[h_min[0][1]]:
                heapq.heappop(h_min)
            if len(h_min) > 0:
                _, c_id = heapq.heappop(h_min)
                visited[c_id] = False
        else:
            while h_max and not visited[h_max[0][1]]:
                heapq.heappop(h_max)
            if len(h_max) > 0:
                _, c_id = heapq.heappop(h_max)
                visited[c_id] = False

    _max = None
    _min = None
    while h_max:
        n, c_id = heapq.heappop(h_max)
        if visited[c_id]:
            _max = n
            break
    while h_min:
        n, c_id = heapq.heappop(h_min)
        if visited[c_id]:
            _min = n
            break

    print(-_max, _min) if _max is not None else print('EMPTY')
