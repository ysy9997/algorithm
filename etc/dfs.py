def dfs(graph, p, visit, order):
    visit[p] = True
    order.append(p + 1)

    for i in graph[p]:
        if not visit[i]:
            order = dfs(graph, i, visit, order)

    return order


def dfs_(p, graph):
    visit = [False for _ in range(len(graph))]
    order = list()
    stack = list()
    stack.append(p)
    order.append(p)
    visit[p] = True

    while stack:
        p = stack[-1]
        visit_p = False
        for i in graph[p]:
            if not visit[i]:
                visit[i] = True
                stack.append(i)
                order.append(i + 1)
                visit_p = True
                break

        if not visit_p:
            stack = stack[:-1]

    return order


graph = [[1, 2, 7], [0, 6], [0, 3, 4], [2, 4], [2, 3], [6], [1, 5, 7], [0, 6]]
visit = [False for _ in range(8)]
order = list()

stack = list()
stack.append(0)
order.append(1)
visit[0] = True

while stack:
    p = stack[-1]
    visit_p = False
    for i in graph[p]:
        if not visit[i]:
            visit[i] = True
            stack.append(i)
            order.append(i + 1)
            visit_p = True
            break

    if not visit_p:
        stack = stack[:-1]

print(order)
#[1, 2, 7, 6, 8, 3, 4, 5]
