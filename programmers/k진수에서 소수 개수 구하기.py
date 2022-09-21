def convert(k, n):
    nums = 0

    i = 0
    while n > k:
        nums = nums + ((n % k) * 10 ** i)
        n = n // k
        i = i + 1
    nums = nums + ((n % k) * 10 ** i)

    return str(nums)


def ver_pri(num):
    if num == '':
        return False
    num = int(num)
    if num == 1:
        return False
    if num == 2:
        return True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def solution(n, k):
    n = convert(k, n)
    ns = n.split('0')

    answer = 0

    for i in ns:
        answer = answer + ver_pri(i)

    return answer