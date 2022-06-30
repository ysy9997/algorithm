# https://www.acmicpc.net/problem/1244
# wrong
import sys


n = int(sys.stdin.readline()[:-1])
switches = list(map(bool, list(map(int, sys.stdin.readline()[:-1].split(' ')))))
stu_n = int(sys.stdin.readline()[:-1])
students = [list(map(int, sys.stdin.readline()[:-1].split(' '))) for _ in range(stu_n)]

for student in students:
    if student[0] == 1:
        for i in range(n):
            if (i + 1) % student[1] == 0:
                switches[i] = not switches[i]

    else:
        student[1] = student[1] - 1
        switches[student[1]] = not switches[student[1]]
        for i in range(min(student[1], n - student[1] - 1)):
            if switches[student[1] - i - 1] == switches[student[1] + i + 1]:
                switches[student[1] - i - 1] = not switches[student[1] - i - 1]
                switches[student[1] + i + 1] = not switches[student[1] + i + 1]
            else:
                break

    for switch in switches:
        print(int(switch), end=' ')
    print()

for n, switch in enumerate(switches):
    print(int(switch), end=' ')
    if (n + 1) % 20 == 0:
        print()

# 25
# 1 0 1 1 0 1 0 0 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 0 1
# 3
# 2 3
# 1 5
# 2 6