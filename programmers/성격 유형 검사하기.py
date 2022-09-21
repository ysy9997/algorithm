def solution(survey, choices):
    person = [0, 0, 0, 0]
    choices = [-(_ - 4) for _ in choices]
    survey = [_[0] for _ in survey]

    for s, c in zip(survey, choices):
        if c == 0:
            pass
        if s == 'T' or s == 'F' or s == 'M' or s == 'N':
            c = -c
        if s == 'R' or s == 'T':
            person[0] = person[0] + c
        elif s == 'C' or s == 'F':
            person[1] = person[1] + c
        elif s == 'J' or s == 'M':
            person[2] = person[2] + c
        else:
            person[3] = person[3] + c

        print(person)

    answer = ''
    answer = answer + 'R' if person[0] >= 0 else answer + 'T'
    answer = answer + 'C' if person[1] >= 0 else answer + 'F'
    answer = answer + 'J' if person[2] >= 0 else answer + 'M'
    answer = answer + 'A' if person[3] >= 0 else answer + 'N'

    return answer
