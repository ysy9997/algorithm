import itertools

db = list()


def varify(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def list2int(l):
    out = ''
    for i in l:
        out = out + i
    return int(out)


def solution(numbers):
    answer = 0

    for i in range(1, len(numbers) + 1):
        nums = list(itertools.permutations(numbers, i))

        for n in nums:
            _n = list2int(n)
            if _n not in db:
                answer = answer + varify(_n)
                db.append(_n)

    return answer
