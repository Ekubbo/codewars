from datetime import datetime


def size_ship(l):
    return next(iter([i for i, v in enumerate(l) if v == 0]), len(l))


def get_ship(bf, x, y):
    coll = size_ship(bf[x][y:])
    row = size_ship([i[y] for i in bf[x:]])
    if coll > row:
        return ((x, y + i) for i in range(coll))
    else:
        return((x + i, y) for i in range(row))


def is_valid_ship(bf, l):
    for x, y in l:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                x_, y_ = x + i, y + j
                if x_ in range(len(bf)) and y_ in range(len(bf[x_])):
                    if bf[x_][y_] == 1:
                        return False
    return True


def validate_battlefield(bf):
    ships = {4: 0, 3: 0, 2: 0, 1: 0}
    for x, line in enumerate(bf):
        for y, i in enumerate(line):
            if bf[x][y] == 0:
                continue
            ship = list(get_ship(bf, x, y))
            for x_, y_ in ship:
                bf[x_][y_] = 0

            if len(ship) > 4 or not is_valid_ship(bf, ship):
                return False
            else:
                ships[len(ship)] += 1

    if (ships[4], ships[3], ships[2], ships[1]) == (1, 2, 3, 4):
        return True
    else:
        return False


bf = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


if __name__ == '__main__':
    start = datetime.now()
    print(validate_battlefield(bf))
    print(datetime.now() - start)
