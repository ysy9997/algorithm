import itertools


def varify(key, query):
    for c in key:
        if c not in query:
            return False
    return True


def list2str(l):
    out = ''
    for i in l:
        out = out + i
    return out


def solution(orders, course):
    check = dict()

    for c in course:
        for order in orders:
            candies = itertools.combinations(order, c)
            for candi in candies:
                candi = tuple(sorted(list(candi)))
                if candi not in check.keys():
                    check[candi] = 0
                    for o in orders:
                        if varify(candi, o):
                            check[candi] = check[candi] + 1

    can = dict()
    for c in course:
        can[c] = [[None], 0]

    for key in check.keys():
        c = len(key)
        if check[key] > 1:
            if can[c][1] < check[key]:
                can[c] = [[key], check[key]]
            elif can[c][1] == check[key]:
                can[c][0].append(key)

    answer = list()
    for key in can.keys():
        for i in can[key][0]:
            if i is not None:
                answer.append(list2str(i))

    return sorted(answer)
