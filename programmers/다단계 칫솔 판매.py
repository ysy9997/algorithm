def solution(enroll, referral, seller, amount):
    graph = {'-': [None, 0]}
    for e, r in zip(enroll, referral):
        graph[e] = [r, 0]

    for s, a in zip(seller, amount):
        p = s
        a = a * 100
        while p != '-':
            a10 = a // 10
            a90 = a - a10
            a = a10
            graph[p][1] = graph[p][1] + a90
            p = graph[p][0]

            if a == 0:
                break

    answer = [graph[_][1] for _ in enroll]
    return answer
