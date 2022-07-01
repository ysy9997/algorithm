def cor(s):
    stack = 0
    for c in s:
        if c == '(':
            stack = stack + 1
        else:
            stack = stack - 1
        if stack < 0:
            return False
    return True


def devUV(s):
    stack = 0
    bal = 0
    for n, c in enumerate(s):
        if c == '(':
            stack = stack + 1
        else:
            stack = stack - 1
        if stack == 0:
            bal = n
            break

    return s[:bal + 1], s[bal + 1:]


def fun(v):
    if v == '':
        return ''

    u, v = devUV(v)
    if cor(u):
        return f'{u}{fun(v)}'
    else:
        u = u[1:-1]
        new = ''
        for s in u:
            if s == '(':
                new = new + ')'
            else:
                new = new + '('
        return f'({fun(v)}){new}'


# def solution(p):
#     return fun(p)
print(fun("()))((()"))
