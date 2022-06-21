import sys


def dfs(x, y, visit):

    stack = [[x, y]]
    visit[x][y] = False

    while len(stack) != 0:
        x, y = stack.pop(-1)

        if x > 0:
            if visit[x - 1][y]:
                visit[x - 1][y] = False
                stack.append([x, y])
                stack.append([x - 1, y])
        if x < len(visit) - 1:
            if visit[x + 1][y]:
                visit[x + 1][y] = False
                stack.append([x, y])
                stack.append([x + 1, y])
        if y > 0:
            if visit[x][y - 1]:
                visit[x][y - 1] = False
                stack.append([x, y])
                stack.append([x, y - 1])
        if y < len(visit[0]) - 1:
            if visit[x][y + 1]:
                visit[x][y + 1] = False
                stack.append([x, y])
                stack.append([x, y + 1])


def graph(h, w, cab):
    ground = [[False for _ in range(w)] for _ in range(h)]

    for _ in range(cab):
        x, y = map(int, sys.stdin.readline()[:-1].split(' '))
        ground[x][y] = True

    return ground


def count():
    h, w, cab = map(int, sys.stdin.readline()[:-1].split(' '))

    ground = graph(h, w, cab)

    cnt = 0
    for x in range(h):
        for y in range(w):
            if ground[x][y]:
                cnt = cnt + 1
                dfs(x, y, ground)

    print(cnt)


if __name__ == '__main__':
    t = int(sys.stdin.readline()[:-1])

    for i in range(t):
        count()
