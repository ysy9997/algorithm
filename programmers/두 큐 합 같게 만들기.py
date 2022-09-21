import collections


def solution(queue1, queue2):
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    mid = (sum1 + sum2) // 2
    total_l = len(queue1) + len(queue2)

    queue1 = collections.deque(queue1)
    queue2 = collections.deque(queue2)

    count = 0
    while sum1 != mid:
        if sum1 > mid:
            temp = queue1.popleft()
            sum1 = sum1 - temp
            queue2.append(temp)
            sum2 = sum2 + temp
        else:
            temp = queue2.popleft()
            sum2 = sum2 - temp
            queue1.append(temp)
            sum1 = sum1 + temp

        count = count + 1

        if count > total_l * 2:
            count = -1
            break

    return count
