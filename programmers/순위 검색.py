def cut_list(info, value):
    start = 0
    end = len(info)

    while True:
        p = (start + end) // 2
        if end - start < 5:
            for i in range(start, end):
                if info[i][4] >= value:
                    return info[i:]

        if info[p][4] >= value:
            end = p
        else:
            start = p


def solution(info, query):
    info = [_.split(' ') for _ in info]
    for i in range(len(info)):
        info[i][4] = int(info[i][4])
    info = sorted(info, key=lambda x: x[4])

    querys = list()
    for q in query:
        l, _, j, _, e, _, f, s = q.split(' ')
        querys.append([l, j, e, f, s])

    del query

    answer = list()

    for query in querys:
        total = 0
        if query[4] != '-':
            cut_info = cut_list(info, int(query[4]))
        else:
            cut_info = info
        for i in cut_info:
            if query[0] != '-' and query[0] != i[0]:
                continue
            if query[1] != '-' and query[1] != i[1]:
                continue
            if query[2] != '-' and query[2] != i[2]:
                continue
            if query[3] != '-' and query[3] != i[3]:
                continue
            total = total + 1
        answer.append(total)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
