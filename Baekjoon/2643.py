# https://www.acmicpc.net/problem/2110
# wrong
import sys


def link(papers):
    n = len(papers)
    graph = [[False for _ in range(n)] for _ in range(n)]

    for y in range(n):
        paper = papers[y]
        for x in range(n):
            c_paper = papers[x]
            if (paper[0] >= c_paper[0] and paper[1] >= c_paper[1]) or (paper[0] >= c_paper[1] and paper[1] >= c_paper[0]):
                graph[y][x] = True

    return graph


def link_count(papers):
    n = len(papers)
    graph = [0 for _ in range(n)]

    for y in range(n):
        paper = papers[y]
        for x in range(n):
            c_paper = papers[x]
            if (paper[0] >= c_paper[0] and paper[1] >= c_paper[1]) or (paper[0] >= c_paper[1] and paper[1] >= c_paper[0]):
                graph[y] = graph[y] + 1

    return graph


n = int(sys.stdin.readline()[:-1])
papers = [list(map(int, sys.stdin.readline()[:-1].split(' '))) for _ in range(n)]
total = link_count(papers)

sorted_papers = [0 for _ in range(n)]
for i, paper in zip(range(n), papers):
    sorted_papers[i] = [total[i], paper]
sorted_papers = sorted(sorted_papers, reverse=True)
sorted_papers = [_[1] for _ in sorted_papers]

graph = link(sorted_papers)
total = sorted(total, reverse=True)

p = 0
count = 1
while p < n - 1:
    var = False
    for i in range(p + 1, n):
        if graph[p][i]:
            count = count + 1
            p = i
            var = True
            break
    if not var:
        break

print(count)

