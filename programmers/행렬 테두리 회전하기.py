def rot_min(mat, query, only_min: bool = False):
    y_min, x_min, y_max, x_max = query
    y_min, x_min, y_max, x_max = y_min - 1, x_min - 1, y_max - 1, x_max - 1

    nums = list()

    for x in range(x_min, x_max + 1):
        nums.append(mat[y_min][x])

    for y in range(y_min + 1, y_max + 1):
        nums.append(mat[y][x_max])

    xs = [_ for _ in range(x_min, x_max)]
    xs.reverse()
    for x in xs:
        nums.append(mat[y_max][x])

    ys = [_ for _ in range(y_min + 1, y_max)]
    ys.reverse()
    for y in ys:
        nums.append(mat[y][x_min])

    if only_min:
        return min(nums)

    nums = [nums[-1]] + nums[:-1]

    i = 0
    for x in range(x_min, x_max + 1):
        mat[y_min][x] = nums[i]
        i = i + 1

    for y in range(y_min + 1, y_max + 1):
        mat[y][x_max] = nums[i]
        i = i + 1

    for x in xs:
        mat[y_max][x] = nums[i]
        i = i + 1

    for y in ys:
        mat[y][x_min] = nums[i]
        i = i + 1

    return mat, min(nums)


def matrix(rows, columns):
    return [[x + y * columns + 1 for x in range(columns)] for y in range(rows)]


def solution(rows, columns, queries):
    mat = matrix(rows, columns)

    mins = list()
    for query in queries[:-1]:
        mat, min_num = rot_min(mat, query)
        mins.append(min_num)

    mins.append(rot_min(mat, queries[-1], True))

    return mins
