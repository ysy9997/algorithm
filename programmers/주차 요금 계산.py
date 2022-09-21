def cal(fees, time):
    base_time, base_fee, scale, scale_fee = fees

    if time < base_time:
        return base_fee
    else:
        time = time - base_time
        return base_fee + (time // scale + bool(time % scale)) * scale_fee


def solution(fees, records):
    cars = dict()

    for record in records:
        time, car, state = record.split(' ')
        h, m = map(int, time.split(':'))
        time = 60 * h + m

        if car not in cars.keys():
            cars[car] = [time, 'IN', 0]
        else:
            if state == 'IN':
                cars[car][0] = time
                cars[car][1] = 'IN'
            else:
                cars[car][1] = 'OUT'
                cars[car][2] = cars[car][2] + time - cars[car][0]
                cars[car][0] = None

    for car in cars.keys():
        if cars[car][1] == 'IN':
            cars[car][1] = 'OUT'
            cars[car][2] = cars[car][2] + (60 * 23 + 59 - cars[car][0])
            cars[car][0] = None

    answer = list()
    for car in sorted(cars.keys()):
        answer.append(cal(fees, cars[car][2]))

    return answer
