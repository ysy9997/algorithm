def match2rank(num):
    num = -(num - 7)
    if num > 6:
        num = 6
    return num


def solution(lottos, win_nums):
    _lottos = [_ for _ in lottos]

    count = 0
    for lotto in _lottos:
        if lotto != 0:
            if lotto in win_nums:
                win_nums.remove(lotto)
                count = count + 1
            lottos.remove(lotto)

    _max = count + len(lottos)

    answer = [match2rank(_max), match2rank(count)]
    return answer
