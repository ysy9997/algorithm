import time


def binary_search(l, v):
    start = 0
    end = len(l) - 1

    while True:
        if start - end < 3:
            for i in range(start, end):
                if v < a[i]:
                    return i

        mid = (start + end) // 2
        if l[mid] > v:
            start = mid
        else:
            end = mid


a = [_ for _ in range(10000)]

v = 1


start = time.time()
a = sorted(a)
for i in range(len(a)):
    if v < a[i]:
        index = i
        break
print(a[:index])
end = time.time()

print(end - start)

start = time.time()
a = sorted(a)
print(a[:binary_search(a, v)])
end = time.time()

print(end - start)
