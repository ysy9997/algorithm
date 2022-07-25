# https://www.acmicpc.net/problem/2630
import sys
import collections


def cut(paper):
    papers = [list() for _ in range(4)]

    l = len(paper)
    for n, p in enumerate(papers):
        for i in range(n // 2 * (l // 2), n // 2 * (l // 2) + l // 2):
            p.append(paper[i][(l // 2) * (n % 2):(l // 2) * (n % 2 + 1)])

    return papers


def varify(paper):
    l = len(paper)
    n = paper[0][0]

    var = True
    for x in range(l):
        for y in range(l):
            if paper[x][y] != n:
                var = False
                break
        if not var:
            break

    return var


n = int(sys.stdin.readline()[:-1])

paper = list()
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline()[:-1].split(' '))))

papers = collections.deque()
papers.append(paper)
del paper
m_z_o = {0: 0, 1: 0}

while papers:
    paper = papers.popleft()
    if varify(paper):
        m_z_o[paper[0][0]] = m_z_o[paper[0][0]] + 1
    else:
        paper = cut(paper)
        for c in paper:
            papers.append(c)

print(m_z_o[0])
print(m_z_o[1])
