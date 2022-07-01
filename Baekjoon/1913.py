# https://www.acmicpc.net/problem/1913
# wrong
import sys


odd_n = int(sys.stdin.readline()[:-1])
r_n = int(sys.stdin.readline()[:-1])

graph = [[False for _ in range(odd_n)] for _ in range(odd_n)]
steps = [_ for _ in range(1, odd_n)]

p_n = 1
p_x, p_y = odd_n // 2, odd_n // 2
graph[p_y][p_x] = p_n
remember = [1, 1]

while p_n < odd_n ** 2:
    for step in steps:
        if step % 2 == 1:
            for i in range(step):
                p_y = p_y - 1
                p_n = p_n + 1
                graph[p_y][p_x] = p_n
                if p_n == r_n:
                    remember[0] = p_y + 1
                    remember[1] = p_x + 1
            for i in range(step):
                p_x = p_x + 1
                p_n = p_n + 1
                graph[p_y][p_x] = p_n
                if p_n == r_n:
                    remember[0] = p_y + 1
                    remember[1] = p_x + 1
        else:
            for i in range(step):
                p_y = p_y + 1
                p_n = p_n + 1
                graph[p_y][p_x] = p_n
                if p_n == r_n:
                    remember[0] = p_y + 1
                    remember[1] = p_x + 1
            for i in range(step):
                p_x = p_x - 1
                p_n = p_n + 1
                graph[p_y][p_x] = p_n
                if p_n == r_n:
                    remember[0] = p_y + 1
                    remember[1] = p_x + 1

    for i in range(steps[-1]):
        p_y = p_y - 1
        p_n = p_n + 1
        graph[p_y][p_x] = p_n
        if p_n == r_n:
            remember[0] = p_y + 1
            remember[1] = p_x + 1

for g in graph:
    for i in g:
        print(i, end=' ')
    print()

print(f'{remember[0]} {remember[1]}')
